# collibra_core.ScopesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scope**](ScopesApi.md#add_scope) | **POST** /scopes | Add scope
[**change_scope**](ScopesApi.md#change_scope) | **PATCH** /scopes/{scopeId} | Change scope
[**get_all_scopes**](ScopesApi.md#get_all_scopes) | **GET** /scopes | Find scopes
[**get_scope**](ScopesApi.md#get_scope) | **GET** /scopes/{scopeId} | Get scope
[**remove_scope**](ScopesApi.md#remove_scope) | **DELETE** /scopes/{scopeId} | Remove scope

# **add_scope**
> ScopeImpl add_scope(body=body)

Add scope

Adds a new scope.

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
api_instance = collibra_core.ScopesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddScopeRequest() # AddScopeRequest | the properties of the scope to be added (optional)

try:
    # Add scope
    api_response = api_instance.add_scope(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->add_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddScopeRequest**](AddScopeRequest.md)| the properties of the scope to be added | [optional] 

### Return type

[**ScopeImpl**](ScopeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_scope**
> ScopeImpl change_scope(scope_id, body=body)

Change scope

Changes the scope with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.ScopesApi(collibra_core.ApiClient(configuration))
scope_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the scope to be changed
body = collibra_core.ChangeScopeRequest() # ChangeScopeRequest | the properties of the scope to be changed (optional)

try:
    # Change scope
    api_response = api_instance.change_scope(scope_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->change_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | [**str**](.md)| the id of the scope to be changed | 
 **body** | [**ChangeScopeRequest**](ChangeScopeRequest.md)| the properties of the scope to be changed | [optional] 

### Return type

[**ScopeImpl**](ScopeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_scopes**
> ScopePagedResponse get_all_scopes()

Find scopes

Returns all scopes.

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
api_instance = collibra_core.ScopesApi(collibra_core.ApiClient(configuration))

try:
    # Find scopes
    api_response = api_instance.get_all_scopes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->get_all_scopes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScopePagedResponse**](ScopePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scope**
> ScopeImpl get_scope(scope_id)

Get scope

Returns scope identified by given id.

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
api_instance = collibra_core.ScopesApi(collibra_core.ApiClient(configuration))
scope_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the scope.

try:
    # Get scope
    api_response = api_instance.get_scope(scope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->get_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | [**str**](.md)| The unique identifier of the scope. | 

### Return type

[**ScopeImpl**](ScopeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_scope**
> remove_scope(scope_id)

Remove scope

Removes scope identified by given id.

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
api_instance = collibra_core.ScopesApi(collibra_core.ApiClient(configuration))
scope_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the scope

try:
    # Remove scope
    api_instance.remove_scope(scope_id)
except ApiException as e:
    print("Exception when calling ScopesApi->remove_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | [**str**](.md)| the id of the scope | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

