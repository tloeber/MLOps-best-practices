# Why managed notebooks instances are not enough:
- we need a proper IDE with proper debugging, static code analysis, syntax completion, and quick help when hovering over a variable, function, or object. This enables much greater efficiency and higher code quality, and is necessary to move towards bringing engineering standards to data signs and machine learning.
- While there are some extensions for Jupiter lab that brings some of those benefits – and Sagemaker studio claims to be the first IDE for data science – they are not nearly good enough:
  - debugger doesn't work very well. Most importantly, ability to execute commands at breakpoint doesn't seem to work. Also, it is hard to inspect current values of variables because there are problems with displaying them properly. I've also had problems when breakpoint was in a Python script called by a Jupiter notebook. (Don't remember for sure if it worked to use pdb instead, but I think it did not.)
  - There is a static code analysis extension, but installing these extensions into Sage maker studio didn't work properly. (Looks like it's probably easier on notebook instances). I spent hours because turnaround was so slow [it took at least five minutes for logs to show up in cloud watch, and they were very informative]. I eventually cut my losses and gave up, because without proper debugger, notebook wouldn't be an option anyway.
- How about connecting local IDE to Sage maker using SSH? Couldn't get it to work on studio. Found a tutorial, and it said at the end you just need to slightly change the URL, but the way they changed it in that tutorial did not work anymore, presumably because it relied on an unstable interface. It's too risky to rely on something like that which is not officially supported. Also may introduce security risks.
- Running VS   code on Sagemaker works but is too hacky to rely on (both because it could break anytime AWS makes changes on their land, and because it requires extra work to make sure it is really secure).
- Even if Sagemaker studio offered a good enough IDE, local development would be a must for quicker iterations. Firstly, it takes a while to always log into AWS, because it doesn't easily save all the tabs you have open (e.g., the right S3 bucket you want to inspect, cloud watch logs). In addition, cloud watch logs can be slow to show up. Also, having to pull the data to the instance from S3 can take a while, as can having to spin up a new instance for certain subtasks.


# Workflow:

# Beyond ML
## AWS serverless stack
Use SAM!
