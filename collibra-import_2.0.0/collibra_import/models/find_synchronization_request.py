# coding: utf-8

"""
    Collibra Import API

    <p>The Import API is an efficient way to load large volumes of data into the Collibra Data Governance Center. The API can automatically differentiate between creating and updating data.</p>  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FindSynchronizationRequest(object):
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
        'offset': 'int',
        'limit': 'int',
        'count_limit': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'count_limit': 'countLimit'
    }

    def __init__(self, offset=None, limit=None, count_limit=None):  # noqa: E501
        """FindSynchronizationRequest - a model defined in Swagger"""  # noqa: E501
        self._offset = None
        self._limit = None
        self._count_limit = None
        self.discriminator = None
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if count_limit is not None:
            self.count_limit = count_limit

    @property
    def offset(self):
        """Gets the offset of this FindSynchronizationRequest.  # noqa: E501


        :return: The offset of this FindSynchronizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this FindSynchronizationRequest.


        :param offset: The offset of this FindSynchronizationRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this FindSynchronizationRequest.  # noqa: E501


        :return: The limit of this FindSynchronizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this FindSynchronizationRequest.


        :param limit: The limit of this FindSynchronizationRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def count_limit(self):
        """Gets the count_limit of this FindSynchronizationRequest.  # noqa: E501


        :return: The count_limit of this FindSynchronizationRequest.  # noqa: E501
        :rtype: int
        """
        return self._count_limit

    @count_limit.setter
    def count_limit(self, count_limit):
        """Sets the count_limit of this FindSynchronizationRequest.


        :param count_limit: The count_limit of this FindSynchronizationRequest.  # noqa: E501
        :type: int
        """

        self._count_limit = count_limit

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
        if issubclass(FindSynchronizationRequest, dict):
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
        if not isinstance(other, FindSynchronizationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
