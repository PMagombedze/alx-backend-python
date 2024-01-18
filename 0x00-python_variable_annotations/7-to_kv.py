"""
function to_kv
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns square of v and string rep of k"""
    return str(k), v**2
