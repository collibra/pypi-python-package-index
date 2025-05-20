# collibra_core.RelationsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation**](RelationsApi.md#add_relation) | **POST** /relations | Adds a new relation.
[**add_relations**](RelationsApi.md#add_relations) | **POST** /relations/bulk | Adds multiple relations in one go.
[**change_relation**](RelationsApi.md#change_relation) | **PATCH** /relations/{relationId} | Changes the relation with the information that is present in the request.
[**change_relations**](RelationsApi.md#change_relations) | **PATCH** /relations/bulk | Changes multiple relations.
[**find_relations**](RelationsApi.md#find_relations) | **GET** /relations | Returns relations matching the given search criteria.
[**get_relation**](RelationsApi.md#get_relation) | **GET** /relations/{relationId} | Returns a relation identified by given id.
[**remove_relation**](RelationsApi.md#remove_relation) | **DELETE** /relations/{relationId} | Removes a relation identified by given id.
[**remove_relations**](RelationsApi.md#remove_relations) | **DELETE** /relations/bulk | Removes multiple relations.

# **add_relation**
> RelationImpl add_relation(body=body)

Adds a new relation.

Adds a new relation.

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
api_instance = collibra_core.RelationsApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddRelationRequest() # AddRelationRequest | The properties of the relation to be added (optional)

try:
    # Adds a new relation.
    api_response = api_instance.add_relation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->add_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddRelationRequest**](AddRelationRequest.md)| The properties of the relation to be added | [optional] 

### Return type

[**RelationImpl**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_relations**
> list[RelationImpl] add_relations(body=body)

Adds multiple relations in one go.

Adds multiple relations in one gos.

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
api_instance = collibra_core.RelationsApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddRelationRequest()] # list[AddRelationRequest] | List of the properties of the relations to be added. (optional)

try:
    # Adds multiple relations in one go.
    api_response = api_instance.add_relations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->add_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddRelationRequest]**](AddRelationRequest.md)| List of the properties of the relations to be added. | [optional] 

### Return type

[**list[RelationImpl]**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_relation**
> RelationImpl change_relation(relation_id, body=body)

Changes the relation with the information that is present in the request.

Changes the relation with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.RelationsApi(collibra_core.ApiClient(configuration))
relation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the relation to be changed.
body = collibra_core.ChangeRelationRequest() # ChangeRelationRequest | The properties of the relation to be changed. (optional)

try:
    # Changes the relation with the information that is present in the request.
    api_response = api_instance.change_relation(relation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->change_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | [**str**](.md)| The ID of the relation to be changed. | 
 **body** | [**ChangeRelationRequest**](ChangeRelationRequest.md)| The properties of the relation to be changed. | [optional] 

### Return type

[**RelationImpl**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_relations**
> list[RelationImpl] change_relations(body=body)

Changes multiple relations.

Changes multiple relations.

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
api_instance = collibra_core.RelationsApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeRelationRequest()] # list[ChangeRelationRequest] | The list of properties of the relations to be changed. (optional)

try:
    # Changes multiple relations.
    api_response = api_instance.change_relations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->change_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeRelationRequest]**](ChangeRelationRequest.md)| The list of properties of the relations to be changed. | [optional] 

### Return type

[**list[RelationImpl]**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_relations**
> RelationPagedResponse find_relations(offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, relation_type_id=relation_type_id, source_id=source_id, target_id=target_id, source_target_logical_operator=source_target_logical_operator)

Returns relations matching the given search criteria.

Returns relations matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relations satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relations is returned.

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
api_instance = collibra_core.RelationsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. (optional) (default to -1)
cursor = 'cursor_example' # str | Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (<code>nextCursor</code> property). (optional)
relation_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the type of relations to search for. (optional)
source_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the source of relations to search for. (optional)
target_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target of relations to search for. (optional)
source_target_logical_operator = 'AND' # str | The logical operator determining how to combine the source and target criteria: AND or OR. (optional) (default to AND)

try:
    # Returns relations matching the given search criteria.
    api_response = api_instance.find_relations(offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, relation_type_id=relation_type_id, source_id=source_id, target_id=target_id, source_target_logical_operator=source_target_logical_operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->find_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. | [optional] [default to -1]
 **cursor** | **str**| Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (&lt;code&gt;nextCursor&lt;/code&gt; property). | [optional] 
 **relation_type_id** | [**str**](.md)| The ID of the type of relations to search for. | [optional] 
 **source_id** | [**str**](.md)| The ID of the source of relations to search for. | [optional] 
 **target_id** | [**str**](.md)| The ID of the target of relations to search for. | [optional] 
 **source_target_logical_operator** | **str**| The logical operator determining how to combine the source and target criteria: AND or OR. | [optional] [default to AND]

### Return type

[**RelationPagedResponse**](RelationPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation**
> RelationImpl get_relation(relation_id)

Returns a relation identified by given id.

Returns a relation identified by given id.

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
api_instance = collibra_core.RelationsApi(collibra_core.ApiClient(configuration))
relation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the ID of the relation

try:
    # Returns a relation identified by given id.
    api_response = api_instance.get_relation(relation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->get_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | [**str**](.md)| the ID of the relation | 

### Return type

[**RelationImpl**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_relation**
> remove_relation(relation_id)

Removes a relation identified by given id.

Removes a relation identified by given id.

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
api_instance = collibra_core.RelationsApi(collibra_core.ApiClient(configuration))
relation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the ID of the relation to remove

try:
    # Removes a relation identified by given id.
    api_instance.remove_relation(relation_id)
except ApiException as e:
    print("Exception when calling RelationsApi->remove_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | [**str**](.md)| the ID of the relation to remove | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_relations**
> remove_relations(body=body)

Removes multiple relations.

Removes multiple relations.

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
api_instance = collibra_core.RelationsApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | the IDs of the relations to be removed (optional)

try:
    # Removes multiple relations.
    api_instance.remove_relations(body=body)
except ApiException as e:
    print("Exception when calling RelationsApi->remove_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| the IDs of the relations to be removed | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

