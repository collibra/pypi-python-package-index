# coding: utf-8

"""
    Collibra Protect API

    This API allows you to manage groups.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import collibra_protect
from collibra_protect.api.prescriptive_paths_api import PrescriptivePathsApi  # noqa: E501
from collibra_protect.rest import ApiException


class TestPrescriptivePathsApi(unittest.TestCase):
    """PrescriptivePathsApi unit test stubs"""

    def setUp(self):
        self.api = PrescriptivePathsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_prescriptive_path(self):
        """Test case for add_prescriptive_path

        Add a new prescriptive path  # noqa: E501
        """
        pass

    def test_delete_prescriptive_path(self):
        """Test case for delete_prescriptive_path

        Delete a prescriptive path  # noqa: E501
        """
        pass

    def test_get_prescriptive_path(self):
        """Test case for get_prescriptive_path

        Retrieve a prescriptive path  # noqa: E501
        """
        pass

    def test_list_asset_types(self):
        """Test case for list_asset_types

        List asset types supported by Protect  # noqa: E501
        """
        pass

    def test_list_prescriptive_paths(self):
        """Test case for list_prescriptive_paths

        Lists all available prescriptive paths  # noqa: E501
        """
        pass

    def test_patch_prescriptive_path(self):
        """Test case for patch_prescriptive_path

        Update a prescriptive path  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
