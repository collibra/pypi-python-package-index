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

class DatabaseTag(object):
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
        'id': 'str',
        'name': 'str',
        'maskings': 'list[GroupMasking]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'maskings': 'maskings'
    }

    def __init__(self, id=None, name=None, maskings=None):  # noqa: E501
        """DatabaseTag - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._maskings = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        self.maskings = maskings

    @property
    def id(self):
        """Gets the id of this DatabaseTag.  # noqa: E501

        The id of database tag  # noqa: E501

        :return: The id of this DatabaseTag.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseTag.

        The id of database tag  # noqa: E501

        :param id: The id of this DatabaseTag.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this DatabaseTag.  # noqa: E501

        The name of database tag  # noqa: E501

        :return: The name of this DatabaseTag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseTag.

        The name of database tag  # noqa: E501

        :param name: The name of this DatabaseTag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def maskings(self):
        """Gets the maskings of this DatabaseTag.  # noqa: E501


        :return: The maskings of this DatabaseTag.  # noqa: E501
        :rtype: list[GroupMasking]
        """
        return self._maskings

    @maskings.setter
    def maskings(self, maskings):
        """Sets the maskings of this DatabaseTag.


        :param maskings: The maskings of this DatabaseTag.  # noqa: E501
        :type: list[GroupMasking]
        """
        if maskings is None:
            raise ValueError("Invalid value for `maskings`, must not be `None`")  # noqa: E501

        self._maskings = maskings

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
        if issubclass(DatabaseTag, dict):
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
        if not isinstance(other, DatabaseTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
