# collibra_catalog_cloud_ingestions.GCSApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_crawler**](GCSApi.md#add_crawler) | **POST** /filesystem/{fileSystemType}/{assetId}/crawlers | Add a crawler
[**add_schedule**](GCSApi.md#add_schedule) | **POST** /filesystem/{fileSystemType}/{assetId}/schedule | Add a synchronization schedule
[**attach_capability**](GCSApi.md#attach_capability) | **PUT** /filesystem/{fileSystemType}/{assetId}/capability | Add a capability
[**cancel**](GCSApi.md#cancel) | **DELETE** /filesystem/{fileSystemType}/{assetId}/synchronize | Schedule canceling of cloud synchronization
[**delete_crawler**](GCSApi.md#delete_crawler) | **DELETE** /filesystem/{fileSystemType}/{assetId}/crawlers | Delete a crawler
[**delete_schedule**](GCSApi.md#delete_schedule) | **DELETE** /filesystem/{fileSystemType}/{assetId}/schedule | Delete a synchronization schedule
[**detach_capability**](GCSApi.md#detach_capability) | **DELETE** /filesystem/{fileSystemType}/{assetId}/capability | Remove a capability
[**find_filesystem_asset_ids_for_capability**](GCSApi.md#find_filesystem_asset_ids_for_capability) | **GET** /filesystem | Find filesystem assets that have the given Edge capability attached
[**get_attached_capability_id**](GCSApi.md#get_attached_capability_id) | **GET** /filesystem/{fileSystemType}/{assetId}/capability | Retrieve a capability
[**get_crawlers**](GCSApi.md#get_crawlers) | **GET** /filesystem/{fileSystemType}/{assetId}/crawlers | List crawlers
[**get_schedule**](GCSApi.md#get_schedule) | **GET** /filesystem/{fileSystemType}/{assetId}/schedule | Retrieve a synchronization schedule
[**synchronize_file_system**](GCSApi.md#synchronize_file_system) | **POST** /filesystem/{fileSystemType}/{assetId}/synchronize | Synchronize a file system
[**update_crawler**](GCSApi.md#update_crawler) | **PUT** /filesystem/{fileSystemType}/{assetId}/crawlers | Update a crawler
[**update_schedule**](GCSApi.md#update_schedule) | **PUT** /filesystem/{fileSystemType}/{assetId}/schedule | Update a synchronization schedule

# **add_crawler**
> Crawler add_crawler(file_system_type, asset_id, body=body)

Add a crawler

Adds a new crawler definition to the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_catalog_cloud_ingestions.AddCrawlerRequest() # AddCrawlerRequest |  (optional)

try:
    # Add a crawler
    api_response = api_instance.add_crawler(file_system_type, asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->add_crawler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 
 **body** | [**AddCrawlerRequest**](AddCrawlerRequest.md)|  | [optional] 

### Return type

[**Crawler**](Crawler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_schedule**
> Schedule add_schedule(file_system_type, asset_id, body=body)

Add a synchronization schedule

Adds a synchronization schedule for the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_catalog_cloud_ingestions.AddFileSystemScheduleRequest() # AddFileSystemScheduleRequest |  (optional)

try:
    # Add a synchronization schedule
    api_response = api_instance.add_schedule(file_system_type, asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->add_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 
 **body** | [**AddFileSystemScheduleRequest**](AddFileSystemScheduleRequest.md)|  | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Add a capability
    api_instance.attach_capability(file_system_type, asset_id, body=body)
except ApiException as e:
    print("Exception when calling GCSApi->attach_capability: %s\n" % e)
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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Schedule canceling of cloud synchronization
    api_instance.cancel(file_system_type, asset_id)
except ApiException as e:
    print("Exception when calling GCSApi->cancel: %s\n" % e)
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

# **delete_crawler**
> delete_crawler(file_system_type, asset_id, body=body)

Delete a crawler

Deletes a crawler definition from the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_catalog_cloud_ingestions.RemoveCrawlerRequest() # RemoveCrawlerRequest |  (optional)

try:
    # Delete a crawler
    api_instance.delete_crawler(file_system_type, asset_id, body=body)
except ApiException as e:
    print("Exception when calling GCSApi->delete_crawler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 
 **body** | [**RemoveCrawlerRequest**](RemoveCrawlerRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule**
> delete_schedule(file_system_type, asset_id)

Delete a synchronization schedule

Deletes a synchronization schedule for the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a synchronization schedule
    api_instance.delete_schedule(file_system_type, asset_id)
except ApiException as e:
    print("Exception when calling GCSApi->delete_schedule: %s\n" % e)
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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Remove a capability
    api_instance.detach_capability(file_system_type, asset_id)
except ApiException as e:
    print("Exception when calling GCSApi->detach_capability: %s\n" % e)
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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
capability_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Find filesystem assets that have the given Edge capability attached
    api_response = api_instance.find_filesystem_asset_ids_for_capability(capability_id=capability_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->find_filesystem_asset_ids_for_capability: %s\n" % e)
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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve a capability
    api_response = api_instance.get_attached_capability_id(file_system_type, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->get_attached_capability_id: %s\n" % e)
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

# **get_crawlers**
> list[Crawler] get_crawlers(file_system_type, asset_id)

List crawlers

Returns a list of crawlers that are defined for the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # List crawlers
    api_response = api_instance.get_crawlers(file_system_type, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->get_crawlers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 

### Return type

[**list[Crawler]**](Crawler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule**
> Schedule get_schedule(file_system_type, asset_id)

Retrieve a synchronization schedule

Returns the synchronization schedule for the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve a synchronization schedule
    api_response = api_instance.get_schedule(file_system_type, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->get_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 

### Return type

[**Schedule**](Schedule.md)

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Synchronize a file system
    api_response = api_instance.synchronize_file_system(file_system_type, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->synchronize_file_system: %s\n" % e)
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

# **update_crawler**
> Crawler update_crawler(file_system_type, asset_id, body=body)

Update a crawler

Updates a crawler definition for the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_catalog_cloud_ingestions.UpdateCrawlerRequest() # UpdateCrawlerRequest |  (optional)

try:
    # Update a crawler
    api_response = api_instance.update_crawler(file_system_type, asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->update_crawler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 
 **body** | [**UpdateCrawlerRequest**](UpdateCrawlerRequest.md)|  | [optional] 

### Return type

[**Crawler**](Crawler.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule**
> Schedule update_schedule(file_system_type, asset_id, body=body)

Update a synchronization schedule

Updates a synchronization schedule for the file system with the specified ID.

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
api_instance = collibra_catalog_cloud_ingestions.GCSApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
file_system_type = 'file_system_type_example' # str | 
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_catalog_cloud_ingestions.ChangeFileSystemScheduleRequest() # ChangeFileSystemScheduleRequest |  (optional)

try:
    # Update a synchronization schedule
    api_response = api_instance.update_schedule(file_system_type, asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GCSApi->update_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_type** | **str**|  | 
 **asset_id** | [**str**](.md)|  | 
 **body** | [**ChangeFileSystemScheduleRequest**](ChangeFileSystemScheduleRequest.md)|  | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

