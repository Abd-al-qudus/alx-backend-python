#!/usr/bin/env python3

"""an async routine called wait_n that takes in
    2 int arguments (in this order): n and max_delay
    and spawn the wait_random function using the max_delay param"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.
    '''
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
