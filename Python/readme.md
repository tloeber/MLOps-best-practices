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
Java: 
Julia:

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

# Proper logging
- `logger.error` vs `logger.excception`: These two are often confused, because their behavior is 
so similar. Here is the key point: **If handling an exception, log it using `logger.
exception`. This ensures the stack trace is included in the logged message!**
(While it's also possible to include the stack trace using
`logger.error(msg, exec_info=True)`, there is no need to rely on this more verbose workaround.) 
Outside of exception handling, use `logger.error`. (Again, you could in principle also use 
  `logger.exception`, but this adds an awkward `NoneType: None` to the logged message because the 
  stack trace is missing.) 

