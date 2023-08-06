# Existing coding standards
PEP-8 vs Google Python Style Guide 

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
scripting and rigorous production use, the benefits seem big enough to try if we can make 
it work. Most of the criticisms of Python I encounter are misguided, because they focus on how 
it is *most commonly used** - which unfortunately is full of bad practices - rather than on what 
the language can do if **used appropriately**. **I think it's clear that Python is not a good 
choice for any serious production use unless paired with an understanding - and enforcement - of 
engineering best practices**, such as a having a dependable test suite, using type hints, and 
static code analysis. **Instead, the real question is** 
- **which exact practices we should follow** in order to compensate for Python's weaknesses,
- **whether these safeguards are enough to make Python a good choice** for production use in 
  general,**
- and for **which *types* of use cases** it is a good choice in particular?


### Alternative languages
**Java**: It's ok, but not the most *readable* language (e.g., unnecessarily verbose, inability 
to use keyword arguments and default parameter values for methods), all of which make it easier for 
bugs to hide.

**Scala**: Fixes many of the specific problems of Java: What I like most about Scala is that you 
can still draw on the many insights on object-oriented design patterns that have mainly been 
accumulated in the Java community, and which have been 
proven to be great ways to make software systems *maintainable*. At the same time, however, Scala 
also gives you the option to leverage ideas from functional programming, which can sometimes be a 
better choice (e.g., when building data pipelines, as Spark demonstrates). It can even make 
sense to mix insights from both paradigms in the same line of code: For example, even when
following a standard OO design and implementing a method on a class, we can borrow the idea from 
functional programming that a good way to deal with a function/method having to return a null 
value is to wrap the return value into an `Either` type: This forces the client to explicitly handle 
both the case where we get a valid result and where the value is null, avoiding the danger of 
Java's infamous NullPointerException.

Unfortunately, though, the Scala syntax not only allows you to use the language as a *better* Java, 
but it also makes it easy to write code in a (much) *less* readable way - especially if you go wild 
with some of its advanced functional programming (FP) capabilities that are 
foreign to engineers coming from most other languages. 
For Scala, the danger is much higher than in other languages that one Scala expert ends up 
creating an advanced codebase that cannot be maintained by anyone else on the 
team (which may only become apparent once that one Scala expert leaves.) 

Obviously, the readability highly depends on the reader's Scala/FP expertise, but it's important 
to consider this as a downside of the language - rather than blaming individual engineer's lack 
of knowledge if they don't understand what the code does. The main cost of this need for Scala 
specialists is that 1) talent is harder to come by, and 2) once hired, it is harder to leverage 
these highly specialized engineers somewhere else. The latter is not just a problem if technology 
choices change *in the future*, but already *right from the start* if the Scala portion of our 
work is still too small to require 100% of a team's capacity. 
Thus, it's crucial for teams and organizations to decide whether they want to use such a 
language at all, and - if so - *to what extent they want to limit the 
use of advanced features to reduce the above risks.* (How to set these standards 
is of course not straightforward, especially if you want to set them at the _organizational_ 
level.) 

I've also sometimes found it harder than expected to achieve seemingly basic tasks, 
and debugging sometimes hasn't been straightforward either. But I'm not sure yet 
whether this is still part of the learning curve on my end.

Overall, I'm still making up my mind about Scala. The only place where 
it would generally be my first choice is for Spark: While you don't really get any substantial 
performance benefits in newer versions of Spark, the 
syntax is pretty similar to PySpark anyway so it doesn't add much additional complexity, 
and *debugging actually tends to be easier than what you get when the magic of talking to Spark 
through Python breaks down.* 

**Julia**:

### Conclusion
Overall, to paraphrase a famous saying, I think Python is the worst programming language, except 
for all the others. I can live without strong typing for now, as long as I'm in an environment 
where engineering excellence is enforced in order to make up for the dangers that are inherent 
in Python's flexibility. Still, I'll also stay on the lookout for other languages that 
combine Python's readability and expressiveness with greater guardrails that constrain bad
coding practices as much as possible (and ideally also give better performance).

## Typing
Typing is key if you are using Python for anything more than one-off scripting. Check out my 
detailed reasoning and tips for how to do it [here](./typing/readme.md).


## The most common Python bugs I see:
- Incompatible types – this is the easiest problem to avoid - all it takes is the disciplines to use
  [type hints](./typing/readme.md), and your IDE will point out your mistakes right as you make 
  them!
  - Probably the most common case is forgetting to handle the case where a variable is `None`.
    (This is like a NullPointerException in Java).

## Proper logging
- `logger.error` vs `logger.excception`: These two are often confused, because their behavior is 
so similar. Here is the key point: **If handling an exception, log it using `logger.
exception`. This ensures the stack trace is included in the logged message!**
(While it's also possible to include the stack trace using
`logger.error(msg, exec_info=True)`, there is no need to rely on this more verbose workaround.) 
Outside of exception handling, use `logger.error`. (Again, you could in principle also use 
  `logger.exception`, but this adds an awkward `NoneType: None` to the logged message because the 
  stack trace is missing.) 

