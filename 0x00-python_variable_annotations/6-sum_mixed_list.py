#!/usr/bin/env python3


"""
function sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of list as float"""
    return float(sum(mxd_lst))
