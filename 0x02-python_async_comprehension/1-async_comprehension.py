#!/usr/bin/env python3

"""This script import the async generator function
    in task 0 and use list comprehension"""


import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """returns the list of numbers from generator with async comprehension"""
    return [num async for num in async_generator()]
