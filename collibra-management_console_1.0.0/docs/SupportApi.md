# collibra_management_console.SupportApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_support_file**](SupportApi.md#create_support_file) | **POST** /support/{environmentId}/zip | Create a diagnostic file for a specified environment
[**delete_support_file**](SupportApi.md#delete_support_file) | **DELETE** /support/{id} | Delete a diagnostic file
[**find_all5**](SupportApi.md#find_all5) | **GET** /support | List all diagnostic files
[**get_file3**](SupportApi.md#get_file3) | **GET** /support/{id} | Download a diagnostic file

# **create_support_file**
> SupportModel create_support_file(environment_id, body=body)

Create a diagnostic file for a specified environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.SupportApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment
body = collibra_management_console.SupportSpecificationModel() # SupportSpecificationModel | The model to describe what to include in the diagnostic file (optional)

try:
    # Create a diagnostic file for a specified environment
    api_response = api_instance.create_support_file(environment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportApi->create_support_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 
 **body** | [**SupportSpecificationModel**](SupportSpecificationModel.md)| The model to describe what to include in the diagnostic file | [optional] 

### Return type

[**SupportModel**](SupportModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_support_file**
> delete_support_file(id)

Delete a diagnostic file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.SupportApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target diagnostic file

try:
    # Delete a diagnostic file
    api_instance.delete_support_file(id)
except ApiException as e:
    print("Exception when calling SupportApi->delete_support_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the target diagnostic file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all5**
> list[SupportModel] find_all5()

List all diagnostic files

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.SupportApi()

try:
    # List all diagnostic files
    api_response = api_instance.find_all5()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportApi->find_all5: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SupportModel]**](SupportModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file3**
> get_file3(id)

Download a diagnostic file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.SupportApi()
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target diagnostic file

try:
    # Download a diagnostic file
    api_instance.get_file3(id)
except ApiException as e:
    print("Exception when calling SupportApi->get_file3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the target diagnostic file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

