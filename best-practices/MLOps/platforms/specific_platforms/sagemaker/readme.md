# Shortcomings

## Unclear types (from docs *and* source code)

### Boto3 does not support type checking out of the box

Fortunately there is a [3rd party package of type stubs](https://pypi.org/project/mypy-boto3-sagemaker/), but you have to know about it and install it separately. Also, this introduces the potential for errors if there is a version mismatch between boto3 and boto3-stubs.

### There is no easy way of type-checking Sagemaker SDK

This is because [it does not implement PEP 561](https://github.com/aws/sagemaker-python-sdk/issues/2985). What makes this particularly frustrating is that the Sagemaker SDK's code base *is*in fact already typed, but mypy can't use these types because the package is missing an (empty) py.typed file that would mark it as annotated.

Looks like while there are some workarounds, they seem too hacky for production-grade software.

### No (sufficient) validation early on, bubbling up internal errors that don't tell user what they did wrong

As a result, the user commonly gets internal Sagemaker errors (e.g.,  no such attribute, etc.), often making it very hard to debug simple mistakes.  While some of that can be remediated by using proper type checking on the user side of things like configs,  this does not eliminated all major classes of errors. In particular,  some of the peculiar design choices of Sagemaker, such as how to run a given step  as part of a pipeline or not (e.g., as a processing job) can cause as major issues. What makes this even worse is that these small but impactful differences in the required syntax are often not properly documented.

todo: add examples of what happens if:

- you confuse pipelinesession and sagemakersession
- don't take other additional steps required if a job is turned into a pipeline step

### Relationship with Step Functions

- Sagemaker pipelines has gotten more flexible, in particular by allowing you to integrate lambda functions.  While this allows you to do things like trigger spark jobs, it is a little tedious to add a lambda function for each step, and to then manually check if it was successful (as the trigger is presumably asynchronous).
- Alternatively, we could also use step functions to do  the main orchestration, one step of which would be the Sagemaker pipeline. However, this makes the execution graphs of the step function and the pipeline less useful, as they are not telling the whole picture anymore.
- So it might be appealing to just use step functions for everything (since Sagemaker Pipelines is also built on top of step functions anyway), but  – as I understand – you then loose out on some of the ML specific benefits of Sagemaker, such as lineage.  (Unfortunately, these details are not obvious from the documentation.)
- An example of a better solution that  combines both into a single service is [Databricks Workflows](https://docs.databricks.com/en/workflows/index.html).

### Step input and output

- Using the inbuilt step inputs and outputs (e.g., ProcessingInput) is tedious. It would be much simpler if we could just specify this in the code script of each job.  That's possible, but the documentation is not clear what the downsides are of this (presumably we  lose lineage as well as some model monitoring features -  but  it's not clear how much exactly do we need to specify in order to get these full benefits.)
- Almost all of the documentation revolves around S3 objects. A much more common use case is presumably  using a table abstraction, but it took me a while to find how to use an Athena table (and it is a little convoluted, so haven't tried it out yet if it works).
- Even worse, some common data sources do not seem to be supported. Most surprisingly, even the Sagemaker Feature Store is only supported in very specific cases (as of Jan 2024), based on the documentation.

todo: add links

### Pipeline Execution Variables

Unfortunately, the docs[https://sagemaker.readthedocs.io/en/v2.200.1/workflows/pipelines/sagemaker.workflow.pipelines.html#execution-variables] are not useful in telling us how to use it (e.g., which methods we can call on it)
![Alt text](../../../../../_img/sagemaker_pipeline_executionvariables_docs.png)

In other parts of the docs, this class is mentioned as an arg type (e.g., for Conditionstep). However, this is not linked here.
Even more importantly, we have to guess how else we can use it, .e.g., could we print it in logs? You would assume so, but in fact printing fails because it turns out that this class only has a to_string() method, but lacks the conventional \_\_str\_\_() method.

![Alt text](../../../../../_img/sagemaker_pipeline_executionvariable.png)

At least the error message tells you how to fix it, but it would be better if we could find this out before runtime. (In addition,  to_string() should simply be renamed to the standard \_\_str\_\_().).

(Also remember it is hard to play with this cdoe interactively and simply call \_\_dir\_\_() on an instance, because this code only runs in a pipeline.)

Note: **The reason this problem is also not caught by the type checker is because of the library's missing py.typed marker discussed above, which leads mypy to skip it!**

# Other people's issues with Sagemaker from around the web

-
