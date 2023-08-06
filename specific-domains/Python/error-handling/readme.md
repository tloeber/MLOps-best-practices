# Should a method return an exception or handle it and return None
- The most explicit option is to only return an exception if it is not expected from the 
  method's contract. On the other hand, if an exception is a possibility - e.g., looking up a 
  value in the dictionary without first checking if the key exists – we instead return None. 
  The main advantage of this approach is that it 
  allows us to *distinguish these two kinds of situations*: If we get None, we don't have to worry 
  whether something went wrong, because it's not a "real" exception.
- **In a language like Python - where you can not tell from a function's signature which 
  exceptions it may raise -  returning None offers the advantage that a function's signature can 
  alert the caller (by means of the type annotations) that this case needs to be handled. 
  Otherwise, the only way to 
  document which exceptions a function may raise is in the docstring, but there is no way for the static
  code analysis to leverage this 
  information.** While the typing module has the `NoReturn` and `Never` types to annotate a 
  function that does not return, [this does not work for this purpose](../_img/). **By 
  contrast, if we add None to the return type, the type checker will complain 
  if you forget to handle this if you call this function but forget to handle the case of `None`.** 
- Conclusion:
  - **In a language like Python, I think it is safest to handle any exceptions as soon as possible and 
    return None. This way, our IDE's static analysis plug-in can alert us right away if we 
    call this function and forget to address the case where it returns None.** 
  - **In languages where there are other ways to deal with this issue, choose option 1 
    because it is more-explicit: Whenever an exception is not expected, let 
    downstream clients handle it.** In addition, **take care a compile-time or static analysis 
    exception is raised if downstream client forgets to do this.**
    - E.g., in Java we will be able to tell from the function signature which exceptions it may raise, 
      and the code will not compile if you forget to handle a (non-runtime) exception. (Of 
      course, in Java we should take additional steps to guard against NullPointerExceptions, which 
      [require us to add annotations - similar to Python - to communicate this to static analysis 
      tools](https://www.beyondjava.net/getting-rid-of-the-nullpointerexception-in-2020#Nullchecks%20with%20static%20code%20analyzers)). 
    - E.g., in Scala or Rust, we can return wrapper types that either contain a valid result or 
      an exception or None, but that need to be explicitly unwrapped downstream.  
      
# Exceptions within AWS Lambda functions: 
The best practices for dealing with exceptions in Lambda 
functions are different from what my most engineers are used to from traditional (non-serverless)
applications: There are only few cases in which we want to *handle* the 
exception *within* the lambda function: The most common case would be a lambda running an API: 
Obviously, we don't want this to crash, but instead return an error code to the user. 

However, **in most use cases, it is indeed best to 
let the execution fail**. For _asynchronous_ invocations, not handling an exception gives us the additional benefit that the 
function call will be retried a few more times later in case the failure 
was due to transient networking issues or another service being temporarily unavailable. If it 
still does not succeed, we want to handle this failure *outside of the Lambda function* 
by sending the input that raised the exception to a **failure destinations**. E.g., we may handle the 
exception by executing a different lambda function, and we probably also want to persist the input 
that caused the exception to a SQS dead letter queue.

For *synchronous* invocation, we let the caller decide how to handle it.
(Note: double check whether it gets retried automatically - it's complicated.) 