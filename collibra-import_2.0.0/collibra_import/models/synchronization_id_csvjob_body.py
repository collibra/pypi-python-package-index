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

class SynchronizationIdCsvjobBody(object):
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
        'send_notification': 'bool',
        'batch_size': 'int',
        'simulation': 'bool',
        'save_result': 'bool',
        'file_id': 'str',
        'file': 'str',
        'file_name': 'str',
        'delete_file': 'bool',
        'continue_on_error': 'bool',
        'finalization_strategy': 'str',
        'missing_asset_status_id': 'str',
        'separator': 'str',
        'quote': 'str',
        'escape': 'str',
        'strict_quotes': 'bool',
        'ignore_leading_whitespace': 'bool',
        'header_row': 'bool',
        'template': 'str'
    }

    attribute_map = {
        'send_notification': 'sendNotification',
        'batch_size': 'batchSize',
        'simulation': 'simulation',
        'save_result': 'saveResult',
        'file_id': 'fileId',
        'file': 'file',
        'file_name': 'fileName',
        'delete_file': 'deleteFile',
        'continue_on_error': 'continueOnError',
        'finalization_strategy': 'finalizationStrategy',
        'missing_asset_status_id': 'missingAssetStatusId',
        'separator': 'separator',
        'quote': 'quote',
        'escape': 'escape',
        'strict_quotes': 'strictQuotes',
        'ignore_leading_whitespace': 'ignoreLeadingWhitespace',
        'header_row': 'headerRow',
        'template': 'template'
    }

    def __init__(self, send_notification=False, batch_size=1000, simulation=False, save_result=False, file_id=None, file=None, file_name='synchronization_file', delete_file=False, continue_on_error=False, finalization_strategy='REMOVE_RESOURCES', missing_asset_status_id=None, separator=';', quote='"', escape='\\', strict_quotes=None, ignore_leading_whitespace=None, header_row=None, template=None):  # noqa: E501
        """SynchronizationIdCsvjobBody - a model defined in Swagger"""  # noqa: E501
        self._send_notification = None
        self._batch_size = None
        self._simulation = None
        self._save_result = None
        self._file_id = None
        self._file = None
        self._file_name = None
        self._delete_file = None
        self._continue_on_error = None
        self._finalization_strategy = None
        self._missing_asset_status_id = None
        self._separator = None
        self._quote = None
        self._escape = None
        self._strict_quotes = None
        self._ignore_leading_whitespace = None
        self._header_row = None
        self._template = None
        self.discriminator = None
        if send_notification is not None:
            self.send_notification = send_notification
        if batch_size is not None:
            self.batch_size = batch_size
        if simulation is not None:
            self.simulation = simulation
        if save_result is not None:
            self.save_result = save_result
        if file_id is not None:
            self.file_id = file_id
        if file is not None:
            self.file = file
        if file_name is not None:
            self.file_name = file_name
        if delete_file is not None:
            self.delete_file = delete_file
        if continue_on_error is not None:
            self.continue_on_error = continue_on_error
        if finalization_strategy is not None:
            self.finalization_strategy = finalization_strategy
        if missing_asset_status_id is not None:
            self.missing_asset_status_id = missing_asset_status_id
        self.separator = separator
        self.quote = quote
        self.escape = escape
        if strict_quotes is not None:
            self.strict_quotes = strict_quotes
        if ignore_leading_whitespace is not None:
            self.ignore_leading_whitespace = ignore_leading_whitespace
        if header_row is not None:
            self.header_row = header_row
        self.template = template

    @property
    def send_notification(self):
        """Gets the send_notification of this SynchronizationIdCsvjobBody.  # noqa: E501

        Whether job status notification should be sent. <b>The default value</b> is <code>false</code>.  # noqa: E501

        :return: The send_notification of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: bool
        """
        return self._send_notification

    @send_notification.setter
    def send_notification(self, send_notification):
        """Sets the send_notification of this SynchronizationIdCsvjobBody.

        Whether job status notification should be sent. <b>The default value</b> is <code>false</code>.  # noqa: E501

        :param send_notification: The send_notification of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: bool
        """

        self._send_notification = send_notification

    @property
    def batch_size(self):
        """Gets the batch_size of this SynchronizationIdCsvjobBody.  # noqa: E501

        <i>The batchSize parameter is now deprecated and is ignored during command execution.</i>  # noqa: E501

        :return: The batch_size of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this SynchronizationIdCsvjobBody.

        <i>The batchSize parameter is now deprecated and is ignored during command execution.</i>  # noqa: E501

        :param batch_size: The batch_size of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: int
        """

        self._batch_size = batch_size

    @property
    def simulation(self):
        """Gets the simulation of this SynchronizationIdCsvjobBody.  # noqa: E501

        Whether the import should be triggered as a simulation. <b>The default value</b> is <code>false</code>.<p>If <code>true</code>, the result of the import simulation will be available at the end of the job but no change will be applied to the DGC.  # noqa: E501

        :return: The simulation of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: bool
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this SynchronizationIdCsvjobBody.

        Whether the import should be triggered as a simulation. <b>The default value</b> is <code>false</code>.<p>If <code>true</code>, the result of the import simulation will be available at the end of the job but no change will be applied to the DGC.  # noqa: E501

        :param simulation: The simulation of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: bool
        """

        self._simulation = simulation

    @property
    def save_result(self):
        """Gets the save_result of this SynchronizationIdCsvjobBody.  # noqa: E501

        Whether the import Result should be persisted or forgotten. <b>The default value</b> is <code>false</code>.<p>If <code>true</code>, the result of the import simulation will be available at the end of the job but no change will be applied to the DGC.<p><b>DEPRECATED:</b>This parameter is deprecated and will be removed in the future.</b>.  # noqa: E501

        :return: The save_result of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: bool
        """
        return self._save_result

    @save_result.setter
    def save_result(self, save_result):
        """Sets the save_result of this SynchronizationIdCsvjobBody.

        Whether the import Result should be persisted or forgotten. <b>The default value</b> is <code>false</code>.<p>If <code>true</code>, the result of the import simulation will be available at the end of the job but no change will be applied to the DGC.<p><b>DEPRECATED:</b>This parameter is deprecated and will be removed in the future.</b>.  # noqa: E501

        :param save_result: The save_result of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: bool
        """

        self._save_result = save_result

    @property
    def file_id(self):
        """Gets the file_id of this SynchronizationIdCsvjobBody.  # noqa: E501

        The <code>id</code> of uploaded file.<p><b>NOTE:</b> if this field is used, <code>file</code> should not be set.  # noqa: E501

        :return: The file_id of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this SynchronizationIdCsvjobBody.

        The <code>id</code> of uploaded file.<p><b>NOTE:</b> if this field is used, <code>file</code> should not be set.  # noqa: E501

        :param file_id: The file_id of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def file(self):
        """Gets the file of this SynchronizationIdCsvjobBody.  # noqa: E501

        The file to upload. If set, then also <code>fileName</code> should be provided.<p><b>NOTE:</b> if this field is used, <code>fileId</code> should not be set.  # noqa: E501

        :return: The file of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this SynchronizationIdCsvjobBody.

        The file to upload. If set, then also <code>fileName</code> should be provided.<p><b>NOTE:</b> if this field is used, <code>fileId</code> should not be set.  # noqa: E501

        :param file: The file of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def file_name(self):
        """Gets the file_name of this SynchronizationIdCsvjobBody.  # noqa: E501

        The name of the file to upload. If set, then also <code>file</code> should be provided.<p><b>NOTE:</b> if this field is used, <code>fileId</code> should not be set.  # noqa: E501

        :return: The file_name of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this SynchronizationIdCsvjobBody.

        The name of the file to upload. If set, then also <code>file</code> should be provided.<p><b>NOTE:</b> if this field is used, <code>fileId</code> should not be set.  # noqa: E501

        :param file_name: The file_name of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def delete_file(self):
        """Gets the delete_file of this SynchronizationIdCsvjobBody.  # noqa: E501

        Whether the file should be deleted after the synchronization job is finished, regardless of the result. <b>The default value</b> is <code>false</code>.<p><b>NOTE:</b> if the file corresponds to an attachment, the attachment will be deleted.  # noqa: E501

        :return: The delete_file of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: bool
        """
        return self._delete_file

    @delete_file.setter
    def delete_file(self, delete_file):
        """Sets the delete_file of this SynchronizationIdCsvjobBody.

        Whether the file should be deleted after the synchronization job is finished, regardless of the result. <b>The default value</b> is <code>false</code>.<p><b>NOTE:</b> if the file corresponds to an attachment, the attachment will be deleted.  # noqa: E501

        :param delete_file: The delete_file of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: bool
        """

        self._delete_file = delete_file

    @property
    def continue_on_error(self):
        """Gets the continue_on_error of this SynchronizationIdCsvjobBody.  # noqa: E501

        Whether the import should continue if some of the import commands are invalid or failed to execute. <b>The default value</b> is <code>false</code>.<p>If <code>true</code>, the valid commands are still committed to the database, which can lead to partial results being stored.  # noqa: E501

        :return: The continue_on_error of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: bool
        """
        return self._continue_on_error

    @continue_on_error.setter
    def continue_on_error(self, continue_on_error):
        """Sets the continue_on_error of this SynchronizationIdCsvjobBody.

        Whether the import should continue if some of the import commands are invalid or failed to execute. <b>The default value</b> is <code>false</code>.<p>If <code>true</code>, the valid commands are still committed to the database, which can lead to partial results being stored.  # noqa: E501

        :param continue_on_error: The continue_on_error of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: bool
        """

        self._continue_on_error = continue_on_error

    @property
    def finalization_strategy(self):
        """Gets the finalization_strategy of this SynchronizationIdCsvjobBody.  # noqa: E501

        The synchronization finalization strategy used in the clean up action. This determines whether to remove, ignore or change the status of assets that no longer exist in the external system.<br />Possible values are `REMOVE_RESOURCES`, `CHANGE_STATUS` and `IGNORE`.<br />When you select `CHANGE_STATUS`, you must also provide a value for `missingAssetStatusId`.  # noqa: E501

        :return: The finalization_strategy of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._finalization_strategy

    @finalization_strategy.setter
    def finalization_strategy(self, finalization_strategy):
        """Sets the finalization_strategy of this SynchronizationIdCsvjobBody.

        The synchronization finalization strategy used in the clean up action. This determines whether to remove, ignore or change the status of assets that no longer exist in the external system.<br />Possible values are `REMOVE_RESOURCES`, `CHANGE_STATUS` and `IGNORE`.<br />When you select `CHANGE_STATUS`, you must also provide a value for `missingAssetStatusId`.  # noqa: E501

        :param finalization_strategy: The finalization_strategy of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """

        self._finalization_strategy = finalization_strategy

    @property
    def missing_asset_status_id(self):
        """Gets the missing_asset_status_id of this SynchronizationIdCsvjobBody.  # noqa: E501

        If <b>finalizationStrategy</b> is set to `CHANGE_STATUS` then this parameter determines the new status ID for assets that no longer exist in the external system.  # noqa: E501

        :return: The missing_asset_status_id of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._missing_asset_status_id

    @missing_asset_status_id.setter
    def missing_asset_status_id(self, missing_asset_status_id):
        """Sets the missing_asset_status_id of this SynchronizationIdCsvjobBody.

        If <b>finalizationStrategy</b> is set to `CHANGE_STATUS` then this parameter determines the new status ID for assets that no longer exist in the external system.  # noqa: E501

        :param missing_asset_status_id: The missing_asset_status_id of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """

        self._missing_asset_status_id = missing_asset_status_id

    @property
    def separator(self):
        """Gets the separator of this SynchronizationIdCsvjobBody.  # noqa: E501

        The delimiter character used to separate entries. <b>The default value</b> is <code>';'</code>.  # noqa: E501

        :return: The separator of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this SynchronizationIdCsvjobBody.

        The delimiter character used to separate entries. <b>The default value</b> is <code>';'</code>.  # noqa: E501

        :param separator: The separator of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """
        if separator is None:
            raise ValueError("Invalid value for `separator`, must not be `None`")  # noqa: E501

        self._separator = separator

    @property
    def quote(self):
        """Gets the quote of this SynchronizationIdCsvjobBody.  # noqa: E501

        The delimiter character used for quoted entries. <b>The default value</b>  is <code>'\"'</code>.  # noqa: E501

        :return: The quote of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this SynchronizationIdCsvjobBody.

        The delimiter character used for quoted entries. <b>The default value</b>  is <code>'\"'</code>.  # noqa: E501

        :param quote: The quote of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """
        if quote is None:
            raise ValueError("Invalid value for `quote`, must not be `None`")  # noqa: E501

        self._quote = quote

    @property
    def escape(self):
        """Gets the escape of this SynchronizationIdCsvjobBody.  # noqa: E501

        The delimiter character used to escape separator or quote character. <b>The default value</b> is <code>'\\\\'</code>.  # noqa: E501

        :return: The escape of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._escape

    @escape.setter
    def escape(self, escape):
        """Sets the escape of this SynchronizationIdCsvjobBody.

        The delimiter character used to escape separator or quote character. <b>The default value</b> is <code>'\\\\'</code>.  # noqa: E501

        :param escape: The escape of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """
        if escape is None:
            raise ValueError("Invalid value for `escape`, must not be `None`")  # noqa: E501

        self._escape = escape

    @property
    def strict_quotes(self):
        """Gets the strict_quotes of this SynchronizationIdCsvjobBody.  # noqa: E501

        Whether the characters outside quotes should be ignored. <b>The default value</b> is <code>false</code>.  # noqa: E501

        :return: The strict_quotes of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: bool
        """
        return self._strict_quotes

    @strict_quotes.setter
    def strict_quotes(self, strict_quotes):
        """Sets the strict_quotes of this SynchronizationIdCsvjobBody.

        Whether the characters outside quotes should be ignored. <b>The default value</b> is <code>false</code>.  # noqa: E501

        :param strict_quotes: The strict_quotes of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: bool
        """

        self._strict_quotes = strict_quotes

    @property
    def ignore_leading_whitespace(self):
        """Gets the ignore_leading_whitespace of this SynchronizationIdCsvjobBody.  # noqa: E501

        Whether whitespace characters before quotes should be ignored. <b>The default value</b> is <code>false</code>.  # noqa: E501

        :return: The ignore_leading_whitespace of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_leading_whitespace

    @ignore_leading_whitespace.setter
    def ignore_leading_whitespace(self, ignore_leading_whitespace):
        """Sets the ignore_leading_whitespace of this SynchronizationIdCsvjobBody.

        Whether whitespace characters before quotes should be ignored. <b>The default value</b> is <code>false</code>.  # noqa: E501

        :param ignore_leading_whitespace: The ignore_leading_whitespace of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: bool
        """

        self._ignore_leading_whitespace = ignore_leading_whitespace

    @property
    def header_row(self):
        """Gets the header_row of this SynchronizationIdCsvjobBody.  # noqa: E501

        Whether the first row of the synchronized CSV file is the header. <b>The default value</b> is <code>false</code>.  # noqa: E501

        :return: The header_row of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: bool
        """
        return self._header_row

    @header_row.setter
    def header_row(self, header_row):
        """Sets the header_row of this SynchronizationIdCsvjobBody.

        Whether the first row of the synchronized CSV file is the header. <b>The default value</b> is <code>false</code>.  # noqa: E501

        :param header_row: The header_row of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: bool
        """

        self._header_row = header_row

    @property
    def template(self):
        """Gets the template of this SynchronizationIdCsvjobBody.  # noqa: E501

        The template that should be used for parsing and synchronizing the contents of the CSV file.  <br/><p>There is one placeholder currently supported:<ul>     <li><b>${x}</b> - refers to the n-th column in the CSV file, e.g. ${1}, ${2}, ...)</li></ul><p>Example of a correct JSON template:</p> <pre> [   {     \"resourceType\": \"Asset\",     \"identifier\": {       \"name\": \"${1}\",       \"domain\": {         \"name\": \"${2}\",         \"community\": {           \"name\": \"Some Community\"         }       }     },     \"attributes\" : {       \"00000000-0000-0000-0000-000000003115\" : [ {         \"value\" : \"${3}\"        } ],       \"00000000-0000-0000-0000-000000000222\" : [ {         \"value\" : \"${4}\"       } ]     }   } ] </pre>  # noqa: E501

        :return: The template of this SynchronizationIdCsvjobBody.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this SynchronizationIdCsvjobBody.

        The template that should be used for parsing and synchronizing the contents of the CSV file.  <br/><p>There is one placeholder currently supported:<ul>     <li><b>${x}</b> - refers to the n-th column in the CSV file, e.g. ${1}, ${2}, ...)</li></ul><p>Example of a correct JSON template:</p> <pre> [   {     \"resourceType\": \"Asset\",     \"identifier\": {       \"name\": \"${1}\",       \"domain\": {         \"name\": \"${2}\",         \"community\": {           \"name\": \"Some Community\"         }       }     },     \"attributes\" : {       \"00000000-0000-0000-0000-000000003115\" : [ {         \"value\" : \"${3}\"        } ],       \"00000000-0000-0000-0000-000000000222\" : [ {         \"value\" : \"${4}\"       } ]     }   } ] </pre>  # noqa: E501

        :param template: The template of this SynchronizationIdCsvjobBody.  # noqa: E501
        :type: str
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

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
        if issubclass(SynchronizationIdCsvjobBody, dict):
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
        if not isinstance(other, SynchronizationIdCsvjobBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
