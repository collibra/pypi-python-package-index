# collibra_management_console.JvmApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration_definition1**](JvmApi.md#get_configuration_definition1) | **GET** /jvm/definition | Get JVM configuration definition

# **get_configuration_definition1**
> get_configuration_definition1()

Get JVM configuration definition

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JvmApi()

try:
    # Get JVM configuration definition
    api_instance.get_configuration_definition1()
except ApiException as e:
    print("Exception when calling JvmApi->get_configuration_definition1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

