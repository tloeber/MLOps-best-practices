# How to write robust Python code
## Typing
  Typing is key! While it's not intended to be used for performance optimization, it can catch a 
  plethora of errors through static code analysis. Mastering typing requires only a small upfront 
  investment but quickly pays off: You can save 
  a lot of time, as this static type checkers will catch your errors right as you make them. In 
  addition, it also makes the code easier to read because it provides useful documentation! 
  While it  is also possible to write this documentation in the form  of comments or docstrings, 
  we all know that it's virtually impossible to force everyone to keep these up to date. By 
  contrast, type hints can be enforced in the CI pipeline - so they offer the only realistic 
  solution to keep documentation of input and output types up to date!
  - If possible, use Python 3.10 to get new syntax for type hints. If not possible, import new 
    syntax using `from __future__ import annotations`
  - Perform type checking in IDE to give the engineer instant feedback, AND enforce it by running 
    mypy in CI/CD pipeline.
  - Leverage **enum.Enum** if you want to allow only a subset of valid values.
  - Leverage **typing.Final** to make a variable/object immutable.
  - Leverage type aliases for better readability and documentation of output types, and for 
    easier changeability. (Add example.)
  - Explicitly distinguish class and instance variables!
    - E.g., don't use class variables to set defaults for instance variables. (Just set 
      default directly in `__init__()`.)
    - Annotate class variables using **typing.ClassVar**. Every variable that is defined in a 
      class outside of a method should carry this annotation!
  - Enforce schemas of data using pydantic.
    - Speaking of which, avoid mixing *data structures* like pydantic classes (or Python's 
      inbuilt dataclasses) with "proper" classes! Data structures should primarily expose data 
      (though I 
      have occasionally found the need to add a few simple methods), whereas proper classes 
      encapsulate data and expose behavior. (See 'Clean Code' by Uncle Bob.)