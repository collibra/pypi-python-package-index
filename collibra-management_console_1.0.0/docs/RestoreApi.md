# collibra_management_console.RestoreApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_restore**](RestoreApi.md#cancel_restore) | **PUT** /restore/{environmentId}/cancel | Cancel a restore operation in progress
[**restore_backup_from_id**](RestoreApi.md#restore_backup_from_id) | **POST** /restore/{environmentId} | Restore a backup to an environment
[**restore_to_factory_defaults**](RestoreApi.md#restore_to_factory_defaults) | **POST** /restore/{environmentId}/factoryDefaults | Restore an environment to factory defaults
[**state_map**](RestoreApi.md#state_map) | **GET** /restore/{environmentId}/state | Retrieve the state of all steps of the restore operation on a specified environment

# **cancel_restore**
> cancel_restore(environment_id)

Cancel a restore operation in progress

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.RestoreApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment

try:
    # Cancel a restore operation in progress
    api_instance.cancel_restore(environment_id)
except ApiException as e:
    print("Exception when calling RestoreApi->cancel_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_backup_from_id**
> restore_backup_from_id(environment_id, body=body)

Restore a backup to an environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.RestoreApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment
body = collibra_management_console.RestoreSpecificationModel() # RestoreSpecificationModel | The model to describe what to restore (optional)

try:
    # Restore a backup to an environment
    api_instance.restore_backup_from_id(environment_id, body=body)
except ApiException as e:
    print("Exception when calling RestoreApi->restore_backup_from_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 
 **body** | [**RestoreSpecificationModel**](RestoreSpecificationModel.md)| The model to describe what to restore | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_to_factory_defaults**
> restore_to_factory_defaults(environment_id)

Restore an environment to factory defaults

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.RestoreApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment

try:
    # Restore an environment to factory defaults
    api_instance.restore_to_factory_defaults(environment_id)
except ApiException as e:
    print("Exception when calling RestoreApi->restore_to_factory_defaults: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_map**
> state_map(environment_id)

Retrieve the state of all steps of the restore operation on a specified environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.RestoreApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment

try:
    # Retrieve the state of all steps of the restore operation on a specified environment
    api_instance.state_map(environment_id)
except ApiException as e:
    print("Exception when calling RestoreApi->state_map: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

