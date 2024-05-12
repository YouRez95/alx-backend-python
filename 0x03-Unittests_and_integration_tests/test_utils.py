#!/usr/bin/env python3
'''
    module:
        test_utlis
        class:
            TestAccessNestedMap
'''

import unittest
from parameterized import parameterized
from client import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
