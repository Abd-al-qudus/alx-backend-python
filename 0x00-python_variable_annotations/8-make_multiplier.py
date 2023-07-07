#!/usr/bin/env python3

"""this function takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns the multiplier function"""
    def multiply(value: float) -> float:
        """multiply the value by multiplier"""
        return value * multiplier

    return multiply
