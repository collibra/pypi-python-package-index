# collibra_protect.GroupsApi

All URIs are relative to */rest/protect/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](GroupsApi.md#add_group) | **POST** /groups | Add a new group
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{id} | Delete a group
[**get_group**](GroupsApi.md#get_group) | **GET** /groups/{id} | Retrieve a group
[**list_groups**](GroupsApi.md#list_groups) | **GET** /groups | List groups
[**patch_group**](GroupsApi.md#patch_group) | **PATCH** /groups/{id} | Update a group

# **add_group**
> Group add_group(body)

Add a new group

Adds a new group.

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
api_instance = collibra_protect.GroupsApi(collibra_protect.ApiClient(configuration))
body = collibra_protect.AddGroupRequest() # AddGroupRequest | The group to add.

try:
    # Add a new group
    api_response = api_instance.add_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->add_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddGroupRequest**](AddGroupRequest.md)| The group to add. | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(id)

Delete a group

Deletes the group with the specified ID.

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
api_instance = collibra_protect.GroupsApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the group.

try:
    # Delete a group
    api_instance.delete_group(id)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the group. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(id)

Retrieve a group

Returns information about the group with the specified ID.

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
api_instance = collibra_protect.GroupsApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the group.

try:
    # Retrieve a group
    api_response = api_instance.get_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the group. | 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> PagedGroups list_groups(limit=limit, after=after)

List groups

Lists all available groups.

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
api_instance = collibra_protect.GroupsApi(collibra_protect.ApiClient(configuration))
limit = 25 # int | This is the maximum number of results that may be returned. Fewer may be returned than the value of <code>limit</code>.  Do not depend on the number of results being fewer than the <code>limit</code> value to indicate that your query reached the end of the list of data, use the absence of <code>after</code> (see Cursors) instead. For example, if you set <code>limit</code> to 10 and 9 results are returned, there may be more data available.  If not set, the default limit (limit = <code>25</code>) will be used. The maximum value for this parameter is <code>500</code>.  (optional) (default to 25)
after = 'after_example' # str | This is the cursor that points to the end of the page of data that has been returned. (optional)

try:
    # List groups
    api_response = api_instance.list_groups(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| This is the maximum number of results that may be returned. Fewer may be returned than the value of &lt;code&gt;limit&lt;/code&gt;.  Do not depend on the number of results being fewer than the &lt;code&gt;limit&lt;/code&gt; value to indicate that your query reached the end of the list of data, use the absence of &lt;code&gt;after&lt;/code&gt; (see Cursors) instead. For example, if you set &lt;code&gt;limit&lt;/code&gt; to 10 and 9 results are returned, there may be more data available.  If not set, the default limit (limit &#x3D; &lt;code&gt;25&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;/code&gt;.  | [optional] [default to 25]
 **after** | **str**| This is the cursor that points to the end of the page of data that has been returned. | [optional] 

### Return type

[**PagedGroups**](PagedGroups.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_group**
> Group patch_group(id, body=body)

Update a group

Updates the group with the specified ID.

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
api_instance = collibra_protect.GroupsApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the group.
body = collibra_protect.ChangeGroupRequest() # ChangeGroupRequest | The changes that need to be applied to the group. (optional)

try:
    # Update a group
    api_response = api_instance.patch_group(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->patch_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the group. | 
 **body** | [**ChangeGroupRequest**](ChangeGroupRequest.md)| The changes that need to be applied to the group. | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

