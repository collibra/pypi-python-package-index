# collibra_management_console.DgcLicenseApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_license**](DgcLicenseApi.md#update_license) | **POST** /license/{environmentId}/licenseText | Update the license by providing the content of the new license file
[**update_license1**](DgcLicenseApi.md#update_license1) | **POST** /license/{environmentId}/licenseFile | Update the license by uploading a new license file

# **update_license**
> update_license(environment_id, body=body)

Update the license by providing the content of the new license file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcLicenseApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment
body = 'body_example' # str |  (optional)

try:
    # Update the license by providing the content of the new license file
    api_instance.update_license(environment_id, body=body)
except ApiException as e:
    print("Exception when calling DgcLicenseApi->update_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_license1**
> update_license1(body_parts, content_disposition, entity, fields, headers, media_type, message_body_workers, parameterized_headers, parent, providers, environment_id)

Update the license by uploading a new license file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcLicenseApi()
body_parts = [collibra_management_console.BodyPart()] # list[BodyPart] | 
content_disposition = collibra_management_console.ContentDisposition() # ContentDisposition | 
entity = NULL # object | 
fields = {'key': collibra_management_console.list[FormDataBodyPart]()} # dict(str, list[FormDataBodyPart]) | 
headers = collibra_management_console.BodyPartHeaders() # BodyPartHeaders | 
media_type = collibra_management_console.MediaType() # MediaType | 
message_body_workers = collibra_management_console.MessageBodyWorkers() # MessageBodyWorkers | 
parameterized_headers = collibra_management_console.BodyPartParameterizedHeaders() # BodyPartParameterizedHeaders | 
parent = collibra_management_console.MultiPart() # MultiPart | 
providers = collibra_management_console.Providers() # Providers | 
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment

try:
    # Update the license by uploading a new license file
    api_instance.update_license1(body_parts, content_disposition, entity, fields, headers, media_type, message_body_workers, parameterized_headers, parent, providers, environment_id)
except ApiException as e:
    print("Exception when calling DgcLicenseApi->update_license1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_parts** | [**list[BodyPart]**](BodyPart.md)|  | 
 **content_disposition** | [**ContentDisposition**](.md)|  | 
 **entity** | [**object**](.md)|  | 
 **fields** | [**dict(str, list[FormDataBodyPart])**](list[FormDataBodyPart].md)|  | 
 **headers** | [**BodyPartHeaders**](.md)|  | 
 **media_type** | [**MediaType**](.md)|  | 
 **message_body_workers** | [**MessageBodyWorkers**](.md)|  | 
 **parameterized_headers** | [**BodyPartParameterizedHeaders**](.md)|  | 
 **parent** | [**MultiPart**](.md)|  | 
 **providers** | [**Providers**](.md)|  | 
 **environment_id** | [**str**](.md)| The ID of the target environment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

