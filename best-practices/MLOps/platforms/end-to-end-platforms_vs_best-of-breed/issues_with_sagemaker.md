# general

- requires a lot of boilerplate code (see sagemaker examples) and results in code that is hard to change, unless adding a ton more code to rewrite SDK, like I am doing with my project
using a ton of inheritance, for example framework processor, making it a lot of work to chase down what valid arguments are.
- even worse, a lot of that is not documented properly, so you just have to look through the source code.

# typing issues

- inflexible inputs and outputs. want you to write to S3, and don't support table abstraction through Athena, for example, without installing third-party libraries, since boto3 SDK is not very usable for Athena query. doesn't support reading from sagemaker feature store either, strangely enough.
- it's not documented at all what the downsides are of just handling the input and output yourself. probably fine, but you might lose out on some other features later on. for example, model monitoring and data lineage <https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html> ?
- doesn't take the burden of creating good observability away from the user. have to dig through various log streams.
- Doesn't work well without containers, so it fails to meet the requirements of many companies who would be most likely to need a default ML platform, rather than being able to use a more custom best of breed solution:
- not very well documented how to install extra dependencies. for example, for preprocessing, you need to use a framework processor.
- there are often problems with dependency resolution. while this is partially unavoidable, one basic problem seems to be that the default dependencies are installed with conda, whereas the documented way to add dependencies is by using PIP.

- Pipeline runs very slow even if the computation itself is trivial. so it seems there is much overhead. this is better if using a step directly, for example running a processing step outside of the pipeline, but again you have to implement the logic yourself to be able to easily switch out the different ways of running.

# awkward design

- inheritance (good example to dive deeper: framework processor)
- Whether we are using PipelineSession or normal Sagemaker session determines whether processor.run() returns `None` or pipeline step args. (See <https://github.com/aws/sagemaker-python-sdk/blob/8462f1a1975da59304da4441aea956a43deec380/src/sagemaker/processing.py#L1763>)
  - misleads type checker (maybe it's stuff like that why they didn't include py.typed?)
  - can lead to hard-to-debug error messages if the underlying problem is we're using the wrong session. (good example to show)
