#!/usr/bin/env python3
"""Module qui collecte des nombres via une comprehension asynchrone."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collecte 10 nombres aleatoires depuis async_generator et les retourne."""
    return [number async for number in async_generator()]
