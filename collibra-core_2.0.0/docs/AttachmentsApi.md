# collibra_core.AttachmentsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_attachment**](AttachmentsApi.md#add_attachment) | **POST** /attachments | Add attachment
[**find_attachments**](AttachmentsApi.md#find_attachments) | **GET** /attachments | Find attachments
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /attachments/{attachmentId} | Get attachment
[**get_attachment_content**](AttachmentsApi.md#get_attachment_content) | **GET** /attachments/{attachmentId}/file | Get attachment content
[**remove_attachment**](AttachmentsApi.md#remove_attachment) | **DELETE** /attachments/{attachmentId} | Remove attachment

# **add_attachment**
> AttachmentImpl add_attachment(file=file, file_name=file_name, resource_type=resource_type, resource_id=resource_id)

Add attachment

Adds new attachment.

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
api_instance = collibra_core.AttachmentsApi(collibra_core.ApiClient(configuration))
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
resource_type = 'resource_type_example' # str |  (optional)
resource_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Add attachment
    api_response = api_instance.add_attachment(file=file, file_name=file_name, resource_type=resource_type, resource_id=resource_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->add_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **resource_type** | **str**|  | [optional] 
 **resource_id** | [**str**](.md)|  | [optional] 

### Return type

[**AttachmentImpl**](AttachmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_attachments**
> AttachmentPagedResponse find_attachments(offset=offset, limit=limit, count_limit=count_limit, file_name=file_name, file_content_type=file_content_type, upload_date=upload_date, user_id=user_id, base_resource_id=base_resource_id, sort_field=sort_field, sort_order=sort_order)

Find attachments

Returns attachments matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attachments satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attachments is returned.

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
api_instance = collibra_core.AttachmentsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
file_name = 'file_name_example' # str | The name of the file representing searched attachment. (optional)
file_content_type = 'file_content_type_example' # str | The type of the content of the file representing searched attachment. (optional)
upload_date = 789 # int | The date of attachment upload. It is the timestamp (in UTC time standard). (optional)
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the user who uploaded the attachment. (optional)
base_resource_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource the attachment refers to. (optional)
sort_field = 'LAST_MODIFIED' # str | The field that should be used as reference for sorting. (optional) (default to LAST_MODIFIED)
sort_order = 'DESC' # str | The order of sorting. (optional) (default to DESC)

try:
    # Find attachments
    api_response = api_instance.find_attachments(offset=offset, limit=limit, count_limit=count_limit, file_name=file_name, file_content_type=file_content_type, upload_date=upload_date, user_id=user_id, base_resource_id=base_resource_id, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->find_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **file_name** | **str**| The name of the file representing searched attachment. | [optional] 
 **file_content_type** | **str**| The type of the content of the file representing searched attachment. | [optional] 
 **upload_date** | **int**| The date of attachment upload. It is the timestamp (in UTC time standard). | [optional] 
 **user_id** | [**str**](.md)| The ID of the user who uploaded the attachment. | [optional] 
 **base_resource_id** | [**str**](.md)| The ID of the resource the attachment refers to. | [optional] 
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] [default to LAST_MODIFIED]
 **sort_order** | **str**| The order of sorting. | [optional] [default to DESC]

### Return type

[**AttachmentPagedResponse**](AttachmentPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> AttachmentImpl get_attachment(attachment_id)

Get attachment

Returns information about the attachment identified by id.

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
api_instance = collibra_core.AttachmentsApi(collibra_core.ApiClient(configuration))
attachment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the attachment

try:
    # Get attachment
    api_response = api_instance.get_attachment(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**str**](.md)| the id of the attachment | 

### Return type

[**AttachmentImpl**](AttachmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_content**
> str get_attachment_content(attachment_id)

Get attachment content

Returns content of the attachment identified by given id.

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
api_instance = collibra_core.AttachmentsApi(collibra_core.ApiClient(configuration))
attachment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the attachment

try:
    # Get attachment content
    api_response = api_instance.get_attachment_content(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**str**](.md)| the id of the attachment | 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_attachment**
> remove_attachment(attachment_id)

Remove attachment

Removes attachment identified by given id.

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
api_instance = collibra_core.AttachmentsApi(collibra_core.ApiClient(configuration))
attachment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the attachment

try:
    # Remove attachment
    api_instance.remove_attachment(attachment_id)
except ApiException as e:
    print("Exception when calling AttachmentsApi->remove_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | [**str**](.md)| the id of the attachment | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

