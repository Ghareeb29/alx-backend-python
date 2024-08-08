# 0x02-python_async_comprehension

## Task 0

Here's a suggested algorithm for the `async_generator` coroutine:

1. Import the necessary modules (e.g., `asyncio`, `random`). Also, from typing import AsyncGenerator
2. Define an `async` function named `async_generator` and type-annotated as AsyncGenerator.
3. Inside the function, use a `for` loop to iterate 10 times.
4. Within each iteration of the loop:
   a. Use `asyncio.sleep(1)` to wait for 1 second asynchronously.
   b. Generate a random number between 0 and 10 using `random.uniform(0, 10)`.
   c. Yield the generated random number.
5. Return the coroutine.

## Task 1

Here's the suggested algorithm for the `async_comprehension` coroutine:

1. Import the `async_generator` function from the previous task.
2. Define an `async` function named `async_comprehension`.
3. Inside the function, use an asynchronous list comprehension to collect 10 random numbers from the `async_generator` coroutine.
   a. Iterate 10 times using a `for` loop.
   b. Within each iteration, use the `async for` syntax to get the next random number from the `async_generator` coroutine and add it to the list.
4. Return the list of 10 random numbers.
