# collibra_core.FilesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_files**](FilesApi.md#add_files) | **POST** /files | Upload files
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /files/{fileId} | Delete file
[**delete_files**](FilesApi.md#delete_files) | **DELETE** /files/bulk | Delete multiple files
[**get_file**](FilesApi.md#get_file) | **GET** /files/{fileId} | Download file
[**get_file_info**](FilesApi.md#get_file_info) | **GET** /files/{fileId}/info | Get file information

# **add_files**
> list[FileInfoImpl] add_files(file=file)

Upload files

Upload files

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
api_instance = collibra_core.FilesApi(collibra_core.ApiClient(configuration))
file = 'file_example' # str |  (optional)

try:
    # Upload files
    api_response = api_instance.add_files(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->add_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 

### Return type

[**list[FileInfoImpl]**](FileInfoImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(file_id)

Delete file

Delete file for a given Id

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
api_instance = collibra_core.FilesApi(collibra_core.ApiClient(configuration))
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the file

try:
    # Delete file
    api_instance.delete_file(file_id)
except ApiException as e:
    print("Exception when calling FilesApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)| the id of the file | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_files**
> delete_files(time_to_live=time_to_live)

Delete multiple files

Deletes files that are older than the given time to live.

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
api_instance = collibra_core.FilesApi(collibra_core.ApiClient(configuration))
time_to_live = 789 # int |  (optional)

try:
    # Delete multiple files
    api_instance.delete_files(time_to_live=time_to_live)
except ApiException as e:
    print("Exception when calling FilesApi->delete_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_to_live** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> str get_file(file_id)

Download file

Downloads file identified by given id.  Keep in mind to use GET /attachments/{attachmentId}/file instead of this endpoint when you want to get the file of an attachment.  A File and its id can be temporary so it's possible this endpoint will not get you the desired file.

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
api_instance = collibra_core.FilesApi(collibra_core.ApiClient(configuration))
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the file

try:
    # Download file
    api_response = api_instance.get_file(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)| the id of the file | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_info**
> ScopeImpl get_file_info(file_id)

Get file information

Returns information about the file identified by given id. Keep in mind to use GET /attachments/{attachmentId} instead of this endpoint when you want to get information of an attachment. A File and its id can be temporary so it's possible this endpoint will not get you the information of the desired file.

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
api_instance = collibra_core.FilesApi(collibra_core.ApiClient(configuration))
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the file

try:
    # Get file information
    api_response = api_instance.get_file_info(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_file_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)| the id of the file | 

### Return type

[**ScopeImpl**](ScopeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

