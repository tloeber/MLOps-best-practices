# How to write robust Python code
## Why I have a love-hate relationship with Python
### Can a single language satisfy two very different use cases - explorative scripting and reliable production use?
This will always be a challenge, but there are also some great benefits to it - namely 
that it's much easier to productionize models without having to translate them into another 
language. Translating Python or R models into Java used to be a common way of 
productionizing models, but it came with a lot of challenges: 
- Translation can lead to slight 
differences in model behavior - both because humans are inevitably going to make some mistakes 
when rewriting the code in another language, but 
also because of differences in implementations that are usually insubstantial but can 
occasionally make a sizable difference. 
- It decreases Agility: 
  - Extra lead-time for deployment, since it requires translation.
  - Dis-incentivizes quick iteration because of this extra step.
  - More costly, since you are doing the work twice. (Remember, engineers' time is often the 
   highest cost!)

Thus, even though there are some challenges to using a single language for both explorative 
scripting as well as rigorous production use, the benefits seem big enough to try if we can make 
it work. These 
substantial benefits explain the popularity of Python in machine learning, but I think that 
there are ways to much bettwe, so that we can get all of these benefits at a lower cost (i.e., 
greater reliability):

### Alternative languages
Scala:
JavaL: 
Julia:

### Conclusion
Overall, to paraphrase a famous saying, I think Python is the worst programming language, except 
for all the others. I can live without strong typing for now, as long as I'm in an environment 
where engineering excellence is enforced in order to make up for the dangers that are inherent 
in Python's flexibility. Still, I'll also stay on the lookout for other languages that 
combine Python's readability and expressiveness with greater guardrails that constrain bad
coding practices as much as possible (and ideally also give better performance). 

## Typing
  Typing is key if you are using Python for anything more than one-off scripting. By using type 
  hints plus a type checker, we get a viable alternative to strongly typed languages! While 
  Python's type hints won't be used for performance optimization, they help catch a 
  plethora of errors through static code analysis, so they are essential to writing robust code. 
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

  Concrete guidelines:
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
          address that (e.g., use a type alias for composite types). However, don't be to purist 
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


# Proper logging
- `logger.error` vs `logger.excception`: These two are often confused, because their behavior is 
so similar. Here is the key point: **If handling an exception, log it using `logger.
exception`. This ensures the stack trace is included in the logged message!**
(While it's also possible to include the stack trace using
`logger.error(msg, exec_info=True)`, there is no need to rely on this more verbose workaround.) 
Outside of exception handling, use `logger.error`. (Again, you could in principle also use 
  `logger.exception`, but this adds an awkward `NoneType: None` to the logged message because the 
  stack trace is missing.) 

