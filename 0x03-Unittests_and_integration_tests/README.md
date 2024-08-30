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

### Task 1: Parameterize and patch

1. We've added a new method `test_access_nested_map_exception` to the `TestAccessNestedMap` class.

2. This method uses `@parameterized.expand` to test two scenarios:
   * An empty dictionary with a path of `("a",)`
   * A dictionary `{"a": 1}` with a path of `("a", "b")`

3. The method takes three parameters:
   * `nested_map`: The input dictionary
   * `path`: The path to access
   * `expected_exception_msg`: The expected message of the KeyError

4. We use the `assertRaises` context manager to check that a `KeyError` is raised when calling `access_nested_map` with the given inputs.

5. After the `assertRaises` block, we check that the exception message matches the expected message using `self.assertEqual`.

6. We've also updated the type annotations to include `Union` for more precise typing.

This implementation tests both that a `KeyError` is raised and that the exception message is correct for each input case. The test will fail if either the exception is not raised or if the exception message is not as expected.

### Task 2: Mock HTTP calls

1. We've imported `patch` and `Mock` from `unittest.mock`.

2. We've added a new class `TestGetJson` that inherits from `unittest.TestCase`.

3. In this class, we've implemented the `test_get_json` method, which is decorated with `@parameterized.expand` to test two scenarios:
   * URL: "<http://example.com>" with payload `{"payload": True}`
   * URL: "<http://holberton.io>" with payload `{"payload": False}`

4. We've also added the `@patch('requests.get')` decorator to mock the `requests.get` function.

5. In the `test_get_json` method:
   * We create a mock response object and set its `json` method to return the `test_payload`.
   * We set the return value of the mocked `get` function to this mock response.
   * We call `get_json` with the `test_url`.
   * We assert that `mock_get` was called once with `test_url` as an argument.
   * We assert that the result of `get_json` is equal to `test_payload`.

6. We've updated the type annotations to include the new types used in this test.

This implementation tests the `get_json` function without making actual HTTP requests, by mocking the `requests.get` function. It verifies that `get_json` calls `requests.get` with the correct URL and returns the expected payload.

### Task 3: Parameterize and patch as decorators

1. We've added a new class `TestMemoize` that inherits from `unittest.TestCase`.

2. Inside `TestMemoize`, we've implemented the `test_memoize` method.

3. Within `test_memoize`, we define the `TestClass` as specified in the task, with `a_method` and `a_property` (decorated with `@memoize`).

4. We use `patch.object` to mock the `a_method` of `TestClass`, setting its return value to 42.

5. In the test:
   * We create an instance of `TestClass`.
   * We call `a_property` twice and store the results.
   * We assert that both calls to `a_property` return 42.
   * We use `assert_called_once()` to verify that `a_method` was only called once, demonstrating that the memoization worked.

6. We've updated the type annotations to include the new types used in this test.

This implementation tests the `memoize` decorator by verifying that:

* The correct result (42) is returned when calling the memoized property.
* The underlying method (`a_method`) is only called once, even when the property is accessed multiple times.

This addition completes the implementation of the `TestMemoize` class with the `test_memoize` method as requested in the task. It demonstrates understanding of memoization and correctly tests the behavior of the `memoize` decorator.

### Task 4: Parameterize and patch as decorators

1. We import the necessary modules: `unittest` for creating test cases, `patch` from `unittest.mock` for mocking, `parameterized` for parametrizing tests, and `GithubOrgClient` from the `client` module.

2. We define the `TestGithubOrgClient` class that inherits from `unittest.TestCase`.

3. Inside this class, we implement the `test_org` method:
   * It's decorated with `@parameterized.expand` to test with two different organization names: "google" and "abc".
   * It's also decorated with `@patch('client.get_json')` to mock the `get_json` function used in the `GithubOrgClient` class.

4. In the `test_org` method:
   * We create an instance of `GithubOrgClient` with the given `org_name`.
   * We call the `org` method on this instance.
   * We use `assert_called_once_with` to verify that `get_json` was called exactly once with the correct URL.

5. The `if __name__ == '__main__':` block allows the tests to be run directly from this file.

This test ensures that:

* The `org` method of `GithubOrgClient` is calling `get_json` with the correct URL.
* It's tested for multiple organization names.
* No actual HTTP requests are made during testing, as `get_json` is mocked.

### Task 5: Mocking a property

1. We've added a new method `test_public_repos_url` to the `TestGithubOrgClient` class.

2. In this method:
   * We define a `known_payload` dictionary that mimics the structure of the data we expect from the `org` property.

   * We use `patch.object` as a context manager to mock the `org` property of `GithubOrgClient`. We use `PropertyMock` as the `new_callable` to properly mock a property.

   * Inside the context manager:
     * We create an instance of `GithubOrgClient`.
     * We call the `_public_repos_url` property on this instance.
     * We assert that the result matches the `repos_url` from our known payload.
     * We also assert that the mocked `org` property was called once.

This test ensures that:

* The `_public_repos_url` property is correctly extracting the `repos_url` from the data returned by the `org` property.
* It's doing so without making any actual HTTP requests, as the `org` property is mocked to return our known payload.

### Task 6: More patching

1. We've added a new method `test_public_repos` to the `TestGithubOrgClient` class.

2. This method is decorated with `@patch('client.get_json')` to mock the `get_json` function.

3. In this method:
   * We define a `test_payload` list that mimics the structure of the data we expect from the API call.

   * We set the return value of the mocked `get_json` to our `test_payload`.

   * We use `patch.object` as a context manager to mock the `_public_repos_url` property of `GithubOrgClient`. We use `PropertyMock` as the `new_callable` to properly mock a property.

   * Inside the context manager:
     * We create an instance of `GithubOrgClient`.
     * We call the `public_repos` method on this instance.
     * We assert that the result matches the expected list of repo names extracted from our test payload.
     * We assert that both the mocked `_public_repos_url` property and the mocked `get_json` function were called once.

This test ensures that:

* The `public_repos` method is correctly extracting the repo names from the data returned by the API call.
* It's doing so without making any actual HTTP requests, as both `get_json` and `_public_repos_url` are mocked.
* The method is calling `get_json` with the correct URL (indirectly tested by mocking `_public_repos_url`).

### Task 7: Parameterize

1. We've added a new method `test_has_license` to the `TestGithubOrgClient` class.

2. This method is decorated with `@parameterized.expand` to test multiple inputs for the `has_license` method.

3. We've defined two test cases:
   * A repo with a license key that matches the input license key (expected to return True)
   * A repo with a license key that doesn't match the input license key (expected to return False)

4. In this method:
   * We create an instance of `GithubOrgClient`.
   * We call the `has_license` method with the provided `repo` and `license_key`.
   * We assert that the result matches the expected boolean value.

This test ensures that:

* The `has_license` method correctly identifies when a repo has a specific license.
* It correctly returns False when the repo doesn't have the specified license.
* It works correctly with different input structures.

### Task 8: Integration tests: fixtures:

### Task 9: Integration tests:

To be implemented.
