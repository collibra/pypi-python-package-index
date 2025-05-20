# ChangeCommunityRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the community to be changed. Silently ignored if the ID is provided as path parameter of the request. | 
**parent_id** | **str** | The ID of the new parent community for the community. | [optional] 
**name** | **str** | The new name for the community. | [optional] 
**description** | **str** | The new description for the community. | [optional] 
**remove_scope_overlap_on_move** | **bool** | Whether scopes assigned to domain community and its children should be removed on move if there are any inherited scopes in new parent community | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

