# collibra_core.ViewPermissionsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_view_permission**](ViewPermissionsApi.md#add_view_permission) | **POST** /viewPermissions | Adds a view permission. It can be applied only to &#x27;Community&#x27; and &#x27;Domain&#x27; resource types.
[**find_view_permissions**](ViewPermissionsApi.md#find_view_permissions) | **GET** /viewPermissions | Finds view permissions with given criteria.
[**get_view_permission**](ViewPermissionsApi.md#get_view_permission) | **GET** /viewPermissions/{viewPermissionId} | Retrieves a view permission.
[**remove_view_permission**](ViewPermissionsApi.md#remove_view_permission) | **DELETE** /viewPermissions/{viewPermissionId} | Removes a view permission.

# **add_view_permission**
> ViewPermissionImpl add_view_permission(body=body)

Adds a view permission. It can be applied only to 'Community' and 'Domain' resource types.

Adds a view permission. It can be applied only to 'Community' and 'Domain' resource types.

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
api_instance = collibra_core.ViewPermissionsApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddViewPermissionRequest() # AddViewPermissionRequest | Properties of the new view permission. Valid resource types are: 'Community', 'Domain'. (optional)

try:
    # Adds a view permission. It can be applied only to 'Community' and 'Domain' resource types.
    api_response = api_instance.add_view_permission(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewPermissionsApi->add_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddViewPermissionRequest**](AddViewPermissionRequest.md)| Properties of the new view permission. Valid resource types are: &#x27;Community&#x27;, &#x27;Domain&#x27;. | [optional] 

### Return type

[**ViewPermissionImpl**](ViewPermissionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_view_permissions**
> PagedResponseViewPermission find_view_permissions(offset=offset, limit=limit, count_limit=count_limit, user_id=user_id, user_group_id=user_group_id, resource_id=resource_id, resource_type=resource_type, include_inherited=include_inherited)

Finds view permissions with given criteria.

Finds view permissions with given criteria.

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
api_instance = collibra_core.ViewPermissionsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the user for whom the view permission applies. (optional)
user_group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the user group for whose members the view permission applies. (optional)
resource_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the community or domain to which the view permissions apply. (optional)
resource_type = 'resource_type_example' # str | Deprecated. Use <code>Community</code> or <code>Domain</code> to only retrieve view permissions assigned directly on a community or domain respectively. Do not use this filter in conjunction with the <code>resourceId</code> parameter. (optional)
include_inherited = true # bool | When you provide a <code>resourceId</code>, setting this parameter to <code>true</code> also returns the view permissions inherited from a parent community. (optional)

try:
    # Finds view permissions with given criteria.
    api_response = api_instance.find_view_permissions(offset=offset, limit=limit, count_limit=count_limit, user_id=user_id, user_group_id=user_group_id, resource_id=resource_id, resource_type=resource_type, include_inherited=include_inherited)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewPermissionsApi->find_view_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **user_id** | [**str**](.md)| The ID of the user for whom the view permission applies. | [optional] 
 **user_group_id** | [**str**](.md)| The ID of the user group for whose members the view permission applies. | [optional] 
 **resource_id** | [**str**](.md)| The ID of the community or domain to which the view permissions apply. | [optional] 
 **resource_type** | **str**| Deprecated. Use &lt;code&gt;Community&lt;/code&gt; or &lt;code&gt;Domain&lt;/code&gt; to only retrieve view permissions assigned directly on a community or domain respectively. Do not use this filter in conjunction with the &lt;code&gt;resourceId&lt;/code&gt; parameter. | [optional] 
 **include_inherited** | **bool**| When you provide a &lt;code&gt;resourceId&lt;/code&gt;, setting this parameter to &lt;code&gt;true&lt;/code&gt; also returns the view permissions inherited from a parent community. | [optional] 

### Return type

[**PagedResponseViewPermission**](PagedResponseViewPermission.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view_permission**
> ViewPermissionImpl get_view_permission(view_permission_id)

Retrieves a view permission.

Retrieves a view permission.

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
api_instance = collibra_core.ViewPermissionsApi(collibra_core.ApiClient(configuration))
view_permission_id = 'view_permission_id_example' # str | Identifier of the view permission to retrieve.

try:
    # Retrieves a view permission.
    api_response = api_instance.get_view_permission(view_permission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewPermissionsApi->get_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_permission_id** | **str**| Identifier of the view permission to retrieve. | 

### Return type

[**ViewPermissionImpl**](ViewPermissionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_view_permission**
> remove_view_permission(view_permission_id)

Removes a view permission.

Removes a view permission.

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
api_instance = collibra_core.ViewPermissionsApi(collibra_core.ApiClient(configuration))
view_permission_id = 'view_permission_id_example' # str | Identifier of the view permission to remove.

try:
    # Removes a view permission.
    api_instance.remove_view_permission(view_permission_id)
except ApiException as e:
    print("Exception when calling ViewPermissionsApi->remove_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_permission_id** | **str**| Identifier of the view permission to remove. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

