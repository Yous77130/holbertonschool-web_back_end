#!/usr/bin/env python3
"""Module fournissant une coroutine asynchrone de délai aléatoire."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Attend un délai aléatoire entre 0 et max_delay et le retourne."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
