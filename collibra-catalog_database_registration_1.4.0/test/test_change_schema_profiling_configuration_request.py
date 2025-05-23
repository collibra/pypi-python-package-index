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
from collibra_catalog_database_registration.models.change_schema_profiling_configuration_request import ChangeSchemaProfilingConfigurationRequest  # noqa: E501
from collibra_catalog_database_registration.rest import ApiException


class TestChangeSchemaProfilingConfigurationRequest(unittest.TestCase):
    """ChangeSchemaProfilingConfigurationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChangeSchemaProfilingConfigurationRequest(self):
        """Test ChangeSchemaProfilingConfigurationRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = collibra_catalog_database_registration.models.change_schema_profiling_configuration_request.ChangeSchemaProfilingConfigurationRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
