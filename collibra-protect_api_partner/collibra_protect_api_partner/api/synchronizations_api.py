# coding: utf-8

"""
    Collibra Protect API - Partner

    API to retrieve the data access rule set it needs to synchronize. This API is targeted to be used by Collibra Partners.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from collibra_protect_api_partner.api_client import ApiClient


class SynchronizationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_synchronization_by_data_source(self, data_source, **kwargs):  # noqa: E501
        """Returns the details of the synchronization for the provided data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_synchronization_by_data_source(data_source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_source: Name of the data source (required)
        :return: Synchronization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_synchronization_by_data_source_with_http_info(data_source, **kwargs)  # noqa: E501
        else:
            (data) = self.get_synchronization_by_data_source_with_http_info(data_source, **kwargs)  # noqa: E501
            return data

    def get_synchronization_by_data_source_with_http_info(self, data_source, **kwargs):  # noqa: E501
        """Returns the details of the synchronization for the provided data source.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_synchronization_by_data_source_with_http_info(data_source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_source: Name of the data source (required)
        :return: Synchronization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_synchronization_by_data_source" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_source' is set
        if ('data_source' not in params or
                params['data_source'] is None):
            raise ValueError("Missing the required parameter `data_source` when calling `get_synchronization_by_data_source`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data_source' in params:
            query_params.append(('dataSource', params['data_source']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/synchronizations/byDataSource', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Synchronization',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
