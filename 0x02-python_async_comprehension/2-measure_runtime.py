#!/usr/bin/env python3
"""Measuring runtime"""
import asyncio
import time
from typing import Awaitable, float

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> Awaitable[float]:
    """measure runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
