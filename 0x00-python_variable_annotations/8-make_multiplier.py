#!/usr/bin/env python3


"""
function make_multiplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that multiplies a float by multiplier"""
    def make_multiplier_func(n: float) -> float:
        return n * multiplier
    return make_multiplier_func
