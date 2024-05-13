#!/usr/bin/env python3
'''
    module:
        test_client
        class:
            TestGithubOrgClient
'''

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    '''
        github org client tests
    '''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, name, mock):
        '''
            test org
        '''
        test = GithubOrgClient(name)
        test.org()
        mock.called_with_once(test.ORG_URL.format(org=name))


if __name__ == "__main__":
    unittest.main()
