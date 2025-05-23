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

class AddClassificationMatchRequest(object):
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
        'asset_id': 'str',
        'classification_id': 'str'
    }

    attribute_map = {
        'asset_id': 'assetId',
        'classification_id': 'classificationId'
    }

    def __init__(self, asset_id=None, classification_id=None):  # noqa: E501
        """AddClassificationMatchRequest - a model defined in Swagger"""  # noqa: E501
        self._asset_id = None
        self._classification_id = None
        self.discriminator = None
        self.asset_id = asset_id
        self.classification_id = classification_id

    @property
    def asset_id(self):
        """Gets the asset_id of this AddClassificationMatchRequest.  # noqa: E501

        The <code>id</code> of an asset for which classification matches will be added.  # noqa: E501

        :return: The asset_id of this AddClassificationMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this AddClassificationMatchRequest.

        The <code>id</code> of an asset for which classification matches will be added.  # noqa: E501

        :param asset_id: The asset_id of this AddClassificationMatchRequest.  # noqa: E501
        :type: str
        """
        if asset_id is None:
            raise ValueError("Invalid value for `asset_id`, must not be `None`")  # noqa: E501

        self._asset_id = asset_id

    @property
    def classification_id(self):
        """Gets the classification_id of this AddClassificationMatchRequest.  # noqa: E501

        The <code>id</code> of classification to be used in created classification match.  # noqa: E501

        :return: The classification_id of this AddClassificationMatchRequest.  # noqa: E501
        :rtype: str
        """
        return self._classification_id

    @classification_id.setter
    def classification_id(self, classification_id):
        """Sets the classification_id of this AddClassificationMatchRequest.

        The <code>id</code> of classification to be used in created classification match.  # noqa: E501

        :param classification_id: The classification_id of this AddClassificationMatchRequest.  # noqa: E501
        :type: str
        """
        if classification_id is None:
            raise ValueError("Invalid value for `classification_id`, must not be `None`")  # noqa: E501

        self._classification_id = classification_id

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
        if issubclass(AddClassificationMatchRequest, dict):
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
        if not isinstance(other, AddClassificationMatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
