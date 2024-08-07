# 0x01-python_async_function

## Task 1

    1. Imports:

    ```python
    import asyncio
    from typing import List
    wait_random = __import__('0-basic_async_syntax').wait_random
    ```

    We import the necessary modules: `asyncio` for asynchronous programming, `List` for type hinting, and `wait_random` from the previous file.

    2. Function definition:

    ```python
    async def wait_n(n: int, max_delay: int) -> List[float]:
    ```

    This defines an asynchronous function `wait_n` that takes two integer arguments: `n` and `max_delay`. It returns a list of floats.

    3. Initialize the delays list:

    ```python
    delays = []
    ```

    This empty list will store the delay values in ascending order.

    4. Inner function definition:

    ```python
    async def add_delay():
    ```

    This is an asynchronous inner function that will be called for each of the `n` iterations.

    5. Get a random delay:

    ```python
    delay = await wait_random(max_delay)
    ```

    We await the result of `wait_random(max_delay)` to get a random delay.

    6. Insert the delay in the correct position:

    ```python
    for i, d in enumerate(delays):
        if delay < d:
            delays.insert(i, delay)
            return
    delays.append(delay)
    ```

    This loop finds the correct position to insert the new delay to maintain ascending order. If no smaller delay is found, it's appended to the end.

    7. Spawn `n` coroutines:

    ```python
    await asyncio.gather(*(add_delay() for _ in range(n)))
    ```

    This line creates `n` coroutines of `add_delay()` and runs them concurrently using `asyncio.gather()`.

    8. Return the result:

    ```python
    return delays
    ```

    The function returns the list of delays, which is now in ascending order.

    This implementation ensures that the delays are added to the list in ascending order without using `sort()`. It maintains the order as the delays are generated concurrently, which is more efficient than sorting afterward, especially for large `n`.
