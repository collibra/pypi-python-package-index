# collibra_core.ValidationApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_validation_results**](ValidationApi.md#find_validation_results) | **GET** /validation | Returns the validation results matching the given search criteria.
[**validate**](ValidationApi.md#validate) | **POST** /validation/{assetId} | Validates a single asset.
[**validate_in_job**](ValidationApi.md#validate_in_job) | **POST** /validation/bulk | Validates multiple assets.

# **find_validation_results**
> ValidationResultPagedResponse find_validation_results(offset=offset, limit=limit, count_limit=count_limit, asset_id=asset_id, job_id=job_id, validation_rule_id=validation_rule_id, most_recent_job=most_recent_job, most_recent_execution=most_recent_execution, result=result)

Returns the validation results matching the given search criteria.

Returns the validation results matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned validation results satisfy all constraints that are specified in this search criteria. By default a result containing at most 1000 validation results is returned. 

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
api_instance = collibra_core.ValidationApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the asset for which we are searching validation results. (optional)
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the job for which we are searching validation results. (optional)
validation_rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the validation rule for which we are searching validation results. (optional)
most_recent_job = true # bool | Check the validationResults of only the most recent job according to the other criteria. (optional)
most_recent_execution = true # bool | Check the validationResults of only the most recent execution (inside or outside a validation job) according to the other criteria. (optional)
result = true # bool | Filter on the result of validation results. (optional)

try:
    # Returns the validation results matching the given search criteria.
    api_response = api_instance.find_validation_results(offset=offset, limit=limit, count_limit=count_limit, asset_id=asset_id, job_id=job_id, validation_rule_id=validation_rule_id, most_recent_job=most_recent_job, most_recent_execution=most_recent_execution, result=result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationApi->find_validation_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **asset_id** | [**str**](.md)| The unique identifier of the asset for which we are searching validation results. | [optional] 
 **job_id** | [**str**](.md)| The unique identifier of the job for which we are searching validation results. | [optional] 
 **validation_rule_id** | [**str**](.md)| The unique identifier of the validation rule for which we are searching validation results. | [optional] 
 **most_recent_job** | **bool**| Check the validationResults of only the most recent job according to the other criteria. | [optional] 
 **most_recent_execution** | **bool**| Check the validationResults of only the most recent execution (inside or outside a validation job) according to the other criteria. | [optional] 
 **result** | **bool**| Filter on the result of validation results. | [optional] 

### Return type

[**ValidationResultPagedResponse**](ValidationResultPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate**
> list[ValidationResultImpl] validate(asset_id)

Validates a single asset.

Validates a single asset.

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
api_instance = collibra_core.ValidationApi(collibra_core.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the asset to be validated

try:
    # Validates a single asset.
    api_response = api_instance.validate(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationApi->validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| the unique identifier of the asset to be validated | 

### Return type

[**list[ValidationResultImpl]**](ValidationResultImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_in_job**
> Job validate_in_job(body=body)

Validates multiple assets.

Validates multiple assets.

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
api_instance = collibra_core.ValidationApi(collibra_core.ApiClient(configuration))
body = collibra_core.ValidateInJobRequest() # ValidateInJobRequest |  (optional)

try:
    # Validates multiple assets.
    api_response = api_instance.validate_in_job(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ValidationApi->validate_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ValidateInJobRequest**](ValidateInJobRequest.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

