# SearchAggregation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The reference field for aggregation. Distinct values of the field are counted in the search results, ignoring pagination, and the top most common are presented in the response.&lt;br /&gt; Possible values are &#x60;rootCommunity&#x60;, &#x60;resourceType&#x60;, &#x60;assetType&#x60;, &#x60;domainType&#x60;, &#x60;status&#x60;, &#x60;lastModifiedOn&#x60;, &#x60;createdOn&#x60;, &#x60;createdBy&#x60; and &#x60;tags&#x60;. | [optional] 
**limit** | **int** | Optional limit for the number of top aggregated results to return. If not set, the default limit of &#x60;10&#x60; is used.&lt;br /&gt; The maximum possible value is 1000. | [optional] [default to 10]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

