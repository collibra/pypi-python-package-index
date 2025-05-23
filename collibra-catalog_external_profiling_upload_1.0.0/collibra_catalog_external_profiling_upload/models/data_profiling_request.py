# coding: utf-8

"""
    Collibra Catalog External Profiling Upload API

    <p>This API is used to manually push profiling data.</p>  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DataProfilingRequest(object):
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
        'column_profiles': 'list[ColumnProfile]'
    }

    attribute_map = {
        'column_profiles': 'columnProfiles'
    }

    def __init__(self, column_profiles=None):  # noqa: E501
        """DataProfilingRequest - a model defined in Swagger"""  # noqa: E501
        self._column_profiles = None
        self.discriminator = None
        if column_profiles is not None:
            self.column_profiles = column_profiles

    @property
    def column_profiles(self):
        """Gets the column_profiles of this DataProfilingRequest.  # noqa: E501


        :return: The column_profiles of this DataProfilingRequest.  # noqa: E501
        :rtype: list[ColumnProfile]
        """
        return self._column_profiles

    @column_profiles.setter
    def column_profiles(self, column_profiles):
        """Sets the column_profiles of this DataProfilingRequest.


        :param column_profiles: The column_profiles of this DataProfilingRequest.  # noqa: E501
        :type: list[ColumnProfile]
        """

        self._column_profiles = column_profiles

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
        if issubclass(DataProfilingRequest, dict):
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
        if not isinstance(other, DataProfilingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
