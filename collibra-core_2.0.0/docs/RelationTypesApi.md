# collibra_core.RelationTypesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_type**](RelationTypesApi.md#add_relation_type) | **POST** /relationTypes | Adds a new relation type.
[**add_relation_types**](RelationTypesApi.md#add_relation_types) | **POST** /relationTypes/bulk | Adds multiple new relation type.
[**change_relation_type**](RelationTypesApi.md#change_relation_type) | **PATCH** /relationTypes/{relationTypeId} | Changes the relation type.
[**change_relation_types**](RelationTypesApi.md#change_relation_types) | **PATCH** /relationTypes/bulk | Changes the relation types.
[**find_relation_types**](RelationTypesApi.md#find_relation_types) | **GET** /relationTypes | Finds all the relation types matching the given criteria.
[**get_relation_type**](RelationTypesApi.md#get_relation_type) | **GET** /relationTypes/{relationTypeId} | Returns relation type identified by given UUID.
[**remove_relation_type**](RelationTypesApi.md#remove_relation_type) | **DELETE** /relationTypes/{relationTypeId} | Removes relation type identified by given UUID.
[**remove_relation_types**](RelationTypesApi.md#remove_relation_types) | **DELETE** /relationTypes/bulk | Removes multiple relation types.

# **add_relation_type**
> RelationTypeImpl add_relation_type(body=body)

Adds a new relation type.

Adds a new relation type.

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
api_instance = collibra_core.RelationTypesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddRelationTypeRequest() # AddRelationTypeRequest |  (optional)

try:
    # Adds a new relation type.
    api_response = api_instance.add_relation_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->add_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddRelationTypeRequest**](AddRelationTypeRequest.md)|  | [optional] 

### Return type

[**RelationTypeImpl**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_relation_types**
> list[RelationTypeImpl] add_relation_types(body=body)

Adds multiple new relation type.

Adds multiple new relation type.

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
api_instance = collibra_core.RelationTypesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddRelationTypeRequest()] # list[AddRelationTypeRequest] |  (optional)

try:
    # Adds multiple new relation type.
    api_response = api_instance.add_relation_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->add_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddRelationTypeRequest]**](AddRelationTypeRequest.md)|  | [optional] 

### Return type

[**list[RelationTypeImpl]**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_relation_type**
> RelationTypeImpl change_relation_type(relation_type_id, body=body)

Changes the relation type.

Changes the relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.RelationTypesApi(collibra_core.ApiClient(configuration))
relation_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the relationType
body = collibra_core.ChangeRelationTypeRequest() # ChangeRelationTypeRequest |  (optional)

try:
    # Changes the relation type.
    api_response = api_instance.change_relation_type(relation_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->change_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | [**str**](.md)| The unique identifier of the relationType | 
 **body** | [**ChangeRelationTypeRequest**](ChangeRelationTypeRequest.md)|  | [optional] 

### Return type

[**RelationTypeImpl**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_relation_types**
> list[RelationTypeImpl] change_relation_types(body=body)

Changes the relation types.

Changes the relation types with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.RelationTypesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeRelationTypeRequest()] # list[ChangeRelationTypeRequest] |  (optional)

try:
    # Changes the relation types.
    api_response = api_instance.change_relation_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->change_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeRelationTypeRequest]**](ChangeRelationTypeRequest.md)|  | [optional] 

### Return type

[**list[RelationTypeImpl]**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_relation_types**
> RelationTypePagedResponse find_relation_types(offset=offset, limit=limit, count_limit=count_limit, source_type_id=source_type_id, source_type_name=source_type_name, role=role, target_type_id=target_type_id, target_type_name=target_type_name, co_role=co_role, sort_field=sort_field, sort_order=sort_order, role_co_role_logical_operator=role_co_role_logical_operator)

Finds all the relation types matching the given criteria.

Returns relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relation types is returned. 

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
api_instance = collibra_core.RelationTypesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
source_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the source type of the Relation Type to search for. (optional)
source_type_name = 'source_type_name_example' # str | The name of the source type of the Relation Type to search for. (optional)
role = 'role_example' # str | The name of the role that the source plays to search for. (optional)
target_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target type of the Relation Type to search for. (optional)
target_type_name = 'target_type_name_example' # str | The name of the target type of the Relation Type to search for. (optional)
co_role = 'co_role_example' # str | The name of the role that the target plays to search for. (optional)
sort_field = 'ROLE' # str | The field that should be used as reference for sorting. (optional) (default to ROLE)
sort_order = 'ASC' # str | The order of sorting. (optional) (default to ASC)
role_co_role_logical_operator = 'AND' # str | The logical operator determining how to combine the role and coRole criteria: AND or OR. (optional) (default to AND)

try:
    # Finds all the relation types matching the given criteria.
    api_response = api_instance.find_relation_types(offset=offset, limit=limit, count_limit=count_limit, source_type_id=source_type_id, source_type_name=source_type_name, role=role, target_type_id=target_type_id, target_type_name=target_type_name, co_role=co_role, sort_field=sort_field, sort_order=sort_order, role_co_role_logical_operator=role_co_role_logical_operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->find_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **source_type_id** | [**str**](.md)| The ID of the source type of the Relation Type to search for. | [optional] 
 **source_type_name** | **str**| The name of the source type of the Relation Type to search for. | [optional] 
 **role** | **str**| The name of the role that the source plays to search for. | [optional] 
 **target_type_id** | [**str**](.md)| The ID of the target type of the Relation Type to search for. | [optional] 
 **target_type_name** | **str**| The name of the target type of the Relation Type to search for. | [optional] 
 **co_role** | **str**| The name of the role that the target plays to search for. | [optional] 
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] [default to ROLE]
 **sort_order** | **str**| The order of sorting. | [optional] [default to ASC]
 **role_co_role_logical_operator** | **str**| The logical operator determining how to combine the role and coRole criteria: AND or OR. | [optional] [default to AND]

### Return type

[**RelationTypePagedResponse**](RelationTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation_type**
> RelationTypeImpl get_relation_type(relation_type_id)

Returns relation type identified by given UUID.

Returns relation type identified by given UUID.

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
api_instance = collibra_core.RelationTypesApi(collibra_core.ApiClient(configuration))
relation_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the relationType

try:
    # Returns relation type identified by given UUID.
    api_response = api_instance.get_relation_type(relation_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->get_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | [**str**](.md)| The unique identifier of the relationType | 

### Return type

[**RelationTypeImpl**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_relation_type**
> remove_relation_type(relation_type_id)

Removes relation type identified by given UUID.

Removes relation type identified by given UUID.

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
api_instance = collibra_core.RelationTypesApi(collibra_core.ApiClient(configuration))
relation_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the relationType

try:
    # Removes relation type identified by given UUID.
    api_instance.remove_relation_type(relation_type_id)
except ApiException as e:
    print("Exception when calling RelationTypesApi->remove_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | [**str**](.md)| The unique identifier of the relationType | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_relation_types**
> remove_relation_types(body=body)

Removes multiple relation types.

Removes multiple relation types identified by the UUIDs passed as parameter.

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
api_instance = collibra_core.RelationTypesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | The unique identifiers of the relationTypes (optional)

try:
    # Removes multiple relation types.
    api_instance.remove_relation_types(body=body)
except ApiException as e:
    print("Exception when calling RelationTypesApi->remove_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The unique identifiers of the relationTypes | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

