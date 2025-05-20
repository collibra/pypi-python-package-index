# collibra_search.SearchApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_views**](SearchApi.md#find_views) | **GET** /search/views | Lists search views.
[**get_view**](SearchApi.md#get_view) | **GET** /search/views/{viewId} | Returns the details of an existing search view.
[**search**](SearchApi.md#search) | **POST** /search | Search.

# **find_views**
> SearchViewPagedResponse find_views(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, sort_field=sort_field, sort_order=sort_order)

Lists search views.

Returns a list of all search views, also known as search filters, matching the given search criteria.<br /> Only search views the logged in user has access to are listed.

### Example
```python
from __future__ import print_function
import time
import collibra_search
from collibra_search.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_search.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_search.SearchApi(collibra_search.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The search term for a search view to retrieve.<br /> The query is case sensitive and does not support wildcards.<br /> Use in conjunction with `nameMatchMode`. (optional)
name_match_mode = 'ANYWHERE' # str | The match requirements for `name` queries.<br /> Works in conjunction with `name`. The search is case-sensitive. (optional) (default to ANYWHERE)
sort_field = 'NAME' # str | The reference field for sorting the results. (optional) (default to NAME)
sort_order = 'ASC' # str | The order in which the results are sorted. (optional) (default to ASC)

try:
    # Lists search views.
    api_response = api_instance.find_views(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->find_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The search term for a search view to retrieve.&lt;br /&gt; The query is case sensitive and does not support wildcards.&lt;br /&gt; Use in conjunction with &#x60;nameMatchMode&#x60;. | [optional] 
 **name_match_mode** | **str**| The match requirements for &#x60;name&#x60; queries.&lt;br /&gt; Works in conjunction with &#x60;name&#x60;. The search is case-sensitive. | [optional] [default to ANYWHERE]
 **sort_field** | **str**| The reference field for sorting the results. | [optional] [default to NAME]
 **sort_order** | **str**| The order in which the results are sorted. | [optional] [default to ASC]

### Return type

[**SearchViewPagedResponse**](SearchViewPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_view**
> SearchView get_view(view_id)

Returns the details of an existing search view.

Returns the details of a search view, also known as a search filter, identified by the given ID.

### Example
```python
from __future__ import print_function
import time
import collibra_search
from collibra_search.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_search.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_search.SearchApi(collibra_search.ApiClient(configuration))
view_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the search view to be queried.

try:
    # Returns the details of an existing search view.
    api_response = api_instance.get_view(view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->get_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | [**str**](.md)| The ID of the search view to be queried. | 

### Return type

[**SearchView**](SearchView.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(body=body)

Search.

Performs a search and returns a list of resources which meet the search criteria defined in the request body.

### Example
```python
from __future__ import print_function
import time
import collibra_search
from collibra_search.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_search.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_search.SearchApi(collibra_search.ApiClient(configuration))
body = collibra_search.SearchRequest() # SearchRequest | The search criteria. (optional)

try:
    # Search.
    api_response = api_instance.search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| The search criteria. | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

