#!/usr/bin/env python3
"""Measuring runtime"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """returns the runtime"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    Totat_time = end_time - start_time
    return Totat_time / n
