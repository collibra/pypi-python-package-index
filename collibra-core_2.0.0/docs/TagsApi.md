# collibra_core.TagsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_tag**](TagsApi.md#change_tag) | **PATCH** /tags/{tagId} | Change tag.
[**exists**](TagsApi.md#exists) | **GET** /tags/exists/{tagName} | Check tag name.
[**find_tags**](TagsApi.md#find_tags) | **GET** /tags | Find tags.
[**get_tag**](TagsApi.md#get_tag) | **GET** /tags/{tagId} | Get tag.
[**get_tags_by_asset_id**](TagsApi.md#get_tags_by_asset_id) | **GET** /tags/asset/{assetId} | Get asset tags.
[**merge_tags**](TagsApi.md#merge_tags) | **POST** /tags/merge | Merge tags.
[**remove_tag**](TagsApi.md#remove_tag) | **DELETE** /tags/{tagId} | Remove tag.
[**remove_tags**](TagsApi.md#remove_tags) | **DELETE** /tags/bulk | Remove tags.

# **change_tag**
> Tag change_tag(tag_id, body=body)

Change tag.

Modifies the tag with the specified ID.

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
api_instance = collibra_core.TagsApi(collibra_core.ApiClient(configuration))
tag_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the tag to be changed.
body = collibra_core.ChangeTagRequest() # ChangeTagRequest | The properties of the tag to be changed. (optional)

try:
    # Change tag.
    api_response = api_instance.change_tag(tag_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->change_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | [**str**](.md)| The ID of the tag to be changed. | 
 **body** | [**ChangeTagRequest**](ChangeTagRequest.md)| The properties of the tag to be changed. | [optional] 

### Return type

[**Tag**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exists**
> bool exists(tag_name, encoded=encoded)

Check tag name.

Checks whether a tag with given name exists. Returns <code>true</code> if a tag with given name exists, <code>false</code> otherwise.

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
api_instance = collibra_core.TagsApi(collibra_core.ApiClient(configuration))
tag_name = 'tag_name_example' # str | The name of the tag.
encoded = false # bool | Whether the tag name is encoded using URL and Filename safe type base64 encoding scheme. (optional) (default to false)

try:
    # Check tag name.
    api_response = api_instance.exists(tag_name, encoded=encoded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The name of the tag. | 
 **encoded** | **bool**| Whether the tag name is encoded using URL and Filename safe type base64 encoding scheme. | [optional] [default to false]

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_tags**
> TagPagedResponse find_tags(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode)

Find tags.

Returns tags matching the given search criteria.The returned tags satisfy all constraints that are specified in this search criteria. By default, the result contains 1000 tags.

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
api_instance = collibra_core.TagsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The name of the tag to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) (default to ANYWHERE)

try:
    # Find tags.
    api_response = api_instance.find_tags(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->find_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The name of the tag to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] [default to ANYWHERE]

### Return type

[**TagPagedResponse**](TagPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> Tag get_tag(tag_id)

Get tag.

Returns the tag with the specified ID.

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
api_instance = collibra_core.TagsApi(collibra_core.ApiClient(configuration))
tag_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the tag.

try:
    # Get tag.
    api_response = api_instance.get_tag(tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | [**str**](.md)| The ID of the tag. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_by_asset_id**
> list[Tag] get_tags_by_asset_id(asset_id)

Get asset tags.

Returns all the tags of the asset with the specified ID.

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
api_instance = collibra_core.TagsApi(collibra_core.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the asset.

try:
    # Get asset tags.
    api_response = api_instance.get_tags_by_asset_id(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->get_tags_by_asset_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| The ID of the asset. | 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_tags**
> merge_tags(body=body)

Merge tags.

Merges two tags into one. All assets tagged with the fromId tag receive the toId tag and the fromId tag is removed.

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
api_instance = collibra_core.TagsApi(collibra_core.ApiClient(configuration))
body = collibra_core.MergeTagsRequest() # MergeTagsRequest | The IDs of the tags to be merged. (optional)

try:
    # Merge tags.
    api_instance.merge_tags(body=body)
except ApiException as e:
    print("Exception when calling TagsApi->merge_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MergeTagsRequest**](MergeTagsRequest.md)| The IDs of the tags to be merged. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tag**
> remove_tag(tag_id)

Remove tag.

Removes the tag with the specified ID.

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
api_instance = collibra_core.TagsApi(collibra_core.ApiClient(configuration))
tag_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the tag.

try:
    # Remove tag.
    api_instance.remove_tag(tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->remove_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | [**str**](.md)| The ID of the tag. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tags**
> remove_tags(body=body)

Remove tags.

Removes multiple tags with the specified IDs.

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
api_instance = collibra_core.TagsApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | The IDs of the tags to be removed. (optional)

try:
    # Remove tags.
    api_instance.remove_tags(body=body)
except ApiException as e:
    print("Exception when calling TagsApi->remove_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The IDs of the tags to be removed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

