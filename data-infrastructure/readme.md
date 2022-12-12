
# Building a state-of-the-art Data Ecosystem
- **Delta lake** and **Lakehouse architecture**
  - There is often no need anymore to have a separate data warehouse. Even compared to modern
    MPP data warehouses such as Snowflake, a delta lake gives you all the same 
    benefits (ACID transactions; ability to for less technical 
    users to query data using SQL; fine-grained access control), but offer some additional advantages: Much easier to 
    build machine learning on top; native support for semi- and unstructured data (and thus the 
    ability to store all your data in a single system); no vendor 
    lock in 
    (even if you use Databricks' commercial offering, the delta format is open source); lower costs.
- Like for machine learning, it usually makes sense to leverage the benefits of ***managed* 
  offerings** - at the moment probably Databricks, together with more specialized providers. Managing infrastructure is undifferentiated 
  heavy lifting, which - in the era of the cloud - is more efficiently provided by specialized 
  companies that can leverage economies of scale.