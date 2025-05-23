# coding: utf-8

"""
    Collibra Protect API

    This API allows you to manage groups.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProviderMaskingMappings(object):
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
        'provider': 'Provider',
        'mappings': 'list[MaskingMapping]'
    }

    attribute_map = {
        'provider': 'provider',
        'mappings': 'mappings'
    }

    def __init__(self, provider=None, mappings=None):  # noqa: E501
        """ProviderMaskingMappings - a model defined in Swagger"""  # noqa: E501
        self._provider = None
        self._mappings = None
        self.discriminator = None
        self.provider = provider
        self.mappings = mappings

    @property
    def provider(self):
        """Gets the provider of this ProviderMaskingMappings.  # noqa: E501


        :return: The provider of this ProviderMaskingMappings.  # noqa: E501
        :rtype: Provider
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ProviderMaskingMappings.


        :param provider: The provider of this ProviderMaskingMappings.  # noqa: E501
        :type: Provider
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def mappings(self):
        """Gets the mappings of this ProviderMaskingMappings.  # noqa: E501


        :return: The mappings of this ProviderMaskingMappings.  # noqa: E501
        :rtype: list[MaskingMapping]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this ProviderMaskingMappings.


        :param mappings: The mappings of this ProviderMaskingMappings.  # noqa: E501
        :type: list[MaskingMapping]
        """
        if mappings is None:
            raise ValueError("Invalid value for `mappings`, must not be `None`")  # noqa: E501

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
        if issubclass(ProviderMaskingMappings, dict):
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
        if not isinstance(other, ProviderMaskingMappings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
