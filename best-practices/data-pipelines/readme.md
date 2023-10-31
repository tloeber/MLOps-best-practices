# Data Pipeline

## Tools and libraries

### Considerations/requirements

- adoption costs: which tools are employees already familiar with?
- performance / scalability:
  - How much performance do we need for our use case?
  - Are we willing to incur the cost (monetary and in terms of time) of a less performant solution to avoid the adoption cost of more performant alternatives?
- maintainability
- How hard is it to write bug-free software? How easy is it to make changes to the logic? Does the syntax make it easy for bugs to hide (readability)? Does the tool violate the principle of least surprise? How easy is it to perform automated testing and validation?
- Maintenance cost
  - Highly influenced by maintainability
  - A pay premium is incurred for more advanced skills (e.g., Spark Scala)
  - It's also more expensive to hire employees with niche specialties that we cannot fully utilize all the time.

### Which to use?

#### Polars

- Like Pandas, run on a single machine, thereby avoiding complexity. More performant though (written in Rust; better at utilizing all cores).
- Requires learning a new syntax, but great option for intermediate-sized workloads that don't warrant the additional complexity that come from distributed workloads.

#### Dask

#### Ray
