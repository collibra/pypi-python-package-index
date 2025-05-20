# Assessment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the assessment. | 
**name** | **str** | The name of the assessment. | 
**asset** | [**Asset**](Asset.md) |  | [optional] 
**status** | [**AssessmentStatus**](AssessmentStatus.md) |  | 
**template** | [**Template**](Template.md) |  | 
**owner** | [**User**](User.md) |  | 
**assignees** | [**list[UserOrGroupAssignee]**](UserOrGroupAssignee.md) |  | 
**content** | [**list[QuestionAndAnswer]**](QuestionAndAnswer.md) | The set of questions and answers of the assessment. | 
**created_on** | **datetime** | The date and time of the assessment creation. | 
**created_by** | [**User**](User.md) |  | 
**last_modified_on** | **datetime** | The date and time of the assessment last update. | 
**last_modified_by** | [**User**](User.md) |  | 
**submitted_on** | **datetime** | The date and time of the assessment submission. | [optional] 
**submitted_by** | [**User**](User.md) |  | [optional] 
**assessment_review** | [**Asset**](Asset.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

