#!/usr/bin/env python3

"""this module is writen using the basic syntax of async await"""


import random
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """This function waits for a random value between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await sleep(delay)
    return delay
