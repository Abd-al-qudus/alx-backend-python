#!/usr/bin/env python3

"""an async routine called wait_n that takes in
    2 int arguments (in this order): n and max_delay
    and spawn the wait_random function using the max_delay param"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random for n times and returns a list of floats"""
    tasks = [await task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
