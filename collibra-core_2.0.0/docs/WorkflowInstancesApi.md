# collibra_core.WorkflowInstancesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_workflow_instances**](WorkflowInstancesApi.md#cancel_workflow_instances) | **POST** /workflowInstances/{workflowInstanceId}/canceled | Cancel workflow instance.
[**find_workflow_instances**](WorkflowInstancesApi.md#find_workflow_instances) | **GET** /workflowInstances | Find workflow instances.
[**get_workflow_instance_diagram**](WorkflowInstancesApi.md#get_workflow_instance_diagram) | **GET** /workflowInstances/{workflowInstanceId}/diagram | Returns the file representing the diagram of workflow instance identified by the given ID.
[**message_event_received**](WorkflowInstancesApi.md#message_event_received) | **POST** /workflowInstances/{processInstanceId}/messageEvents/{messageName} | Pass message event to workflow engine.
[**start_workflow_instances**](WorkflowInstancesApi.md#start_workflow_instances) | **POST** /workflowInstances | Start workflow instances.
[**start_workflow_instances_in_job**](WorkflowInstancesApi.md#start_workflow_instances_in_job) | **POST** /workflowInstances/startJobs | Start workflow instances.

# **cancel_workflow_instances**
> cancel_workflow_instances(workflow_instance_id, body=body)

Cancel workflow instance.

Cancels the workflow instance with the specified ID with a reason. Canceling the workflow instance also cancels the workflow sub-processes.

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
api_instance = collibra_core.WorkflowInstancesApi(collibra_core.ApiClient(configuration))
workflow_instance_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The identifier of the workflow instance to be cancelled.
body = 'body_example' # str | The reason for the cancellation of the workflow instance. (optional)

try:
    # Cancel workflow instance.
    api_instance.cancel_workflow_instances(workflow_instance_id, body=body)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->cancel_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_instance_id** | [**str**](.md)| The identifier of the workflow instance to be cancelled. | 
 **body** | [**str**](str.md)| The reason for the cancellation of the workflow instance. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workflow_instances**
> PagedResponse find_workflow_instances(offset=offset, limit=limit, count_limit=count_limit, business_item_name=business_item_name, business_item_id=business_item_id, workflow_definition_id=workflow_definition_id, workflow_definition_name=workflow_definition_name, sort_field=sort_field, sort_order=sort_order, parent_workflow_instance_id=parent_workflow_instance_id)

Find workflow instances.

Returns workflow instances matching given search criteria.<p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned workflow instances satisfy all constraints that are specified in this search criteria.

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
api_instance = collibra_core.WorkflowInstancesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
business_item_name = 'business_item_name_example' # str | The display name of the business item that should be contained by the searched workflows. (optional)
business_item_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the business item that should be contained by the searched workflows. (optional)
workflow_definition_id = 'workflow_definition_id_example' # str | The ID of the workflow definition. (optional)
workflow_definition_name = 'workflow_definition_name_example' # str | The name (or a part of it) of the workflow definition. (optional)
sort_field = 'START_DATE' # str | The field on which the results are sorted. (optional) (default to START_DATE)
sort_order = 'DESC' # str | The sorting order. (optional) (default to DESC)
parent_workflow_instance_id = 'parent_workflow_instance_id_example' # str | The ID of the parent workflow instance. (optional)

try:
    # Find workflow instances.
    api_response = api_instance.find_workflow_instances(offset=offset, limit=limit, count_limit=count_limit, business_item_name=business_item_name, business_item_id=business_item_id, workflow_definition_id=workflow_definition_id, workflow_definition_name=workflow_definition_name, sort_field=sort_field, sort_order=sort_order, parent_workflow_instance_id=parent_workflow_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->find_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **business_item_name** | **str**| The display name of the business item that should be contained by the searched workflows. | [optional] 
 **business_item_id** | [**str**](.md)| The ID of the business item that should be contained by the searched workflows. | [optional] 
 **workflow_definition_id** | **str**| The ID of the workflow definition. | [optional] 
 **workflow_definition_name** | **str**| The name (or a part of it) of the workflow definition. | [optional] 
 **sort_field** | **str**| The field on which the results are sorted. | [optional] [default to START_DATE]
 **sort_order** | **str**| The sorting order. | [optional] [default to DESC]
 **parent_workflow_instance_id** | **str**| The ID of the parent workflow instance. | [optional] 

### Return type

[**PagedResponse**](PagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_instance_diagram**
> object get_workflow_instance_diagram(workflow_instance_id)

Returns the file representing the diagram of workflow instance identified by the given ID.

Returns the file representing the diagram of workflow instance identified by the given ID. The diagram input stream returned can be null as deployed workflow defintions without graphical notation included don't have a diagram

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
api_instance = collibra_core.WorkflowInstancesApi(collibra_core.ApiClient(configuration))
workflow_instance_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow instance to return the diagram for.

try:
    # Returns the file representing the diagram of workflow instance identified by the given ID.
    api_response = api_instance.get_workflow_instance_diagram(workflow_instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->get_workflow_instance_diagram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_instance_id** | [**str**](.md)| The ID of the workflow instance to return the diagram for. | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_event_received**
> message_event_received(process_instance_id, message_name, body=body)

Pass message event to workflow engine.

Passes the message event to the workflow engine. It will pass on this specific event to the engine with the given name, process instance and variables.

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
api_instance = collibra_core.WorkflowInstancesApi(collibra_core.ApiClient(configuration))
process_instance_id = 'process_instance_id_example' # str | The ID of an instance of a process. Given process instance should have only one execution running at the time. Otherwise this method will fail.
message_name = 'message_name_example' # str | The name of the message to trigger.
body = collibra_core.MessageEventReceivedRequest() # MessageEventReceivedRequest | The properties of the message event to be received. (optional)

try:
    # Pass message event to workflow engine.
    api_instance.message_event_received(process_instance_id, message_name, body=body)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->message_event_received: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_instance_id** | **str**| The ID of an instance of a process. Given process instance should have only one execution running at the time. Otherwise this method will fail. | 
 **message_name** | **str**| The name of the message to trigger. | 
 **body** | [**MessageEventReceivedRequest**](MessageEventReceivedRequest.md)| The properties of the message event to be received. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_workflow_instances**
> list[WorkflowInstance] start_workflow_instances(body=body)

Start workflow instances.

Starts multiple workflow instances based on the provided request.

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
api_instance = collibra_core.WorkflowInstancesApi(collibra_core.ApiClient(configuration))
body = collibra_core.StartWorkflowInstancesRequest() # StartWorkflowInstancesRequest | The properties of the workflow to be started. (optional)

try:
    # Start workflow instances.
    api_response = api_instance.start_workflow_instances(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->start_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StartWorkflowInstancesRequest**](StartWorkflowInstancesRequest.md)| The properties of the workflow to be started. | [optional] 

### Return type

[**list[WorkflowInstance]**](WorkflowInstance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_workflow_instances_in_job**
> Job start_workflow_instances_in_job(body=body)

Start workflow instances.

Starts multiple workflow instances asynchronously based on the provided request.

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
api_instance = collibra_core.WorkflowInstancesApi(collibra_core.ApiClient(configuration))
body = collibra_core.StartWorkflowInstancesRequest() # StartWorkflowInstancesRequest | Properties of the workflow to be started. (optional)

try:
    # Start workflow instances.
    api_response = api_instance.start_workflow_instances_in_job(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->start_workflow_instances_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StartWorkflowInstancesRequest**](StartWorkflowInstancesRequest.md)| Properties of the workflow to be started. | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

