# ComplexRelationLegTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | The minimum number of Leg Type occurrences. | [optional] 
**max** | **int** | The maximum number of Leg Type occurrences. | [optional] 
**role** | **str** | The name of the role that the source plays. | 
**co_role** | **str** | The name of the role that the target plays. | [optional] 
**asset_type_id** | **str** | The ID of the Asset Type of the Relation.&lt;br/&gt;In the next major release, this parameter will only be valid when adding a new leg to the ComplexRelationType. Changing the Asset Type of an existing leg won&#x27;t be allowed and will result in an error. | 
**id** | **str** | The id of the Complex Relation Leg Type. The Leg Type will be created with this id or updated.&lt;br/&gt;If left empty on update the Leg Type will be recreated. | [optional] 
**relation_type_id** | **str** | The id of Relation Type of the Leg Type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

