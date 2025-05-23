# coding: utf-8

"""
    Collibra Catalog External Profiling Upload API

    <p>This API is used to manually push profiling data.</p>  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ColumnProfile(object):
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
        'asset_identifier': 'AssetIdentifier',
        'column_name': 'str',
        'technical_data_type': 'str',
        'data_type': 'str',
        'column_position': 'int',
        'counts': 'Counts',
        'samples': 'Samples',
        'statistics': 'Statistics',
        'database_metadata': 'DatabaseMetadata',
        'categorical_metadata': 'CategoricalMetadata',
        'quantiles': 'Quantiles',
        'distributions': 'Distributions'
    }

    attribute_map = {
        'asset_identifier': 'assetIdentifier',
        'column_name': 'columnName',
        'technical_data_type': 'technicalDataType',
        'data_type': 'dataType',
        'column_position': 'columnPosition',
        'counts': 'counts',
        'samples': 'samples',
        'statistics': 'statistics',
        'database_metadata': 'databaseMetadata',
        'categorical_metadata': 'categoricalMetadata',
        'quantiles': 'quantiles',
        'distributions': 'distributions'
    }

    def __init__(self, asset_identifier=None, column_name=None, technical_data_type=None, data_type=None, column_position=None, counts=None, samples=None, statistics=None, database_metadata=None, categorical_metadata=None, quantiles=None, distributions=None):  # noqa: E501
        """ColumnProfile - a model defined in Swagger"""  # noqa: E501
        self._asset_identifier = None
        self._column_name = None
        self._technical_data_type = None
        self._data_type = None
        self._column_position = None
        self._counts = None
        self._samples = None
        self._statistics = None
        self._database_metadata = None
        self._categorical_metadata = None
        self._quantiles = None
        self._distributions = None
        self.discriminator = None
        self.asset_identifier = asset_identifier
        if column_name is not None:
            self.column_name = column_name
        if technical_data_type is not None:
            self.technical_data_type = technical_data_type
        if data_type is not None:
            self.data_type = data_type
        if column_position is not None:
            self.column_position = column_position
        if counts is not None:
            self.counts = counts
        if samples is not None:
            self.samples = samples
        if statistics is not None:
            self.statistics = statistics
        if database_metadata is not None:
            self.database_metadata = database_metadata
        if categorical_metadata is not None:
            self.categorical_metadata = categorical_metadata
        if quantiles is not None:
            self.quantiles = quantiles
        if distributions is not None:
            self.distributions = distributions

    @property
    def asset_identifier(self):
        """Gets the asset_identifier of this ColumnProfile.  # noqa: E501


        :return: The asset_identifier of this ColumnProfile.  # noqa: E501
        :rtype: AssetIdentifier
        """
        return self._asset_identifier

    @asset_identifier.setter
    def asset_identifier(self, asset_identifier):
        """Sets the asset_identifier of this ColumnProfile.


        :param asset_identifier: The asset_identifier of this ColumnProfile.  # noqa: E501
        :type: AssetIdentifier
        """
        if asset_identifier is None:
            raise ValueError("Invalid value for `asset_identifier`, must not be `None`")  # noqa: E501

        self._asset_identifier = asset_identifier

    @property
    def column_name(self):
        """Gets the column_name of this ColumnProfile.  # noqa: E501


        :return: The column_name of this ColumnProfile.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ColumnProfile.


        :param column_name: The column_name of this ColumnProfile.  # noqa: E501
        :type: str
        """

        self._column_name = column_name

    @property
    def technical_data_type(self):
        """Gets the technical_data_type of this ColumnProfile.  # noqa: E501


        :return: The technical_data_type of this ColumnProfile.  # noqa: E501
        :rtype: str
        """
        return self._technical_data_type

    @technical_data_type.setter
    def technical_data_type(self, technical_data_type):
        """Sets the technical_data_type of this ColumnProfile.


        :param technical_data_type: The technical_data_type of this ColumnProfile.  # noqa: E501
        :type: str
        """

        self._technical_data_type = technical_data_type

    @property
    def data_type(self):
        """Gets the data_type of this ColumnProfile.  # noqa: E501


        :return: The data_type of this ColumnProfile.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ColumnProfile.


        :param data_type: The data_type of this ColumnProfile.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def column_position(self):
        """Gets the column_position of this ColumnProfile.  # noqa: E501


        :return: The column_position of this ColumnProfile.  # noqa: E501
        :rtype: int
        """
        return self._column_position

    @column_position.setter
    def column_position(self, column_position):
        """Sets the column_position of this ColumnProfile.


        :param column_position: The column_position of this ColumnProfile.  # noqa: E501
        :type: int
        """

        self._column_position = column_position

    @property
    def counts(self):
        """Gets the counts of this ColumnProfile.  # noqa: E501


        :return: The counts of this ColumnProfile.  # noqa: E501
        :rtype: Counts
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this ColumnProfile.


        :param counts: The counts of this ColumnProfile.  # noqa: E501
        :type: Counts
        """

        self._counts = counts

    @property
    def samples(self):
        """Gets the samples of this ColumnProfile.  # noqa: E501


        :return: The samples of this ColumnProfile.  # noqa: E501
        :rtype: Samples
        """
        return self._samples

    @samples.setter
    def samples(self, samples):
        """Sets the samples of this ColumnProfile.


        :param samples: The samples of this ColumnProfile.  # noqa: E501
        :type: Samples
        """

        self._samples = samples

    @property
    def statistics(self):
        """Gets the statistics of this ColumnProfile.  # noqa: E501


        :return: The statistics of this ColumnProfile.  # noqa: E501
        :rtype: Statistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this ColumnProfile.


        :param statistics: The statistics of this ColumnProfile.  # noqa: E501
        :type: Statistics
        """

        self._statistics = statistics

    @property
    def database_metadata(self):
        """Gets the database_metadata of this ColumnProfile.  # noqa: E501


        :return: The database_metadata of this ColumnProfile.  # noqa: E501
        :rtype: DatabaseMetadata
        """
        return self._database_metadata

    @database_metadata.setter
    def database_metadata(self, database_metadata):
        """Sets the database_metadata of this ColumnProfile.


        :param database_metadata: The database_metadata of this ColumnProfile.  # noqa: E501
        :type: DatabaseMetadata
        """

        self._database_metadata = database_metadata

    @property
    def categorical_metadata(self):
        """Gets the categorical_metadata of this ColumnProfile.  # noqa: E501


        :return: The categorical_metadata of this ColumnProfile.  # noqa: E501
        :rtype: CategoricalMetadata
        """
        return self._categorical_metadata

    @categorical_metadata.setter
    def categorical_metadata(self, categorical_metadata):
        """Sets the categorical_metadata of this ColumnProfile.


        :param categorical_metadata: The categorical_metadata of this ColumnProfile.  # noqa: E501
        :type: CategoricalMetadata
        """

        self._categorical_metadata = categorical_metadata

    @property
    def quantiles(self):
        """Gets the quantiles of this ColumnProfile.  # noqa: E501


        :return: The quantiles of this ColumnProfile.  # noqa: E501
        :rtype: Quantiles
        """
        return self._quantiles

    @quantiles.setter
    def quantiles(self, quantiles):
        """Sets the quantiles of this ColumnProfile.


        :param quantiles: The quantiles of this ColumnProfile.  # noqa: E501
        :type: Quantiles
        """

        self._quantiles = quantiles

    @property
    def distributions(self):
        """Gets the distributions of this ColumnProfile.  # noqa: E501


        :return: The distributions of this ColumnProfile.  # noqa: E501
        :rtype: Distributions
        """
        return self._distributions

    @distributions.setter
    def distributions(self, distributions):
        """Sets the distributions of this ColumnProfile.


        :param distributions: The distributions of this ColumnProfile.  # noqa: E501
        :type: Distributions
        """

        self._distributions = distributions

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
        if issubclass(ColumnProfile, dict):
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
        if not isinstance(other, ColumnProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
