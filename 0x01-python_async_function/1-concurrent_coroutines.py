#!/usr/bin/env python3
""" Concurrent Coroutines """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """returns the list of all the delays (float values)."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [task for task in asyncio.as_completed(tasks)]
