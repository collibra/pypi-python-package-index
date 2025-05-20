# collibra_core.CommentsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment**](CommentsApi.md#add_comment) | **POST** /comments | Add comment.
[**change_comment**](CommentsApi.md#change_comment) | **PATCH** /comments/{commentId} | Change comment.
[**find_comments**](CommentsApi.md#find_comments) | **GET** /comments | Find comments.
[**get_comment**](CommentsApi.md#get_comment) | **GET** /comments/{commentId} | Get comment.
[**remove_comment**](CommentsApi.md#remove_comment) | **DELETE** /comments/{commentId} | Remove comment.

# **add_comment**
> Comment add_comment(body=body)

Add comment.

Adds a new comment.

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
api_instance = collibra_core.CommentsApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddCommentRequest() # AddCommentRequest | The properties of new comment. (optional)

try:
    # Add comment.
    api_response = api_instance.add_comment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddCommentRequest**](AddCommentRequest.md)| The properties of new comment. | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_comment**
> Comment change_comment(comment_id, body=body)

Change comment.

<p>Modifies the comment with the specified ID.</p><p>Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.</p>

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
api_instance = collibra_core.CommentsApi(collibra_core.ApiClient(configuration))
comment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the comment to be changed.
body = collibra_core.ChangeCommentRequest() # ChangeCommentRequest | The properties to change comment. (optional)

try:
    # Change comment.
    api_response = api_instance.change_comment(comment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->change_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | [**str**](.md)| The ID of the comment to be changed. | 
 **body** | [**ChangeCommentRequest**](ChangeCommentRequest.md)| The properties to change comment. | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_comments**
> CommentPagedResponse find_comments(offset=offset, limit=limit, count_limit=count_limit, parent_id=parent_id, user_id=user_id, base_resource_id=base_resource_id, root_comment=root_comment, sort_order=sort_order)

Find comments.

<p>Returns comments matching the given search criteria.</p><p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.</p><p>The returned comments satisfy all constraints that are specified in this search criteria.</p><p>By default, the result contains up to 1000 comments.</p>

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
api_instance = collibra_core.CommentsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
parent_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the comment which the reply comments should be searched for (optional)
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the user who created the comment. (optional)
base_resource_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource which the searched comments refer to. (optional)
root_comment = true # bool | Whether the searched comments should be root comments (not reply comments). (optional)
sort_order = 'DESC' # str | The order of sorting on the date the comment was created. (optional) (default to DESC)

try:
    # Find comments.
    api_response = api_instance.find_comments(offset=offset, limit=limit, count_limit=count_limit, parent_id=parent_id, user_id=user_id, base_resource_id=base_resource_id, root_comment=root_comment, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->find_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **parent_id** | [**str**](.md)| The ID of the comment which the reply comments should be searched for | [optional] 
 **user_id** | [**str**](.md)| The ID of the user who created the comment. | [optional] 
 **base_resource_id** | [**str**](.md)| The ID of the resource which the searched comments refer to. | [optional] 
 **root_comment** | **bool**| Whether the searched comments should be root comments (not reply comments). | [optional] 
 **sort_order** | **str**| The order of sorting on the date the comment was created. | [optional] [default to DESC]

### Return type

[**CommentPagedResponse**](CommentPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> Comment get_comment(comment_id)

Get comment.

Returns the comment with the specified ID.

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
api_instance = collibra_core.CommentsApi(collibra_core.ApiClient(configuration))
comment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the comment.

try:
    # Get comment.
    api_response = api_instance.get_comment(comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | [**str**](.md)| The ID of the comment. | 

### Return type

[**Comment**](Comment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_comment**
> remove_comment(comment_id)

Remove comment.

Removes the comment with the specified ID.

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
api_instance = collibra_core.CommentsApi(collibra_core.ApiClient(configuration))
comment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the comment to be removed.

try:
    # Remove comment.
    api_instance.remove_comment(comment_id)
except ApiException as e:
    print("Exception when calling CommentsApi->remove_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | [**str**](.md)| The ID of the comment to be removed. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

