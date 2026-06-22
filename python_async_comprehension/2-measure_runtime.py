#!/usr/bin/env python3
"""Module qui mesure le temps de quatre comprehensions en parallele."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 fois en parallele et mesure le temps."""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start
