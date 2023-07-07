#!/usr/bin/env python3

"""This function takes in a mixed list and compute the sum"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return the mixed list sum"""
    return sum(mxd_lst)
