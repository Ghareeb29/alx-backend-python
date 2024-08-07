#!/usr/bin/env python3
""" Concurrent Coroutines with a random waiting time"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """returns the list of all the delays (float values)."""
    delays = []

    async def add_delay():
        delay = await task_wait_random(max_delay)
        for i, d in enumerate(delays):
            if delay < d:
                delays.insert(i, delay)
                return
        delays.append(delay)

    await asyncio.gather(*(add_delay() for _ in range(n)))
    return delays
