# collibra_core.JDBCDriverApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_jdbc_drivers**](JDBCDriverApi.md#find_jdbc_drivers) | **GET** /jdbc | Find JDBC Drivers

# **find_jdbc_drivers**
> JdbcDriverPagedResponse find_jdbc_drivers(offset=offset, limit=limit, count_limit=count_limit, database_name=database_name, database_version=database_version)

Find JDBC Drivers

Finds JDBC drivers that match the given search criteria. By default a result containing 1000 JDBC drivers are returned.<br />This operation is deprecated and it will be removed in the future.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_core.JDBCDriverApi()
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
database_name = 'database_name_example' # str |  (optional)
database_version = 'database_version_example' # str |  (optional)

try:
    # Find JDBC Drivers
    api_response = api_instance.find_jdbc_drivers(offset=offset, limit=limit, count_limit=count_limit, database_name=database_name, database_version=database_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JDBCDriverApi->find_jdbc_drivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **database_name** | **str**|  | [optional] 
 **database_version** | **str**|  | [optional] 

### Return type

[**JdbcDriverPagedResponse**](JdbcDriverPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

