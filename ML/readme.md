# Creating a state-of-the-art ML ecosystem
- **Most companies are overly focused on modeling, which is just a small piece of the overall ML 
  lifecycle.**
Modeling is increasingly becoming a solved problem, as the best models for many use cases are 
  becoming increasingly standardized, and we can increasingly leverage pre-trained models 
  (especially in NLP and computer vision). 
  - AutoML & Declarative ML:
  - **MLOps: This is where we should focus our investment, in order to reliably productionize 
    models!**
- That being said, there are use cases where modeling needs to be a focus area as well: 
  These are companies which compete on the basis of ML, and there is an immediate impact of 
  even incrementally better models on revenue. My point is, however, that this is the exception 
  rather than the norm (and Negative even for these types of use cases, figuring out how to 
  reliably productionize ML models is a challenge that has to be solved _first_).  
- Manual feature engineering is also becoming less important as available data size grows, 
  because this allows us to use neural networks which automate feature engineering. 

## Build vs. Buy (vs. Open-Source)
### The old Build vs. Buy Discussion
Build versus Buy is of course an old question that has been discussed for many other types of software 
systems. I think the general answer is clear: **Companies should concentrate on the core of their 
business, and offload all other *generic* problems to specialized providers *as much as 
possible*.**  

Note an important qualifications I'm making: A problem must be *generic* - 
otherwise there won't be an industry around providing solutions 
for it. 
(We can think of _consulting_ as offloading non-generic problems to a third party-provider. This can still be beneficial in order to 
take advantage of _specialized knowledge and an outside perspective_, but - amost by definition - 
you do not really get any economies of scale).

It also follows that we should try to turn our 
problems _outside of our core business_ from specific into generic ones as much as possible, so 
that we can benefit from the efficiency increase we get from offloading them to a specialized provider.
While this may seem obvious, it is often not a priority in practice. It's easy to 
end up with a cobbled-together mess of hacks if you are overly focused on solving 
immediate problems and never get the time to think about the system architecture as a whole (or 
if you're not willing to invest into the future by paying down technical debt). 
Furthermore, over the last decade the mainstream adoption of the 
cloud has made it easy to offload much more than we previously thought possible, so non-generic 
systems have become a larger drag than originally anticipated. 

Let's now dive into the reasons why buying is generally better than building:
- It's a pretty safe assumption that **the core of a company's business is where its competitive 
  advantage lies** - otherwise it would not be profitable (or receive continued 
  investment in order to get over the hump to become profitable, in the case of a startup). Most 
  companies fail, so if a company made it far enough to survive for a number of years, it likely 
  must be doing something right. 
- By contrast, for many tasks businesses face that are outside of their core area of expertise, 
  many other specialized companies are already competing to own this niche. They 
  have learned valuable lessons along the way, and the best ones have survived. So why reinvent 
  the wheel, rather than picking the winner? (Michael Dell has a good quote around that, but 
  couldn't find it anymore.)
- In addition, specialized providers enjoy **economies of scale** that give them a huge cost 
  advantage. (However, if you forget to factor in the cost of your own teams's labor, 
  building-yourself may wrongly seem cheaper). These **economies of scale are particularly large 
  for digital goods such as software, because most of the cost associated with their production is 
  fixed cost, whereas their marginal cost is near zero** (i.e., they can be shared at virtually 
  zero cost). While we need to also remember that much of the lifetime cost of software systems is 
  in their maintenance - not their initial creation - these economies of scale also extend to the 
  ongoing maintenance, albeit to a lesser extent: Firstly, some of the maintenance is generic, and 
  thus many different 
  users can benefit from it (e.g., staying up-to-date with security vulnerabilities, or adding new
  features). Secondly, even for maintenance tasks isolated to a specific client - such as 
  production support for infrastructure issues - there are still some economies of scale 
  because of the _specialized knowledge_ required.
- The previous two points imply that buying is generally more *efficient* than building. (Even if 
  you factor in [transaction costs](https://en.wikipedia.org/wiki/Transaction_cost), the 
  advantage of buying is generally so big that transaction costs are negligible.) However, 
  *just because managed solutions are more efficient does not mean that they are automatically 
  better and cheaper.* What it does imply, though, is that it is generally *possible* to provide 
  better solutions at a lower price, and in a competitive market economy these business 
  opportunities will not remain unfilled for very long.  
  Still, particularly in the short term, 
  suboptimal pricing strategies that don't make a solution attractive to all different kinds of 
  customers can persist for surprisingly long times. (E.g., pricing may not sufficiently vary with scale, and thus only 
  makes sense for large customers). *Therefore, we will still have to do the math ourselves to 
  figure out if it is worth it - but if we arrive at the solution that it's cheaper to build it 
  ourselves, we should be skeptical and double-check our numbers and assumptions* (e.g., did we 
  account for the risk from the well-known fact that most software projects take much longer and 
  are much more expensive than initially estimated?
  Did we factor in the cost associated with the fact that the business will only be able to draw 
  value from our homegrown solution a lot later than if we bought a prebuilt solution, because it 
  takes longer to build than to buy?)
- Finally, managing the core business is already hard enough – in fact, a common reason why 
  established companies fail in the face of disruptive innovations is because they don't focus 
  enough on the core business they are in (such as Blockbuster failing to go through with purchasing Netflix, 
  because they thought they were in the business of *renting out* movies, rather than in the more 
  general business of letting customers watch movies). Thus, since it's already hard enough to 
  make the right strategic decisions in the area of your own core expertise, it's best to limit 
  the complexity of all the strategic decisions you have to make by offloading everything else 
  as much as possible.
- A risk with buying  that needs to be managed as a vendor lock-in. This goes both for the 
  risk of price 
  hikes and the vendor going out of business. This risk is higher the longer it takes to 
  migrate the solution to a different vendor, and the more critical the process is to our core 
  business. 
  - I think the price hike argument is often overstated: While it is true that we worsen 
    our bargaining position the more dependent we are, this may at their worst result in less 
    discounts, but as long as there is still some competition between providers, they do not 
    have an incentive to make general pricing less favorable. They still need to remain attractive 
    to new customers and be mindful of their reputation as a partner, and make sure their 
    customers stay in business.  
  - However, the risk of a service provider going out of business is real, and is higher for 
    smaller and younger companies. Thus, if you go with a less established company, we better be able to 
    easily migrate elsewhere (or to do the task ourselves, such as if we are just buying support). 
    On the other hand, while it would be hard to migrate away from something like AWS Lambda or 
    even Step Functions, the risk of AWS going out of business (or discontinuing these popular 
    services) is very low. On the other hand, the cost of avoiding the risk by instead replicating 
    the same functionality in 
    a cloud-provider agnostic way (probably using Kubernetes) is orders of magnitudes higher - 
    so accepting the risk of vendor lock-in is clearly a risk worth taking.

### What about free and open-source software?
A third option is to leverage free and open-source software (FOSS) options, if any are available.
In some ways, these are 
similar to buying a prebuilt solution: You have less ability implement customization, but it's much 
quicker, easier, and cheaper to get started. In other ways, though, leveraging FOSS is more 
similar to building-yourself: You may still have to put in a lot of work yourself, whether it is to 
do some customization for specific needs, or to add additional features that are not supported. 
Overall, I think it really depends on the specifics of the use case whether relying on FOSS
solutions makes sense:
- Some solutions are FOSS first (e.g., Linux), others are a company's product first (e.g.,
  MLFlow or BentoML). The latter often 
  lack critical features that are a must-have for enterprise customer, such as role-based access 
  control, audit logging, etc. If the only viable open-source solution is of this kind, it 
  only makes sense to adopt it if:
  - you're sure you can add the missing features yourself, or
  - you're willing to live without them for a while (remember: a re-architecture is generally 
    necessary after a few years anyway), or
  - you are willing and able to pay for the commercial offering once needed.
- But even if a FOSS solution gives you everything you need, it may still make sense to 
  pay for the commercial offering: Like the "buy" solution discussed above, a commercial version 
  can help companies offload the undifferentiated heavy lifting (e.g., implementing access 
  control or management of the underlying infrastructure), which a specialized provide can 
  generally provide at a lower cost. In addition, it also reduces the complexity for the 
  buyer, as they only need to worry about a smaller subset of problems (namely the ones that are 
  specific to their core business).
  - By the way, I know it feels like you're losing out if you're not taking advantage of a free 
    open-source version, but - if the license also allows using the software for commercial use -  
    it is cheaper for other companies to build a business on top of it. In fact, there will be more 
    competition than if every company was starting from scratch, so the cost savings will get 
    passed down to the purchaser more quickly. Thus, *you're basically still getting the 
    open-source core of the software for free, and you're just paying for the additional 
    features and support if you go with the managed offering!*


### ML-specific considerations
- There is a plethora of both commercial and open source solutions available for the vast 
  majority of use cases. Even for specialized use cases, there are flexible solutions such as 
  Sagemaker's Bring Your Own Container or Metaflow's ability to integrate with a wide variety of 
  specialized tools. Thus, just because you need to use your own algorithms doesn't mean you 
  need to build a custom ML platform yourself!
- There are only few companies (large tech companies) that have  the resources,
  expertise, and custom requirements to compete with AWS's or Google's offerings - almost 
  everyone else is mainly going to be reinventing the wheel.

### Conclusion
- I would really **try to find a *managed* service*** - having to deal 
  with lower levels problems such as managing the infrastructure and having to deal with the problems that come with distributed systems (e.g., partial failure)
  failures adds unnecessary complexity. While leveraging a managed service costs extra, 
  once you factor in the cost of engineers' time, managed services are often much cheaper.  
  Remember: Successful companies focus on their business's *core* expertise, and try to offload 
  everything else!
- 
## End-to-end platforms vs specialized
- Even for managed services, ***integrating* these third-party solutions into an 
  existing cloud infrastructure is always much harder than going with something 
  native to your cloud provider**. Thus, the easiest way to get started is to simply leverage 
  the ML platform of your
  cloud providers (Sagemaker for AWS, Vertex AI for GCP), or Managed MLFlow for companies who 
  already use Databricks. I would recommend checking out if any of these options 
  meets your needs.
- Generally doesn't support the most cutting-edge use-cases - but for the vast amount of 
  companies that's ok. Many companies still struggle with deploying even a simple model into 
  production, so there are plenty of low-hanging fruits, and any of the major ML platforms will 
  be powerful enough for these generic ML use cases.
- That said, while end-to-end platforms may _do_ the job, the question is if we want to *pick 
  the **best** tool for each job* by mixing-and-matching specialized solutions for different stages of 
  the ML lifecycle. E.g., use Tecton's feature platform, MLFlow for 
  experiment tracking and as a model registry, BentoML for model serving, etc. (Of course, you 
  still have the option of using a _subset_ of your cloud provider's ML platform for specific parts 
  of the job, if that makes sense).  
  Specialized providers live and die by the quality of their product, so they have a greater 
  incentive than cloud providers for whom their ML tooling is just a small part of their 
  offering, and thus may not necessarily be their focus area. On the other hand - as already 
  mentioned - it is harder to integrate diverse tools with each other and into your existing 
  cloud infrastructure (especially if we think about things such as identity and access management, 
  etc.). Also, you are more exposed to vendor risk, because virtually all of these companies 
  have sprung up in the last few years, and it is not clear yet how much consolidation will take 
  place and who the winners will be.
- The choice for end-to-end platforms is generally limited to only that one from your major 
  cloud provider because there are no major cloud-agnostic end-to-end solutions. (A few years 
  back, H2O was a good choice, but not sure where they went.) It usually doesn't make 
  sense either to use an ML platform from a _different_ cloud provider than where your data and 
  downstream consumers of the outputs live: Data-transfer cost is massive, and many tasks become
  much harder, e.g. identity and access management, monitoring for data-drift, etc. Thus, whether 
  an end to end platform makes sense not just depends on the ML use case but also which option 
  you have available based on your current cloud provider: 
  - I'm most familiar with **Amazon Sagemaker**, but I'm not a great fan of it. I really wanted 
    to be a viable solution – and it probably still is the best option for delivering 
    value most quickly - but overall I feel like it does not deliver on its promises and is 
    frustrating to use. My main critique is that it is not designed with proper interfaces between 
    the different components, so they don't fit together as much as you would expect from 
    something claiming to be an end-to-end platform – which defeats the whole point. 
  - For the minority of companies who are on 
    Google cloud, **Vertex AI** is probably the strongest offering, since it's basically a managed 
    version of Kubeflow. I'm not familiar enough with it, though, to provide any recommendation 
    on it.
  - **MLFlow** is known mainly for experiment tracking and as a model registry, but with recent 
    feature additions (such as pipelines), it is moving towards becoming an end-to-end ML platform.   
    Since these features are still pretty new, they are probably still less mature. On the other 
    hand, Databricks is known to create software that is great to use, so I would definitely 
    explore it if already using Databricks Delta Lake, etc.
  - I'm not familiar with Azure's ML offerings, but the fact that discussions of ML platforms 
    usually only bring up Sagemaker and Vertex AI make me skeptical whether Azure has a viable 
    option.


### Conclusion
Overall, I think it's hard to make a general recommendation at this point. 
- An end-to-end platform allows you to deliver value more quickly, so it should probably be the first choice for 
  companies for whom this is a priority (early-stage start ups, as well as 
  potentially even established companies where the business side is not willing to make the 
  investment before they see any concrete value).
- 


## Running infrastructure on Kubernetes?
TLDR Only makes sense in a limited set of use cases: 
- Need: Off-the-shelf infra is not enough, because ML is at the business core, so it makes sense 
  to invest 10X in order to get a 1% improvement.
- Technical ability: Able to attract superior talent (because everything becomes much harder)
- Financial ability: Able to have dedicated DevOps team focused on Kubernetes

### Should data scientists know Kubernetes?
Surprisingly, this is still a question where you hear arguments for both sides. However, I think 
the right answer is a resounding **no!: If data scientists need to know Kubernetes to be 
productive, there is something seriously wrong with the design of their ML platform** (or they 
might not have access to one at all).

I think the main reason goes back to the general insight that to solve complex engineering 
problems, **we need to decompose problems in a way that we can divide labor amongst people who 
specialize in different parts of the problem**. To enable the specialization, we come up with 
stable interfaces that provide contracts for how the different parts of the system interact. While 
we might have to revise these interfaces occasionally, for most of the time most engineers can 
focus only on their respective domain - which is already hard enough if we're pushing boundaries. 

The best example I can think of is how we make some as complex as the Internet work: As a software 
engineer, I mainly have to understand the application layer (e.g., http protocol) and to a 
lesser extent the transport layer (e.g., TCP). However, I don't 
have to worry about how packages will be routed to the right address, and I 
definitely don't have to know anything about how this communication works at the physical level 
(e.g.,how the signal is transmitted through fiber-optic cables). 

Similarly, if we are faced with building something as complex as a machine learning system, we need to find a way of 
slicing this domain into specialties that can be fulfilled by different people.
**I do think it is essential that data scientists learn more about software 
engineering** as the field is transformed from a research done in Jupyter notebooks 
to an engineering discipline that deals with production code. However, it already takes a 
lot of time to master data science and machine learning (and to keep one's knowledge up to date 
in the face of rapid innovation). Thus, 
expecting data scientists to master all (or even most) of software engineering and DevOps is 
clearly unrealistic, and would go at the expense of their core domain knowledge.  
Instead, the question is not just which parts of the traditional engineering knowledge we need to 
have involved in the data science process, but also **which of these roles can be performed by
specialists, and which aspects are so basic and intertwined with the core data science work that 
every member of the team is expected to master them.** 

One natural division specializations that has emerged is between software engineers writing code 
and infrastructure-, security- and DevOps engineers (or in earlier times, system admins)
focusing on different aspects of the infrastructure side. While the discussions around DevOps 
and DevSecOps have shown that there often is still a need for collaboration between the 
different sides, and that everyone still needs to have an understanding of the basics of the 
whole lifecycle, it's clear that each of these fields is complex enough to warrant 
deep specialists.

But what about a small startup that can't afford to have dedicated specialists for each of these 
fields, you may ask? As I argued in the previous section, the answer is simple: In that case, 
you definitely shouldn't run your infrastructure on Kubernetes at all! If you have a small team, 
you don't want your engineers to spend most of their time on something like setting up and 
managing infrastructure that doesn't create any immediate business value. 

By contrast, which basics of software engineering should data scientists learn?
- writing *clean* code (an understanding the importance of *maintainability*)
- automatic testing 
- design patterns
- DevOps (high-level)
These are things everyone on the team needs to know. We don't want to have separate software 
engineers who constantly rewrite bad code and fix that design, etc.


### Should _ML engineers_ know Kubernetes?
There is obviously more of a case to be made that _machine learning engineers_ need to know 
Kubernetes (K8s). However, I would still argue that:
- not all ML engineers need to know K8s, because K8s only makes sense as an infrastructure 
  solution for a small subset of companies, and  
- even for ML engineers who work with ML platforms that _are_ deployed on K8s, they don't need to 
  be K8s experts. K8s is a complex beast, and it requires dedicated DevOps engineers to tame.
  It's a long way from understanding its basic architecture and being able to 
  deploy to it, to troubleshooting complex networking issue (which unfortunately not a rare 
  occurrence).
  The latter problems require experts that work with K8s full-time - having ML engineers  
  solve these problems themselves detracts from their core function. If a company doesn't have 
  the resources to employ a fleet of dedicated DevOps engineers to work on these problems, it 
  should not be on K8s.
 
## Which specific tools to pick
- I'm currently exploring one tool that may be superior enough to Sagemaker and Vertex AI to 
  potentially change my mind in the Future: **Ludwig**, a **Declarative ML** framework open-sourced by 
  Uber. While it does help you manage distributed training using [Horovod](https://github.com/horovod/horovod), having to worry about the infrastructure is still something that's better to avoid if possible. This has been addressed recently when its creators came out with a commercial offering around Ludwig and Horovod, called **Predibase**, which should take care of much of the undifferentiated heavy lifting. I'm very impressed by Ludwig, but I haven't used Predibase yet, so I can't comment on how well it works and how affordable it is.

## Final Thoughts
- **Invest the time-savings you get from these suggestions** (leveraging free and
  open-source or managed solutions, start with off-the-shelf models, etc) 
  **into striving for engineering excellence**. This is a much better investment and will 
  greatly pay off soon by making your ML system **maintainable and scalable**. In order to make 
  it easier to get started, I have documented my own insights as well as 
  associated configurations in this repo.
- Remember that the ML infrastructure depends on a solid _data_ infrastructure. See my 
  discussion of the data side [here](../data-infrastructure/readme.md).
