# collibra_core.AttributesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attribute**](AttributesApi.md#add_attribute) | **POST** /attributes | Add attribute
[**add_attributes**](AttributesApi.md#add_attributes) | **POST** /attributes/bulk | Add attributes
[**change_attribute**](AttributesApi.md#change_attribute) | **PATCH** /attributes/{attributeId} | Change attribute
[**change_attributes**](AttributesApi.md#change_attributes) | **PATCH** /attributes/bulk | Change attributes
[**find_attributes**](AttributesApi.md#find_attributes) | **GET** /attributes | Find attributes
[**get_attribute**](AttributesApi.md#get_attribute) | **GET** /attributes/{attributeId} | Get attribute
[**remove_attribute**](AttributesApi.md#remove_attribute) | **DELETE** /attributes/{attributeId} | Remove attribute
[**remove_attributes**](AttributesApi.md#remove_attributes) | **DELETE** /attributes/bulk | Remove attributes

# **add_attribute**
> Attribute add_attribute(body=body)

Add attribute

Adds a new attribute to an asset.

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
api_instance = collibra_core.AttributesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddAttributeRequest() # AddAttributeRequest | the properties of the attribute to be added (optional)

try:
    # Add attribute
    api_response = api_instance.add_attribute(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->add_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddAttributeRequest**](AddAttributeRequest.md)| the properties of the attribute to be added | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_attributes**
> list[Attribute] add_attributes(body=body)

Add attributes

Adds multiple attributes.

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
api_instance = collibra_core.AttributesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddAttributeRequest()] # list[AddAttributeRequest] | the list of the properties of the attributes to be added (optional)

try:
    # Add attributes
    api_response = api_instance.add_attributes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->add_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddAttributeRequest]**](AddAttributeRequest.md)| the list of the properties of the attributes to be added | [optional] 

### Return type

[**list[Attribute]**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_attribute**
> Attribute change_attribute(attribute_id, body=body)

Change attribute

Changes the attribute with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.AttributesApi(collibra_core.ApiClient(configuration))
attribute_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the attribute
body = collibra_core.ChangeAttributeRequest() # ChangeAttributeRequest | the properties of the attribute to be changed (optional)

try:
    # Change attribute
    api_response = api_instance.change_attribute(attribute_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->change_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | [**str**](.md)| the id of the attribute | 
 **body** | [**ChangeAttributeRequest**](ChangeAttributeRequest.md)| the properties of the attribute to be changed | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_attributes**
> list[Attribute] change_attributes(body=body)

Change attributes

Changes multiple attributes with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.AttributesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeAttributeRequest()] # list[ChangeAttributeRequest] | the list of properties of the attributes to be changed (optional)

try:
    # Change attributes
    api_response = api_instance.change_attributes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->change_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeAttributeRequest]**](ChangeAttributeRequest.md)| the list of properties of the attributes to be changed | [optional] 

### Return type

[**list[Attribute]**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_attributes**
> AttributePagedResponse find_attributes(sort_field, offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, type_ids=type_ids, asset_id=asset_id, sort_order=sort_order)

Find attributes

Returns attributes matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attributes satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attributes is returned.

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
api_instance = collibra_core.AttributesApi(collibra_core.ApiClient(configuration))
sort_field = 'LAST_MODIFIED' # str | The field on which the results are sorted. (default to LAST_MODIFIED)
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. (optional) (default to -1)
cursor = 'cursor_example' # str | Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (<code>nextCursor</code> property). (optional)
type_ids = ['type_ids_example'] # list[str] | The list of IDs of the attribute types the found attributes should have, or null or empty if no type filtering should be applied. (optional)
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the asset to find the attributes in, or null if no asset filtering should be applied. (optional)
sort_order = 'DESC' # str | The sorting order. (optional) (default to DESC)

try:
    # Find attributes
    api_response = api_instance.find_attributes(sort_field, offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, type_ids=type_ids, asset_id=asset_id, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->find_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_field** | **str**| The field on which the results are sorted. | [default to LAST_MODIFIED]
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. | [optional] [default to -1]
 **cursor** | **str**| Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (&lt;code&gt;nextCursor&lt;/code&gt; property). | [optional] 
 **type_ids** | [**list[str]**](str.md)| The list of IDs of the attribute types the found attributes should have, or null or empty if no type filtering should be applied. | [optional] 
 **asset_id** | [**str**](.md)| The ID of the asset to find the attributes in, or null if no asset filtering should be applied. | [optional] 
 **sort_order** | **str**| The sorting order. | [optional] [default to DESC]

### Return type

[**AttributePagedResponse**](AttributePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute**
> Attribute get_attribute(attribute_id)

Get attribute

Returns the attribute identified by given id.

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
api_instance = collibra_core.AttributesApi(collibra_core.ApiClient(configuration))
attribute_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the attribute

try:
    # Get attribute
    api_response = api_instance.get_attribute(attribute_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | [**str**](.md)| the id of the attribute | 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attribute**
> remove_attribute(attribute_id)

Remove attribute

Removes the attribute identified by given id.

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
api_instance = collibra_core.AttributesApi(collibra_core.ApiClient(configuration))
attribute_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the attribute

try:
    # Remove attribute
    api_instance.remove_attribute(attribute_id)
except ApiException as e:
    print("Exception when calling AttributesApi->remove_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | [**str**](.md)| the id of the attribute | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attributes**
> remove_attributes(body=body)

Remove attributes

Removes the attributes identified by given ids.

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
api_instance = collibra_core.AttributesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | the ids of the attributes to remove (optional)

try:
    # Remove attributes
    api_instance.remove_attributes(body=body)
except ApiException as e:
    print("Exception when calling AttributesApi->remove_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| the ids of the attributes to remove | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

