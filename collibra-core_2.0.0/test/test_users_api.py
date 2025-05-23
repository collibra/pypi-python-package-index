# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import collibra_core
from collibra_core.api.users_api import UsersApi  # noqa: E501
from collibra_core.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_user(self):
        """Test case for add_user

        Adds a new user  # noqa: E501
        """
        pass

    def test_add_user_groups_for_user(self):
        """Test case for add_user_groups_for_user

        Add a user to multiple user groups  # noqa: E501
        """
        pass

    def test_add_users(self):
        """Test case for add_users

        Adds multiple new users  # noqa: E501
        """
        pass

    def test_change_user(self):
        """Test case for change_user

        Changes the user with the information that is present in the request  # noqa: E501
        """
        pass

    def test_change_user_avatar(self):
        """Test case for change_user_avatar

        Changes the avatar for the user identified by the given ID  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Deletes the user with the given ID  # noqa: E501
        """
        pass

    def test_delete_user_avatar(self):
        """Test case for delete_user_avatar

        Deletes the avatar for the user identified by the given ID  # noqa: E501
        """
        pass

    def test_find_users(self):
        """Test case for find_users

        Returns users matching the given search criteria  # noqa: E501
        """
        pass

    def test_get_avatar_file(self):
        """Test case for get_avatar_file

        Get the avatar image for the user with the given ID  # noqa: E501
        """
        pass

    def test_get_current_user(self):
        """Test case for get_current_user

        Returns the current user, if logged in  # noqa: E501
        """
        pass

    def test_get_current_user_permissions(self):
        """Test case for get_current_user_permissions

        Returns the current user global permissions, if logged in  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Gets the user with the given ID  # noqa: E501
        """
        pass

    def test_get_user_by_email_address(self):
        """Test case for get_user_by_email_address

        Gets the user identified by given e-mail address  # noqa: E501
        """
        pass

    def test_get_user_required_license_type(self):
        """Test case for get_user_required_license_type

        Gets the required LicenseType for the given user  # noqa: E501
        """
        pass

    def test_remove_user_from_user_groups(self):
        """Test case for remove_user_from_user_groups

        Removes user from multiple user groups  # noqa: E501
        """
        pass

    def test_set_user_groups_for_user(self):
        """Test case for set_user_groups_for_user

        Sets user groups for the indicated user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
