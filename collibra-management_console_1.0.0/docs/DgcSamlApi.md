# collibra_management_console.DgcSamlApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_content**](DgcSamlApi.md#get_content) | **GET** /saml/{environmentId} | Get the contents of the saml.xml configuration file
[**get_file2**](DgcSamlApi.md#get_file2) | **GET** /saml/{environmentId}/file | Download the saml.xml configuration file
[**remove1**](DgcSamlApi.md#remove1) | **DELETE** /saml/{environmentId} | Remove the saml.xml configuration file
[**upload_file1**](DgcSamlApi.md#upload_file1) | **POST** /saml/{environmentId}/file | Update the saml.xml configuration by uploading a new file

# **get_content**
> get_content(environment_id)

Get the contents of the saml.xml configuration file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcSamlApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment

try:
    # Get the contents of the saml.xml configuration file
    api_instance.get_content(environment_id)
except ApiException as e:
    print("Exception when calling DgcSamlApi->get_content: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file2**
> get_file2(environment_id)

Download the saml.xml configuration file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcSamlApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment

try:
    # Download the saml.xml configuration file
    api_instance.get_file2(environment_id)
except ApiException as e:
    print("Exception when calling DgcSamlApi->get_file2: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove1**
> remove1(environment_id)

Remove the saml.xml configuration file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcSamlApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment

try:
    # Remove the saml.xml configuration file
    api_instance.remove1(environment_id)
except ApiException as e:
    print("Exception when calling DgcSamlApi->remove1: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file1**
> upload_file1(body_parts, content_disposition, entity, fields, headers, media_type, message_body_workers, parameterized_headers, parent, providers, environment_id)

Update the saml.xml configuration by uploading a new file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcSamlApi()
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
    # Update the saml.xml configuration by uploading a new file
    api_instance.upload_file1(body_parts, content_disposition, entity, fields, headers, media_type, message_body_workers, parameterized_headers, parent, providers, environment_id)
except ApiException as e:
    print("Exception when calling DgcSamlApi->upload_file1: %s\n" % e)
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
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

