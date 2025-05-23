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

class Distributions(object):
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
        'distribution_density_estimation': 'list[Point]',
        'histogram': 'list[HistogramBin]'
    }

    attribute_map = {
        'distribution_density_estimation': 'distributionDensityEstimation',
        'histogram': 'histogram'
    }

    def __init__(self, distribution_density_estimation=None, histogram=None):  # noqa: E501
        """Distributions - a model defined in Swagger"""  # noqa: E501
        self._distribution_density_estimation = None
        self._histogram = None
        self.discriminator = None
        if distribution_density_estimation is not None:
            self.distribution_density_estimation = distribution_density_estimation
        if histogram is not None:
            self.histogram = histogram

    @property
    def distribution_density_estimation(self):
        """Gets the distribution_density_estimation of this Distributions.  # noqa: E501


        :return: The distribution_density_estimation of this Distributions.  # noqa: E501
        :rtype: list[Point]
        """
        return self._distribution_density_estimation

    @distribution_density_estimation.setter
    def distribution_density_estimation(self, distribution_density_estimation):
        """Sets the distribution_density_estimation of this Distributions.


        :param distribution_density_estimation: The distribution_density_estimation of this Distributions.  # noqa: E501
        :type: list[Point]
        """

        self._distribution_density_estimation = distribution_density_estimation

    @property
    def histogram(self):
        """Gets the histogram of this Distributions.  # noqa: E501


        :return: The histogram of this Distributions.  # noqa: E501
        :rtype: list[HistogramBin]
        """
        return self._histogram

    @histogram.setter
    def histogram(self, histogram):
        """Sets the histogram of this Distributions.


        :param histogram: The histogram of this Distributions.  # noqa: E501
        :type: list[HistogramBin]
        """

        self._histogram = histogram

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
        if issubclass(Distributions, dict):
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
        if not isinstance(other, Distributions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
