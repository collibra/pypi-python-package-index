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

class PrescriptivePathAssetType(object):
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
        'asset_type_id': 'str',
        'relation': 'PrescriptivePathRelation'
    }

    attribute_map = {
        'asset_type_id': 'assetTypeId',
        'relation': 'relation'
    }

    def __init__(self, asset_type_id=None, relation=None):  # noqa: E501
        """PrescriptivePathAssetType - a model defined in Swagger"""  # noqa: E501
        self._asset_type_id = None
        self._relation = None
        self.discriminator = None
        if asset_type_id is not None:
            self.asset_type_id = asset_type_id
        if relation is not None:
            self.relation = relation

    @property
    def asset_type_id(self):
        """Gets the asset_type_id of this PrescriptivePathAssetType.  # noqa: E501


        :return: The asset_type_id of this PrescriptivePathAssetType.  # noqa: E501
        :rtype: str
        """
        return self._asset_type_id

    @asset_type_id.setter
    def asset_type_id(self, asset_type_id):
        """Sets the asset_type_id of this PrescriptivePathAssetType.


        :param asset_type_id: The asset_type_id of this PrescriptivePathAssetType.  # noqa: E501
        :type: str
        """

        self._asset_type_id = asset_type_id

    @property
    def relation(self):
        """Gets the relation of this PrescriptivePathAssetType.  # noqa: E501


        :return: The relation of this PrescriptivePathAssetType.  # noqa: E501
        :rtype: PrescriptivePathRelation
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this PrescriptivePathAssetType.


        :param relation: The relation of this PrescriptivePathAssetType.  # noqa: E501
        :type: PrescriptivePathRelation
        """

        self._relation = relation

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
        if issubclass(PrescriptivePathAssetType, dict):
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
        if not isinstance(other, PrescriptivePathAssetType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
