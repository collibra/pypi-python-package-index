# collibra_core.IssuesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_issue**](IssuesApi.md#add_issue) | **POST** /issues | Adds a new issue.
[**find_issues**](IssuesApi.md#find_issues) | **GET** /issues | Returns issues matching the given search criteria.
[**move_issue**](IssuesApi.md#move_issue) | **PATCH** /issues/{issueId}/community/{communityId} | Moves an issue to another community.

# **add_issue**
> AssetImpl add_issue(body=body)

Adds a new issue.

Adds a new issue with the given parameters.

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
api_instance = collibra_core.IssuesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddIssueRequest() # AddIssueRequest | The properties of the issue to be added (optional)

try:
    # Adds a new issue.
    api_response = api_instance.add_issue(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->add_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddIssueRequest**](AddIssueRequest.md)| The properties of the issue to be added | [optional] 

### Return type

[**AssetImpl**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_issues**
> AssetPagedResponse find_issues(offset=offset, limit=limit, count_limit=count_limit, sort_order=sort_order, sort_field=sort_field, only_open_issues=only_open_issues, user_relation=user_relation)

Returns issues matching the given search criteria.

Returns issues matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned issues satisfy all constraints that are specified in this search criteria. By default a result containing 1000 issues is returned.

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
api_instance = collibra_core.IssuesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
sort_order = 'ASC' # str | The sorting order of the results. (optional) (default to ASC)
sort_field = 'NAME' # str | The field on which the results are sorted. Default is NAME. (optional) (default to NAME)
only_open_issues = true # bool | Whether only open issues should be returned. (optional) (default to true)
user_relation = 'ALL' # str | The relation of the user with the issues to be returned. By default all issues for the current user will be returned. (optional) (default to ALL)

try:
    # Returns issues matching the given search criteria.
    api_response = api_instance.find_issues(offset=offset, limit=limit, count_limit=count_limit, sort_order=sort_order, sort_field=sort_field, only_open_issues=only_open_issues, user_relation=user_relation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->find_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **sort_order** | **str**| The sorting order of the results. | [optional] [default to ASC]
 **sort_field** | **str**| The field on which the results are sorted. Default is NAME. | [optional] [default to NAME]
 **only_open_issues** | **bool**| Whether only open issues should be returned. | [optional] [default to true]
 **user_relation** | **str**| The relation of the user with the issues to be returned. By default all issues for the current user will be returned. | [optional] [default to ALL]

### Return type

[**AssetPagedResponse**](AssetPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_issue**
> AssetImpl move_issue(issue_id, community_id)

Moves an issue to another community.

Moves an issue to another community.

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
api_instance = collibra_core.IssuesApi(collibra_core.ApiClient(configuration))
issue_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the issue to be moved
community_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the community to move the issue to

try:
    # Moves an issue to another community.
    api_response = api_instance.move_issue(issue_id, community_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->move_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | [**str**](.md)| ID of the issue to be moved | 
 **community_id** | [**str**](.md)| ID of the community to move the issue to | 

### Return type

[**AssetImpl**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

