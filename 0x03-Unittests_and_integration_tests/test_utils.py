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


class TestAccessNestedMap(TestCase):
    """Unit testing class for utils.access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a"], {"b": 2}),
            ({"a": {"b": 2}}, ["a", "b"], 2),
        ]
    )
    def test_access_nested_map(
        self: "TestAccessNestedMap",
        nested_map: dict,
        path: list,
        expected: any
    ) -> None:
        """Test that access_nested_map returns the expected value"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ["a"]),
            ({"a": 1}, ["a", "b"]),
        ]
    )
    def test_access_nested_map_exception(
        self: "TestAccessNestedMap", nested_map: dict, path: list
    ) -> None:
        """Test that access_nested_map raises a KeyError"""
        with self.assertRaises(KeyError) as exception:
            access_nested_map(nested_map, path)
        self.assertEqual(str(exception.exception), f"KeyError({path})")


class TestGetJson(TestCase):
    """Unit testing class for utils.get_json"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://example.com", {"payload": True}),
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(
        self: "TestGetJson", url: str, payload: dict, mock_get: mock
    ) -> None:
        """Test that get_json returns the expected value"""
        mock_get.return_value.json.return_value = payload
        self.assertEqual(get_json(url), payload)
