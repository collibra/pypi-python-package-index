# collibra_core.SAMLApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_certificate**](SAMLApi.md#change_certificate) | **POST** /security/saml/certificate/{type} | Changes the certificate to be used with SAML
[**delete_customizations**](SAMLApi.md#delete_customizations) | **DELETE** /security/saml/certificate/{type} | Delete the specified SAML certificate from the SAML keystore.
[**get_sp_metadata_as_string**](SAMLApi.md#get_sp_metadata_as_string) | **GET** /security/saml | Returns the SAML Service Provider metadata for this instance.

# **change_certificate**
> change_certificate(type, file=file)

Changes the certificate to be used with SAML

Replaces the currently used certificate with the one uploaded in PEM format. The PEM file must be unencrypted (no password) and contain both the certificate and the private key.

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
api_instance = collibra_core.SAMLApi(collibra_core.ApiClient(configuration))
type = 'type_example' # str | 
file = NULL # object |  (optional)

try:
    # Changes the certificate to be used with SAML
    api_instance.change_certificate(type, file=file)
except ApiException as e:
    print("Exception when calling SAMLApi->change_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **file** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customizations**
> delete_customizations(type)

Delete the specified SAML certificate from the SAML keystore.

Delete the certificate from the SAML keystore and replace it with a generated certificate as done by default.

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
api_instance = collibra_core.SAMLApi(collibra_core.ApiClient(configuration))
type = 'type_example' # str | 

try:
    # Delete the specified SAML certificate from the SAML keystore.
    api_instance.delete_customizations(type)
except ApiException as e:
    print("Exception when calling SAMLApi->delete_customizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sp_metadata_as_string**
> get_sp_metadata_as_string(complete=complete)

Returns the SAML Service Provider metadata for this instance.

Returns the SAML Service Provider metadata for this instance.

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
api_instance = collibra_core.SAMLApi(collibra_core.ApiClient(configuration))
complete = true # bool | Whether or not the meta data generated should include the non-required attributes (completeMetadata = true means all the non-essential attributes too). (optional)

try:
    # Returns the SAML Service Provider metadata for this instance.
    api_instance.get_sp_metadata_as_string(complete=complete)
except ApiException as e:
    print("Exception when calling SAMLApi->get_sp_metadata_as_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complete** | **bool**| Whether or not the meta data generated should include the non-required attributes (completeMetadata &#x3D; true means all the non-essential attributes too). | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

