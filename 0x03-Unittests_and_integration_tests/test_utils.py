#!/usr/bin/env python3
"""Tests for utils where we:
- Create a TestAccessNestedMap class
that inherits from unittest.TestCase

- Implement the TestAccessNestedMap.test_access_nested_map method
to test that the method returns what it is supposed to.

- Decorate the method with @parameterized.expand
to test the function with provided inputs
"""
from unittest import TestCase, mock
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


@parameterized.expand(
    [
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ]
)
class TestAccessNestedMap(TestCase):
    """Unit testing class for utils.access_nested_map"""

    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected value"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
