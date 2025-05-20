# collibra_management_console.DgcLoggerApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_logger_level**](DgcLoggerApi.md#delete_logger_level) | **DELETE** /dgcLog/{managedServiceId}/{logger} | Remove the given DGC logger
[**get_logger_level**](DgcLoggerApi.md#get_logger_level) | **GET** /dgcLog/{managedServiceId}/{logger} | Retrieve the level of the given DGC logger
[**set_logger_level**](DgcLoggerApi.md#set_logger_level) | **POST** /dgcLog | Adjust the level of the given DGC logger

# **delete_logger_level**
> str delete_logger_level(managed_service_id, logger)

Remove the given DGC logger

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcLoggerApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
logger = 'logger_example' # str | 

try:
    # Remove the given DGC logger
    api_response = api_instance.delete_logger_level(managed_service_id, logger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgcLoggerApi->delete_logger_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)|  | 
 **logger** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logger_level**
> str get_logger_level(managed_service_id, logger)

Retrieve the level of the given DGC logger

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcLoggerApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
logger = 'logger_example' # str | 

try:
    # Retrieve the level of the given DGC logger
    api_response = api_instance.get_logger_level(managed_service_id, logger)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgcLoggerApi->get_logger_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)|  | 
 **logger** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_logger_level**
> DGCManagedServiceModel set_logger_level(body=body)

Adjust the level of the given DGC logger

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcLoggerApi()
body = collibra_management_console.SetLoggerLevelRequest() # SetLoggerLevelRequest | the logger identified by its name and the dgc managed service id (optional)

try:
    # Adjust the level of the given DGC logger
    api_response = api_instance.set_logger_level(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgcLoggerApi->set_logger_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetLoggerLevelRequest**](SetLoggerLevelRequest.md)| the logger identified by its name and the dgc managed service id | [optional] 

### Return type

[**DGCManagedServiceModel**](DGCManagedServiceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

