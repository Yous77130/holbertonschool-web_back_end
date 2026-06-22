#!/usr/bin/env python3
"""Module qui fournit un generateur asynchrone de nombres aleatoires."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Boucle 10 fois, attend 1s et yield un nombre entre 0 et 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
