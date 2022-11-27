# Engineering Standards
## Purpose:
- **Make striving for engineering excellence easier for other teams by cloning this repo as a 
  starting point.** 
- **Link engineering standards to corresponding infra-as-code for proper setup and configuration** 
  (mostly located [here](https://github.com/tloeber/utils_and_configs))
- Clarify my own thoughts and document insights for later.
- Standardize my approach for consistency over time.

## Why engineering excellence matters
**While striving for greater engineering excellence is an investment that pays of greatly, many 
organization/decision makers don't have the time horizon or technical understanding to 
sufficiently prioritize it. 
Since my own role within a team is often to push for greater engineering excellence, I 
want to reduce this hurdle by making it less time-consuming to get started.**

**I'm a strong advocate for Agile software development, so I'm all for an iterative approach - but
I think it is a common pitfall to keep de-prioritizing tasks that are *important but never 
urgent*.** If we want to create applications that are agile – i.e., maintainable and 
extendable -  we have to get the foundations right and avoid accumulating technical debt that 
eventually reslts in a  
[big ball of mud](https://en.wikipedia.org/wiki/Big_ball_of_mud) - and a focus on engineering 
excellence from the start helps us achieve just that. 

**Fortunately, a lot of the investments into engineering excellence are only one-time.** (Yes, you 
do have to keep writing and updating tests, but once this process has been established, it 
probably takes less time to keep doing so than manually verifying that the 
code still works after every little change you make. Thus, much of the challenge is about 
keeping up the *discipline*, rather than keep making a large investment in terms of time/money).
So most of the initial cost of embracing engineering excellence stems from:
- Researching and deciding which standards and tools to adopt;
- Setting up these tools;
- Training all engineers.

I myself have already spent a lot of time researching and experimenting with the first two 
questions. This repository documents my findings from the first bullet point, and it links to 
configurations which are currently part of 
[one of my other repositories](https://github.com/tloeber/utils_and_configs).
This collection offer a good starting point to get off the ground quickly, and can be easily 
customized to  specific needs. The third bullet point, training other engineers, is 
less costly once we have the first two checked off: Not only is it is much easier to just 
*follow* - rather than *design* this 
process, but in addition much of the learning can happen while already starting to reap the 
benefits from the improved process.

## Making Machine Learning a mature discipline by adopting proper engineering standards
*"To make great products: do machine learning like the great engineer you are, not like the great 
machine learning expert you aren’t. Most of the problems you will face are, in fact, engineering 
problems."*
[Google's Rules for ML](https://developers.google.com/machine-learning/guides/rules-of-ml)