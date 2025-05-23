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

class DatabaseCustomMasking(object):
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
        'mappings': 'list[MaskingMappings]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mappings': 'mappings'
    }

    def __init__(self, id=None, name=None, mappings=None):  # noqa: E501
        """DatabaseCustomMasking - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._mappings = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if mappings is not None:
            self.mappings = mappings

    @property
    def id(self):
        """Gets the id of this DatabaseCustomMasking.  # noqa: E501

        The id of database custom masking  # noqa: E501

        :return: The id of this DatabaseCustomMasking.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseCustomMasking.

        The id of database custom masking  # noqa: E501

        :param id: The id of this DatabaseCustomMasking.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DatabaseCustomMasking.  # noqa: E501

        The name of database custom masking  # noqa: E501

        :return: The name of this DatabaseCustomMasking.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseCustomMasking.

        The name of database custom masking  # noqa: E501

        :param name: The name of this DatabaseCustomMasking.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mappings(self):
        """Gets the mappings of this DatabaseCustomMasking.  # noqa: E501


        :return: The mappings of this DatabaseCustomMasking.  # noqa: E501
        :rtype: list[MaskingMappings]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this DatabaseCustomMasking.


        :param mappings: The mappings of this DatabaseCustomMasking.  # noqa: E501
        :type: list[MaskingMappings]
        """

        self._mappings = mappings

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
        if issubclass(DatabaseCustomMasking, dict):
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
        if not isinstance(other, DatabaseCustomMasking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
