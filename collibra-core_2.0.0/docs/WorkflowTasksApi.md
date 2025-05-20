# collibra_core.WorkflowTasksApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_workflow_task**](WorkflowTasksApi.md#cancel_workflow_task) | **POST** /workflowTasks/{workflowTaskId}/canceled | Cancel workflow task.
[**complete_workflow_tasks**](WorkflowTasksApi.md#complete_workflow_tasks) | **POST** /workflowTasks/completed | Complete workflow tasks.
[**find_workflow_tasks**](WorkflowTasksApi.md#find_workflow_tasks) | **GET** /workflowTasks | Find workflow tasks.
[**get_task_form_data**](WorkflowTasksApi.md#get_task_form_data) | **GET** /workflowTasks/{workflowTaskId}/taskFormData | Get task form data.
[**get_workflow_task**](WorkflowTasksApi.md#get_workflow_task) | **GET** /workflowTasks/{workflowTaskId} | Get workflow task.
[**reassign_task**](WorkflowTasksApi.md#reassign_task) | **POST** /workflowTasks/{workflowTaskId}/reassign | Reassign task.

# **cancel_workflow_task**
> cancel_workflow_task(workflow_task_id, body=body)

Cancel workflow task.

Cancels the workflow task with the specified ID with a reason. If the given workflow is a subprocess, this method makes sure everything is cancelled from the root process instance. If the given task is not found, this method will assume it already was cancelled without throwing any error.

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
api_instance = collibra_core.WorkflowTasksApi(collibra_core.ApiClient(configuration))
workflow_task_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow task.
body = 'body_example' # str | The reason for the cancellation of the workflow task. (optional)

try:
    # Cancel workflow task.
    api_instance.cancel_workflow_task(workflow_task_id, body=body)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->cancel_workflow_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_task_id** | [**str**](.md)| The ID of the workflow task. | 
 **body** | [**str**](str.md)| The reason for the cancellation of the workflow task. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_workflow_tasks**
> list[WorkflowTask] complete_workflow_tasks(body=body)

Complete workflow tasks.

Completes tasks based on the provided request and returns the following tasks, if the same user is assigned to them.

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
api_instance = collibra_core.WorkflowTasksApi(collibra_core.ApiClient(configuration))
body = collibra_core.CompleteWorkflowTasksRequest() # CompleteWorkflowTasksRequest | Request to complete the workflow tasks. (optional)

try:
    # Complete workflow tasks.
    api_response = api_instance.complete_workflow_tasks(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->complete_workflow_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompleteWorkflowTasksRequest**](CompleteWorkflowTasksRequest.md)| Request to complete the workflow tasks. | [optional] 

### Return type

[**list[WorkflowTask]**](WorkflowTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workflow_tasks**
> WorkflowTaskPagedResponse find_workflow_tasks(offset=offset, limit=limit, count_limit=count_limit, business_item_id=business_item_id, business_item_type=business_item_type, workflow_task_user_relation=workflow_task_user_relation, business_item_name=business_item_name, description=description, user_id=user_id, create_date=create_date, due_date=due_date, title=title, type=type, sort_field=sort_field, sort_order=sort_order)

Find workflow tasks.

Returns the workflow tasks matching given search criteria.

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
api_instance = collibra_core.WorkflowTasksApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
business_item_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the business item (optional)
business_item_type = 'business_item_type_example' # str | The type of the business item (optional)
workflow_task_user_relation = 'ALL' # str | The type of relation between user and searched tasks. This could be either set to search for all the tasks the user is permitted to view or just those assigned to the user. (optional) (default to ALL)
business_item_name = 'business_item_name_example' # str | The part of the name of the business item. (optional)
description = 'description_example' # str | The part of the task description. (optional)
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the user for which the tasks need to be returned. If empty, the current logged in user will be used (optional)
create_date = 789 # int | The creation date of the task. It is the timestamp (in UTC time standard) (optional)
due_date = 789 # int | The due date of the task. It is the timestamp (in UTC time standard) (optional)
title = 'title_example' # str | The title/name of the task. (optional)
type = 'type_example' # str | The task type. (optional)
sort_field = 'DUE_DATE' # str | The field on which the results are sorted. On due date by default. (optional) (default to DUE_DATE)
sort_order = 'DESC' # str | The sorting order. (optional) (default to DESC)

try:
    # Find workflow tasks.
    api_response = api_instance.find_workflow_tasks(offset=offset, limit=limit, count_limit=count_limit, business_item_id=business_item_id, business_item_type=business_item_type, workflow_task_user_relation=workflow_task_user_relation, business_item_name=business_item_name, description=description, user_id=user_id, create_date=create_date, due_date=due_date, title=title, type=type, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->find_workflow_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **business_item_id** | [**str**](.md)| The ID of the business item | [optional] 
 **business_item_type** | **str**| The type of the business item | [optional] 
 **workflow_task_user_relation** | **str**| The type of relation between user and searched tasks. This could be either set to search for all the tasks the user is permitted to view or just those assigned to the user. | [optional] [default to ALL]
 **business_item_name** | **str**| The part of the name of the business item. | [optional] 
 **description** | **str**| The part of the task description. | [optional] 
 **user_id** | [**str**](.md)| The ID of the user for which the tasks need to be returned. If empty, the current logged in user will be used | [optional] 
 **create_date** | **int**| The creation date of the task. It is the timestamp (in UTC time standard) | [optional] 
 **due_date** | **int**| The due date of the task. It is the timestamp (in UTC time standard) | [optional] 
 **title** | **str**| The title/name of the task. | [optional] 
 **type** | **str**| The task type. | [optional] 
 **sort_field** | **str**| The field on which the results are sorted. On due date by default. | [optional] [default to DUE_DATE]
 **sort_order** | **str**| The sorting order. | [optional] [default to DESC]

### Return type

[**WorkflowTaskPagedResponse**](WorkflowTaskPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_form_data**
> TaskFormData get_task_form_data(workflow_task_id, form_property_type=form_property_type)

Get task form data.

Returns the task form data of the workflow task with the specified ID and form property type.

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
api_instance = collibra_core.WorkflowTasksApi(collibra_core.ApiClient(configuration))
workflow_task_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Workflow task ID.
form_property_type = 'form_property_type_example' # str | Form property type. (optional)

try:
    # Get task form data.
    api_response = api_instance.get_task_form_data(workflow_task_id, form_property_type=form_property_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->get_task_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_task_id** | [**str**](.md)| Workflow task ID. | 
 **form_property_type** | **str**| Form property type. | [optional] 

### Return type

[**TaskFormData**](TaskFormData.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_task**
> WorkflowTask get_workflow_task(workflow_task_id)

Get workflow task.

Returns the workflow task with the specified ID. A task will only be returned when the user has the correct permission to view it.

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
api_instance = collibra_core.WorkflowTasksApi(collibra_core.ApiClient(configuration))
workflow_task_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow task to return.

try:
    # Get workflow task.
    api_response = api_instance.get_workflow_task(workflow_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->get_workflow_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_task_id** | [**str**](.md)| The ID of the workflow task to return. | 

### Return type

[**WorkflowTask**](WorkflowTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reassign_task**
> reassign_task(workflow_task_id, users=users, groups=groups, roles=roles, communities=communities)

Reassign task.

Reassigns the task with the specified ID to one or more users, groups or roles. Caller needs to provide at least one of the value list for users, groups or roles. If roles are provided then the same number of communities needs to be provided also.

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
api_instance = collibra_core.WorkflowTasksApi(collibra_core.ApiClient(configuration))
workflow_task_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow task.
users = ['users_example'] # list[str] | The user IDs to reassign to. (optional)
groups = ['groups_example'] # list[str] | The group IDs to reassign to. (optional)
roles = ['roles_example'] # list[str] | The role IDs to reassign to. (optional)
communities = ['communities_example'] # list[str] | The Community IDs of the specified roles to reassign to. (optional)

try:
    # Reassign task.
    api_instance.reassign_task(workflow_task_id, users=users, groups=groups, roles=roles, communities=communities)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->reassign_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_task_id** | [**str**](.md)| The ID of the workflow task. | 
 **users** | [**list[str]**](str.md)| The user IDs to reassign to. | [optional] 
 **groups** | [**list[str]**](str.md)| The group IDs to reassign to. | [optional] 
 **roles** | [**list[str]**](str.md)| The role IDs to reassign to. | [optional] 
 **communities** | [**list[str]**](str.md)| The Community IDs of the specified roles to reassign to. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

