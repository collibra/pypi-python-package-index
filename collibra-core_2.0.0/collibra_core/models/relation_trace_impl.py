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

class RelationTraceImpl(object):
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
        'last_modified_on': 'int',
        'system': 'bool',
        'resource_type': 'str',
        'relation_trace_entries': 'list[RelationTraceEntryImpl]'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'relation_trace_entries': 'relationTraceEntries'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, relation_trace_entries=None):  # noqa: E501
        """RelationTraceImpl - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._system = None
        self._resource_type = None
        self._relation_trace_entries = None
        self.discriminator = None
        self.id = id
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if system is not None:
            self.system = system
        self.resource_type = resource_type
        if relation_trace_entries is not None:
            self.relation_trace_entries = relation_trace_entries

    @property
    def id(self):
        """Gets the id of this RelationTraceImpl.  # noqa: E501

        The id of the represented object (entity).  # noqa: E501

        :return: The id of this RelationTraceImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RelationTraceImpl.

        The id of the represented object (entity).  # noqa: E501

        :param id: The id of this RelationTraceImpl.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this RelationTraceImpl.  # noqa: E501

        The id of the user that created this resource.  # noqa: E501

        :return: The created_by of this RelationTraceImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RelationTraceImpl.

        The id of the user that created this resource.  # noqa: E501

        :param created_by: The created_by of this RelationTraceImpl.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this RelationTraceImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :return: The created_on of this RelationTraceImpl.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this RelationTraceImpl.

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :param created_on: The created_on of this RelationTraceImpl.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this RelationTraceImpl.  # noqa: E501

        The id of the user who modified this resource the last time.  # noqa: E501

        :return: The last_modified_by of this RelationTraceImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this RelationTraceImpl.

        The id of the user who modified this resource the last time.  # noqa: E501

        :param last_modified_by: The last_modified_by of this RelationTraceImpl.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this RelationTraceImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :return: The last_modified_on of this RelationTraceImpl.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this RelationTraceImpl.

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :param last_modified_on: The last_modified_on of this RelationTraceImpl.  # noqa: E501
        :type: int
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this RelationTraceImpl.  # noqa: E501

        Whether this is a system resource or not.  # noqa: E501

        :return: The system of this RelationTraceImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this RelationTraceImpl.

        Whether this is a system resource or not.  # noqa: E501

        :param system: The system of this RelationTraceImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this RelationTraceImpl.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :return: The resource_type of this RelationTraceImpl.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RelationTraceImpl.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :param resource_type: The resource_type of this RelationTraceImpl.  # noqa: E501
        :type: str
        """
        if resource_type is None:
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501
        allowed_values = ["View", "Asset", "Community", "Domain", "AssetType", "DomainType", "Status", "User", "ClassificationMatch", "UserGroup", "Attribute", "StringAttribute", "ScriptAttribute", "BooleanAttribute", "DateAttribute", "NumericAttribute", "SingleValueListAttribute", "MultiValueListAttribute", "Comment", "Attachment", "Responsibility", "Workflow", "Job", "Relation", "RelationType", "ComplexRelation", "ComplexRelationType", "ArticulationRule", "Assignment", "Scope", "RelationTrace", "ValidationRule", "DataQualityRule", "DataQualityMetric", "Address", "InstantMessagingAccount", "Email", "PhoneNumber", "Website", "Activity", "FormProperty", "WorkflowTask", "ActivityChange", "WorkflowInstance", "Role", "AttributeType", "BooleanAttributeType", "DateAttributeType", "DateTimeAttributeType", "MultiValueListAttributeType", "NumericAttributeType", "ScriptAttributeType", "SingleValueListAttributeType", "StringAttributeType", "ViewSharingRule", "ViewAssignmentRule", "JdbcDriverFile", "JdbcDriver", "JdbcIngestionProperties", "CsvIngestionProperties", "ExcelIngestionProperties", "ConnectionStringParameter", "AssignedCharacteristicType", "Notification", "Tag", "ComplexRelationLegType", "ComplexRelationAttributeType", "ComplexRelationLeg", "BaseDataType", "AdvancedDataType", "DiagramPicture", "DiagramPictureSharingRule", "DiagramPictureAssignmentRule", "Rating", "Classification", "PhysicalDataConnector", "Context"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def relation_trace_entries(self):
        """Gets the relation_trace_entries of this RelationTraceImpl.  # noqa: E501

        The list of relation trace entries.  # noqa: E501

        :return: The relation_trace_entries of this RelationTraceImpl.  # noqa: E501
        :rtype: list[RelationTraceEntryImpl]
        """
        return self._relation_trace_entries

    @relation_trace_entries.setter
    def relation_trace_entries(self, relation_trace_entries):
        """Sets the relation_trace_entries of this RelationTraceImpl.

        The list of relation trace entries.  # noqa: E501

        :param relation_trace_entries: The relation_trace_entries of this RelationTraceImpl.  # noqa: E501
        :type: list[RelationTraceEntryImpl]
        """

        self._relation_trace_entries = relation_trace_entries

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
        if issubclass(RelationTraceImpl, dict):
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
        if not isinstance(other, RelationTraceImpl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
