
# Building a state-of-the-art Data Ecosystem

- **Lakehouse architecture**
  - There is usually no need anymore to have a separate data warehouse. Even compared to modern
    MPP data warehouses such as Snowflake, a lakehouse architecture gives you all the same
    benefits (ACID transactions; ability to for less technical
    users to query data using SQL; fine-grained access control), but offer some additional advantages: Much easier to
    build machine learning on top; native support for semi- and unstructured data (and thus the
    ability to store all your data in a single system); no vendor lock-in.
    (even if you use Databricks' commercial offering, the delta format is open source); lower costs.
  - Major examples:
    - DataBricks Delta Lake (great - not cheap, but if you take into account how much engineering time it saves, it is probably much cheaper than using inferior tools.)
    - Apache Iceberg table format (New but rapidly growing – have to delve deep into how it compares to Delta Lake. Obviously, it is not *directly* comparable - but the reason I see it as the most serious competitor is because it is being integrated into the managed offerings of cloud providers – whereas AWS's offerings for even running Spark or Presto (Athena) are far inferior to Databricks).
- Like for machine learning, it usually makes sense to leverage the benefits of ***managed*
  offerings** - at the moment probably Databricks (potentially in combination with some more
  specialized providers). Managing infrastructure is undifferentiated
  heavy lifting, which - in the era of the cloud - is more efficiently provided by specialized
  companies that can leverage economies of scale.
