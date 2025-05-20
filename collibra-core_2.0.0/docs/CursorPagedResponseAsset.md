# CursorPagedResponseAsset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of results. -1 when cursor pagination is used. | [optional] 
**offset** | **int** | The offset for the results. -1 when cursor pagination is used. | [optional] 
**limit** | **int** | The maximum number of results to be returned. | [optional] 
**results** | [**list[AssetImpl]**](AssetImpl.md) | The list of results. | [optional] 
**next_cursor** | **str** | Cursor value to be passed in next request to retrieve next page of results. Not returned on last page or when offset pagination is used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

