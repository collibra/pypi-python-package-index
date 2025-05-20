# collibra_protect.CustomMaskingsApi

All URIs are relative to */rest/protect/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_masking**](CustomMaskingsApi.md#add_custom_masking) | **POST** /customMaskings | Add a new custom masking
[**delete_custom_masking**](CustomMaskingsApi.md#delete_custom_masking) | **DELETE** /customMaskings/{id} | Delete a custom masking
[**get_custom_masking**](CustomMaskingsApi.md#get_custom_masking) | **GET** /customMaskings/{id} | Retrieve a custom masking
[**list_custom_maskings**](CustomMaskingsApi.md#list_custom_maskings) | **GET** /customMaskings | List custom maskings
[**patch_custom_masking**](CustomMaskingsApi.md#patch_custom_masking) | **PATCH** /customMaskings/{id} | Update a custom masking

# **add_custom_masking**
> CustomMasking add_custom_masking(body)

Add a new custom masking

Adds a new custom masking.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.CustomMaskingsApi(collibra_protect.ApiClient(configuration))
body = collibra_protect.AddCustomMaskingRequest() # AddCustomMaskingRequest | The new custom masking you want to add.

try:
    # Add a new custom masking
    api_response = api_instance.add_custom_masking(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMaskingsApi->add_custom_masking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddCustomMaskingRequest**](AddCustomMaskingRequest.md)| The new custom masking you want to add. | 

### Return type

[**CustomMasking**](CustomMasking.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_masking**
> delete_custom_masking(id)

Delete a custom masking

Deletes the custom masking with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.CustomMaskingsApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the custom masking.

try:
    # Delete a custom masking
    api_instance.delete_custom_masking(id)
except ApiException as e:
    print("Exception when calling CustomMaskingsApi->delete_custom_masking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the custom masking. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_masking**
> CustomMasking get_custom_masking(id)

Retrieve a custom masking

Returns information about the custom masking with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.CustomMaskingsApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the custom masking.

try:
    # Retrieve a custom masking
    api_response = api_instance.get_custom_masking(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMaskingsApi->get_custom_masking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the custom masking. | 

### Return type

[**CustomMasking**](CustomMasking.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_maskings**
> PagedCustomMaskings list_custom_maskings(limit=limit, after=after)

List custom maskings

Lists all custom maskings.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.CustomMaskingsApi(collibra_protect.ApiClient(configuration))
limit = 25 # int | This is the maximum number of results that may be returned. Fewer may be returned than the value of <code>limit</code>.  Do not depend on the number of results being fewer than the <code>limit</code> value to indicate that your query reached the end of the list of data, use the absence of <code>after</code> (see Cursors) instead. For example, if you set <code>limit</code> to 10 and 9 results are returned, there may be more data available.  If not set, the default limit (limit = <code>25</code>) will be used. The maximum value for this parameter is <code>500</code>.  (optional) (default to 25)
after = 'after_example' # str | This is the cursor that points to the end of the page of data that has been returned. (optional)

try:
    # List custom maskings
    api_response = api_instance.list_custom_maskings(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMaskingsApi->list_custom_maskings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| This is the maximum number of results that may be returned. Fewer may be returned than the value of &lt;code&gt;limit&lt;/code&gt;.  Do not depend on the number of results being fewer than the &lt;code&gt;limit&lt;/code&gt; value to indicate that your query reached the end of the list of data, use the absence of &lt;code&gt;after&lt;/code&gt; (see Cursors) instead. For example, if you set &lt;code&gt;limit&lt;/code&gt; to 10 and 9 results are returned, there may be more data available.  If not set, the default limit (limit &#x3D; &lt;code&gt;25&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;/code&gt;.  | [optional] [default to 25]
 **after** | **str**| This is the cursor that points to the end of the page of data that has been returned. | [optional] 

### Return type

[**PagedCustomMaskings**](PagedCustomMaskings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_custom_masking**
> CustomMasking patch_custom_masking(id, body=body)

Update a custom masking

Updates the custom masking with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.CustomMaskingsApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the custom masking.
body = collibra_protect.ChangeCustomMaskingRequest() # ChangeCustomMaskingRequest | The changes that need to be applied to the custom masking. (optional)

try:
    # Update a custom masking
    api_response = api_instance.patch_custom_masking(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomMaskingsApi->patch_custom_masking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the custom masking. | 
 **body** | [**ChangeCustomMaskingRequest**](ChangeCustomMaskingRequest.md)| The changes that need to be applied to the custom masking. | [optional] 

### Return type

[**CustomMasking**](CustomMasking.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

