# Existing standards

- Google's Rules for ML
- AWS Well-architected framework (ML lens)

# Creating a state-of-the-art ML ecosystem

- **Most companies are overly focused on *modeling*, which is just a small piece of the overall ML
  lifecycle.** Modeling is increasingly becoming a solved problem, as the best models for many use cases are
  becoming standardized, and we can often leverage pre-trained models.
  - AutoML & Declarative ML:
  - **MLOps: This is where we should focus our investment, in order to reliably productionize
    models!**
- That being said, there are use cases where modeling needs to be a focus area as well:
  These are companies which compete on the basis of ML, and there is an immediate impact of
  even incrementally better models on the bottom line. My point is, however, that this is the *exception
  rather than the norm* (and even for these types of use cases, figuring out how to
  reliably productionize ML models is a challenge that has to be solved *first*).
- Manual feature engineering is also becoming less important as available data size grows,
  because this allows us to use neural networks which automate feature engineering.

## Which specific tools to pick

I'm currently checking out how to piece together a better alternative to Sagemaker. The main questions
I'm trying to answer is how much better (and "better" what ways) of a platform you can build this way,
and how much more overhead this adds, and whether it speeds up your work once set up. Specific tools I'm
currently evaluating:

- Metaflow
- BentoML
- I'm currently exploring whether **Declarative ML** is mature enough. I think once it is, it may be
  the best approach for most ML use-cases. The main tool currently available is **Ludwig**, a
  framework open-sourced by Uber. A related open-source tool is
  [Horovod](https://github.com/horovod/horovod), which helps manage distributed training. There is also a
  commercial offering around Ludwig and Horovod, called **Predibase**. I'm very impressed by Ludwig, but I haven't used Predibase yet, so I can't comment on how well it works and how affordable it is.
- Next tool on my list: MLFlow

## Final Thoughts

- **Invest the time-savings you get from these suggestions** (leveraging free and
  open-source or managed solutions, start with off-the-shelf models, etc)
  **into striving for engineering excellence**. This is a much better investment and will
  greatly pay off soon by making your ML system **maintainable and scalable**. In order to make
  it easier to get started, I have documented my own insights as well as
  associated configurations in this repo.
- Remember that the ML infrastructure depends on a solid *data* infrastructure. See my
  discussion of the data side [here](../data-infrastructure/readme.md).
