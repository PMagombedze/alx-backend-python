#!/usr/bin/env python3


"""
function safe_first_element
"""


from typing import Union, Sequence, Any


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """annotate"""
    if lst:
        return lst[0]
    else:
        return None
