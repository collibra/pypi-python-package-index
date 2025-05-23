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

class SessionConfiguration(object):
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
        'session_idle_timeout': 'int'
    }

    attribute_map = {
        'session_idle_timeout': 'sessionIdleTimeout'
    }

    def __init__(self, session_idle_timeout=None):  # noqa: E501
        """SessionConfiguration - a model defined in Swagger"""  # noqa: E501
        self._session_idle_timeout = None
        self.discriminator = None
        self.session_idle_timeout = session_idle_timeout

    @property
    def session_idle_timeout(self):
        """Gets the session_idle_timeout of this SessionConfiguration.  # noqa: E501


        :return: The session_idle_timeout of this SessionConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._session_idle_timeout

    @session_idle_timeout.setter
    def session_idle_timeout(self, session_idle_timeout):
        """Sets the session_idle_timeout of this SessionConfiguration.


        :param session_idle_timeout: The session_idle_timeout of this SessionConfiguration.  # noqa: E501
        :type: int
        """
        if session_idle_timeout is None:
            raise ValueError("Invalid value for `session_idle_timeout`, must not be `None`")  # noqa: E501

        self._session_idle_timeout = session_idle_timeout

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
        if issubclass(SessionConfiguration, dict):
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
        if not isinstance(other, SessionConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
