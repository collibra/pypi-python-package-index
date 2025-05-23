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

class StandardErrorResponse(object):
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
        'status_code': 'int',
        'title_message': 'str',
        'help_message': 'str',
        'user_message': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'status_code': 'statusCode',
        'title_message': 'titleMessage',
        'help_message': 'helpMessage',
        'user_message': 'userMessage',
        'error_code': 'errorCode'
    }

    def __init__(self, status_code=None, title_message=None, help_message=None, user_message=None, error_code=None):  # noqa: E501
        """StandardErrorResponse - a model defined in Swagger"""  # noqa: E501
        self._status_code = None
        self._title_message = None
        self._help_message = None
        self._user_message = None
        self._error_code = None
        self.discriminator = None
        if status_code is not None:
            self.status_code = status_code
        if title_message is not None:
            self.title_message = title_message
        if help_message is not None:
            self.help_message = help_message
        if user_message is not None:
            self.user_message = user_message
        if error_code is not None:
            self.error_code = error_code

    @property
    def status_code(self):
        """Gets the status_code of this StandardErrorResponse.  # noqa: E501

        HTTP response code  # noqa: E501

        :return: The status_code of this StandardErrorResponse.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this StandardErrorResponse.

        HTTP response code  # noqa: E501

        :param status_code: The status_code of this StandardErrorResponse.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def title_message(self):
        """Gets the title_message of this StandardErrorResponse.  # noqa: E501


        :return: The title_message of this StandardErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._title_message

    @title_message.setter
    def title_message(self, title_message):
        """Sets the title_message of this StandardErrorResponse.


        :param title_message: The title_message of this StandardErrorResponse.  # noqa: E501
        :type: str
        """

        self._title_message = title_message

    @property
    def help_message(self):
        """Gets the help_message of this StandardErrorResponse.  # noqa: E501


        :return: The help_message of this StandardErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._help_message

    @help_message.setter
    def help_message(self, help_message):
        """Sets the help_message of this StandardErrorResponse.


        :param help_message: The help_message of this StandardErrorResponse.  # noqa: E501
        :type: str
        """

        self._help_message = help_message

    @property
    def user_message(self):
        """Gets the user_message of this StandardErrorResponse.  # noqa: E501


        :return: The user_message of this StandardErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_message

    @user_message.setter
    def user_message(self, user_message):
        """Sets the user_message of this StandardErrorResponse.


        :param user_message: The user_message of this StandardErrorResponse.  # noqa: E501
        :type: str
        """

        self._user_message = user_message

    @property
    def error_code(self):
        """Gets the error_code of this StandardErrorResponse.  # noqa: E501


        :return: The error_code of this StandardErrorResponse.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this StandardErrorResponse.


        :param error_code: The error_code of this StandardErrorResponse.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

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
        if issubclass(StandardErrorResponse, dict):
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
        if not isinstance(other, StandardErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
