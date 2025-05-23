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

class DatabaseConnectionPagedResponse(object):
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
        'results': 'list[DatabaseConnection]'
    }

    attribute_map = {
        'results': 'results'
    }

    def __init__(self, results=None):  # noqa: E501
        """DatabaseConnectionPagedResponse - a model defined in Swagger"""  # noqa: E501
        self._results = None
        self.discriminator = None
        if results is not None:
            self.results = results

    @property
    def results(self):
        """Gets the results of this DatabaseConnectionPagedResponse.  # noqa: E501

        The list of results.  # noqa: E501

        :return: The results of this DatabaseConnectionPagedResponse.  # noqa: E501
        :rtype: list[DatabaseConnection]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this DatabaseConnectionPagedResponse.

        The list of results.  # noqa: E501

        :param results: The results of this DatabaseConnectionPagedResponse.  # noqa: E501
        :type: list[DatabaseConnection]
        """

        self._results = results

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
        if issubclass(DatabaseConnectionPagedResponse, dict):
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
        if not isinstance(other, DatabaseConnectionPagedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
