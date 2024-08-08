#!/usr/bin/env python3
"""Async Generation"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """async comprehension"""
    numbers = [numbers async for numbers in async_generator()]
    return numbers
