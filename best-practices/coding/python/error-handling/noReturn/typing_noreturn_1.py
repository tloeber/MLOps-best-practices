"""Examples to go with engineering standards documentation."""

from typing import NoReturn

def function_that_may_fail_1(fail: bool) -> str:
    """Type hint does NOT document failure possibility."""
    if fail:
        raise Exception
    else:
        return "success"


def function_that_may_fail_2(fail: bool) -> str | NoReturn:
    """Type hint does document failure possibility"""
    if fail:
        raise Exception
    else:
        return "success"

# These calls both will raise Exception - at least in the second case, we would
# like the type checker to warn us because it can be inferred from type hints.
function_that_may_fail_1(fail=True)
function_that_may_fail_2(fail=True)
