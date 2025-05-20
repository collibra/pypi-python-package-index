# collibra_core.ApplicationApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_info**](ApplicationApi.md#get_info) | **GET** /application/info | Returns the basic information about the application.

# **get_info**
> ApplicationInfo get_info()

Returns the basic information about the application.

Returns the basic information about the application.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ApplicationApi(collibra_core.ApiClient(configuration))

try:
    # Returns the basic information about the application.
    api_response = api_instance.get_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->get_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationInfo**](ApplicationInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

