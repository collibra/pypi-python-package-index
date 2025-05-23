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

class PrescriptivePathRelation(object):
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
        'relation_type_id': 'str',
        'relation_type_direction': 'RelationTypeDirection',
        'asset_type': 'PrescriptivePathAssetType'
    }

    attribute_map = {
        'relation_type_id': 'relationTypeId',
        'relation_type_direction': 'relationTypeDirection',
        'asset_type': 'assetType'
    }

    def __init__(self, relation_type_id=None, relation_type_direction=None, asset_type=None):  # noqa: E501
        """PrescriptivePathRelation - a model defined in Swagger"""  # noqa: E501
        self._relation_type_id = None
        self._relation_type_direction = None
        self._asset_type = None
        self.discriminator = None
        self.relation_type_id = relation_type_id
        self.relation_type_direction = relation_type_direction
        self.asset_type = asset_type

    @property
    def relation_type_id(self):
        """Gets the relation_type_id of this PrescriptivePathRelation.  # noqa: E501


        :return: The relation_type_id of this PrescriptivePathRelation.  # noqa: E501
        :rtype: str
        """
        return self._relation_type_id

    @relation_type_id.setter
    def relation_type_id(self, relation_type_id):
        """Sets the relation_type_id of this PrescriptivePathRelation.


        :param relation_type_id: The relation_type_id of this PrescriptivePathRelation.  # noqa: E501
        :type: str
        """
        if relation_type_id is None:
            raise ValueError("Invalid value for `relation_type_id`, must not be `None`")  # noqa: E501

        self._relation_type_id = relation_type_id

    @property
    def relation_type_direction(self):
        """Gets the relation_type_direction of this PrescriptivePathRelation.  # noqa: E501


        :return: The relation_type_direction of this PrescriptivePathRelation.  # noqa: E501
        :rtype: RelationTypeDirection
        """
        return self._relation_type_direction

    @relation_type_direction.setter
    def relation_type_direction(self, relation_type_direction):
        """Sets the relation_type_direction of this PrescriptivePathRelation.


        :param relation_type_direction: The relation_type_direction of this PrescriptivePathRelation.  # noqa: E501
        :type: RelationTypeDirection
        """
        if relation_type_direction is None:
            raise ValueError("Invalid value for `relation_type_direction`, must not be `None`")  # noqa: E501

        self._relation_type_direction = relation_type_direction

    @property
    def asset_type(self):
        """Gets the asset_type of this PrescriptivePathRelation.  # noqa: E501


        :return: The asset_type of this PrescriptivePathRelation.  # noqa: E501
        :rtype: PrescriptivePathAssetType
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this PrescriptivePathRelation.


        :param asset_type: The asset_type of this PrescriptivePathRelation.  # noqa: E501
        :type: PrescriptivePathAssetType
        """
        if asset_type is None:
            raise ValueError("Invalid value for `asset_type`, must not be `None`")  # noqa: E501

        self._asset_type = asset_type

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
        if issubclass(PrescriptivePathRelation, dict):
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
        if not isinstance(other, PrescriptivePathRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
