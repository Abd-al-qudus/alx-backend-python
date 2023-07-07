#!/usr/bin/env python3

"""this function takes in two arguments(str, [int, float]) k, v
    and returns a tuple of format(k, square_of(v))
    as (str, [int, float])"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """converts key-value pair to tuple(k, v**2)"""
    return (k, v**2)
