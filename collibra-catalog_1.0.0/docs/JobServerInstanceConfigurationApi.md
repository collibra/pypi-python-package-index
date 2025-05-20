# collibra_catalog.JobServerInstanceConfigurationApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_job_server_instances**](JobServerInstanceConfigurationApi.md#get_available_job_server_instances) | **GET** /configuration/jobServerInstance | Retrieve existing JobServer instance configurations

# **get_available_job_server_instances**
> JobServerInstanceResponse get_available_job_server_instances(offset=offset, limit=limit, count_limit=count_limit)

Retrieve existing JobServer instance configurations

Retrieve existing JobServer instance configurations. <br />This operation is deprecated and it will be removed the next major release

### Example
```python
from __future__ import print_function
import time
import collibra_catalog
from collibra_catalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog.JobServerInstanceConfigurationApi()
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)

try:
    # Retrieve existing JobServer instance configurations
    api_response = api_instance.get_available_job_server_instances(offset=offset, limit=limit, count_limit=count_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobServerInstanceConfigurationApi->get_available_job_server_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]

### Return type

[**JobServerInstanceResponse**](JobServerInstanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

