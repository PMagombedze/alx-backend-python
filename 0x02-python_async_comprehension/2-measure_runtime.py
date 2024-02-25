#!/usr/bin/env python3
"""
concurrency
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Collect 10 random numbers then return the 10 random numbers.
    """
    begin: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop: float = time.perf_counter()
    return (stop - begin)
