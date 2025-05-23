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
from collibra_protect.models.editable_custom_masking import EditableCustomMasking  # noqa: F401,E501

class CustomMasking(EditableCustomMasking):
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
        'created_by': 'str',
        'created_on': 'int',
        'last_modified_by': 'str',
        'last_modified_on': 'int'
    }
    if hasattr(EditableCustomMasking, "swagger_types"):
        swagger_types.update(EditableCustomMasking.swagger_types)

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn'
    }
    if hasattr(EditableCustomMasking, "attribute_map"):
        attribute_map.update(EditableCustomMasking.attribute_map)

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, *args, **kwargs):  # noqa: E501
        """CustomMasking - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self.discriminator = None
        self.id = id
        self.created_by = created_by
        self.created_on = created_on
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        EditableCustomMasking.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this CustomMasking.  # noqa: E501

        The ID of the masking.  # noqa: E501

        :return: The id of this CustomMasking.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomMasking.

        The ID of the masking.  # noqa: E501

        :param id: The id of this CustomMasking.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this CustomMasking.  # noqa: E501

        ID of the Collibra user who created this custom mapping.  # noqa: E501

        :return: The created_by of this CustomMasking.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CustomMasking.

        ID of the Collibra user who created this custom mapping.  # noqa: E501

        :param created_by: The created_by of this CustomMasking.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this CustomMasking.  # noqa: E501

        The timestamp of when this custom mapping was created  # noqa: E501

        :return: The created_on of this CustomMasking.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this CustomMasking.

        The timestamp of when this custom mapping was created  # noqa: E501

        :param created_on: The created_on of this CustomMasking.  # noqa: E501
        :type: int
        """
        if created_on is None:
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this CustomMasking.  # noqa: E501

        ID of the Collibra user who last updated this custom mapping.  # noqa: E501

        :return: The last_modified_by of this CustomMasking.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this CustomMasking.

        ID of the Collibra user who last updated this custom mapping.  # noqa: E501

        :param last_modified_by: The last_modified_by of this CustomMasking.  # noqa: E501
        :type: str
        """
        if last_modified_by is None:
            raise ValueError("Invalid value for `last_modified_by`, must not be `None`")  # noqa: E501

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this CustomMasking.  # noqa: E501

        The timestamp of when this custom mapping was last updated.  # noqa: E501

        :return: The last_modified_on of this CustomMasking.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this CustomMasking.

        The timestamp of when this custom mapping was last updated.  # noqa: E501

        :param last_modified_on: The last_modified_on of this CustomMasking.  # noqa: E501
        :type: int
        """
        if last_modified_on is None:
            raise ValueError("Invalid value for `last_modified_on`, must not be `None`")  # noqa: E501

        self._last_modified_on = last_modified_on

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
        if issubclass(CustomMasking, dict):
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
        if not isinstance(other, CustomMasking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
