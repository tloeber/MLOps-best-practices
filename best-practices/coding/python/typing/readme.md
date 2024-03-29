# Typing
Typing is key if you are using Python for anything more than one-off scripting. By using type 
hints plus a type checker, we get a viable alternative to strongly typed languages!  
Python's type hints won't be used for performance optimization by default, though there are independent projects such as PyPy which have had some success with this. More importantly, however, they help catch a 
plethora of errors through static code analysis, so they are essential to writing robust code. 
Like automated tests, static typing also provide the further benefit of making it much easier to keep the code base healthy: Not only do types make automated factory tools more powerful, because they provide additional semantics to our IDE, but static typing also provides an additional safety net that greatly reduces the risk that refactoring will break production, hence reducing the incentive to push our problems into the future. Similarly, having access to static analysis makes keeping dependencies up to date much easier, because our IDE can alert us right away if any package upgrade resulted in changed function/method/class signatures which are incompatible with our code.

Mastering typing requires only a small upfront investment but quickly pays off: You can save 
a lot of time, as the IDE can alert you to your errors right as you make them. Due to the
*instant* nature of this feedback - which has been shown to be of vital factors in 
general studies of learning - it also helps you avoid the same kinds of errors in the future. 

Furthermore, type hints make code easier to read because they provide useful 
documentation! While it's also conceivable to write this documentation in the form  of 
comments or docstrings, 
we all know that it's virtually impossible to force everyone to keep these up to date. By 
contrast, type hints can be enforced in the CI/CD pipeline - so they offer the only realistic 
solution to keep documentation of types up to date!

Finally, they also provide these extra benefits:
- You need to write less unit tests to assert the same behavior (because you can focus on testing only valid input types, and can rely on static analysis to automatically catch invalid types.)
- enables better IDE autocompletion
- Enables IDE to provide better refactoring recommendations

By the way, type hints in Python are similar to Java's way of adding annotations such 
as `@Nullable` or `@NotNull` to make the code more robust against NullPointerExceptions.  


## Concrete guidelines:
- If possible, use Python 3.10 to get new syntax for type hints. If not possible, import new 
  syntax using `from __future__ import annotations`
- Perform type checking in IDE to provide instant feedback, but also enforce 
  adherence by running mypy in CI/CD pipeline.
- Leverage **enum.Enum** or **typing.Literal** if you want to allow only a subset of valid values.
- Leverage **typing.Final** to make a variable immutable. E.g., `self._unix_timestamp: 
  Final[int] = unix_timestamp`.
  - Decision to make: Only use `Final` if mutating would be a semantic error, or also to 
    document that a variable *happens* to be immutable, e.g. because there wouldn't be 
    any reason (that we can think of) to change it, or because a class does not have any method 
    defined to update a private variable?
    - Pro of using `Final` in all these cases: It provides useful *documentation*. For an 
      engineer skimming the code for the first time, it might not be as obvious as for the 
      person writing the code that there is no built-in way  to change a variable.
    - Cons: 
      - Adds clutter - `Final` is easy to understand by itself, but combined with type 
        annotation - especially if it is a nested type - the type annotation becomes increasingly 
        complicated.
      - We may fail to foresee some use cases in which it does make sense to change a variable.
        - Retort: Not a big deal, then we simply change the type hint! Having to explicitly make 
          this change would likely be productive, as it makes different assumptions 
          (presumably of different team members) explicit, and forces them to get on the same page 
          whether a variable should be changeable or not!
      - Preliminary decision: Err on the side of including `Final`, because the only real 
        downside is that it makes stipends slightly more complicated, but there are ways to 
        address that (e.g., use a type alias for composite types). However, don't be too purist 
        about it - if it seems too obvious or unimportant, leave it out.
- Leverage **type aliases**. They can provide 
  - better readability and documentation of return variables (because by contrast to a function's 
    *parameters*, return values don't have a name that is included in the function's signature - 
    so the only way to leverage descriptive naming is through type aliases!)
  - easier changeability of type (because we only need to change the type in one place, namely 
    where the type alias is *defined*, but not in all the places where it is *used*). 
  - (Add example.)
- Type hints are especially useful for telling us if a function's argument or return value is 
  allowed to be 'None': `def get_name(self) -> str | None:`
- Being forced to write type hints actually *forces you to think in more detail about the 
  function or method you are writing*, thereby leading to better design. E.g., how do I need to  
  handle null values? This is similar to 
  how TDD - or striving for good naming - forces you to think about what exactly you want your 
  function to do.
- Explicitly distinguish between class and instance variables!
  - E.g., don't use class variables to set defaults for instance variables. Just set 
    default directly in `__init__()`. If that is not possible – e.g., because you 
    want to be sure it is inherited by subclasses - then be explicit and make it a class 
    variable that has a different name than the instance variable, e.g.: `default_name: 
    ClassVar[str] = 'Unknown'; def __init__(self, name=default_name)`.
  - Annotate class variables using **typing.ClassVar**. Every variable that is defined in a 
    class outside of a method should carry this annotation! E.g., `_data_directory: ClassVar[Path] = ...`
    - Decision to make: For the standard case of immutable class variables, should we just 
      use typing.Final instead of ClassVar, [since it fulfills the same purpose?](https://peps.python.org/pep-0591/)
      - pro: stricter, since it also enforces immutability (and it's not possible to combine 
        both using `Final[ClassVar[str]]`.)
      - con: less explicit about the distinction between class and instant variables.
      - Decision: If reassignment would be dangerous, use `Final`; if reassignment is not intended 
        but simply not needed, be explicit and use ClassVar.
- Enforce schemas of data using pydantic.
  - Speaking of which, avoid mixing *data structures* like pydantic classes (or Python's 
    inbuilt dataclasses) with "proper" classes! Data structures should primarily expose data 
    (though I 
    have occasionally found the need to add a few simple methods), whereas proper classes 
    encapsulate data and expose behavior. (See 'Clean Code' by Uncle Bob.)
