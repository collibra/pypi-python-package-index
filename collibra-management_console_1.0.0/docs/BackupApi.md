# collibra_management_console.BackupApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup**](BackupApi.md#backup) | **POST** /backup/{environmentId} | Create a backup for the specified environment
[**delete_backup**](BackupApi.md#delete_backup) | **DELETE** /backup/file/{id} | Delete a backup
[**find_all**](BackupApi.md#find_all) | **GET** /backup | List all backups
[**get_by_id**](BackupApi.md#get_by_id) | **GET** /backup/id/{backupId} | Get a backup by ID
[**get_current_state_map**](BackupApi.md#get_current_state_map) | **GET** /backup/{environmentId}/state | Get the state of the current backup for the specified environment
[**get_file**](BackupApi.md#get_file) | **POST** /backup/file/{id} | Download a backup file
[**is_environment_backing_up**](BackupApi.md#is_environment_backing_up) | **GET** /backup/{environmentId}/globalState | Get the global status of the current backup for the specified environment
[**update_backup_information**](BackupApi.md#update_backup_information) | **POST** /backup/{id}/backupinformation | Update name and/or description of an existing backup
[**upload_backup**](BackupApi.md#upload_backup) | **POST** /backup | Upload a backup file
[**upload_backup_async_validation**](BackupApi.md#upload_backup_async_validation) | **POST** /backup/async | Upload a backup file and process it asynchronously

# **backup**
> BackupModel backup(environment_id, body=body)

Create a backup for the specified environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment to backup
body = collibra_management_console.BackupSpecificationModel() # BackupSpecificationModel | The specification for the backup to create (optional)

try:
    # Create a backup for the specified environment
    api_response = api_instance.backup(environment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the environment to backup | 
 **body** | [**BackupSpecificationModel**](BackupSpecificationModel.md)| The specification for the backup to create | [optional] 

### Return type

[**BackupModel**](BackupModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_backup**
> delete_backup(id)

Delete a backup

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the backup to delete

try:
    # Delete a backup
    api_instance.delete_backup(id)
except ApiException as e:
    print("Exception when calling BackupApi->delete_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the backup to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all**
> list[BackupModel] find_all()

List all backups

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()

try:
    # List all backups
    api_response = api_instance.find_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->find_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BackupModel]**](BackupModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id**
> BackupModel get_by_id(backup_id)

Get a backup by ID

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
backup_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the backup to retrieve

try:
    # Get a backup by ID
    api_response = api_instance.get_by_id(backup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backup_id** | [**str**](.md)| The ID of the backup to retrieve | 

### Return type

[**BackupModel**](BackupModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_state_map**
> get_current_state_map(environment_id)

Get the state of the current backup for the specified environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment

try:
    # Get the state of the current backup for the specified environment
    api_instance.get_current_state_map(environment_id)
except ApiException as e:
    print("Exception when calling BackupApi->get_current_state_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the environment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> get_file(id, key=key)

Download a backup file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The backup id
key = 'key_example' # str |  (optional)

try:
    # Download a backup file
    api_instance.get_file(id, key=key)
except ApiException as e:
    print("Exception when calling BackupApi->get_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The backup id | 
 **key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_environment_backing_up**
> bool is_environment_backing_up(environment_id)

Get the global status of the current backup for the specified environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment

try:
    # Get the global status of the current backup for the specified environment
    api_response = api_instance.is_environment_backing_up(environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->is_environment_backing_up: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the environment | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_backup_information**
> update_backup_information(id, description=description, name=name)

Update name and/or description of an existing backup

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
description = 'description_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    # Update name and/or description of an existing backup
    api_instance.update_backup_information(id, description=description, name=name)
except ApiException as e:
    print("Exception when calling BackupApi->update_backup_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **description** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_backup**
> BackupModel upload_backup(body=body)

Upload a backup file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
body = collibra_management_console.BackupBody() # BackupBody |  (optional)

try:
    # Upload a backup file
    api_response = api_instance.upload_backup(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->upload_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupBody**](BackupBody.md)|  | [optional] 

### Return type

[**BackupModel**](BackupModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_backup_async_validation**
> upload_backup_async_validation(body=body)

Upload a backup file and process it asynchronously

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi()
body = collibra_management_console.BackupAsyncBody() # BackupAsyncBody |  (optional)

try:
    # Upload a backup file and process it asynchronously
    api_instance.upload_backup_async_validation(body=body)
except ApiException as e:
    print("Exception when calling BackupApi->upload_backup_async_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupAsyncBody**](BackupAsyncBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

