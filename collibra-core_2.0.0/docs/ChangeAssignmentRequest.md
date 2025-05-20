# ChangeAssignmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_ids** | **list[str]** | The list of IDs of the statuses | [optional] 
**characteristic_types** | [**list[CharacteristicTypeAssignmentReference]**](CharacteristicTypeAssignmentReference.md) | A list of references to characteristic types corresponding to the assignment.  When adding a &#x27;relationTypeDirection&#x27; for a CharacteristicTypeAssignmentReference, all characteristicTypes that reference a RelationType must have the direction set. | [optional] 
**articulation_rules** | [**list[ArticulationRuleRequest]**](ArticulationRuleRequest.md) | The articulation rule definitions | [optional] 
**validation_rule_ids** | **list[str]** | The list of IDs of the validation rules | [optional] 
**data_quality_rule_ids** | **list[str]** | The list of IDs of the data quality rules | [optional] 
**domain_type_ids** | **list[str]** | The list of IDs of the domain types | [optional] 
**default_status_id** | **str** | The ID of the default status for the asset type | [optional] 
**scope_id** | **str** | The ID of the scope the assignment corresponds to. The scopeId is ignored, and will be removed in the future. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

