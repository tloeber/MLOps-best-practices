# Why notebooks instances are not enough:
- we need a proper IDE with proper debugging, static code analysis, syntax completion, and quick help when hovering over a variable, function, or object. This enables much greater efficiency and higher code quality, and is necessary to move towards bringing engineering standards to data signs and machine learning.
- While there are some extensions for Jupiter lab that brings some of those benefits – and Sagemaker studio claims to be the first IDE for data science – they are not nearly good enough:
  - debugger doesn't work very well. Most importantly, ability to execute commands at breakpoint doesn't seem to work. Also, it is hard to inspect current values of variables because there are problems with displaying them properly. I've also had problems when breakpoint was in a Python script called by a Jupiter notebook. (Don't remember for sure if it worked to use pdb instead, but I think it did not.)
  - There is a static code analysis extension, but installing these extensions into Sage maker 
    studio didn't work properly. (Looks like it's probably easier on notebook instances). I 
    spent hours because turnaround was so slow (it took at least five minutes for logs to show 
    up in Cloudwatch, and they were not very informative). I eventually cut my losses and gave up,
    because without proper debugger, notebook wouldn't be an option anyway.
- Even if Sagemaker Studio constituted a good enough IDE, local development would be a must for 
  quicker iterations. 
  - Firstly, it takes a while to always log into AWS, because - by contrast to GCP - it 
    frequently requires you to log in again, and then doesn't give you an easy way to restore 
    all the tabs you had open for the different services you're interacting with. (e.g., the 
    right S3 bucket you want to inspect, cloud watch logs). 
  - In addition, Cloudwatch logs can be slow to show up, and it often takes a few steps each 
    time you want to inspect the logs of a new run (which is fine if you do it once, but if you 
    have to try the same step many times, it quickly gets frustrating). 
  - Having to pull the data to the instance from S3 can take a while, as can having to spin up a 
    new instance for certain subtasks.

# How to use a proper IDE with Amazon Sagemaker
## Why we shouldn't just connect local IDE to Sagemaker Studio
- How about connecting local IDE to Sagemaker using SSH? **Not *officially* supported!**  I found 
  a tutorial, and it said at the end you just need to slightly change the URL, but the way they 
  changed it in that tutorial did not work anymore, presumably because it relied on an unstable 
  interface. 
- You could actually run VS Code on Sagemaker, but it too is **not *officially* supported**.
- Bottom line: Since there is no officially supported solution, I think it's **too risky** to rely on 
  something that could break anytime if AWS makes changes on their end. In addition,  
  such a solution requires extra care to make sure it really is secure.

## Remaining options:
Need to set up environment on a dedicated machine – either local laptop or cloud VM. 

**Note: We are talking about replicating the Sagemaker notebook environment, not any of the 
environments that actually perform processing jobs, model training, etc.! The latter would be much 
harder to set up locally - but there is no need to do so, because these tasks are performed 
internally by Sagemaker. The task of our environment is simply to make an API call to Sagemaker 
\- so the main library that needs to match the AWS environment is the Sagemaker version. Even 
  if we are using Sagemaker Local Mode, it will use AWS's Docker images to perform any 
computations such as model training.** 

Challenges: Make sure our environment is as similar as possible to Sagemaker, minimizing the 
risk that code works on our laptop but not on AWS.
- If we are using Sagemaker Pipelines for production (we probably should), most of our code will 
  run in AWS-provided containers anyway. Since with us should not need any ML-specific packages 
  beyond Sagemaker, we don't need to use conda. Thus, we can use Pipenv, making cross-platform 
  compatibility is not a major problem.
- Replicating a notebook environment locally becomes challenging once we need to use 
  conda.
  - First off, it should be emphasized that we should only use this for dev anyway, so any problems 
    become less dangerous – though we still want to avoid wasting time on these kind of environment issues.
  - If we are running on Linux, we can simply export the conda environment from a Sagemaker 
    notebook and imported into our environment. However, since conda only allows export of *all* 
    installed packages (including dependencies) - rather than only packages explicitly installed, like Pipenv 
    does - the resulting environment 
    file is not cross-platform compatible. (There are several options in conda that seem like the 
    might do this, but they do not include packages installed with pip, so it is useless for our 
    purposes.) 

### Run code on EC2 and connect local IDE using SSH
- Here is an [example setup that automates instance start and shutdown.](https://aws.amazon.com/blogs/architecture/field-notes-use-aws-cloud9-to-power-your-visual-studio-code-ide/) 
- Pros: 
  - Can run on Linux, even if our laptops use different OS
    - Environment setup is easier and much quicker.
    - Environment is more similar to AWS than running locally on MacOS or Windows.
    - Greater hardware choice 
      - (rare cases where extra 
        performance or GPU is needed - though that generally shouldn't be the case since we should 
        small data set for dev 
      anyway, and once it's working we may as well run it from Sagemaker Studio).

- Cons: 
  - Slightly more overhead.
  - Have to worry about security.
    - If you lock ssh ingress down to your IP, have to update security group whenever your IP 
      changes or you work from elsewhere.
    - Can use AWS Systems Manager to ssh into private subnet, but more overhead.

### Create local environment
- Pro: Least overhead for day-to-day use, not dependent on Internet and VPN.
- Cons: 
  - If not on Linux, have to manage Python environments ourselves.
    - Conda doesn't give you an option 

### Decision: 
  - If using Linux laptops, local should work just fine

# Workflow
- When in lifecycle should we start using Sagemaker Pipeline?

# Beyond ML
## AWS serverless stack
Use SAM to easily define infrastructure that can be both run locally and on AWS! 
  - Limitation: Only supports the key serverless Services, but if you are able to use it, it 
    provides great benefits. 
  - Biggest benefit: ability to attached IDE's debugger to a lambda functions. Unfortunately, 
    the main open-source lambda image (was it Localstack?Okay Google remind me tonight at six to 
    commit) does not easily allow that.  
