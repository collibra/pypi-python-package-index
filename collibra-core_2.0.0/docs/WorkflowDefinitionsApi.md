# collibra_core.WorkflowDefinitionsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_type_assignment_rule**](WorkflowDefinitionsApi.md#add_asset_type_assignment_rule) | **POST** /workflowDefinitions/{workflowDefinitionId}/assetTypeAssignmentRules | Add asset type assignment rule.
[**add_domain_type_assignment_rule**](WorkflowDefinitionsApi.md#add_domain_type_assignment_rule) | **POST** /workflowDefinitions/{workflowDefinitionId}/domainTypeAssignmentRules | Add domain type assignment rule.
[**change_asset_type_assignment_rule**](WorkflowDefinitionsApi.md#change_asset_type_assignment_rule) | **PATCH** /workflowDefinitions/{workflowDefinitionId}/assetTypeAssignmentRules/{ruleId} | Change asset type assignment rule.
[**change_domain_type_assignment_rule**](WorkflowDefinitionsApi.md#change_domain_type_assignment_rule) | **PATCH** /workflowDefinitions/{workflowDefinitionId}/domainTypeAssignmentRules/{ruleId} | Change domain type assignment rule.
[**change_workflow_definition**](WorkflowDefinitionsApi.md#change_workflow_definition) | **PATCH** /workflowDefinitions/{workflowDefinitionId} | Change workflow definition.
[**deploy_workflow_definition**](WorkflowDefinitionsApi.md#deploy_workflow_definition) | **POST** /workflowDefinitions | Deploy workflow definition.
[**find_workflow_definitions**](WorkflowDefinitionsApi.md#find_workflow_definitions) | **GET** /workflowDefinitions | Find workflow definitions.
[**get_configuration_start_form_data**](WorkflowDefinitionsApi.md#get_configuration_start_form_data) | **GET** /workflowDefinitions/workflowDefinition/{workflowDefinitionId}/configurationStartFormData | Get configuration start form data.
[**get_possible_start_events**](WorkflowDefinitionsApi.md#get_possible_start_events) | **GET** /workflowDefinitions/startEvents | Get all possible workflow start events
[**get_start_form_data**](WorkflowDefinitionsApi.md#get_start_form_data) | **GET** /workflowDefinitions/workflowDefinition/{workflowDefinitionId}/startFormData | Get start form data.
[**get_workflow_definition**](WorkflowDefinitionsApi.md#get_workflow_definition) | **GET** /workflowDefinitions/{workflowDefinitionId} | Get workflow definition.
[**get_workflow_definition_by_process_id**](WorkflowDefinitionsApi.md#get_workflow_definition_by_process_id) | **GET** /workflowDefinitions/process/{processId} | Get workflow definition.
[**get_workflow_definition_diagram**](WorkflowDefinitionsApi.md#get_workflow_definition_diagram) | **GET** /workflowDefinitions/{workflowDefinitionId}/diagram | Get process diagram.
[**get_workflow_definition_xml**](WorkflowDefinitionsApi.md#get_workflow_definition_xml) | **GET** /workflowDefinitions/{workflowDefinitionId}/xml | Get XML of workflow definition.
[**remove_assignment_rule**](WorkflowDefinitionsApi.md#remove_assignment_rule) | **DELETE** /workflowDefinitions/{workflowDefinitionId}/assignmentRules/{ruleId} | Remove assignment rule.
[**remove_workflow_definition**](WorkflowDefinitionsApi.md#remove_workflow_definition) | **DELETE** /workflowDefinitions/{workflowDefinitionId} | Remove workflow definition.
[**remove_workflow_definitions_in_job**](WorkflowDefinitionsApi.md#remove_workflow_definitions_in_job) | **POST** /workflowDefinitions/removalJobs | Remove multiple workflow definitions.

# **add_asset_type_assignment_rule**
> AssetAssignmentRuleImpl add_asset_type_assignment_rule(workflow_definition_id, body=body)

Add asset type assignment rule.

Adds an asset type assignment rule to the workflow definition with the specified ID.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.
body = collibra_core.AddAssetTypeAssignmentRuleRequest() # AddAssetTypeAssignmentRuleRequest | The request describing assignment rule to be added. (optional)

try:
    # Add asset type assignment rule.
    api_response = api_instance.add_asset_type_assignment_rule(workflow_definition_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->add_asset_type_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 
 **body** | [**AddAssetTypeAssignmentRuleRequest**](AddAssetTypeAssignmentRuleRequest.md)| The request describing assignment rule to be added. | [optional] 

### Return type

[**AssetAssignmentRuleImpl**](AssetAssignmentRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_domain_type_assignment_rule**
> AssetAssignmentRuleImpl add_domain_type_assignment_rule(workflow_definition_id, body=body)

Add domain type assignment rule.

Adds a domain type assignment rule to the workflow definition with the specified ID.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.
body = collibra_core.AddDomainTypeAssignmentRuleRequest() # AddDomainTypeAssignmentRuleRequest | The request describing assignment rule to be added. (optional)

try:
    # Add domain type assignment rule.
    api_response = api_instance.add_domain_type_assignment_rule(workflow_definition_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->add_domain_type_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 
 **body** | [**AddDomainTypeAssignmentRuleRequest**](AddDomainTypeAssignmentRuleRequest.md)| The request describing assignment rule to be added. | [optional] 

### Return type

[**AssetAssignmentRuleImpl**](AssetAssignmentRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_asset_type_assignment_rule**
> AssetAssignmentRuleImpl change_asset_type_assignment_rule(workflow_definition_id, rule_id, body=body)

Change asset type assignment rule.

Modifies the asset type assignment rule with the specified ID of the workflow definition with the specified ID.<p>Only properties that are specified in this request and have not <code>null</code> values are updated.<p>All other properties are ignored.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the assignment rule to be changed.
body = collibra_core.ChangeAssetTypeAssignmentRuleRequest() # ChangeAssetTypeAssignmentRuleRequest | Parameters for the assignment rule to be changed. (optional)

try:
    # Change asset type assignment rule.
    api_response = api_instance.change_asset_type_assignment_rule(workflow_definition_id, rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->change_asset_type_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 
 **rule_id** | [**str**](.md)| The ID of the assignment rule to be changed. | 
 **body** | [**ChangeAssetTypeAssignmentRuleRequest**](ChangeAssetTypeAssignmentRuleRequest.md)| Parameters for the assignment rule to be changed. | [optional] 

### Return type

[**AssetAssignmentRuleImpl**](AssetAssignmentRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domain_type_assignment_rule**
> AssetAssignmentRuleImpl change_domain_type_assignment_rule(workflow_definition_id, rule_id, body=body)

Change domain type assignment rule.

Modifies the domain type assignment rule with the specified ID of the workflow definition with the specified ID.<p>Only properties that are specified in this request and have not <code>null</code> values are updated.<p>All other properties are ignored.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the assignment rule to be changed.
body = collibra_core.ChangeDomainTypeAssignmentRuleRequest() # ChangeDomainTypeAssignmentRuleRequest | Parameters for the assignment rule to be changed. (optional)

try:
    # Change domain type assignment rule.
    api_response = api_instance.change_domain_type_assignment_rule(workflow_definition_id, rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->change_domain_type_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 
 **rule_id** | [**str**](.md)| The ID of the assignment rule to be changed. | 
 **body** | [**ChangeDomainTypeAssignmentRuleRequest**](ChangeDomainTypeAssignmentRuleRequest.md)| Parameters for the assignment rule to be changed. | [optional] 

### Return type

[**AssetAssignmentRuleImpl**](AssetAssignmentRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_workflow_definition**
> WorkflowDefinitionImpl change_workflow_definition(workflow_definition_id, body=body)

Change workflow definition.

Modifies the workflow definition with the specified ID.<p>Only properties that are specified in this request and have not <code>null</code> values are updated.<p>All other properties are ignored.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.
body = collibra_core.ChangeWorkflowDefinitionRequest() # ChangeWorkflowDefinitionRequest | Parameters for the workflow definition to be changed. (optional)

try:
    # Change workflow definition.
    api_response = api_instance.change_workflow_definition(workflow_definition_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->change_workflow_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 
 **body** | [**ChangeWorkflowDefinitionRequest**](ChangeWorkflowDefinitionRequest.md)| Parameters for the workflow definition to be changed. | [optional] 

### Return type

[**WorkflowDefinitionImpl**](WorkflowDefinitionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_workflow_definition**
> WorkflowDefinitionImpl deploy_workflow_definition(file=file, file_name=file_name)

Deploy workflow definition.

Deploys workflow definition (the business process and resources) using the specified request.<p> The input stream can represent a single file(e.g: .bpmn20.xml or .bpmn) or an archive file (e.g: .zip or .bar). It is not allowed to deploy a resource containing more than one process definition.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)

try:
    # Deploy workflow definition.
    api_response = api_instance.deploy_workflow_definition(file=file, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->deploy_workflow_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 

### Return type

[**WorkflowDefinitionImpl**](WorkflowDefinitionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workflow_definitions**
> WorkflowDefinitionPagedResponse find_workflow_definitions(offset=offset, limit=limit, count_limit=count_limit, asset_id=asset_id, domain_id=domain_id, community_id=community_id, enabled=enabled, _global=_global, name=name, sort_order=sort_order, sort_field=sort_field, description=description, guardrails_validation_result=guardrails_validation_result)

Find workflow definitions.

Finds the workflow definitions matching the criteria described in the request object. By default, the result contains up to 1000 workflow definitions.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
asset_id = ['asset_id_example'] # list[str] | The list of the IDs of business items (assets) for which the workflow definitions should be found. (optional)
domain_id = ['domain_id_example'] # list[str] | The list of the IDs of business items (domains) for which the workflow definitions should be found. (optional)
community_id = ['community_id_example'] # list[str] | The list of the IDs of business items (communities) for which the workflow definitions should be found. (optional)
enabled = true # bool | Whether the found workflow definitions should be enabled. (optional)
_global = true # bool | Whether the found workflow definitions should be global. (optional)
name = 'name_example' # str | The name (could be partial) of the workflow definition to search for. (optional)
sort_order = 'ASC' # str | The sorting order. (optional) (default to ASC)
sort_field = 'NAME' # str | The field on which the results are sorted. (optional) (default to NAME)
description = 'description_example' # str | The description (could be partial) of the workflow definition to search for. (optional)
guardrails_validation_result = 'guardrails_validation_result_example' # str | The result of the guardrails validation of this workflow definition (optional)

try:
    # Find workflow definitions.
    api_response = api_instance.find_workflow_definitions(offset=offset, limit=limit, count_limit=count_limit, asset_id=asset_id, domain_id=domain_id, community_id=community_id, enabled=enabled, _global=_global, name=name, sort_order=sort_order, sort_field=sort_field, description=description, guardrails_validation_result=guardrails_validation_result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->find_workflow_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **asset_id** | [**list[str]**](str.md)| The list of the IDs of business items (assets) for which the workflow definitions should be found. | [optional] 
 **domain_id** | [**list[str]**](str.md)| The list of the IDs of business items (domains) for which the workflow definitions should be found. | [optional] 
 **community_id** | [**list[str]**](str.md)| The list of the IDs of business items (communities) for which the workflow definitions should be found. | [optional] 
 **enabled** | **bool**| Whether the found workflow definitions should be enabled. | [optional] 
 **_global** | **bool**| Whether the found workflow definitions should be global. | [optional] 
 **name** | **str**| The name (could be partial) of the workflow definition to search for. | [optional] 
 **sort_order** | **str**| The sorting order. | [optional] [default to ASC]
 **sort_field** | **str**| The field on which the results are sorted. | [optional] [default to NAME]
 **description** | **str**| The description (could be partial) of the workflow definition to search for. | [optional] 
 **guardrails_validation_result** | **str**| The result of the guardrails validation of this workflow definition | [optional] 

### Return type

[**WorkflowDefinitionPagedResponse**](WorkflowDefinitionPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_start_form_data**
> StartFormDataImpl get_configuration_start_form_data(workflow_definition_id, form_property_type=form_property_type)

Get configuration start form data.

Returns the task configuration start form data of the workflow definition with the specified ID.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition that should be used for the form data retrieval.
form_property_type = 'form_property_type_example' # str | The form type to be returned. (optional)

try:
    # Get configuration start form data.
    api_response = api_instance.get_configuration_start_form_data(workflow_definition_id, form_property_type=form_property_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->get_configuration_start_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition that should be used for the form data retrieval. | 
 **form_property_type** | **str**| The form type to be returned. | [optional] 

### Return type

[**StartFormDataImpl**](StartFormDataImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_possible_start_events**
> list[NamedDescribedWorkflowStartEventType] get_possible_start_events()

Get all possible workflow start events

Returns all possible workflow start events, including event name and description

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))

try:
    # Get all possible workflow start events
    api_response = api_instance.get_possible_start_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->get_possible_start_events: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NamedDescribedWorkflowStartEventType]**](NamedDescribedWorkflowStartEventType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_start_form_data**
> StartFormDataImpl get_start_form_data(workflow_definition_id, form_property_type=form_property_type)

Get start form data.

Returns the task start form data of the workflow definition with the specified ID.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition that should be used for the form data retrieval.
form_property_type = 'form_property_type_example' # str | The form type to be returned. (optional)

try:
    # Get start form data.
    api_response = api_instance.get_start_form_data(workflow_definition_id, form_property_type=form_property_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->get_start_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition that should be used for the form data retrieval. | 
 **form_property_type** | **str**| The form type to be returned. | [optional] 

### Return type

[**StartFormDataImpl**](StartFormDataImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_definition**
> WorkflowDefinitionImpl get_workflow_definition(workflow_definition_id)

Get workflow definition.

Returns the workflow definition with the specified ID.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.

try:
    # Get workflow definition.
    api_response = api_instance.get_workflow_definition(workflow_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->get_workflow_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 

### Return type

[**WorkflowDefinitionImpl**](WorkflowDefinitionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_definition_by_process_id**
> WorkflowDefinitionImpl get_workflow_definition_by_process_id(process_id)

Get workflow definition.

Returns the workflow definition with the specified process ID.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
process_id = 'process_id_example' # str | The process ID of the workflow definition.

try:
    # Get workflow definition.
    api_response = api_instance.get_workflow_definition_by_process_id(process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->get_workflow_definition_by_process_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| The process ID of the workflow definition. | 

### Return type

[**WorkflowDefinitionImpl**](WorkflowDefinitionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_definition_diagram**
> get_workflow_definition_diagram(workflow_definition_id)

Get process diagram.

Returns the process diagram of the workflow definition with the specified ID. The diagram input stream returned can be null as deployed workflow definitions without graphical notation included do not have a diagram.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.

try:
    # Get process diagram.
    api_instance.get_workflow_definition_diagram(workflow_definition_id)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->get_workflow_definition_diagram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_definition_xml**
> get_workflow_definition_xml(workflow_definition_id)

Get XML of workflow definition.

Returns the XML source of the workflow definition with the specified ID.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.

try:
    # Get XML of workflow definition.
    api_instance.get_workflow_definition_xml(workflow_definition_id)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->get_workflow_definition_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_assignment_rule**
> remove_assignment_rule(workflow_definition_id, rule_id)

Remove assignment rule.

Removes the assignment rule with the specified ID from the workflow definition with the specified ID.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the assignment rule.

try:
    # Remove assignment rule.
    api_instance.remove_assignment_rule(workflow_definition_id, rule_id)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->remove_assignment_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 
 **rule_id** | [**str**](.md)| The ID of the assignment rule. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workflow_definition**
> remove_workflow_definition(workflow_definition_id)

Remove workflow definition.

Removes the workflow definition with the specified ID. The workflow definition will be completely removed from the application, including any history.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
workflow_definition_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the workflow definition.

try:
    # Remove workflow definition.
    api_instance.remove_workflow_definition(workflow_definition_id)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->remove_workflow_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | [**str**](.md)| The ID of the workflow definition. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workflow_definitions_in_job**
> Job remove_workflow_definitions_in_job(body=body)

Remove multiple workflow definitions.

Removes multiple workflow definitions asynchronously. The workflow definition(s) will be completely removed from the application, including any history.

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
api_instance = collibra_core.WorkflowDefinitionsApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | The list of IDs of the workflow definitions to remove. (optional)

try:
    # Remove multiple workflow definitions.
    api_response = api_instance.remove_workflow_definitions_in_job(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->remove_workflow_definitions_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The list of IDs of the workflow definitions to remove. | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

