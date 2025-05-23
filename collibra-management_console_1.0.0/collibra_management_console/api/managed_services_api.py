# coding: utf-8

"""
    Collibra Management Console

    Collibra Management Console public REST API \\n Please ensure that cookies are not present within the API request. Including cookies within the call will cause 403 error.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from collibra_management_console.api_client import ApiClient


class ManagedServicesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change1(self, managed_service_id, **kwargs):  # noqa: E501
        """Change an existing managed service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change1(managed_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_service_id: The ID of the managed service to change (required)
        :param ManagedServiceModel body: The new model for the managed service to change
        :return: ManagedServiceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change1_with_http_info(managed_service_id, **kwargs)  # noqa: E501
        else:
            (data) = self.change1_with_http_info(managed_service_id, **kwargs)  # noqa: E501
            return data

    def change1_with_http_info(self, managed_service_id, **kwargs):  # noqa: E501
        """Change an existing managed service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change1_with_http_info(managed_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_service_id: The ID of the managed service to change (required)
        :param ManagedServiceModel body: The new model for the managed service to change
        :return: ManagedServiceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['managed_service_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'managed_service_id' is set
        if ('managed_service_id' not in params or
                params['managed_service_id'] is None):
            raise ValueError("Missing the required parameter `managed_service_id` when calling `change1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'managed_service_id' in params:
            path_params['managedServiceId'] = params['managed_service_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/service/{managedServiceId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedServiceModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_all2(self, **kwargs):  # noqa: E501
        """List all managed services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_all2(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.find_all2_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.find_all2_with_http_info(**kwargs)  # noqa: E501
            return data

    def find_all2_with_http_info(self, **kwargs):  # noqa: E501
        """List all managed services  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_all2_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_all2" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/service', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_by_id3(self, managed_service_id, **kwargs):  # noqa: E501
        """Get a managed service by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id3(managed_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_service_id: The ID of the managed service (required)
        :return: ManagedServiceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_by_id3_with_http_info(managed_service_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_by_id3_with_http_info(managed_service_id, **kwargs)  # noqa: E501
            return data

    def get_by_id3_with_http_info(self, managed_service_id, **kwargs):  # noqa: E501
        """Get a managed service by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id3_with_http_info(managed_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_service_id: The ID of the managed service (required)
        :return: ManagedServiceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['managed_service_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_id3" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'managed_service_id' is set
        if ('managed_service_id' not in params or
                params['managed_service_id'] is None):
            raise ValueError("Missing the required parameter `managed_service_id` when calling `get_by_id3`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'managed_service_id' in params:
            path_params['managedServiceId'] = params['managed_service_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/service/{managedServiceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManagedServiceModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start1(self, managed_service_id, **kwargs):  # noqa: E501
        """Start a managed service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start1(managed_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_service_id: The ID of the managed service to start (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.start1_with_http_info(managed_service_id, **kwargs)  # noqa: E501
        else:
            (data) = self.start1_with_http_info(managed_service_id, **kwargs)  # noqa: E501
            return data

    def start1_with_http_info(self, managed_service_id, **kwargs):  # noqa: E501
        """Start a managed service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start1_with_http_info(managed_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_service_id: The ID of the managed service to start (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['managed_service_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'managed_service_id' is set
        if ('managed_service_id' not in params or
                params['managed_service_id'] is None):
            raise ValueError("Missing the required parameter `managed_service_id` when calling `start1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'managed_service_id' in params:
            path_params['managedServiceId'] = params['managed_service_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/service/{managedServiceId}/start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stop1(self, managed_service_id, **kwargs):  # noqa: E501
        """Stop a managed service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop1(managed_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_service_id: The ID of the managed service to stop (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stop1_with_http_info(managed_service_id, **kwargs)  # noqa: E501
        else:
            (data) = self.stop1_with_http_info(managed_service_id, **kwargs)  # noqa: E501
            return data

    def stop1_with_http_info(self, managed_service_id, **kwargs):  # noqa: E501
        """Stop a managed service  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stop1_with_http_info(managed_service_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str managed_service_id: The ID of the managed service to stop (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['managed_service_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'managed_service_id' is set
        if ('managed_service_id' not in params or
                params['managed_service_id'] is None):
            raise ValueError("Missing the required parameter `managed_service_id` when calling `stop1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'managed_service_id' in params:
            path_params['managedServiceId'] = params['managed_service_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/service/{managedServiceId}/stop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
