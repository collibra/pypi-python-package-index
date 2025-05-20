# collibra_core.JobsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_job**](JobsApi.md#cancel_job) | **POST** /jobs/{jobId}/canceled | Cancels given Job.
[**find_jobs**](JobsApi.md#find_jobs) | **GET** /jobs | Find jobs
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{jobId} | Returns the Job identified by the given UUID.

# **cancel_job**
> cancel_job(job_id, body=body)

Cancels given Job.

Calling this endpoint will return immediately and not wait until the Job is actually stopped.

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
api_instance = collibra_core.JobsApi(collibra_core.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the Job.
body = collibra_core.CancelJobRequest() # CancelJobRequest |  (optional)

try:
    # Cancels given Job.
    api_instance.cancel_job(job_id, body=body)
except ApiException as e:
    print("Exception when calling JobsApi->cancel_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| The unique identifier of the Job. | 
 **body** | [**CancelJobRequest**](CancelJobRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_jobs**
> JobPagedResponse find_jobs(offset=offset, limit=limit, count_limit=count_limit, created_by=created_by, name=name, name_match_mode=name_match_mode, states=states, results=results, types=types, max_visibility=max_visibility, visible=visible, sort_order=sort_order, sort_field=sort_field)

Find jobs

Returns jobs matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.

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
api_instance = collibra_core.JobsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
created_by = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the user who created the searched job. (optional)
name = 'name_example' # str | The name of the job to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) (default to ANYWHERE)
states = ['states_example'] # list[str] | The list of states which the jobs should be searched for. (optional)
results = ['results_example'] # list[str] | The list of results which the jobs should be searched for. (optional)
types = ['types_example'] # list[str] | The list of types of the jobs. (optional)
max_visibility = 2147483647 # int | The maximum visibility of the job. Ignored, use visible instead (optional) (default to 2147483647)
visible = true # bool | The visibility of the jobs. Defaults to all jobs (both visible and non-visible). (optional)
sort_order = 'DESC' # str | The order of sorting. (optional) (default to DESC)
sort_field = 'CREATED_ON' # str | The field that should be used as reference for sorting. (optional) (default to CREATED_ON)

try:
    # Find jobs
    api_response = api_instance.find_jobs(offset=offset, limit=limit, count_limit=count_limit, created_by=created_by, name=name, name_match_mode=name_match_mode, states=states, results=results, types=types, max_visibility=max_visibility, visible=visible, sort_order=sort_order, sort_field=sort_field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->find_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **created_by** | [**str**](.md)| The ID of the user who created the searched job. | [optional] 
 **name** | **str**| The name of the job to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] [default to ANYWHERE]
 **states** | [**list[str]**](str.md)| The list of states which the jobs should be searched for. | [optional] 
 **results** | [**list[str]**](str.md)| The list of results which the jobs should be searched for. | [optional] 
 **types** | [**list[str]**](str.md)| The list of types of the jobs. | [optional] 
 **max_visibility** | **int**| The maximum visibility of the job. Ignored, use visible instead | [optional] [default to 2147483647]
 **visible** | **bool**| The visibility of the jobs. Defaults to all jobs (both visible and non-visible). | [optional] 
 **sort_order** | **str**| The order of sorting. | [optional] [default to DESC]
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] [default to CREATED_ON]

### Return type

[**JobPagedResponse**](JobPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job**
> Job get_job(job_id)

Returns the Job identified by the given UUID.

Returns the Job identified by the given UUID.

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
api_instance = collibra_core.JobsApi(collibra_core.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the job.

try:
    # Returns the Job identified by the given UUID.
    api_response = api_instance.get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| The ID of the job. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

