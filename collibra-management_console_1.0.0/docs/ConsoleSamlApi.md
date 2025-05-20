# collibra_management_console.ConsoleSamlApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_certificate**](ConsoleSamlApi.md#change_certificate) | **POST** /samlconsole/certificate | Changes the certificate to be used with SAML
[**delete_certificate**](ConsoleSamlApi.md#delete_certificate) | **DELETE** /samlconsole/certificate | Delete the specified SAML certificate from the SAML keystore.
[**get_file1**](ConsoleSamlApi.md#get_file1) | **GET** /samlconsole | Download the saml.xml configuration file
[**get_sp_metadata_as_string**](ConsoleSamlApi.md#get_sp_metadata_as_string) | **GET** /samlconsole/metadata | Returns the SAML Service Provider metadata for this instance.
[**remove**](ConsoleSamlApi.md#remove) | **DELETE** /samlconsole | Remove the saml.xml configuration file
[**upload_file**](ConsoleSamlApi.md#upload_file) | **POST** /samlconsole | Update the saml.xml configuration by uploading a new file

# **change_certificate**
> change_certificate(file=file)

Changes the certificate to be used with SAML

Replaces the currently used certificate with the one uploaded in PEM format. The PEM file must be unencrypted (no password) and contain both the certificate and the private key.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleSamlApi()
file = NULL # object |  (optional)

try:
    # Changes the certificate to be used with SAML
    api_instance.change_certificate(file=file)
except ApiException as e:
    print("Exception when calling ConsoleSamlApi->change_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate**
> delete_certificate()

Delete the specified SAML certificate from the SAML keystore.

Delete the certificate from the SAML keystore and replace it with a generated certificate as done by default.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleSamlApi()

try:
    # Delete the specified SAML certificate from the SAML keystore.
    api_instance.delete_certificate()
except ApiException as e:
    print("Exception when calling ConsoleSamlApi->delete_certificate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file1**
> get_file1()

Download the saml.xml configuration file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleSamlApi()

try:
    # Download the saml.xml configuration file
    api_instance.get_file1()
except ApiException as e:
    print("Exception when calling ConsoleSamlApi->get_file1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_metadata_as_string**
> get_sp_metadata_as_string(complete=complete)

Returns the SAML Service Provider metadata for this instance.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleSamlApi()
complete = true # bool |  (optional)

try:
    # Returns the SAML Service Provider metadata for this instance.
    api_instance.get_sp_metadata_as_string(complete=complete)
except ApiException as e:
    print("Exception when calling ConsoleSamlApi->get_sp_metadata_as_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complete** | **bool**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> remove()

Remove the saml.xml configuration file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleSamlApi()

try:
    # Remove the saml.xml configuration file
    api_instance.remove()
except ApiException as e:
    print("Exception when calling ConsoleSamlApi->remove: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> upload_file(body_parts, content_disposition, entity, fields, headers, media_type, message_body_workers, parameterized_headers, parent, providers)

Update the saml.xml configuration by uploading a new file

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleSamlApi()
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

try:
    # Update the saml.xml configuration by uploading a new file
    api_instance.upload_file(body_parts, content_disposition, entity, fields, headers, media_type, message_body_workers, parameterized_headers, parent, providers)
except ApiException as e:
    print("Exception when calling ConsoleSamlApi->upload_file: %s\n" % e)
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

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

