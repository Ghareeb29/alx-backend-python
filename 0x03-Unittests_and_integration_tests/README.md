# 0x03-Unittests_and_integration_tests

## # Unittests and Integration Tests

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/alx-backend-python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-backend-python/0x03-Unittests_and_integration_tests
   ```

3. Ensure you have Python 3.7 installed:

   ```bash
   python3 --version
   ```

4. Install required packages:

   ```bash
   pip install parameterized
   ```

## Running Tests

To run the tests, use the following command:

```python
python3 -m unittest test_utils.py
```

## Tasks

### Task 0: Parameterize a unit test

* Create a `TestAccessNestedMap` class that inherits from `unittest.TestCase`
* Implement `TestAccessNestedMap.test_access_nested_map` method to test `utils.access_nested_map`
* Use `@parameterized.expand` to test the function with different inputs
* Verify that the function returns the expected results using `assertEqual`
