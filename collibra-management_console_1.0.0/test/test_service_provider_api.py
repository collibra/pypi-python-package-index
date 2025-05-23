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
from collibra_management_console.api.service_provider_api import ServiceProviderApi  # noqa: E501
from collibra_management_console.rest import ApiException


class TestServiceProviderApi(unittest.TestCase):
    """ServiceProviderApi unit test stubs"""

    def setUp(self):
        self.api = ServiceProviderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_slave_to_repository_cluster(self):
        """Test case for add_slave_to_repository_cluster

        Add a slave repository to a repository cluster  # noqa: E501
        """
        pass

    def test_create_repository_cluster(self):
        """Test case for create_repository_cluster

        Create a new repository cluster  # noqa: E501
        """
        pass

    def test_find_all4(self):
        """Test case for find_all4

        List all service providers  # noqa: E501
        """
        pass

    def test_get_by_id5(self):
        """Test case for get_by_id5

        Get a service provider by ID  # noqa: E501
        """
        pass

    def test_remove4(self):
        """Test case for remove4

        Delete a service provider  # noqa: E501
        """
        pass

    def test_remove_from_repository_cluster(self):
        """Test case for remove_from_repository_cluster

        Remove a repository from the cluster  # noqa: E501
        """
        pass

    def test_set_master_in_repository_cluster(self):
        """Test case for set_master_in_repository_cluster

        Set the master repository of a repository cluster  # noqa: E501
        """
        pass

    def test_start2(self):
        """Test case for start2

        Start a service provider  # noqa: E501
        """
        pass

    def test_stop2(self):
        """Test case for stop2

        Stop a service provider  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
