# collibra_import.ImportResultsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_import_errors**](ImportResultsApi.md#find_import_errors) | **GET** /import/results/{jobId}/errors | List the errors of a finished import job
[**get_import_job_summary**](ImportResultsApi.md#get_import_job_summary) | **GET** /import/results/{jobId}/summary | Retrieve a summary of a finished import job

# **find_import_errors**
> ImportErrorPagedResponse find_import_errors(job_id, offset=offset, limit=limit, count_limit=count_limit)

List the errors of a finished import job

Returns a list of errors of a finished import job with the specified ID. By default the maximum number of results is limited to 1000.

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportResultsApi(collibra_import.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the job
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)

try:
    # List the errors of a finished import job
    api_response = api_instance.find_import_errors(job_id, offset=offset, limit=limit, count_limit=count_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportResultsApi->find_import_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| The ID of the job | 
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]

### Return type

[**ImportErrorPagedResponse**](ImportErrorPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_job_summary**
> ImportSummary get_import_job_summary(job_id)

Retrieve a summary of a finished import job

Returns details about a finished import job with the specified ID such as the total number of resources and types of resources that were added, removed or updated and the number of errors.

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportResultsApi(collibra_import.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the job

try:
    # Retrieve a summary of a finished import job
    api_response = api_instance.get_import_job_summary(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportResultsApi->get_import_job_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| The ID of the job | 

### Return type

[**ImportSummary**](ImportSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

