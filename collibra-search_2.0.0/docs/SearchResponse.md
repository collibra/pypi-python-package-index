# SearchResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total number of resources matching the search criteria, ignoring pagination (&#x60;limit&#x60; and &#x60;offset&#x60;). | [optional] 
**results** | [**list[SearchResult]**](SearchResult.md) | The list of search results ordered as per the search request. | [optional] 
**aggregations** | [**list[SearchResponseAggregation]**](SearchResponseAggregation.md) | The aggregations performed on all the results matching the search criteria, ignoring pagination (&#x60;limit&#x60; and &#x60;offset&#x60;). Aggregations are only performed on the fields requested in the search request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

