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

## Task 2

1. Import necessary modules:

    - Import wait_n from the previous file
    - Import time module
    - Import asyncio module

2. Define the measure_time function:

    - Parameters: n (int) and max_delay (int)
    - Return type: float

3. Inside measure_time:

    - Record the start time using time.time()
    - Run the wait_n(n, max_delay) function using asyncio.run()
    - Record the end time using time.time()
    - Calculate total time by subtracting start time from end time
    - Calculate and return average time by dividing total time by n

- This implementation measures the total execution time of wait_n(n, max_delay) and returns the average time per operation. The time.time() function gives us a float representing the current time, which we use to calculate the elapsed time. We use asyncio.run() to execute the asynchronous wait_n function in a synchronous context.

## Task 3

Here's an algorithm for the problem you've described, without actual code:

1. Import required modules:
   - Import `wait_random` from the file `0-basic_async_syntax`
   - Import `asyncio` module

2. Define a regular function named `task_wait_random`:
   - Parameter: `max_delay` (integer)
   - Return type: `asyncio.Task`

3. Inside `task_wait_random`:
   - Use `asyncio.create_task()` function to create a new task
   - Pass the coroutine object returned by `wait_random(max_delay)` to `create_task()`
   - Return the created task

This algorithm will create and return an `asyncio.Task` object that, when run, will execute the `wait_random` coroutine with the given `max_delay`.

The key points of this algorithm are:

- It's a regular function, not an async function
- It doesn't await the result of `wait_random`
- It creates and returns a task, which is a wrapper around the coroutine

This approach allows for more flexible handling of the asynchronous operation, as the caller can decide when and how to await the task or run it concurrently with other tasks.
