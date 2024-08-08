#!/usr/bin/env python3
"""Async Generation"""
import asyncio
import random


async def async_generator() -> None:
    """async generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)