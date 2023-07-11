#!/usr/bin/env python3

"""This is a coroutine called async generator that
    yields async iterables"""


import random
import asyncio
import typing


async def async_generator() -> typing.Generator[int, None, None]:
    """yield a random value between 1 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
