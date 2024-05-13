#!/usr/bin/env python3
'''
    module:
        test_utlis
        class:
            TestAccessNestedMap
'''

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    '''
        class for testing the method
        access_nested_map
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
            check if the method return the expected result
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''
            check if the KeyError raised successfully
            with the key expected
        '''
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        key = cm.exception.args[0]
        self.assertEqual(key, expected)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, payload):
        '''
            test the get_json method with patch the get method
        '''
        config = {'return_value.json.return_value': payload}
        patch('requests.get', **config).start()
        self.assertEqual(get_json(url), payload)


if __name__ == "__main__":
    unittest.main()
