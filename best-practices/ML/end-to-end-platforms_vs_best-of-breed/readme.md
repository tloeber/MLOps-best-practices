Last content update: Dec 2022

# End-to-end platforms vs specialized

- End-to-end platforms generally won't support the most cutting-edge use-cases - but for the vast amount of
  companies that's ok. Many companies still struggle with deploying even a simple model into
  production, so there are plenty of low-hanging fruits, and any of the major ML platforms will
  be powerful enough for these generic use cases.
- If we mix-and-match specialized solutions - whether open source or managed services from
  third-party providers – ***integrating* these solutions into an
  existing cloud infrastructure is always much harder than going with something
  native to your cloud provider. Thus, the easiest way to get started is to simply leverage
  the ML platform of your cloud providers** (Sagemaker for AWS, Vertex AI for GCP), or Managed MLFlow for companies who
  already use Databricks. Definitely check out if any of these options
  meets your needs before choosing something more complex.
- However, the choice for end-to-end platforms is generally limited to only the one from your
  cloud provider, because there are no major cloud-agnostic end-to-end solutions.  (A few years
  back, H2O was a good choice, but not sure where they went.) For companies
  who are already Databricks customers, Managed MLFlow is a second option, but most companies only
  have a single choice if they want to go with an end-to-and platform.
  The reason why it usually doesn't make sense to use an ML platform from a *different* cloud
  provider than where your data and
  downstream consumers of the outputs live is that data-transfer cost is massive, and many tasks
  would become much harder, e.g. identity and access management, monitoring for data-drift, etc. Thus, whether
  an end-to-end platform makes sense not just depends on the ML use case, but also which option
  you have available based on your current cloud provider:
  - I'm most familiar with **Amazon Sagemaker**, but I'm not a great fan of it. I really want it
    to be a viable solution – and it probably still is the best option for delivering
    value most quickly - but overall I feel like it does not deliver on its promises, and is often
    frustrating to use. My main critique is that it is not designed with proper interfaces between
    the different components, so they don't fit together as much as you would expect from
    something claiming to be an end-to-end platform – which kind of defeats the whole point.
  - For the minority of companies who are on Google cloud, **Vertex AI** is probably the strongest
    offering, since it's basically a managed version of Kubeflow. I'm not familiar enough with it,
    though, to provide any recommendation on it.
  - Databricks' **MLFlow** is known mainly for experiment tracking and as a model registry, but
    with recent
    feature additions (such as pipelines), it is moving towards becoming an end-to-end ML platform.
    Since these features are still pretty new, they are probably still less mature. On the other
    hand, Databricks is known to create software that is great to use, so I would definitely
    explore it if already using Databricks Delta Lake, etc.
  - I'm not familiar with Azure's ML offerings, but the fact that discussions of ML platforms
    usually only bring up Sagemaker and Vertex AI make me skeptical whether Azure has a viable
    option.
- In terms of vendor risk, it's probably a tie:
  - On the one hand, the major cloud providers and Databricks have been around for long enough
    that you don't have to worry about them going away soon. By contrast, virtually all of the
    companies solving specialized problems in ML lifecycle
    have sprung up in the last few years, and it is not clear yet how much consolidation will take
    place and who the winners will be.
  - On the other hand, much of the specialized offerings tend to be managed services on top of
    a core open-source product. So in the worst case, even if these companies go out of business, the
    open-source frameworks they are based on will not go away with them. The same is true for
    Databricks. (While Kubeflow, on which Vertex AI is based, is also open source, it is orders
    of magnitude harder to maintain yourself, compared to the specialized tools.)

- That said, while end-to-end platforms may *do* the job, the question, is do we want to **pick
  the *best* tool for each job** by mixing-and-matching specialized solutions for different
  stages of the ML lifecycle. E.g., use Tecton's feature platform, MLFlow for
  experiment tracking and as a model registry, BentoML for model serving, etc. (Of course, you
  still have the option of using a *subset* of your cloud provider's ML platform for specific parts
  of the job, if it makes sense to do so). Specialized providers live and die by the quality of their
  product, so they have a greater incentive to offer the best experience. By contrast, for the major
  cloud providers, ML tooling is just a small part of their offering, and thus it may not
  necessarily be their focus area.
- **Note that "best" may not only mean that you get additional
  features, but it can also mean that you get a better *user experience* or *ability to iterate on
  more quickly*.**
  - If it was just about getting additional features, the answer would be more
    straightforward: In that case, end-to-end solutions would probably be the best choice for
    companies that need to deliver value very quickly (early-stage start-ups, as well as potentially even established companies where the business side
    is not willing to make the investment before they see any concrete value).
  - However, if it also gives you a better user experience and the ability to iterate
    more quickly, going with specialized solutions may pay off very quickly (potentially even
    within say a couple of months). In that case, it could be the preferred option for most use cases.
- A final consideration is *how difficult* it is to set up and maintain an ML platform
  consisting of specialized solutions, compared to going with your cloud provider's default
  offering.  If this difference is substantial, it raises the question
  whether it would require a higher level of talent than some companies can retain.

# Conclusion

Overall, I think it's hard to make a general recommendation at this point. In the end, it
mainly comes down to the question *how much better* specialized providers are, *in
what ways* they are better, and *how much extra work* they require. Unfortunately, a clear
answer to these questions hasn't emerged yet, because the landscape is constantly changing.
