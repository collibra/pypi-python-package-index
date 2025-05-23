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

class DatabaseMetadata(object):
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
        'default_value': 'str',
        'number_of_decimal_digits': 'int',
        'char_octet_length': 'int',
        'column_size': 'int',
        'primary_key_name': 'str',
        'is_nullable': 'bool',
        'is_auto_incremented': 'bool',
        'is_generated': 'bool',
        'is_primary_key': 'bool'
    }

    attribute_map = {
        'default_value': 'defaultValue',
        'number_of_decimal_digits': 'numberOfDecimalDigits',
        'char_octet_length': 'charOctetLength',
        'column_size': 'columnSize',
        'primary_key_name': 'primaryKeyName',
        'is_nullable': 'isNullable',
        'is_auto_incremented': 'isAutoIncremented',
        'is_generated': 'isGenerated',
        'is_primary_key': 'isPrimaryKey'
    }

    def __init__(self, default_value=None, number_of_decimal_digits=None, char_octet_length=None, column_size=None, primary_key_name=None, is_nullable=None, is_auto_incremented=None, is_generated=None, is_primary_key=None):  # noqa: E501
        """DatabaseMetadata - a model defined in Swagger"""  # noqa: E501
        self._default_value = None
        self._number_of_decimal_digits = None
        self._char_octet_length = None
        self._column_size = None
        self._primary_key_name = None
        self._is_nullable = None
        self._is_auto_incremented = None
        self._is_generated = None
        self._is_primary_key = None
        self.discriminator = None
        if default_value is not None:
            self.default_value = default_value
        if number_of_decimal_digits is not None:
            self.number_of_decimal_digits = number_of_decimal_digits
        if char_octet_length is not None:
            self.char_octet_length = char_octet_length
        if column_size is not None:
            self.column_size = column_size
        if primary_key_name is not None:
            self.primary_key_name = primary_key_name
        if is_nullable is not None:
            self.is_nullable = is_nullable
        if is_auto_incremented is not None:
            self.is_auto_incremented = is_auto_incremented
        if is_generated is not None:
            self.is_generated = is_generated
        if is_primary_key is not None:
            self.is_primary_key = is_primary_key

    @property
    def default_value(self):
        """Gets the default_value of this DatabaseMetadata.  # noqa: E501


        :return: The default_value of this DatabaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this DatabaseMetadata.


        :param default_value: The default_value of this DatabaseMetadata.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def number_of_decimal_digits(self):
        """Gets the number_of_decimal_digits of this DatabaseMetadata.  # noqa: E501


        :return: The number_of_decimal_digits of this DatabaseMetadata.  # noqa: E501
        :rtype: int
        """
        return self._number_of_decimal_digits

    @number_of_decimal_digits.setter
    def number_of_decimal_digits(self, number_of_decimal_digits):
        """Sets the number_of_decimal_digits of this DatabaseMetadata.


        :param number_of_decimal_digits: The number_of_decimal_digits of this DatabaseMetadata.  # noqa: E501
        :type: int
        """

        self._number_of_decimal_digits = number_of_decimal_digits

    @property
    def char_octet_length(self):
        """Gets the char_octet_length of this DatabaseMetadata.  # noqa: E501


        :return: The char_octet_length of this DatabaseMetadata.  # noqa: E501
        :rtype: int
        """
        return self._char_octet_length

    @char_octet_length.setter
    def char_octet_length(self, char_octet_length):
        """Sets the char_octet_length of this DatabaseMetadata.


        :param char_octet_length: The char_octet_length of this DatabaseMetadata.  # noqa: E501
        :type: int
        """

        self._char_octet_length = char_octet_length

    @property
    def column_size(self):
        """Gets the column_size of this DatabaseMetadata.  # noqa: E501


        :return: The column_size of this DatabaseMetadata.  # noqa: E501
        :rtype: int
        """
        return self._column_size

    @column_size.setter
    def column_size(self, column_size):
        """Sets the column_size of this DatabaseMetadata.


        :param column_size: The column_size of this DatabaseMetadata.  # noqa: E501
        :type: int
        """

        self._column_size = column_size

    @property
    def primary_key_name(self):
        """Gets the primary_key_name of this DatabaseMetadata.  # noqa: E501


        :return: The primary_key_name of this DatabaseMetadata.  # noqa: E501
        :rtype: str
        """
        return self._primary_key_name

    @primary_key_name.setter
    def primary_key_name(self, primary_key_name):
        """Sets the primary_key_name of this DatabaseMetadata.


        :param primary_key_name: The primary_key_name of this DatabaseMetadata.  # noqa: E501
        :type: str
        """

        self._primary_key_name = primary_key_name

    @property
    def is_nullable(self):
        """Gets the is_nullable of this DatabaseMetadata.  # noqa: E501


        :return: The is_nullable of this DatabaseMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable):
        """Sets the is_nullable of this DatabaseMetadata.


        :param is_nullable: The is_nullable of this DatabaseMetadata.  # noqa: E501
        :type: bool
        """

        self._is_nullable = is_nullable

    @property
    def is_auto_incremented(self):
        """Gets the is_auto_incremented of this DatabaseMetadata.  # noqa: E501


        :return: The is_auto_incremented of this DatabaseMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_auto_incremented

    @is_auto_incremented.setter
    def is_auto_incremented(self, is_auto_incremented):
        """Sets the is_auto_incremented of this DatabaseMetadata.


        :param is_auto_incremented: The is_auto_incremented of this DatabaseMetadata.  # noqa: E501
        :type: bool
        """

        self._is_auto_incremented = is_auto_incremented

    @property
    def is_generated(self):
        """Gets the is_generated of this DatabaseMetadata.  # noqa: E501


        :return: The is_generated of this DatabaseMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_generated

    @is_generated.setter
    def is_generated(self, is_generated):
        """Sets the is_generated of this DatabaseMetadata.


        :param is_generated: The is_generated of this DatabaseMetadata.  # noqa: E501
        :type: bool
        """

        self._is_generated = is_generated

    @property
    def is_primary_key(self):
        """Gets the is_primary_key of this DatabaseMetadata.  # noqa: E501


        :return: The is_primary_key of this DatabaseMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary_key

    @is_primary_key.setter
    def is_primary_key(self, is_primary_key):
        """Sets the is_primary_key of this DatabaseMetadata.


        :param is_primary_key: The is_primary_key of this DatabaseMetadata.  # noqa: E501
        :type: bool
        """

        self._is_primary_key = is_primary_key

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
        if issubclass(DatabaseMetadata, dict):
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
        if not isinstance(other, DatabaseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
