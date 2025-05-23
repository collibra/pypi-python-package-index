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

class MappingIdentifier(object):
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
        'external_system_id': 'str',
        'external_entity_id': 'str',
        'dgc_id': 'str',
        'asset': 'AssetIdentifier',
        'domain': 'DomainIdentifier',
        'community': 'CommunityIdentifier',
        'complex_relation': 'ComplexRelationIdentifier'
    }

    attribute_map = {
        'id': 'id',
        'external_system_id': 'externalSystemId',
        'external_entity_id': 'externalEntityId',
        'dgc_id': 'dgcId',
        'asset': 'asset',
        'domain': 'domain',
        'community': 'community',
        'complex_relation': 'complexRelation'
    }

    def __init__(self, id=None, external_system_id=None, external_entity_id=None, dgc_id=None, asset=None, domain=None, community=None, complex_relation=None):  # noqa: E501
        """MappingIdentifier - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._external_system_id = None
        self._external_entity_id = None
        self._dgc_id = None
        self._asset = None
        self._domain = None
        self._community = None
        self._complex_relation = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if external_system_id is not None:
            self.external_system_id = external_system_id
        if external_entity_id is not None:
            self.external_entity_id = external_entity_id
        if dgc_id is not None:
            self.dgc_id = dgc_id
        if asset is not None:
            self.asset = asset
        if domain is not None:
            self.domain = domain
        if community is not None:
            self.community = community
        if complex_relation is not None:
            self.complex_relation = complex_relation

    @property
    def id(self):
        """Gets the id of this MappingIdentifier.  # noqa: E501


        :return: The id of this MappingIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MappingIdentifier.


        :param id: The id of this MappingIdentifier.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def external_system_id(self):
        """Gets the external_system_id of this MappingIdentifier.  # noqa: E501


        :return: The external_system_id of this MappingIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._external_system_id

    @external_system_id.setter
    def external_system_id(self, external_system_id):
        """Sets the external_system_id of this MappingIdentifier.


        :param external_system_id: The external_system_id of this MappingIdentifier.  # noqa: E501
        :type: str
        """

        self._external_system_id = external_system_id

    @property
    def external_entity_id(self):
        """Gets the external_entity_id of this MappingIdentifier.  # noqa: E501


        :return: The external_entity_id of this MappingIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._external_entity_id

    @external_entity_id.setter
    def external_entity_id(self, external_entity_id):
        """Sets the external_entity_id of this MappingIdentifier.


        :param external_entity_id: The external_entity_id of this MappingIdentifier.  # noqa: E501
        :type: str
        """

        self._external_entity_id = external_entity_id

    @property
    def dgc_id(self):
        """Gets the dgc_id of this MappingIdentifier.  # noqa: E501


        :return: The dgc_id of this MappingIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._dgc_id

    @dgc_id.setter
    def dgc_id(self, dgc_id):
        """Sets the dgc_id of this MappingIdentifier.


        :param dgc_id: The dgc_id of this MappingIdentifier.  # noqa: E501
        :type: str
        """

        self._dgc_id = dgc_id

    @property
    def asset(self):
        """Gets the asset of this MappingIdentifier.  # noqa: E501


        :return: The asset of this MappingIdentifier.  # noqa: E501
        :rtype: AssetIdentifier
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this MappingIdentifier.


        :param asset: The asset of this MappingIdentifier.  # noqa: E501
        :type: AssetIdentifier
        """

        self._asset = asset

    @property
    def domain(self):
        """Gets the domain of this MappingIdentifier.  # noqa: E501


        :return: The domain of this MappingIdentifier.  # noqa: E501
        :rtype: DomainIdentifier
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this MappingIdentifier.


        :param domain: The domain of this MappingIdentifier.  # noqa: E501
        :type: DomainIdentifier
        """

        self._domain = domain

    @property
    def community(self):
        """Gets the community of this MappingIdentifier.  # noqa: E501


        :return: The community of this MappingIdentifier.  # noqa: E501
        :rtype: CommunityIdentifier
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this MappingIdentifier.


        :param community: The community of this MappingIdentifier.  # noqa: E501
        :type: CommunityIdentifier
        """

        self._community = community

    @property
    def complex_relation(self):
        """Gets the complex_relation of this MappingIdentifier.  # noqa: E501


        :return: The complex_relation of this MappingIdentifier.  # noqa: E501
        :rtype: ComplexRelationIdentifier
        """
        return self._complex_relation

    @complex_relation.setter
    def complex_relation(self, complex_relation):
        """Sets the complex_relation of this MappingIdentifier.


        :param complex_relation: The complex_relation of this MappingIdentifier.  # noqa: E501
        :type: ComplexRelationIdentifier
        """

        self._complex_relation = complex_relation

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
        if issubclass(MappingIdentifier, dict):
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
        if not isinstance(other, MappingIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
