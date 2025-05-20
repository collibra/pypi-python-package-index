# collibra_core.DomainTypesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_type**](DomainTypesApi.md#add_domain_type) | **POST** /domainTypes | Adds a new domain type.
[**add_domain_types**](DomainTypesApi.md#add_domain_types) | **POST** /domainTypes/bulk | Adds multiple new domain types.
[**change_domain_type**](DomainTypesApi.md#change_domain_type) | **PATCH** /domainTypes/{domainTypeId} | Changes the domain type.
[**change_domain_types**](DomainTypesApi.md#change_domain_types) | **PATCH** /domainTypes/bulk | Changes the domain types.
[**find_domain_types**](DomainTypesApi.md#find_domain_types) | **GET** /domainTypes | Returns domain types matching the given search criteria.
[**find_sub_domain_types**](DomainTypesApi.md#find_sub_domain_types) | **GET** /domainTypes/{domainTypeId}/subTypes | Returns sub domain types matching the given search criteria.
[**get_domain_type**](DomainTypesApi.md#get_domain_type) | **GET** /domainTypes/{domainTypeId} | Returns domain type identified by given UUID.
[**remove_domain_type**](DomainTypesApi.md#remove_domain_type) | **DELETE** /domainTypes/{domainTypeId} | Removes domain type identified by given UUID.
[**remove_domain_types**](DomainTypesApi.md#remove_domain_types) | **DELETE** /domainTypes/bulk | Removes multiple domain types.

# **add_domain_type**
> DomainTypeImpl add_domain_type(body=body)

Adds a new domain type.

Adds a new domain type.

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddDomainTypeRequest() # AddDomainTypeRequest |  (optional)

try:
    # Adds a new domain type.
    api_response = api_instance.add_domain_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->add_domain_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDomainTypeRequest**](AddDomainTypeRequest.md)|  | [optional] 

### Return type

[**DomainTypeImpl**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_domain_types**
> list[DomainTypeImpl] add_domain_types(body=body)

Adds multiple new domain types.

Adds multiple new domain types.

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddDomainTypeRequest()] # list[AddDomainTypeRequest] |  (optional)

try:
    # Adds multiple new domain types.
    api_response = api_instance.add_domain_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->add_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddDomainTypeRequest]**](AddDomainTypeRequest.md)|  | [optional] 

### Return type

[**list[DomainTypeImpl]**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domain_type**
> DomainTypeImpl change_domain_type(domain_type_id, body=body)

Changes the domain type.

Changes the domain type with the information present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored. 

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
domain_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the domain type
body = collibra_core.ChangeDomainTypeRequest() # ChangeDomainTypeRequest |  (optional)

try:
    # Changes the domain type.
    api_response = api_instance.change_domain_type(domain_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->change_domain_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | [**str**](.md)| the unique identifier of the domain type | 
 **body** | [**ChangeDomainTypeRequest**](ChangeDomainTypeRequest.md)|  | [optional] 

### Return type

[**DomainTypeImpl**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domain_types**
> list[DomainTypeImpl] change_domain_types(body=body)

Changes the domain types.

Changes the domain types with the information present in the request.

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeDomainTypeRequest()] # list[ChangeDomainTypeRequest] |  (optional)

try:
    # Changes the domain types.
    api_response = api_instance.change_domain_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->change_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeDomainTypeRequest]**](ChangeDomainTypeRequest.md)|  | [optional] 

### Return type

[**list[DomainTypeImpl]**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_domain_types**
> DomainTypePagedResponse find_domain_types(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, top_level=top_level)

Returns domain types matching the given search criteria.

Returns domain types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned domain types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 domain types is returned.

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The name of the Domain Type to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. The search is case-insensitive. (optional) (default to ANYWHERE)
parent_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the parent to find the Domain Types in. (optional)
exclude_meta = true # bool | Whether the meta Domain Types should be excluded from search or not. (optional) (default to true)
top_level = false # bool | Whether only top level Domain Types should be searched or not. (optional) (default to false)

try:
    # Returns domain types matching the given search criteria.
    api_response = api_instance.find_domain_types(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, top_level=top_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->find_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The name of the Domain Type to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. The search is case-insensitive. | [optional] [default to ANYWHERE]
 **parent_id** | [**str**](.md)| The ID of the parent to find the Domain Types in. | [optional] 
 **exclude_meta** | **bool**| Whether the meta Domain Types should be excluded from search or not. | [optional] [default to true]
 **top_level** | **bool**| Whether only top level Domain Types should be searched or not. | [optional] [default to false]

### Return type

[**DomainTypePagedResponse**](DomainTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_sub_domain_types**
> DomainTypePagedResponse find_sub_domain_types(domain_type_id, domain_type_id, include_parent=include_parent)

Returns sub domain types matching the given search criteria.

Returns sub domain types matching the given search criteria.

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
domain_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the domain type
domain_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Domain Type to search the subtypes of. Because it duplicates the corresponding domainTypeId path parameter and prevents some client code generators from working as expected, this will be removed in the next quarterly release.
include_parent = true # bool | Whether parent Domain Type should be included in the search result. (optional)

try:
    # Returns sub domain types matching the given search criteria.
    api_response = api_instance.find_sub_domain_types(domain_type_id, domain_type_id, include_parent=include_parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->find_sub_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | [**str**](.md)| the unique identifier of the domain type | 
 **domain_type_id** | [**str**](.md)| The ID of the Domain Type to search the subtypes of. Because it duplicates the corresponding domainTypeId path parameter and prevents some client code generators from working as expected, this will be removed in the next quarterly release. | 
 **include_parent** | **bool**| Whether parent Domain Type should be included in the search result. | [optional] 

### Return type

[**DomainTypePagedResponse**](DomainTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_type**
> DomainTypeImpl get_domain_type(domain_type_id)

Returns domain type identified by given UUID.

Returns domain type identified by given UUID.

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
domain_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the domain type

try:
    # Returns domain type identified by given UUID.
    api_response = api_instance.get_domain_type(domain_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->get_domain_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | [**str**](.md)| the unique identifier of the domain type | 

### Return type

[**DomainTypeImpl**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domain_type**
> remove_domain_type(domain_type_id)

Removes domain type identified by given UUID.

Removes domain type identified by given UUID.

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
domain_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the domain type

try:
    # Removes domain type identified by given UUID.
    api_instance.remove_domain_type(domain_type_id)
except ApiException as e:
    print("Exception when calling DomainTypesApi->remove_domain_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | [**str**](.md)| the unique identifier of the domain type | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domain_types**
> remove_domain_types(body=body)

Removes multiple domain types.

Removes multiple domain types identified by the UUIDs passed as parameter.

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
api_instance = collibra_core.DomainTypesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] |  (optional)

try:
    # Removes multiple domain types.
    api_instance.remove_domain_types(body=body)
except ApiException as e:
    print("Exception when calling DomainTypesApi->remove_domain_types: %s\n" % e)
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

