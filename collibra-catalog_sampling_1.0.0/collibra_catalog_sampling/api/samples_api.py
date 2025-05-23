# coding: utf-8

"""
    Catalog Sampling API

    <p>The Catalog Sampling API offers functionality related to the Collibra Data Catalog application.<br/> It is mainly focused on facilitating the ingestion of information into Data Catalog.<br/> The API enables you to more easily connect Data Catalog to sources that are not necessarily natively supported in the product.</p>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from collibra_catalog_sampling.api_client import ApiClient


class SamplesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def read_samples(self, asset_id, **kwargs):  # noqa: E501
        """Read sample data from the Collibra cloud repository or Edge cache  # noqa: E501

        Reads the available sample data from the Collibra cloud repository or Edge cache depending on how the data is collected.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_samples(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Asset identifier (required)
        :param int column_limit: The maximum number of columns to retrieve. If not set (columnLimit = <code>0</code>), the default column limit will be used. Maximum is set to 1500.
        :param int column_offset: The index of the fist column to retrieve. If not set (columnOffset = <code>0</code>), results will be retrieved starting from column <code>0</code>.
        :return: ReadSamplesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_samples_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.read_samples_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def read_samples_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Read sample data from the Collibra cloud repository or Edge cache  # noqa: E501

        Reads the available sample data from the Collibra cloud repository or Edge cache depending on how the data is collected.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_samples_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Asset identifier (required)
        :param int column_limit: The maximum number of columns to retrieve. If not set (columnLimit = <code>0</code>), the default column limit will be used. Maximum is set to 1500.
        :param int column_offset: The index of the fist column to retrieve. If not set (columnOffset = <code>0</code>), results will be retrieved starting from column <code>0</code>.
        :return: ReadSamplesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_id', 'column_limit', 'column_offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read_samples" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in params or
                params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `read_samples`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in params:
            path_params['assetId'] = params['asset_id']  # noqa: E501

        query_params = []
        if 'column_limit' in params:
            query_params.append(('columnLimit', params['column_limit']))  # noqa: E501
        if 'column_offset' in params:
            query_params.append(('columnOffset', params['column_offset']))  # noqa: E501

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
            '/samples/{assetId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReadSamplesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_samples(self, asset_id, **kwargs):  # noqa: E501
        """Create a request to collect and cache sample data for an Edge data source  # noqa: E501

        Creates a request to collect sample data from an Edge data source for the asset with the specified ID and temporarily makes it available in the Edge cache.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_samples(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Asset identifier (required)
        :return: RequestSamplesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_samples_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.request_samples_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def request_samples_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Create a request to collect and cache sample data for an Edge data source  # noqa: E501

        Creates a request to collect sample data from an Edge data source for the asset with the specified ID and temporarily makes it available in the Edge cache.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_samples_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str asset_id: Asset identifier (required)
        :return: RequestSamplesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_samples" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in params or
                params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `request_samples`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in params:
            path_params['assetId'] = params['asset_id']  # noqa: E501

        query_params = []

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
            '/samples/{assetId}/request', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RequestSamplesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
