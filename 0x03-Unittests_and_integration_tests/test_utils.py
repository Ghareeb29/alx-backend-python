#!/usr/bin/env python3
"""
Module for testing the utils module.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json
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
        Test that access_nested_map raises a KeyError
        with the expected message.

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


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: Dict,
                      mock_get: Mock) -> None:
        """
        Test that utils.get_json returns the expected result.

        Args:
            test_url (str): The URL to test.
            test_payload (Dict): The expected payload.
            mock_get (Mock): The mocked requests.get function.

        Returns:
            None
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
