# coding: utf-8

"""
    Collibra Catalog Classification API

    <p>The Catalog API offers functionality related to the catalog product.<br/> It is mainly focused on facilitating the ingestion of information into Catalog. The API enables users to more easily connect Catalog to sources that are not necessarily natively supported in the product. </p>  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeleteClassificationMatchesRequest(object):
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
        'classification_match_ids': 'list[str]'
    }

    attribute_map = {
        'classification_match_ids': 'classificationMatchIds'
    }

    def __init__(self, classification_match_ids=None):  # noqa: E501
        """DeleteClassificationMatchesRequest - a model defined in Swagger"""  # noqa: E501
        self._classification_match_ids = None
        self.discriminator = None
        if classification_match_ids is not None:
            self.classification_match_ids = classification_match_ids

    @property
    def classification_match_ids(self):
        """Gets the classification_match_ids of this DeleteClassificationMatchesRequest.  # noqa: E501

        The list of classification match ids.  # noqa: E501

        :return: The classification_match_ids of this DeleteClassificationMatchesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._classification_match_ids

    @classification_match_ids.setter
    def classification_match_ids(self, classification_match_ids):
        """Sets the classification_match_ids of this DeleteClassificationMatchesRequest.

        The list of classification match ids.  # noqa: E501

        :param classification_match_ids: The classification_match_ids of this DeleteClassificationMatchesRequest.  # noqa: E501
        :type: list[str]
        """

        self._classification_match_ids = classification_match_ids

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
        if issubclass(DeleteClassificationMatchesRequest, dict):
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
        if not isinstance(other, DeleteClassificationMatchesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
