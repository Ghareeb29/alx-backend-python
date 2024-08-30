#!/usr/bin/env python3
"""
Module for testing the utils module.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple[str], expected: Any
    ) -> None:
        """
        Test that access_nested_map returns the expected result.

        Args:
            nested_map (Dict): The nested dictionary to access.
            path (Tuple[str]): The path of keys to access the nested value.
            expected (Any): The expected result.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), "a"),
            ({"a": 1}, ("a", "b"), "b"),
        ]
    )
    def test_access_nested_map_exception(
        self, nested_map: Dict, path: Tuple[str], expected_exception_msg: str
    ) -> None:
        """
        Test that access_nested_map
        raises a KeyError with the expected message.

        Args:
            nested_map (Dict): The nested dictionary to access.
            path (Tuple[str]): The path of keys to access the nested value.
            expected_exception_msg (str): The expected exception message.

        Returns:
            None
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{expected_exception_msg}'")


if __name__ == "__main__":
    unittest.main()
