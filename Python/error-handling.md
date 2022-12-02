# Should a method return an error, or handle it and return None?
- The most explicit option is to return error if it is not expected, and to return None if error is 
a possibility (e.g., of we are trying to get quantity of stock for a given product, but the product 
is not found because it is out of stock). The main advantage of this approach is that it 
  allows us to distinguish these two kinds of situations: If we get None, we don't have to worry 
  whether something went wrong.
  - In a language like Python where you can not tell from a function's signature which 
    exceptions it may raise, returning None offers the advantage that a function's signature can communicate 
    that it may return None (by using type annotations - which we should do anyway). The only 
    way to 
    document errors a function may raise is in the docstring, which not only gets overlooked easily 
    but even more importantly, there is no way for the static code analysis to leverage this 
    information. By contrast, if we add None to the return type, the type checker will complain 
    if you forget to handle this downstream.
- Conclusion:
  - **In a language like Python, I think it is safest to handle any errors as soon as possible and 
    return None. This way, our IDE's static analysis plug-in can alert us right away if we 
    call this function and forget to address the case where it returns None.** 
  - **In languages where there are other ways to deal with this issue, choose the more-explicit 
    option of passing the error on.**
    - E.g., in Scala or Rust, we can return wrapper types that either contain a valid result or 
      an Error or None. (See Scala's `Either` or `Option` types).
    - E.g., in Java we will be able to tell from the function signature, and the code will 
      not compile if you forget to handle a (non-runtime) exception.
  
# Exceptions within AWS Lambda functions: 
The best practices for dealing with exceptions in Lambda 
functions are different from what my most engineers are used to from traditional (non-serverless)
applications: There are only few cases in which we want to *handle* the 
exception *within* the lambda function: The most common case would be a lambda running an API: 
Obviously, we don't want this to crash, but instead return 
an error code to the user. 

However, **in most use cases, it is indeed best to 
let the execution fail**. For _asynchronous_ invocations, not handling an exception gives us the additional benefit that the 
function call will be retried a few more times later in case the failure 
was due to transient networking issues or another service being temporarily unavailable. If it 
still does not succeed, we want to handle this failure *outside of the Lambda function* 
by sending the input that raised the error to a **failure destinations**. E.g., we may handle the 
exception by executing a different lambda function, and we probably also want to persist the input 
that caused the exception to a SQS dead letter queue.

For *synchronous* invocation, we let the caller decide how to handle it.
(Note: double check whether it gets retried automatically - it's complicated.) 