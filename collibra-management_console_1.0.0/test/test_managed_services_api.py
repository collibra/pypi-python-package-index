# coding: utf-8

"""
    Collibra Management Console

    Collibra Management Console public REST API \\n Please ensure that cookies are not present within the API request. Including cookies within the call will cause 403 error.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import collibra_management_console
from collibra_management_console.api.managed_services_api import ManagedServicesApi  # noqa: E501
from collibra_management_console.rest import ApiException


class TestManagedServicesApi(unittest.TestCase):
    """ManagedServicesApi unit test stubs"""

    def setUp(self):
        self.api = ManagedServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change1(self):
        """Test case for change1

        Change an existing managed service  # noqa: E501
        """
        pass

    def test_find_all2(self):
        """Test case for find_all2

        List all managed services  # noqa: E501
        """
        pass

    def test_get_by_id3(self):
        """Test case for get_by_id3

        Get a managed service by ID  # noqa: E501
        """
        pass

    def test_start1(self):
        """Test case for start1

        Start a managed service  # noqa: E501
        """
        pass

    def test_stop1(self):
        """Test case for stop1

        Stop a managed service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
