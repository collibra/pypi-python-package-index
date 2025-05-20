# collibra_core.ComplexRelationTypesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_complex_relation_type**](ComplexRelationTypesApi.md#add_complex_relation_type) | **POST** /complexRelationTypes | Adds a new complex relation type.
[**change_complex_relation_type**](ComplexRelationTypesApi.md#change_complex_relation_type) | **PATCH** /complexRelationTypes/{complexRelationTypeId} | Changes the complex relation type.
[**find_complex_relation_types**](ComplexRelationTypesApi.md#find_complex_relation_types) | **GET** /complexRelationTypes | Returns complex relation types matching the given search criteria.
[**get_complex_relation_type**](ComplexRelationTypesApi.md#get_complex_relation_type) | **GET** /complexRelationTypes/{complexRelationTypeId} | Returns complex relation type identified by given UUID.
[**remove_complex_relation_type**](ComplexRelationTypesApi.md#remove_complex_relation_type) | **DELETE** /complexRelationTypes/{complexRelationTypeId} | Removes complex relation type identified by given UUID.

# **add_complex_relation_type**
> ComplexRelationTypeImpl add_complex_relation_type(body=body)

Adds a new complex relation type.

Adds a new complex relation type.

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
api_instance = collibra_core.ComplexRelationTypesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddComplexRelationTypeRequest() # AddComplexRelationTypeRequest |  (optional)

try:
    # Adds a new complex relation type.
    api_response = api_instance.add_complex_relation_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->add_complex_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddComplexRelationTypeRequest**](AddComplexRelationTypeRequest.md)|  | [optional] 

### Return type

[**ComplexRelationTypeImpl**](ComplexRelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_complex_relation_type**
> ComplexRelationTypeImpl change_complex_relation_type(complex_relation_type_id, body=body)

Changes the complex relation type.

Changes the complex relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.ComplexRelationTypesApi(collibra_core.ApiClient(configuration))
complex_relation_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the complex relation type
body = collibra_core.ChangeComplexRelationTypeRequest() # ChangeComplexRelationTypeRequest |  (optional)

try:
    # Changes the complex relation type.
    api_response = api_instance.change_complex_relation_type(complex_relation_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->change_complex_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | [**str**](.md)| the unique identifier of the complex relation type | 
 **body** | [**ChangeComplexRelationTypeRequest**](ChangeComplexRelationTypeRequest.md)|  | [optional] 

### Return type

[**ComplexRelationTypeImpl**](ComplexRelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_complex_relation_types**
> ComplexRelationTypePagedResponse find_complex_relation_types(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode)

Returns complex relation types matching the given search criteria.

Returns complex relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned complex relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 complex relation types is returned.

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
api_instance = collibra_core.ComplexRelationTypesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The name of the Complex Relation Type to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) (default to ANYWHERE)

try:
    # Returns complex relation types matching the given search criteria.
    api_response = api_instance.find_complex_relation_types(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->find_complex_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The name of the Complex Relation Type to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] [default to ANYWHERE]

### Return type

[**ComplexRelationTypePagedResponse**](ComplexRelationTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complex_relation_type**
> ComplexRelationTypeImpl get_complex_relation_type(complex_relation_type_id)

Returns complex relation type identified by given UUID.

Returns complex relation type identified by given UUID.

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
api_instance = collibra_core.ComplexRelationTypesApi(collibra_core.ApiClient(configuration))
complex_relation_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the complex relation type

try:
    # Returns complex relation type identified by given UUID.
    api_response = api_instance.get_complex_relation_type(complex_relation_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->get_complex_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | [**str**](.md)| the unique identifier of the complex relation type | 

### Return type

[**ComplexRelationTypeImpl**](ComplexRelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_complex_relation_type**
> remove_complex_relation_type(complex_relation_type_id)

Removes complex relation type identified by given UUID.

Removes complex relation type identified by given UUID.

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
api_instance = collibra_core.ComplexRelationTypesApi(collibra_core.ApiClient(configuration))
complex_relation_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the complex relation type

try:
    # Removes complex relation type identified by given UUID.
    api_instance.remove_complex_relation_type(complex_relation_type_id)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->remove_complex_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | [**str**](.md)| the unique identifier of the complex relation type | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

