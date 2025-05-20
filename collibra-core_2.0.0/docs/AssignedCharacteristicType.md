# AssignedCharacteristicType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_resource_type** | **str** | The type of the resource the characteristic refers to. The value can be one of : AttributeType, RelationType or ComplexRelationType | 
**minimum_occurrences** | **int** | How many times at least the assigned characteristic must be added to the resource. Zero means no restriction. | [optional] 
**maximum_occurrences** | **int** | How many times at least the assigned characteristic may be added to the resource. Null means no limit. | [optional] 
**assigned_resource_id** | **str** | The id of the resource the characteristic refers to. | [optional] 
**read_only** | **bool** | Whether the characteristic value of the assigned type can be edited by the user. | [optional] 
**system** | **bool** | Whether the characteristic type can be unassigned. | [optional] 
**id** | **str** | The id of the represented object (entity). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

