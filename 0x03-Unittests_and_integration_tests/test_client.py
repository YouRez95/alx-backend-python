#!/usr/bin/env python3
'''
    module:
        test_client
        class:
            TestGithubOrgClient
'''

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        '''
            test public repos url
        '''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as m:
            payload = {"repos_url": "something"}
            m.return_value = payload
            test = GithubOrgClient('')
            self.assertEqual(test._public_repos_url, payload['repos_url'])


if __name__ == "__main__":
    unittest.main()
