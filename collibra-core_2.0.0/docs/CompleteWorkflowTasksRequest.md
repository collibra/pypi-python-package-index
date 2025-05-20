# CompleteWorkflowTasksRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_ids** | **list[str]** | The list of IDs for tasks that should be completed. | 
**form_properties** | **dict(str, str)** | The form properties for the workflow tasks to be completed. It allows users to complete workflow tasks using regular forms. This field&#x27;s value will be ignored if the taskFormProperties field is populated. This field will be removed. Please use the &#x27;taskFormProperties&#x27; field instead. | [optional] 
**task_form_properties** | **dict(str, object)** | The form properties for the workflow tasks to be completed. It allows users to complete workflow tasks using either regular forms or external json form definitions. | [optional] 
**guest_user_id** | **str** | The ID of the guest user. This field will be removed without a replacement. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

