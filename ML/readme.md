# Building a state-of-the-art ML ecosystem
- Try to **leverage cloud provider's managed ML platform** (Sagemaker for AWS, Vertex AI for GCP). 
  Databricks' 
  Managed MLFlow may also be a good choice that works with all three major cloud providers, 
  especially if you're already leveraging Databricks (their Lakehouse Platform is a game changer for data engineering!). There are only few companies (large tech companies) that have  the resources, expertise, and custom requirements to compete with AWS's or Google's offerings - almost everyone else is just going to be reinventing the wheel.
- The next best alternative is to **mix and match your cloud provider's ML platform with 
  **specialized offerings****, e.g., Tecton as a feature platform, MLFlow's Model Registry, 
  Seldon for model serving. 
  - I would really **try to find a *managed* service**** - having to deal 
    with lower levels problems such as managing the infrastructure and having to deal with the problems that come with distributed systems (e.g., partial failure)
    failures adds unnecessary complexity. While leveraging a managed service costs extra, 
    once you factor in the cost of engineers' time, managed services are often much cheaper.  
    Remember: Successful companies focus on their business's *core* expertise, and try to offload 
    everything else!
  - But even for managed services, ***integrating* these third-party solutions into your 
    existing cloud infrastructure is always much harder than going with something 
    native to your cloud provider**. Thus, I would recommend going with default services first, 
    and only trying out substituting some of its components with specialized offerings if 
    there is really an important feature gap you don't want to live with, _and_ you are able and 
    willing to invest the resources in integrating outside tools.
- I'm currently exploring one tool that may be superior enough to Sagemaker and Vertex AI to 
  potentially change my mind in the Future: **Ludwig**, a **Declarative ML** framework open-sourced by 
  Uber. While it does help you manage distributed training using [Horovod](https://github.com/horovod/horovod), having to worry about the infrastructure is still something that's better to avoid if possible. This has been addressed recently when its creators came out with a commercial offering around Ludwig and Horovod, called **Predibase**, which should take care of much of the undifferentiated heavy lifting. I'm very impressed by Ludwig, but I haven't used Predibase yet, so I can't comment on how well it works and how affordable it is.
  - **Most companies are overly focused on modeling, which is just a small piece of the ML lifecycle.**
  Modeling is increasingly becoming a solved problem, as the best solutions for many use cases are 
    becoming increasingly standardized, and you can even leverage pre-trained models for use-cases 
    (especially in NLP and computer vision). 
    - AutoML & Declarative ML:
    - **MLOps: This is where we should focus our investment, in order to reliably productionize 
      models!**
- **Invest the time-savings you get from these suggestions** (leveraging managed services, pre-trained 
  models, and AutoML or Declarative ML) **into striving for engineering excellence**, which will 
  greatly pay off soon. In order to make this investment less costly, I have documented my own insights as well as configurations (e.g., IDE, linting, etc) here.


# Building a state-of-the-art Data Ecosystem
- Delta lake
- Lakehouse architecture
  - There is often no need anymore to have a separate data warehouse!
- Leverage the benefits of *managed* offerings (Databricks)