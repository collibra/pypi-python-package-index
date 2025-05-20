# ConductAssessmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | [**BaseTemplate**](BaseTemplate.md) |  | 
**name** | **str** | The name of the assessment. | [optional] 
**asset** | [**BaseAsset**](BaseAsset.md) |  | [optional] 
**owner** | [**BaseUser**](BaseUser.md) |  | [optional] 
**assignees** | [**list[BaseUserOrGroupAssignee]**](BaseUserOrGroupAssignee.md) | The ID of the Collibra users or groups to be assigned as assignees. | [optional] 
**is_visible_to_everyone** | **bool** | Whether the assessment is visible to Everyone in Collibra? | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

