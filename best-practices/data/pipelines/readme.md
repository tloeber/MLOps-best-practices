# Tools and libraries

## Considerations/requirements

- performance / scalability:
  - How much performance do we need for our use case?
    - Data size (or any of our data sets too big to fit into memory of a single machine?)
    - Are computations getting too slow?
- cost
  - adoption costs: which tools are employees already familiar with? how hard is it to switch to another tool (similar syntax, etc.)?
    - Are we willing to incur the cost (monetary and in terms of time) of a less performant solution to avoid the adoption cost of more performant alternatives?
  - Maintenance cost
    - Highly influenced by maintainability (see below)
    - A pay premium is incurred for more advanced skills (e.g., Spark Scala)
    - It's also more expensive to hire employees with niche specialties that we cannot fully utilize all the time.
- maintainability
  - Characteristics of the tool/library:
    - "Quality": How hard is it to write bug-free software? (E.g., does the syntax make it easy for bugs to hide (readability)?) How easy is it to make changes to the logic? Does the tool violate the principle of least surprise? How easy is it to integrate automated testing and other quality gates into the workflow?
    - How do these characteristics vary for simple versus complex use-cases? Is it optimized for one side of the spectrum, or does it have enough flexibility to scale with the requirements (e.g., by gradually adding optional quality gates)?
  - Use-case-specific considerations:
    - How complex is our use case? For a less complex use case
    - How important is avoiding bugs for our use case?
      - What is at stake? (How bad would it be for customers, regulatory and compliance risks, liability risk, etc.)
      - If we get quick and accurate feedback if there is a problem, bugs are less costly (e.g., we predict a web customer's purchase decision). By contrast, if the feedback only comes much later, bugs are much more costly (Zillow).
- Fit with organizational culture
  - Using more advanced tool may require a higher level of engineering excellence than can be cultivated in some organizations (at least in the short term)
  - Retaining the right talent is not just a matter of being able to afford to pay premium.

## Which to use?

### Data formats

#### Arrow

- Allows working with data sets that are bigger than available memory, because not the whole data is loaded into memory at the same time.

#### Parquet

#### csv

#### Conclusion

### Data processing

#### Pandas

- Pandas is the baseline, because it has been around long enough that it is mature and widely known.
- Great support for plotting (which is not always the case with its alternatives).
- Quality/readability:
  - Not all syntax is ideal, and there are a number of quirks, but it's good enough.
    - Some of these problems have been addressed with the recent release of Pandas 2.0 (e.g., view vs copy).
    - Definitely not enough of a reason to switch, but improved readability will hopefully be an additional benefit of new frameworks once we need to switch to them for performance reasons.

#### Polars

- Like Pandas, run on a single machine, thereby avoiding complexity. More performant though (written in Rust; better at utilizing all cores).
- Requires learning a new syntax, but great option for intermediate-sized workloads that don't warrant the additional complexity that come from distributed workloads.

#### Dask

#### Ray

#### Spark

#### Open questions

How easy is it to switch between these frameworks if we use Arrow? E.g., switch back to pandas for plotting?

#### Conclusion

- For existing projects that use pandas (which is the vast majority):
  - The first step is to take advantage of new pandas features – in particular, using the Arrow backend.
  - Switching to Polars gives additional benefits for speeding up computations. But since it is still limited by the memory of a single machine, migration may not be worth the cost.
  - If neither of these is enough, and you are willing to incur the complexity cost of a distributed system, consider these alternatives:

- New projects:
