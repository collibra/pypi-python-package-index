# collibra_core.AttributeTypesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attribute_type**](AttributeTypesApi.md#add_attribute_type) | **POST** /attributeTypes | Adds a new Attribute Type.
[**add_attribute_types**](AttributeTypesApi.md#add_attribute_types) | **POST** /attributeTypes/bulk | Adds multiple Attribute Types.
[**change_attribute_type**](AttributeTypesApi.md#change_attribute_type) | **PATCH** /attributeTypes/{attributeTypeId} | Changes the attribute types.
[**change_attribute_types**](AttributeTypesApi.md#change_attribute_types) | **PATCH** /attributeTypes/bulk | Changes multiple attribute types.
[**find_attribute_types**](AttributeTypesApi.md#find_attribute_types) | **GET** /attributeTypes | Returns attribute types matching the given search criteria.
[**get_attribute_type**](AttributeTypesApi.md#get_attribute_type) | **GET** /attributeTypes/{attributeTypeId} | Returns the attribute type identified by given UUID.
[**get_attribute_type_by_name**](AttributeTypesApi.md#get_attribute_type_by_name) | **GET** /attributeTypes/name/{attributeTypeName} | Returns the attribute type identified by given name.
[**remove_attribute_type**](AttributeTypesApi.md#remove_attribute_type) | **DELETE** /attributeTypes/{attributeTypeId} | Removes attribute type identified by given UUID.
[**remove_attribute_types**](AttributeTypesApi.md#remove_attribute_types) | **DELETE** /attributeTypes/bulk | Removes multiple attribute types.

# **add_attribute_type**
> AttributeType add_attribute_type(body=body)

Adds a new Attribute Type.

Adds a new Attribute Type.

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddAttributeTypeRequest() # AddAttributeTypeRequest |  (optional)

try:
    # Adds a new Attribute Type.
    api_response = api_instance.add_attribute_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->add_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddAttributeTypeRequest**](AddAttributeTypeRequest.md)|  | [optional] 

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_attribute_types**
> list[AttributeType] add_attribute_types(body=body)

Adds multiple Attribute Types.

Adds multiple Attribute Types.

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddAttributeTypeRequest()] # list[AddAttributeTypeRequest] |  (optional)

try:
    # Adds multiple Attribute Types.
    api_response = api_instance.add_attribute_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->add_attribute_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddAttributeTypeRequest]**](AddAttributeTypeRequest.md)|  | [optional] 

### Return type

[**list[AttributeType]**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_attribute_type**
> AttributeType change_attribute_type(attribute_type_id, body=body)

Changes the attribute types.

Changes the attribute types with the information present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored. 

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
attribute_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the attribute type
body = collibra_core.ChangeAttributeTypeRequest() # ChangeAttributeTypeRequest |  (optional)

try:
    # Changes the attribute types.
    api_response = api_instance.change_attribute_type(attribute_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->change_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | [**str**](.md)| the unique identifier of the attribute type | 
 **body** | [**ChangeAttributeTypeRequest**](ChangeAttributeTypeRequest.md)|  | [optional] 

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_attribute_types**
> list[AttributeType] change_attribute_types(body=body)

Changes multiple attribute types.

Changes multiple attribute types with the information present in the request.

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeAttributeTypeRequest()] # list[ChangeAttributeTypeRequest] |  (optional)

try:
    # Changes multiple attribute types.
    api_response = api_instance.change_attribute_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->change_attribute_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeAttributeTypeRequest]**](ChangeAttributeTypeRequest.md)|  | [optional] 

### Return type

[**list[AttributeType]**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_attribute_types**
> AttributeTypePagedResponse find_attribute_types(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, kind=kind, language=language, statistics_enabled=statistics_enabled, is_integer=is_integer, sort_field=sort_field, sort_order=sort_order)

Returns attribute types matching the given search criteria.

Returns attribute types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attribute types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attribute types is returned.

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The name of the Attribute Type to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) (default to ANYWHERE)
kind = 'kind_example' # str | The kind of the Attribute Type to search for. (optional)
language = 'language_example' # str | The language of the Attribute Type to search for. This property is only applicable to Attribute Types of kind \"Script\". (optional)
statistics_enabled = true # bool | Whether the Attribute Types should be searched with statistics enabled or not. This property is only applicable to Attribute Types of kind \"Numeric\" or \"Boolean\". (optional)
is_integer = true # bool | Whether only integer-type Attribute Types should be searched or not. This property is only applicable to Attribute Types of kind \"Numeric\". (optional)
sort_field = 'NAME' # str | The field that should be used as reference for sorting. (optional) (default to NAME)
sort_order = 'ASC' # str | The order of sorting. (optional) (default to ASC)

try:
    # Returns attribute types matching the given search criteria.
    api_response = api_instance.find_attribute_types(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, kind=kind, language=language, statistics_enabled=statistics_enabled, is_integer=is_integer, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->find_attribute_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The name of the Attribute Type to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] [default to ANYWHERE]
 **kind** | **str**| The kind of the Attribute Type to search for. | [optional] 
 **language** | **str**| The language of the Attribute Type to search for. This property is only applicable to Attribute Types of kind \&quot;Script\&quot;. | [optional] 
 **statistics_enabled** | **bool**| Whether the Attribute Types should be searched with statistics enabled or not. This property is only applicable to Attribute Types of kind \&quot;Numeric\&quot; or \&quot;Boolean\&quot;. | [optional] 
 **is_integer** | **bool**| Whether only integer-type Attribute Types should be searched or not. This property is only applicable to Attribute Types of kind \&quot;Numeric\&quot;. | [optional] 
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] [default to NAME]
 **sort_order** | **str**| The order of sorting. | [optional] [default to ASC]

### Return type

[**AttributeTypePagedResponse**](AttributeTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type**
> AttributeType get_attribute_type(attribute_type_id)

Returns the attribute type identified by given UUID.

Returns the attribute type identified by given UUID.

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
attribute_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the attribute type

try:
    # Returns the attribute type identified by given UUID.
    api_response = api_instance.get_attribute_type(attribute_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->get_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | [**str**](.md)| the unique identifier of the attribute type | 

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_type_by_name**
> AttributeType get_attribute_type_by_name(attribute_type_name)

Returns the attribute type identified by given name.

Returns the attribute type identified by given name.

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
attribute_type_name = 'attribute_type_name_example' # str | the unique identifier of the attribute type

try:
    # Returns the attribute type identified by given name.
    api_response = api_instance.get_attribute_type_by_name(attribute_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->get_attribute_type_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_name** | **str**| the unique identifier of the attribute type | 

### Return type

[**AttributeType**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attribute_type**
> remove_attribute_type(attribute_type_id)

Removes attribute type identified by given UUID.

Removes attribute type identified by given UUID.

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
attribute_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the attribute type

try:
    # Removes attribute type identified by given UUID.
    api_instance.remove_attribute_type(attribute_type_id)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->remove_attribute_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | [**str**](.md)| the unique identifier of the attribute type | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attribute_types**
> remove_attribute_types(body=body)

Removes multiple attribute types.

Removes multiple attribute types identified by the UUIDs passed as parameter.

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
api_instance = collibra_core.AttributeTypesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] |  (optional)

try:
    # Removes multiple attribute types.
    api_instance.remove_attribute_types(body=body)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->remove_attribute_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

