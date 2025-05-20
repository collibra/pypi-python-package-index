# collibra_catalog_cloud_ingestions.TABLEAUApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_capability**](TABLEAUApi.md#attach_capability) | **PUT** /filesystem/{fileSystemType}/{assetId}/capability | Add a capability
[**cancel**](TABLEAUApi.md#cancel) | **DELETE** /filesystem/{fileSystemType}/{assetId}/synchronize | Schedule canceling of cloud synchronization
[**detach_capability**](TABLEAUApi.md#detach_capability) | **DELETE** /filesystem/{fileSystemType}/{assetId}/capability | Remove a capability
[**find_filesystem_asset_ids_for_capability**](TABLEAUApi.md#find_filesystem_asset_ids_for_capability) | **GET** /filesystem | Find filesystem assets that have the given Edge capability attached
[**get_attached_capability_id**](TABLEAUApi.md#get_attached_capability_id) | **GET** /filesystem/{fileSystemType}/{assetId}/capability | Retrieve a capability
[**synchronize_file_system**](TABLEAUApi.md#synchronize_file_system) | **POST** /filesystem/{fileSystemType}/{assetId}/synchronize | Synchronize a file system

# **attach_capability**
> attach_capability(file_system_type, asset_id, body=body)

Add a capability

Adds a capability to the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.TABLEAUApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Add a capability
    api_instance.attach_capability(file_system_type, asset_id, body=body)
except ApiException as e:
    print("Exception when calling TABLEAUApi->attach_capability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = collibra_catalog_cloud_ingestions.TABLEAUApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Schedule canceling of cloud synchronization
    api_instance.cancel(file_system_type, asset_id)
except ApiException as e:
    print("Exception when calling TABLEAUApi->cancel: %s\n" % e)
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

# **detach_capability**
> detach_capability(file_system_type, asset_id)

Remove a capability

Removes a capability from the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.TABLEAUApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Remove a capability
    api_instance.detach_capability(file_system_type, asset_id)
except ApiException as e:
    print("Exception when calling TABLEAUApi->detach_capability: %s\n" % e)
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

# **find_filesystem_asset_ids_for_capability**
> list[str] find_filesystem_asset_ids_for_capability(capability_id=capability_id)

Find filesystem assets that have the given Edge capability attached

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
api_instance = collibra_catalog_cloud_ingestions.TABLEAUApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
capability_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Find filesystem assets that have the given Edge capability attached
    api_response = api_instance.find_filesystem_asset_ids_for_capability(capability_id=capability_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TABLEAUApi->find_filesystem_asset_ids_for_capability: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capability_id** | [**str**](.md)|  | [optional] 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attached_capability_id**
> str get_attached_capability_id(file_system_type, asset_id)

Retrieve a capability

Returns the capability of the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.TABLEAUApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve a capability
    api_response = api_instance.get_attached_capability_id(file_system_type, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TABLEAUApi->get_attached_capability_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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
api_instance = collibra_catalog_cloud_ingestions.TABLEAUApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Synchronize a file system
    api_response = api_instance.synchronize_file_system(file_system_type, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TABLEAUApi->synchronize_file_system: %s\n" % e)
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

