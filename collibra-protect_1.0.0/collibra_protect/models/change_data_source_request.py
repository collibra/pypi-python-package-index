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

class ChangeDataSourceRequest(object):
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
        'name': 'str',
        'data_source_name': 'str',
        'data_source_aliases': 'list[DataSourceAlias]'
    }

    attribute_map = {
        'name': 'name',
        'data_source_name': 'dataSourceName',
        'data_source_aliases': 'dataSourceAliases'
    }

    def __init__(self, name=None, data_source_name=None, data_source_aliases=None):  # noqa: E501
        """ChangeDataSourceRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._data_source_name = None
        self._data_source_aliases = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if data_source_name is not None:
            self.data_source_name = data_source_name
        if data_source_aliases is not None:
            self.data_source_aliases = data_source_aliases

    @property
    def name(self):
        """Gets the name of this ChangeDataSourceRequest.  # noqa: E501

        The name of the data source.  # noqa: E501

        :return: The name of this ChangeDataSourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChangeDataSourceRequest.

        The name of the data source.  # noqa: E501

        :param name: The name of this ChangeDataSourceRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def data_source_name(self):
        """Gets the data_source_name of this ChangeDataSourceRequest.  # noqa: E501

        The value of the \"Data Source Type\" attribute on the Database asset. It is also used in group mapping as the \"provider\" name  # noqa: E501

        :return: The data_source_name of this ChangeDataSourceRequest.  # noqa: E501
        :rtype: str
        """
        return self._data_source_name

    @data_source_name.setter
    def data_source_name(self, data_source_name):
        """Sets the data_source_name of this ChangeDataSourceRequest.

        The value of the \"Data Source Type\" attribute on the Database asset. It is also used in group mapping as the \"provider\" name  # noqa: E501

        :param data_source_name: The data_source_name of this ChangeDataSourceRequest.  # noqa: E501
        :type: str
        """

        self._data_source_name = data_source_name

    @property
    def data_source_aliases(self):
        """Gets the data_source_aliases of this ChangeDataSourceRequest.  # noqa: E501

        A list of aliases for the data source name used in the \"Data Source Type\" attribute on the Database asset.  # noqa: E501

        :return: The data_source_aliases of this ChangeDataSourceRequest.  # noqa: E501
        :rtype: list[DataSourceAlias]
        """
        return self._data_source_aliases

    @data_source_aliases.setter
    def data_source_aliases(self, data_source_aliases):
        """Sets the data_source_aliases of this ChangeDataSourceRequest.

        A list of aliases for the data source name used in the \"Data Source Type\" attribute on the Database asset.  # noqa: E501

        :param data_source_aliases: The data_source_aliases of this ChangeDataSourceRequest.  # noqa: E501
        :type: list[DataSourceAlias]
        """

        self._data_source_aliases = data_source_aliases

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
        if issubclass(ChangeDataSourceRequest, dict):
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
        if not isinstance(other, ChangeDataSourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
