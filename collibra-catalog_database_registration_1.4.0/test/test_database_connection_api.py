# coding: utf-8

"""
    Collibra Catalog Database Registration API

    This API allows you to manage the **metadata ingestion**, **profiling**, and **classification** of databases via Edge.  It provides the following functionalities: - Query and synchronize the database and schema connections. - Register the databases to be ingested, profiled and classified. - Configure and trigger the metadata ingestion of databases. - Configure and trigger the profiling and classification of databases.   # noqa: E501

    OpenAPI spec version: 1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import collibra_catalog_database_registration
from collibra_catalog_database_registration.api.database_connection_api import DatabaseConnectionApi  # noqa: E501
from collibra_catalog_database_registration.rest import ApiException


class TestDatabaseConnectionApi(unittest.TestCase):
    """DatabaseConnectionApi unit test stubs"""

    def setUp(self):
        self.api = DatabaseConnectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_database_connections(self):
        """Test case for find_database_connections

        List database connections  # noqa: E501
        """
        pass

    def test_get_database_connection(self):
        """Test case for get_database_connection

        Retrieve a database connection  # noqa: E501
        """
        pass

    def test_refresh_database_connections(self):
        """Test case for refresh_database_connections

        Refresh database connections from the data source  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
