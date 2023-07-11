#!/usr/bin/env python3

"""measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather."""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """async coroutine that measures the rumtime of parallel comprehensions"""
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    stop = time.perf_counter()
    return stop - start
