"""Examples to go with engineering standards documentation."""

from typing import NoReturn


def function_that_always_fails_1() -> NoReturn:
    """Type hint is correct."""
    raise Exception

def function_that_never_fails_1() -> NoReturn:
    """Type hint is wrong - should be `None`"""
    print("success")

def function_that_never_fails_2() -> NoReturn:
    """Type hint is wrong - should be `str`"""
    return "success"

function_that_never_fails_1()
function_that_never_fails_2()
function_that_always_fails_1()
