# collibra_management_console.BackupScheduleApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](BackupScheduleApi.md#create) | **POST** /backupSchedule | Create a backup schedule
[**delete**](BackupScheduleApi.md#delete) | **DELETE** /backupSchedule/{id} | Delete a backup schedule
[**get_all**](BackupScheduleApi.md#get_all) | **GET** /backupSchedule | Retrieve all backup schedules
[**get_backups_by_schedule_id**](BackupScheduleApi.md#get_backups_by_schedule_id) | **GET** /backupSchedule/{id}/backups | Retrieve all backups created by a backup schedule
[**get_by_environment_id**](BackupScheduleApi.md#get_by_environment_id) | **GET** /backupSchedule/environment/{environmentId} | Retrieve all backup schedules for the given environment
[**get_by_id1**](BackupScheduleApi.md#get_by_id1) | **GET** /backupSchedule/{id} | Retrieve a backup schedule
[**update**](BackupScheduleApi.md#update) | **PUT** /backupSchedule/{id} | Update a backup schedule

# **create**
> BackupScheduleModel create(body=body)

Create a backup schedule

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupScheduleApi()
body = collibra_management_console.BackupScheduleCreateRequest() # BackupScheduleCreateRequest | The model from which to create the schedule (optional)

try:
    # Create a backup schedule
    api_response = api_instance.create(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupScheduleApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BackupScheduleCreateRequest**](BackupScheduleCreateRequest.md)| The model from which to create the schedule | [optional] 

### Return type

[**BackupScheduleModel**](BackupScheduleModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

Delete a backup schedule

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupScheduleApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the schedule to delete

try:
    # Delete a backup schedule
    api_instance.delete(id)
except ApiException as e:
    print("Exception when calling BackupScheduleApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The id of the schedule to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> list[BackupScheduleModel] get_all()

Retrieve all backup schedules

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupScheduleApi()

try:
    # Retrieve all backup schedules
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupScheduleApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BackupScheduleModel]**](BackupScheduleModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backups_by_schedule_id**
> list[BackupModel] get_backups_by_schedule_id(id)

Retrieve all backups created by a backup schedule

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupScheduleApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the schedule

try:
    # Retrieve all backups created by a backup schedule
    api_response = api_instance.get_backups_by_schedule_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupScheduleApi->get_backups_by_schedule_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The id of the schedule | 

### Return type

[**list[BackupModel]**](BackupModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_environment_id**
> list[BackupScheduleModel] get_by_environment_id(environment_id)

Retrieve all backup schedules for the given environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupScheduleApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the environment

try:
    # Retrieve all backup schedules for the given environment
    api_response = api_instance.get_by_environment_id(environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupScheduleApi->get_by_environment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The id of the environment | 

### Return type

[**list[BackupScheduleModel]**](BackupScheduleModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id1**
> BackupScheduleModel get_by_id1(id)

Retrieve a backup schedule

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupScheduleApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the schedule

try:
    # Retrieve a backup schedule
    api_response = api_instance.get_by_id1(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupScheduleApi->get_by_id1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The id of the schedule | 

### Return type

[**BackupScheduleModel**](BackupScheduleModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> BackupScheduleModel update(id, body=body)

Update a backup schedule

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupScheduleApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the schedule to update
body = collibra_management_console.BackupScheduleUpdateRequest() # BackupScheduleUpdateRequest | The updated schedule (optional)

try:
    # Update a backup schedule
    api_response = api_instance.update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupScheduleApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The id of the schedule to update | 
 **body** | [**BackupScheduleUpdateRequest**](BackupScheduleUpdateRequest.md)| The updated schedule | [optional] 

### Return type

[**BackupScheduleModel**](BackupScheduleModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

