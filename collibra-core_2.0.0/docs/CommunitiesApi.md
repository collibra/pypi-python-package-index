# collibra_core.CommunitiesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_communities**](CommunitiesApi.md#add_communities) | **POST** /communities/bulk | Add multiple communities
[**add_community**](CommunitiesApi.md#add_community) | **POST** /communities | Add community
[**change_communities**](CommunitiesApi.md#change_communities) | **PATCH** /communities/bulk | Change multiple communities
[**change_community**](CommunitiesApi.md#change_community) | **PATCH** /communities/{communityId} | Change community
[**change_to_root_community**](CommunitiesApi.md#change_to_root_community) | **POST** /communities/{communityId}/root | Change to root community
[**find_communities**](CommunitiesApi.md#find_communities) | **GET** /communities | Find communities
[**get_community**](CommunitiesApi.md#get_community) | **GET** /communities/{communityId} | Get community
[**get_community_breadcrumb**](CommunitiesApi.md#get_community_breadcrumb) | **GET** /communities/{communityId}/breadcrumb | Get community breadcrumb
[**remove_communities**](CommunitiesApi.md#remove_communities) | **DELETE** /communities/bulk | Remove multiple communities
[**remove_communities_in_job**](CommunitiesApi.md#remove_communities_in_job) | **POST** /communities/removalJobs | Remove multiple communities asynchronously
[**remove_community**](CommunitiesApi.md#remove_community) | **DELETE** /communities/{communityId} | Remove community

# **add_communities**
> list[CommunityImpl] add_communities(body=body)

Add multiple communities

Adds multiple communities with the given parameters

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddCommunityRequest()] # list[AddCommunityRequest] | List of the properties of the communities to be added. (optional)

try:
    # Add multiple communities
    api_response = api_instance.add_communities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->add_communities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddCommunityRequest]**](AddCommunityRequest.md)| List of the properties of the communities to be added. | [optional] 

### Return type

[**list[CommunityImpl]**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_community**
> CommunityImpl add_community(body=body)

Add community

Adds a new community with the given parameters.

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddCommunityRequest() # AddCommunityRequest | the properties of the community to be added (optional)

try:
    # Add community
    api_response = api_instance.add_community(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->add_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddCommunityRequest**](AddCommunityRequest.md)| the properties of the community to be added | [optional] 

### Return type

[**CommunityImpl**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_communities**
> list[CommunityImpl] change_communities(body=body)

Change multiple communities

Changes multiple communities using the given request parameters

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeCommunityRequest()] # list[ChangeCommunityRequest] | List of the properties of the communities to be changed. (optional)

try:
    # Change multiple communities
    api_response = api_instance.change_communities(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->change_communities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeCommunityRequest]**](ChangeCommunityRequest.md)| List of the properties of the communities to be changed. | [optional] 

### Return type

[**list[CommunityImpl]**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_community**
> CommunityImpl change_community(community_id, body=body)

Change community

Changes the community with the information that is present in the request. Only properties that are specified in this request and have non-<code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
community_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the community to be changed.
body = collibra_core.ChangeCommunityRequest() # ChangeCommunityRequest | the properties of the community to be changed (optional)

try:
    # Change community
    api_response = api_instance.change_community(community_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->change_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | [**str**](.md)| the id of the community to be changed. | 
 **body** | [**ChangeCommunityRequest**](ChangeCommunityRequest.md)| the properties of the community to be changed | [optional] 

### Return type

[**CommunityImpl**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_to_root_community**
> CommunityImpl change_to_root_community(community_id)

Change to root community

Changes the community with given ID to a root community.

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
community_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the community that will be changed to a root community

try:
    # Change to root community
    api_response = api_instance.change_to_root_community(community_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->change_to_root_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | [**str**](.md)| The ID of the community that will be changed to a root community | 

### Return type

[**CommunityImpl**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_communities**
> CommunityPagedResponse find_communities(sort_field, offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, sort_order=sort_order)

Find communities

Returns communities matching the given search criteria. Only parameters that are specified in this request and have non-<code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 communities is returned.

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
sort_field = 'NAME' # str | The field on which the results are sorted. (default to NAME)
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. (optional) (default to -1)
cursor = 'cursor_example' # str | Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (<code>nextCursor</code> property). (optional)
name = 'name_example' # str | The name of the community to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) (default to ANYWHERE)
parent_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the parent community to find the communities in. (optional)
exclude_meta = true # bool | The exclude meta flag. If this is set to true then the meta communities will not be returned (meta communities are i.e. communities not created manually by the user). (optional) (default to true)
sort_order = 'ASC' # str | The sorting order. (optional) (default to ASC)

try:
    # Find communities
    api_response = api_instance.find_communities(sort_field, offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->find_communities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_field** | **str**| The field on which the results are sorted. | [default to NAME]
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. | [optional] [default to -1]
 **cursor** | **str**| Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (&lt;code&gt;nextCursor&lt;/code&gt; property). | [optional] 
 **name** | **str**| The name of the community to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] [default to ANYWHERE]
 **parent_id** | [**str**](.md)| The ID of the parent community to find the communities in. | [optional] 
 **exclude_meta** | **bool**| The exclude meta flag. If this is set to true then the meta communities will not be returned (meta communities are i.e. communities not created manually by the user). | [optional] [default to true]
 **sort_order** | **str**| The sorting order. | [optional] [default to ASC]

### Return type

[**CommunityPagedResponse**](CommunityPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community**
> CommunityImpl get_community(community_id)

Get community

Returns the community with the given ID.

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
community_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the ID of the community

try:
    # Get community
    api_response = api_instance.get_community(community_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->get_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | [**str**](.md)| the ID of the community | 

### Return type

[**CommunityImpl**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community_breadcrumb**
> list[NamedResourceReferenceImpl] get_community_breadcrumb(community_id)

Get community breadcrumb

Returns the list of communities that lead to the community identified by the given ID.

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
community_id = 'community_id_example' # str | The ID of the community

try:
    # Get community breadcrumb
    api_response = api_instance.get_community_breadcrumb(community_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->get_community_breadcrumb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | **str**| The ID of the community | 

### Return type

[**list[NamedResourceReferenceImpl]**](NamedResourceReferenceImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_communities**
> remove_communities(body=body)

Remove multiple communities

This endpoint will be removed in the future. Please use POST /communities/removalJobs.

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | the IDs of the communities to be removed, i.e. ["6f685f90-1036-4d30-983a-a9bbcdd7b8f6", "6f685f90-1036-4d30-983a-a9bbcdd7b123"] (optional)

try:
    # Remove multiple communities
    api_instance.remove_communities(body=body)
except ApiException as e:
    print("Exception when calling CommunitiesApi->remove_communities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| the IDs of the communities to be removed, i.e. [&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6&quot;, &quot;6f685f90-1036-4d30-983a-a9bbcdd7b123&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_communities_in_job**
> Job remove_communities_in_job(body=body)

Remove multiple communities asynchronously

Removes multiple communities in a job.

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | the IDs of the communities to be removed, i.e. ["6f685f90-1036-4d30-983a-a9bbcdd7b8f6", "6f685f90-1036-4d30-983a-a9bbcdd7b123"] (optional)

try:
    # Remove multiple communities asynchronously
    api_response = api_instance.remove_communities_in_job(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->remove_communities_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| the IDs of the communities to be removed, i.e. [&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6&quot;, &quot;6f685f90-1036-4d30-983a-a9bbcdd7b123&quot;] | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_community**
> remove_community(community_id)

Remove community

This endpoint will be removed in the future. Please use POST /communities/removalJobs

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
api_instance = collibra_core.CommunitiesApi(collibra_core.ApiClient(configuration))
community_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the ID of the community to remove

try:
    # Remove community
    api_instance.remove_community(community_id)
except ApiException as e:
    print("Exception when calling CommunitiesApi->remove_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | [**str**](.md)| the ID of the community to remove | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

