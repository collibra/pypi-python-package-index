# collibra_assessments.AssessmentsApi

All URIs are relative to */rest/assessments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conduct_assessment**](AssessmentsApi.md#conduct_assessment) | **POST** /assessments/conduct | Conduct an assessment
[**get_assessment**](AssessmentsApi.md#get_assessment) | **GET** /assessments/{id} | Retrieve an assessment by ID
[**get_assessment_by_assessment_review**](AssessmentsApi.md#get_assessment_by_assessment_review) | **GET** /assessments/byAssessmentReview/{id} | Retrieve an assessment by assessment review ID
[**list_assessments**](AssessmentsApi.md#list_assessments) | **GET** /assessments | List assessments

# **conduct_assessment**
> Assessment conduct_assessment(body)

Conduct an assessment

Starts conducting an assessment by creating it in `DRAFT` status.

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
api_instance = collibra_assessments.AssessmentsApi(collibra_assessments.ApiClient(configuration))
body = collibra_assessments.ConductAssessmentRequest() # ConductAssessmentRequest | 

try:
    # Conduct an assessment
    api_response = api_instance.conduct_assessment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssessmentsApi->conduct_assessment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConductAssessmentRequest**](ConductAssessmentRequest.md)|  | 

### Return type

[**Assessment**](Assessment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assessment**
> Assessment get_assessment(id)

Retrieve an assessment by ID

Returns information about the assessment with the specified ID.

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
api_instance = collibra_assessments.AssessmentsApi(collibra_assessments.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the assessment.

try:
    # Retrieve an assessment by ID
    api_response = api_instance.get_assessment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssessmentsApi->get_assessment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the assessment. | 

### Return type

[**Assessment**](Assessment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assessment_by_assessment_review**
> Assessment get_assessment_by_assessment_review(id)

Retrieve an assessment by assessment review ID

Returns information about the assessment with the specified assessment review asset ID.

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
api_instance = collibra_assessments.AssessmentsApi(collibra_assessments.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the assessment review asset.

try:
    # Retrieve an assessment by assessment review ID
    api_response = api_instance.get_assessment_by_assessment_review(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssessmentsApi->get_assessment_by_assessment_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The ID of the assessment review asset. | 

### Return type

[**Assessment**](Assessment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assessments**
> PagedAssessments list_assessments(name=name, status=status, last_modified_from=last_modified_from, last_modified_until=last_modified_until, template_id=template_id, template_version=template_version, asset_id=asset_id, limit=limit, cursor=cursor)

List assessments

Returns a list of assessments that you created; and the assessments that you are permitted to view. The assessments are sorted by `lastModifiedOn` in descending order, with the most recent first.

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
api_instance = collibra_assessments.AssessmentsApi(collibra_assessments.ApiClient(configuration))
name = 'name_example' # str | The name of the assessment.   The value is case-insensitive and it returns results that contain this value.  (optional)
status = 'status_example' # str | The status of the assessment.   Possible values are: `DRAFT`, `SUBMITTED`, `COMPLETED` or `OBSOLETE`. The value is case-insensitive. An invalid value results in an error response.  (optional)
last_modified_from = '2013-10-20T19:20:30+01:00' # datetime | The date and time that defines the start of the period when the assessment was last updated, including this timestamp. (optional)
last_modified_until = '2013-10-20T19:20:30+01:00' # datetime | The date and time that defines the end of the period when the assessment was last updated, excluding this timestamp. (optional)
template_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the template. (optional)
template_version = 'template_version_example' # str | The version of the template.   Use `LATEST` to retrieve assessments that are on the latest version of a particular `templateId`. For other values, it returns results that have an exact match.  (optional)
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the asset the assessment relates to. (optional)
limit = 10 # int | The maximum number of resources to retrieve.  If not set, the default limit of `10` is be used. The maximum value for this parameter is `50`.  (optional) (default to 10)
cursor = 'cursor_example' # str | The cursor pointing to the first resource to be included in the response. This cursor cannot be created and must have been extracted from a response returned by a previous API call.  If this parameter is missing, the API returns the resources starting from the first available resource, at index `0`.  (optional)

try:
    # List assessments
    api_response = api_instance.list_assessments(name=name, status=status, last_modified_from=last_modified_from, last_modified_until=last_modified_until, template_id=template_id, template_version=template_version, asset_id=asset_id, limit=limit, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssessmentsApi->list_assessments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the assessment.   The value is case-insensitive and it returns results that contain this value.  | [optional] 
 **status** | **str**| The status of the assessment.   Possible values are: &#x60;DRAFT&#x60;, &#x60;SUBMITTED&#x60;, &#x60;COMPLETED&#x60; or &#x60;OBSOLETE&#x60;. The value is case-insensitive. An invalid value results in an error response.  | [optional] 
 **last_modified_from** | **datetime**| The date and time that defines the start of the period when the assessment was last updated, including this timestamp. | [optional] 
 **last_modified_until** | **datetime**| The date and time that defines the end of the period when the assessment was last updated, excluding this timestamp. | [optional] 
 **template_id** | [**str**](.md)| The ID of the template. | [optional] 
 **template_version** | **str**| The version of the template.   Use &#x60;LATEST&#x60; to retrieve assessments that are on the latest version of a particular &#x60;templateId&#x60;. For other values, it returns results that have an exact match.  | [optional] 
 **asset_id** | [**str**](.md)| The ID of the asset the assessment relates to. | [optional] 
 **limit** | **int**| The maximum number of resources to retrieve.  If not set, the default limit of &#x60;10&#x60; is be used. The maximum value for this parameter is &#x60;50&#x60;.  | [optional] [default to 10]
 **cursor** | **str**| The cursor pointing to the first resource to be included in the response. This cursor cannot be created and must have been extracted from a response returned by a previous API call.  If this parameter is missing, the API returns the resources starting from the first available resource, at index &#x60;0&#x60;.  | [optional] 

### Return type

[**PagedAssessments**](PagedAssessments.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

