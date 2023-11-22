# Pandas best practices

## General

- Make sure you are using version 2.x

## Performance

- Use Arrow backend
  - Greatest performance improvement is for strings (and nested objects?)
  - Added bonus: Better handling of missing values (e.g., integer type allow missing values, rather than requiring storing the whole column as a float, which is inefficient)
  - Use method chaining (also improves readability)
  - Understand how Pandas handles views versus copies
    - Use df.loc[]
      - Exceptions?
      - Definitely don't use double-indexing, i.e. df['a'][df.b == 0]
    - Use 2.x's copy-on-write setting

## Reliability

-

## Maintainability

- Be intentional about what to run in Jupyter notebook
  - Extract functions into separate python files
  - It's okay to run tests in notebook at first (using %ipytest), but tests should be handed over as proper python files. (The right time to do that conversion is probably when merging the code into a shared branch.)

## Productivity

- Run notebook in IDE, not browser
- Leverage iPython magics:
  - Profiling (see [here](https://jakevdp.github.io/PythonDataScienceHandbook/01.07-timing-and-profiling.html) for more detailed explanation).
    - %%time / %%timeit
    - %%ptime: Measures to what extent the code takes advantage of multiple threads (e.g., if constrained by the GIL)
    - %%lprun: Line-by-line profiler (e.g., can show whether function is vectorized or not).
  - %%ipytest?
  - iPython debugger? (Last time I tried it, it didn't work that well, but might have improved by now)
