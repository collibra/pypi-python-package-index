# collibra_assessments.TemplatesApi

All URIs are relative to */rest/assessments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_templates**](TemplatesApi.md#list_templates) | **GET** /templates | List templates

# **list_templates**
> PagedTemplates list_templates(name=name, status=status, asset_type_id=asset_type_id, latest_version_only=latest_version_only, limit=limit, cursor=cursor)

List templates

Returns a list of all available templates. The templates are sorted by `name` in alphabetical order.

### Example
```python
from __future__ import print_function
import time
import collibra_assessments
from collibra_assessments.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_assessments.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_assessments.TemplatesApi(collibra_assessments.ApiClient(configuration))
name = 'name_example' # str | The name of the template.   The value is case-insensitive and it returns results that contain this value.  (optional)
status = 'status_example' # str | The status of the template.   Possible values are: `DRAFT`, `PUBLISHED` or `OBSOLETE`. The value is case-insensitive. An invalid value results in an error response.  (optional)
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the asset type. (optional)
latest_version_only = true # bool | Whether it should only return the latest version of each template. The interaction with the `status` parameter is as follows: - If the `status` parameter is not set, it returns the latest version of each template regardless of the status. - If the `status` parameter is set to `PUBLISHED`, it returns the latest published version of each template. - If the `status` parameter is set to `DRAFT`, it returns the latest draft version of each template. - If the `status` parameter is set to `OBSOLETE`, it returns the latest obsolete version of each template.  (optional)
limit = 10 # int | The maximum number of resources to retrieve.  If not set, the default limit of `10` is be used. The maximum value for this parameter is `50`.  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor pointing to the first resource to be included in the response. This cursor cannot be created and must have been extracted from a response returned by a previous API call.  If this parameter is missing, the API returns the resources starting from the first available resource, at index `0`.  (optional)

try:
    # List templates
    api_response = api_instance.list_templates(name=name, status=status, asset_type_id=asset_type_id, latest_version_only=latest_version_only, limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->list_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the template.   The value is case-insensitive and it returns results that contain this value.  | [optional] 
 **status** | **str**| The status of the template.   Possible values are: &#x60;DRAFT&#x60;, &#x60;PUBLISHED&#x60; or &#x60;OBSOLETE&#x60;. The value is case-insensitive. An invalid value results in an error response.  | [optional] 
 **asset_type_id** | [**str**](.md)| The ID of the asset type. | [optional] 
 **latest_version_only** | **bool**| Whether it should only return the latest version of each template. The interaction with the &#x60;status&#x60; parameter is as follows: - If the &#x60;status&#x60; parameter is not set, it returns the latest version of each template regardless of the status. - If the &#x60;status&#x60; parameter is set to &#x60;PUBLISHED&#x60;, it returns the latest published version of each template. - If the &#x60;status&#x60; parameter is set to &#x60;DRAFT&#x60;, it returns the latest draft version of each template. - If the &#x60;status&#x60; parameter is set to &#x60;OBSOLETE&#x60;, it returns the latest obsolete version of each template.  | [optional] 
 **limit** | **int**| The maximum number of resources to retrieve.  If not set, the default limit of &#x60;10&#x60; is be used. The maximum value for this parameter is &#x60;50&#x60;.  | [optional] [default to 10]
 **cursor** | **str**| The cursor pointing to the first resource to be included in the response. This cursor cannot be created and must have been extracted from a response returned by a previous API call.  If this parameter is missing, the API returns the resources starting from the first available resource, at index &#x60;0&#x60;.  | [optional] 

### Return type

[**PagedTemplates**](PagedTemplates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

