#!/usr/bin/env python3

"""an async routine called wait_n that takes in
    2 int arguments (in this order): n and max_delay
    and spawn the wait_random function using the max_delay param"""


from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random for n times and returns a list of floats"""
    return [await wait_random(max_delay) for _ in range(n)]
