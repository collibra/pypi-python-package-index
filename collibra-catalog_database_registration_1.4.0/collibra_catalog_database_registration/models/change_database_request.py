# coding: utf-8

"""
    Collibra Catalog Database Registration API

    This API allows you to manage the **metadata ingestion**, **profiling**, and **classification** of databases via Edge.  It provides the following functionalities: - Query and synchronize the database and schema connections. - Register the databases to be ingested, profiled and classified. - Configure and trigger the metadata ingestion of databases. - Configure and trigger the profiling and classification of databases.   # noqa: E501

    OpenAPI spec version: 1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ChangeDatabaseRequest(object):
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
        'description': 'str',
        'parent_system_id': 'str',
        'owner_ids': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'parent_system_id': 'parentSystemId',
        'owner_ids': 'ownerIds'
    }

    def __init__(self, description=None, parent_system_id=None, owner_ids=None):  # noqa: E501
        """ChangeDatabaseRequest - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._parent_system_id = None
        self._owner_ids = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if parent_system_id is not None:
            self.parent_system_id = parent_system_id
        if owner_ids is not None:
            self.owner_ids = owner_ids

    @property
    def description(self):
        """Gets the description of this ChangeDatabaseRequest.  # noqa: E501

        A description of the database.  # noqa: E501

        :return: The description of this ChangeDatabaseRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChangeDatabaseRequest.

        A description of the database.  # noqa: E501

        :param description: The description of this ChangeDatabaseRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def parent_system_id(self):
        """Gets the parent_system_id of this ChangeDatabaseRequest.  # noqa: E501

        The ID of the parent System asset.  After registering a database, a relation of type *Technology Asset groups / is grouped by technology Asset* is created between the System asset and the Database asset.   # noqa: E501

        :return: The parent_system_id of this ChangeDatabaseRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_system_id

    @parent_system_id.setter
    def parent_system_id(self, parent_system_id):
        """Sets the parent_system_id of this ChangeDatabaseRequest.

        The ID of the parent System asset.  After registering a database, a relation of type *Technology Asset groups / is grouped by technology Asset* is created between the System asset and the Database asset.   # noqa: E501

        :param parent_system_id: The parent_system_id of this ChangeDatabaseRequest.  # noqa: E501
        :type: str
        """

        self._parent_system_id = parent_system_id

    @property
    def owner_ids(self):
        """Gets the owner_ids of this ChangeDatabaseRequest.  # noqa: E501

        The ID of the users that will be assigned as the Owner of existing domain containing the Database asset.   # noqa: E501

        :return: The owner_ids of this ChangeDatabaseRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_ids

    @owner_ids.setter
    def owner_ids(self, owner_ids):
        """Sets the owner_ids of this ChangeDatabaseRequest.

        The ID of the users that will be assigned as the Owner of existing domain containing the Database asset.   # noqa: E501

        :param owner_ids: The owner_ids of this ChangeDatabaseRequest.  # noqa: E501
        :type: list[str]
        """

        self._owner_ids = owner_ids

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
        if issubclass(ChangeDatabaseRequest, dict):
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
        if not isinstance(other, ChangeDatabaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
