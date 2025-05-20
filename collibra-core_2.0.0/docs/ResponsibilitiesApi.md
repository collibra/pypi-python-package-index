# collibra_core.ResponsibilitiesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_responsibilities**](ResponsibilitiesApi.md#add_responsibilities) | **POST** /responsibilities/bulk | Adds multiple responsibilities in one go.
[**add_responsibility**](ResponsibilitiesApi.md#add_responsibility) | **POST** /responsibilities | Adds a new responsibility.
[**find_responsibilities**](ResponsibilitiesApi.md#find_responsibilities) | **GET** /responsibilities | Finds responsibilities.
[**get_responsibility**](ResponsibilitiesApi.md#get_responsibility) | **GET** /responsibilities/{responsibilityId} | Returns the responsibility identified by the given id.
[**remove_responsibilities**](ResponsibilitiesApi.md#remove_responsibilities) | **DELETE** /responsibilities/bulk | Removes multiple responsibilities in one go.
[**remove_responsibility**](ResponsibilitiesApi.md#remove_responsibility) | **DELETE** /responsibilities/{responsibilityId} | Removes the responsibility identified by the given id.

# **add_responsibilities**
> list[ResponsibilityImpl] add_responsibilities(body=body)

Adds multiple responsibilities in one go.

Adds multiple responsibilities in one go. Assigns the given users to the resources with the given roles.

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
api_instance = collibra_core.ResponsibilitiesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddResponsibilityRequest()] # list[AddResponsibilityRequest] |  (optional)

try:
    # Adds multiple responsibilities in one go.
    api_response = api_instance.add_responsibilities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->add_responsibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddResponsibilityRequest]**](AddResponsibilityRequest.md)|  | [optional] 

### Return type

[**list[ResponsibilityImpl]**](ResponsibilityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_responsibility**
> ResponsibilityImpl add_responsibility(body=body)

Adds a new responsibility.

Adds new responsibility. Assigns given user to resource with given role.

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
api_instance = collibra_core.ResponsibilitiesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddResponsibilityRequest() # AddResponsibilityRequest |  (optional)

try:
    # Adds a new responsibility.
    api_response = api_instance.add_responsibility(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->add_responsibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddResponsibilityRequest**](AddResponsibilityRequest.md)|  | [optional] 

### Return type

[**ResponsibilityImpl**](ResponsibilityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_responsibilities**
> PagedResponseResponsibility find_responsibilities(offset=offset, limit=limit, count_limit=count_limit, resource_ids=resource_ids, owner_ids=owner_ids, role_ids=role_ids, include_inherited=include_inherited, global_only=global_only, sort_field=sort_field, sort_order=sort_order, type=type)

Finds responsibilities.

Returns responsibilities matching the given search criteria.  Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.  All other parameters are ignored.  The returned responsibilities satisfy all constraints that are specified in this search criteria.  By default a result containing 1000 responsibilities is returned.

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
api_instance = collibra_core.ResponsibilitiesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
resource_ids = ['resource_ids_example'] # list[str] | The list of IDs of the resources for which the responsibilities should be found. (optional)
owner_ids = ['owner_ids_example'] # list[str] | The list of IDs of the owners for which the responsibilities should be found. (optional)
role_ids = ['role_ids_example'] # list[str] | The list of IDs of the roles for which the responsibilities should be found. (optional)
include_inherited = true # bool | Whether inherited responsibilities should be included in the search results. (optional) (default to true)
global_only = true # bool | Whether only global responsibilities should be searched. (optional)
sort_field = 'LAST_MODIFIED' # str | The field that should be used as reference for sorting. (optional) (default to LAST_MODIFIED)
sort_order = 'DESC' # str | The order of sorting. (optional) (default to DESC)
type = 'type_example' # str | Indicates which type of responsibilities should be searched for. Usage is mutually exclusive with the deprecated globalOnly flag. (optional)

try:
    # Finds responsibilities.
    api_response = api_instance.find_responsibilities(offset=offset, limit=limit, count_limit=count_limit, resource_ids=resource_ids, owner_ids=owner_ids, role_ids=role_ids, include_inherited=include_inherited, global_only=global_only, sort_field=sort_field, sort_order=sort_order, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->find_responsibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **resource_ids** | [**list[str]**](str.md)| The list of IDs of the resources for which the responsibilities should be found. | [optional] 
 **owner_ids** | [**list[str]**](str.md)| The list of IDs of the owners for which the responsibilities should be found. | [optional] 
 **role_ids** | [**list[str]**](str.md)| The list of IDs of the roles for which the responsibilities should be found. | [optional] 
 **include_inherited** | **bool**| Whether inherited responsibilities should be included in the search results. | [optional] [default to true]
 **global_only** | **bool**| Whether only global responsibilities should be searched. | [optional] 
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] [default to LAST_MODIFIED]
 **sort_order** | **str**| The order of sorting. | [optional] [default to DESC]
 **type** | **str**| Indicates which type of responsibilities should be searched for. Usage is mutually exclusive with the deprecated globalOnly flag. | [optional] 

### Return type

[**PagedResponseResponsibility**](PagedResponseResponsibility.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_responsibility**
> ResponsibilityImpl get_responsibility(responsibility_id)

Returns the responsibility identified by the given id.

Returns the responsibility identified by the given id.

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
api_instance = collibra_core.ResponsibilitiesApi(collibra_core.ApiClient(configuration))
responsibility_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the responsibility.

try:
    # Returns the responsibility identified by the given id.
    api_response = api_instance.get_responsibility(responsibility_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->get_responsibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responsibility_id** | [**str**](.md)| The unique identifier of the responsibility. | 

### Return type

[**ResponsibilityImpl**](ResponsibilityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_responsibilities**
> remove_responsibilities(body=body)

Removes multiple responsibilities in one go.

Removes multiple responsibilities in one go identified by given ids.

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
api_instance = collibra_core.ResponsibilitiesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | The unique identifiers of the responsibilities. (optional)

try:
    # Removes multiple responsibilities in one go.
    api_instance.remove_responsibilities(body=body)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->remove_responsibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The unique identifiers of the responsibilities. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_responsibility**
> remove_responsibility(responsibility_id)

Removes the responsibility identified by the given id.

Removes the responsibility identified by the given id.

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
api_instance = collibra_core.ResponsibilitiesApi(collibra_core.ApiClient(configuration))
responsibility_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the responsibility.

try:
    # Removes the responsibility identified by the given id.
    api_instance.remove_responsibility(responsibility_id)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->remove_responsibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responsibility_id** | [**str**](.md)| The unique identifier of the responsibility. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

