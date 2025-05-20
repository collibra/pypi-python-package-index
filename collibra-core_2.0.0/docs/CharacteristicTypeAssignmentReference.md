# CharacteristicTypeAssignmentReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the reference. | 
**min** | **int** | The minimum allowed. | [optional] 
**max** | **int** | The maximum allowed, unlimited when null. | [optional] 
**type** | **str** | The resource type. | 
**relation_type_direction** | **str** | The relation type direction, if the referenced resource is a relation type; otherwise null. | [optional] 
**relation_type_restriction** | **str** | The relation type restriction of the target Asset Type, if the referenced resource is a relation type; otherwise null. When specified, it effectively replaces the source asset type of the relation when relationTypeDirection &#x3D; TO_SOURCE or the target asset type of the relation when relationTypeDirection &#x3D; TO_TARGET.You can specify the relation type restriction only when relationTypeDirection is not null. If specified, it must be an ID of a subtype of the source or target asset type, depending on the value of relationTypeDirection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

