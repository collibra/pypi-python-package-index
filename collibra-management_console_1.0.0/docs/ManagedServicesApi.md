# collibra_management_console.ManagedServicesApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change1**](ManagedServicesApi.md#change1) | **PUT** /service/{managedServiceId} | Change an existing managed service
[**find_all2**](ManagedServicesApi.md#find_all2) | **GET** /service | List all managed services
[**get_by_id3**](ManagedServicesApi.md#get_by_id3) | **GET** /service/{managedServiceId} | Get a managed service by ID
[**start1**](ManagedServicesApi.md#start1) | **POST** /service/{managedServiceId}/start | Start a managed service
[**stop1**](ManagedServicesApi.md#stop1) | **POST** /service/{managedServiceId}/stop | Stop a managed service

# **change1**
> ManagedServiceModel change1(managed_service_id, body=body)

Change an existing managed service

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ManagedServicesApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the managed service to change
body = collibra_management_console.ManagedServiceModel() # ManagedServiceModel | The new model for the managed service to change (optional)

try:
    # Change an existing managed service
    api_response = api_instance.change1(managed_service_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServicesApi->change1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)| The ID of the managed service to change | 
 **body** | [**ManagedServiceModel**](ManagedServiceModel.md)| The new model for the managed service to change | [optional] 

### Return type

[**ManagedServiceModel**](ManagedServiceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all2**
> find_all2()

List all managed services

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ManagedServicesApi()

try:
    # List all managed services
    api_instance.find_all2()
except ApiException as e:
    print("Exception when calling ManagedServicesApi->find_all2: %s\n" % e)
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

# **get_by_id3**
> ManagedServiceModel get_by_id3(managed_service_id)

Get a managed service by ID

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ManagedServicesApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the managed service

try:
    # Get a managed service by ID
    api_response = api_instance.get_by_id3(managed_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManagedServicesApi->get_by_id3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)| The ID of the managed service | 

### Return type

[**ManagedServiceModel**](ManagedServiceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start1**
> start1(managed_service_id)

Start a managed service

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ManagedServicesApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the managed service to start

try:
    # Start a managed service
    api_instance.start1(managed_service_id)
except ApiException as e:
    print("Exception when calling ManagedServicesApi->start1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)| The ID of the managed service to start | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop1**
> stop1(managed_service_id)

Stop a managed service

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ManagedServicesApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the managed service to stop

try:
    # Stop a managed service
    api_instance.stop1(managed_service_id)
except ApiException as e:
    print("Exception when calling ManagedServicesApi->stop1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)| The ID of the managed service to stop | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

