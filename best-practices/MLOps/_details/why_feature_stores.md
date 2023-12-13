# Why is feature story must have?

I have mentioned a feature store as a must-have in various sections, scattered across the data science and MLOps best practices. This document serves to collect a summary of these benefits in a single place in order to better communicate the big picture of why a feature store is definitely worth the investment:

- Ensure features are computed in the same way for training and serving (to avoid training-serving skew)
  - This is especially challenging if using different compute engines. For example, a common architecture is to use pure python during inference but Spark for batch transforms of large amounts of historical training data. For example, [the Hopsworks feature store allows solving this](https://content.hopsworks.ai/hubfs/Feature%20Store%20Summit%202023/FS%20Summit%2023%20-%20Hopsworks.pdf) by allowing the user to define the transformations as [pandas UDFs](https://www.databricks.com/blog/2017/10/30/introducing-vectorized-udfs-for-pyspark.html). These run the same in both environments (while avoiding the large performance penalty of pure Python UDFs).
- Share features between teams to:
  - Avoid duplicate work
  - Ensure different teams use the *same definition* of how to define and operationalize important business concepts.
- Support time travel
  - A common question from the business is what the data or predictions looked like at a given date. However, without the ability for time travel, this question is usually both time-consuming and error-prone to answer.
  - Makes it much quicker and simpler to prevent information leakage from the training into test set
- lineage / provenance
  - data versioning is a must-have for *reproducability*
  - much easier *debugging* of data issues
  - makes *remediating* the effects of data issues easier, because it becomes possible to find out which model versions were trained on faulty data.
  - Can be a necessity to achieve compliance.
- Low latency serving (using *online* feature store). Note that while the proportion of use cases where this is a must-have is small, it is growing rapidly. Thus, it will likely become a must-have for many companies in the near future.
