#!/usr/bin/env python3
"""
Async Generator
"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    Loop 10 times, each time asynchronously
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
