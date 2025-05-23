# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from collibra_core.models.assigned_characteristic_type import AssignedCharacteristicType  # noqa: F401,E501

class AssignedComplexRelationType(AssignedCharacteristicType):
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
        'complex_relation_type': 'ComplexRelationTypeImpl',
        'matching_leg_types_ids': 'list[str]'
    }
    if hasattr(AssignedCharacteristicType, "swagger_types"):
        swagger_types.update(AssignedCharacteristicType.swagger_types)

    attribute_map = {
        'complex_relation_type': 'complexRelationType',
        'matching_leg_types_ids': 'matchingLegTypesIds'
    }
    if hasattr(AssignedCharacteristicType, "attribute_map"):
        attribute_map.update(AssignedCharacteristicType.attribute_map)

    def __init__(self, complex_relation_type=None, matching_leg_types_ids=None, *args, **kwargs):  # noqa: E501
        """AssignedComplexRelationType - a model defined in Swagger"""  # noqa: E501
        self._complex_relation_type = None
        self._matching_leg_types_ids = None
        self.discriminator = None
        if complex_relation_type is not None:
            self.complex_relation_type = complex_relation_type
        if matching_leg_types_ids is not None:
            self.matching_leg_types_ids = matching_leg_types_ids
        AssignedCharacteristicType.__init__(self, *args, **kwargs)

    @property
    def complex_relation_type(self):
        """Gets the complex_relation_type of this AssignedComplexRelationType.  # noqa: E501


        :return: The complex_relation_type of this AssignedComplexRelationType.  # noqa: E501
        :rtype: ComplexRelationTypeImpl
        """
        return self._complex_relation_type

    @complex_relation_type.setter
    def complex_relation_type(self, complex_relation_type):
        """Sets the complex_relation_type of this AssignedComplexRelationType.


        :param complex_relation_type: The complex_relation_type of this AssignedComplexRelationType.  # noqa: E501
        :type: ComplexRelationTypeImpl
        """

        self._complex_relation_type = complex_relation_type

    @property
    def matching_leg_types_ids(self):
        """Gets the matching_leg_types_ids of this AssignedComplexRelationType.  # noqa: E501

        The list of IDs that should match the legs of the complex relation.  # noqa: E501

        :return: The matching_leg_types_ids of this AssignedComplexRelationType.  # noqa: E501
        :rtype: list[str]
        """
        return self._matching_leg_types_ids

    @matching_leg_types_ids.setter
    def matching_leg_types_ids(self, matching_leg_types_ids):
        """Sets the matching_leg_types_ids of this AssignedComplexRelationType.

        The list of IDs that should match the legs of the complex relation.  # noqa: E501

        :param matching_leg_types_ids: The matching_leg_types_ids of this AssignedComplexRelationType.  # noqa: E501
        :type: list[str]
        """

        self._matching_leg_types_ids = matching_leg_types_ids

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
        if issubclass(AssignedComplexRelationType, dict):
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
        if not isinstance(other, AssignedComplexRelationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
