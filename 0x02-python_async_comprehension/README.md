# 0x02-python_async_comprehension

## Task 0

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

## Task 2

1. Import the `async_comprehension` function from the previous task.
2. Define an `async` function named `measure_runtime`.
3. Inside the function, use `asyncio.gather` to execute `async_comprehension` four times in parallel.
4. Measure the total runtime by calculating the time difference between the start and end of the `asyncio.gather` call.
5. Return the total runtime.

Now, let's explain why the total runtime is roughly 10 seconds:

1. The `async_generator` function in the previous task is defined to yield a random number every 1 second, for a total of 10 times.
2. The `async_comprehension` function collects 10 random numbers from the `async_generator` function, which means it takes approximately 10 seconds to complete.
3. In the `measure_runtime` function, we execute `async_comprehension` four times in parallel using `asyncio.gather`.
4. Since the four instances of `async_comprehension` run in parallel, the total runtime is approximately the runtime of a single `async_comprehension` call, which is 10 seconds.

Therefore, the total runtime for the `measure_runtime` coroutine is around 10 seconds, as the four parallel executions of `async_comprehension` do not add significant overhead to the overall runtime.
