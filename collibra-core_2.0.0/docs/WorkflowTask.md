# WorkflowTask

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the represented object (entity). | 
**system** | **bool** | Whether this is a system resource or not. | [optional] 
**resource_type** | **str** | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]. | 
**workflow_definition** | [**WorkflowDefinitionReference**](WorkflowDefinitionReference.md) |  | [optional] 
**workflow_instance_id** | **str** | The UUID of the workflow instance. | [optional] 
**key** | **str** | The key. | [optional] 
**type** | **str** | The type. | [optional] 
**aggregation_key** | **str** | The key for aggregation purposes. | [optional] 
**priority** | **int** | The priority. | [optional] 
**owner** | **str** | The owner. | [optional] 
**candidate_users** | [**list[User]**](User.md) | The list of candidate users. | [optional] 
**create_time** | **int** | The create time. | [optional] 
**due_date** | **int** | The due date. | [optional] 
**cancelable** | **bool** | Whether this workflow task is cancelable or not. | [optional] 
**reassignable** | **bool** | Whether this workflow task is reassignable or not. | [optional] 
**form_required** | **bool** | Whether this task requires a form or not. | [optional] 
**form_key_available** | **bool** | Whether this task has form key available or not. | [optional] 
**contains_activity_stream** | **bool** | Whether this task contains an activity stream or not. | [optional] 
**in_error** | **bool** | Whether this task is in error or not. | [optional] 
**error_message** | **str** | The error message in case this task is in error. | [optional] 
**custom_buttons** | [**list[FormProperty]**](FormProperty.md) | The list of custom buttons. | [optional] 
**description** | **str** | The description of the workflow task. | [optional] 
**title** | **str** | The title of the task. | [optional] 
**business_item** | [**ResourceReference**](ResourceReference.md) |  | [optional] 
**business_item_reference** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

