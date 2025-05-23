# coding: utf-8

"""
    Collibra Protect API - Partner

    API to retrieve the data access rule set it needs to synchronize. This API is targeted to be used by Collibra Partners.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RowFilter(object):
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
        'operator': 'RowFilterOperator',
        'values': 'list[str]'
    }

    attribute_map = {
        'operator': 'operator',
        'values': 'values'
    }

    def __init__(self, operator=None, values=None):  # noqa: E501
        """RowFilter - a model defined in Swagger"""  # noqa: E501
        self._operator = None
        self._values = None
        self.discriminator = None
        if operator is not None:
            self.operator = operator
        if values is not None:
            self.values = values

    @property
    def operator(self):
        """Gets the operator of this RowFilter.  # noqa: E501


        :return: The operator of this RowFilter.  # noqa: E501
        :rtype: RowFilterOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this RowFilter.


        :param operator: The operator of this RowFilter.  # noqa: E501
        :type: RowFilterOperator
        """

        self._operator = operator

    @property
    def values(self):
        """Gets the values of this RowFilter.  # noqa: E501


        :return: The values of this RowFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this RowFilter.


        :param values: The values of this RowFilter.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(RowFilter, dict):
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
        if not isinstance(other, RowFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
