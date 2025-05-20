# AssetTypeImpl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the represented object (entity). | 
**created_by** | **str** | The id of the user that created this resource. | [optional] 
**created_on** | **int** | The timestamp (in UTC time standard) of the creation of this resource. | [optional] 
**last_modified_by** | **str** | The id of the user who modified this resource the last time. | [optional] 
**last_modified_on** | **int** | The timestamp (in UTC time standard) of the last modification of this resource. | [optional] 
**system** | **bool** | Whether this is a system resource or not. | [optional] 
**resource_type** | **str** | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]. | 
**name** | **str** | The name of the resource. | [optional] 
**description** | **str** | The description of the resource. | [optional] 
**public_id** | **str** | The public id of the asset type. | [optional] 
**parent** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 
**symbol_data** | [**SymbolDataImpl**](SymbolDataImpl.md) |  | [optional] 
**display_name_enabled** | **bool** |  | [optional] 
**rating_enabled** | **bool** |  | [optional] 
**final_type** | **bool** | Whether the ability to create child asset types and scoped assignments for this asset type is locked. | [optional] 
**lock_statuses** | **bool** | Whether the ability to add custom statuses to the assignments of this asset type is locked. | [optional] 
**product** | **str** | The product to which this asset type is linked. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

