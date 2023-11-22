# What the "NoReturn" and "Never" return types can and cannot do
## NoReturn vs Never
`Never` is the newer version of `NoReturn`, starting in Python 3.11. The 
[Python documentation](https://docs.python.org/3.11/library/typing.html#typing.Never) is unclear
whether the two are exactly equivalent: On the one hand, it mentions additional functionality 
for `Never`, but on the other hand it also says that type checkers treat them equivalently.

For now, I still use `NoReturn` for backwards compatibility.

## What NoReturn/Never are for
This type annotation tells you that a function should never return, in particular because it always
raises an error. 

The [documentation for `Never`](https://docs.python.org/3.11/library/typing.html#typing.Never) also 
mentions that it can be used to annotate a function's return type if is *never called*, though 
the associated example actually annotates the function's *argument* - not the return type - with 
`Never`. I have not looked into the case of a function that should never be called in much detail,
though, because I can't think of any situation in which this would be useful. Thus, my discussion 
will focus on annotating that a function may raise an exception.

The first function (line 6) in the code below demonstrates the proper use of `NoReturn`. The 
next two functions show that type checkers correctly complains if NoReturn is used for a function 
that does in fact return. (Note that if a Python function does not contain any explicit return 
statement, it will return `None`.)
See the output of running mypy at the bottom, and Pylance's immediate feedback inline and on the 
right.


![alt text](../../../_img/noReturn_working.png)

## What NoReturn/Never can NOT do
My main motivation for checking out `NoReturn` was that I was [hoping that it
could be used to communicate to static code analyzers that a function may raise an error that 
needs to be handled by the caller](../readme.md#should-a-method-return-an-error-or-handle-it-and-return-none) 
. That is, if we add `NoReturn` or `Never` as *one of multiple* 
return types (see line 13 in screenshot below for an example), the static analysis should complain 
if a caller does not handle any 
exception. (Note: Since NoReturn does not tell us *which specific kinds* of exceptions the call may 
raise, the type checker still won't be able to assert that any downstream exception handling is 
*exhaustive*. For that, the 
static analysis would have to check directly which exception the code raises, which is 
more advanced.) 

Still, if the caller fails to include *any* exception handling - which is 
presumably the most common mistake - I would at least want to be warned that this is 
probably a bug. However, as the below screenshot shows, neither mypy nor 
Pylance currently detect this issue:

![alt text](../../../_img/noReturn_not_supported.png)

The first function can raise an error, depending on the input, but this is *not* documented in 
the output type. We would hope this to be flagged by the type checker, but unfortunately it is 
not. 

Conversely, the second function *does* document the possibility of of a raised exception in the 
output type annotation. This function is then called  in line 23 *without* any exception 
handling (with an input that will in fact raise an exception). We would hope that the type checker 
detects this, but unfortunately it does not.

Thus, **the only way we currently have in Python to guard against the downstream caller forgetting 
to handle such an exception is to handle it where it occurs, and instead return `None`.**
If we add `None` to the output type, the type checker will complain if you perform any operation 
with the output 
that is not supported for `None`. See my more detailed discussion of this problem 
[here](../readme.md#should-a-method-return-an-error-or-handle-it-and-return-none).
