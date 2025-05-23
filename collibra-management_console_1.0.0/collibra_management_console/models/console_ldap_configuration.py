# coding: utf-8

"""
    Collibra Management Console

    Collibra Management Console public REST API \\n Please ensure that cookies are not present within the API request. Including cookies within the call will cause 403 error.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConsoleLdapConfiguration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_ldap_super_users': 'bool',
        'default_role': 'str',
        'enabled': 'bool',
        'servers': 'list[ConsoleLdapServer]',
        'timeout': 'int',
        'user_fields': 'ConsoleLdapUserFields'
    }

    attribute_map = {
        'allow_ldap_super_users': 'allowLdapSuperUsers',
        'default_role': 'defaultRole',
        'enabled': 'enabled',
        'servers': 'servers',
        'timeout': 'timeout',
        'user_fields': 'userFields'
    }

    def __init__(self, allow_ldap_super_users=None, default_role=None, enabled=None, servers=None, timeout=None, user_fields=None):  # noqa: E501
        """ConsoleLdapConfiguration - a model defined in Swagger"""  # noqa: E501
        self._allow_ldap_super_users = None
        self._default_role = None
        self._enabled = None
        self._servers = None
        self._timeout = None
        self._user_fields = None
        self.discriminator = None
        if allow_ldap_super_users is not None:
            self.allow_ldap_super_users = allow_ldap_super_users
        if default_role is not None:
            self.default_role = default_role
        self.enabled = enabled
        if servers is not None:
            self.servers = servers
        self.timeout = timeout
        if user_fields is not None:
            self.user_fields = user_fields

    @property
    def allow_ldap_super_users(self):
        """Gets the allow_ldap_super_users of this ConsoleLdapConfiguration.  # noqa: E501


        :return: The allow_ldap_super_users of this ConsoleLdapConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._allow_ldap_super_users

    @allow_ldap_super_users.setter
    def allow_ldap_super_users(self, allow_ldap_super_users):
        """Sets the allow_ldap_super_users of this ConsoleLdapConfiguration.


        :param allow_ldap_super_users: The allow_ldap_super_users of this ConsoleLdapConfiguration.  # noqa: E501
        :type: bool
        """

        self._allow_ldap_super_users = allow_ldap_super_users

    @property
    def default_role(self):
        """Gets the default_role of this ConsoleLdapConfiguration.  # noqa: E501


        :return: The default_role of this ConsoleLdapConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._default_role

    @default_role.setter
    def default_role(self, default_role):
        """Sets the default_role of this ConsoleLdapConfiguration.


        :param default_role: The default_role of this ConsoleLdapConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["READ", "ADMIN", "SUPER"]  # noqa: E501
        if default_role not in allowed_values:
            raise ValueError(
                "Invalid value for `default_role` ({0}), must be one of {1}"  # noqa: E501
                .format(default_role, allowed_values)
            )

        self._default_role = default_role

    @property
    def enabled(self):
        """Gets the enabled of this ConsoleLdapConfiguration.  # noqa: E501


        :return: The enabled of this ConsoleLdapConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConsoleLdapConfiguration.


        :param enabled: The enabled of this ConsoleLdapConfiguration.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def servers(self):
        """Gets the servers of this ConsoleLdapConfiguration.  # noqa: E501


        :return: The servers of this ConsoleLdapConfiguration.  # noqa: E501
        :rtype: list[ConsoleLdapServer]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this ConsoleLdapConfiguration.


        :param servers: The servers of this ConsoleLdapConfiguration.  # noqa: E501
        :type: list[ConsoleLdapServer]
        """

        self._servers = servers

    @property
    def timeout(self):
        """Gets the timeout of this ConsoleLdapConfiguration.  # noqa: E501


        :return: The timeout of this ConsoleLdapConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ConsoleLdapConfiguration.


        :param timeout: The timeout of this ConsoleLdapConfiguration.  # noqa: E501
        :type: int
        """
        if timeout is None:
            raise ValueError("Invalid value for `timeout`, must not be `None`")  # noqa: E501

        self._timeout = timeout

    @property
    def user_fields(self):
        """Gets the user_fields of this ConsoleLdapConfiguration.  # noqa: E501


        :return: The user_fields of this ConsoleLdapConfiguration.  # noqa: E501
        :rtype: ConsoleLdapUserFields
        """
        return self._user_fields

    @user_fields.setter
    def user_fields(self, user_fields):
        """Sets the user_fields of this ConsoleLdapConfiguration.


        :param user_fields: The user_fields of this ConsoleLdapConfiguration.  # noqa: E501
        :type: ConsoleLdapUserFields
        """

        self._user_fields = user_fields

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConsoleLdapConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConsoleLdapConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
