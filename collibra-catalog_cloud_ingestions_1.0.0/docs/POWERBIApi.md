# collibra_catalog_cloud_ingestions.POWERBIApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](POWERBIApi.md#cancel) | **DELETE** /filesystem/{fileSystemType}/{assetId}/synchronize | Schedule canceling of cloud synchronization
[**synchronize_file_system**](POWERBIApi.md#synchronize_file_system) | **POST** /filesystem/{fileSystemType}/{assetId}/synchronize | Synchronize a file system

# **cancel**
> cancel(file_system_type, asset_id)

Schedule canceling of cloud synchronization

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_cloud_ingestions.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.POWERBIApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Schedule canceling of cloud synchronization
    api_instance.cancel(file_system_type, asset_id)
except ApiException as e:
    print("Exception when calling POWERBIApi->cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_file_system**
> Job synchronize_file_system(file_system_type, asset_id)

Synchronize a file system

Starts an asynchronous Edge synchronization job for the file system or capability with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_cloud_ingestions.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.POWERBIApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Synchronize a file system
    api_response = api_instance.synchronize_file_system(file_system_type, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling POWERBIApi->synchronize_file_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

