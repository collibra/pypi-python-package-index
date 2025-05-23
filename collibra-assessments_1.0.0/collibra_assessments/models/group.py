# coding: utf-8

"""
    Collibra Assessments API

    This API allows you to interact with the Assessments application in a programmatic way and perform actions such as retrieving data from conducted assessments or triggering new assessments.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from collibra_assessments.models.base_group import BaseGroup  # noqa: F401,E501

class Group(BaseGroup):
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
        'name': 'str'
    }
    if hasattr(BaseGroup, "swagger_types"):
        swagger_types.update(BaseGroup.swagger_types)

    attribute_map = {
        'name': 'name'
    }
    if hasattr(BaseGroup, "attribute_map"):
        attribute_map.update(BaseGroup.attribute_map)

    def __init__(self, name=None, *args, **kwargs):  # noqa: E501
        """Group - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self.discriminator = None
        self.name = name
        BaseGroup.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this Group.  # noqa: E501

        The name of the Collibra group.  # noqa: E501

        :return: The name of this Group.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Group.

        The name of the Collibra group.  # noqa: E501

        :param name: The name of this Group.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(Group, dict):
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
        if not isinstance(other, Group):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
