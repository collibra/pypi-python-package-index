# SearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **str** | The search term.&lt;br /&gt; The field is mandatory and cannot be empty. You can use optional wildcards and quotes. No asterisk \&quot;*\&quot; wildcard will be automatically added for REST calls. | [optional] 
**search_in_fields** | [**list[SearchInFields]**](SearchInFields.md) | Optional set of fields to search in. By default, the search is performed in all the supported fields. | [optional] 
**filters** | [**list[SearchFilter]**](SearchFilter.md) | Optional filters to apply to narrow down the search results. | [optional] 
**aggregations** | [**list[SearchAggregation]**](SearchAggregation.md) | Optional set of aggregations to perform. Only results that match the search criteria (including all filters) are aggregated. Aggregation counts ignore pagination settings (limit and offset). Aggregations can be used to visualize a faceted search on frontend-related applications. | [optional] 
**sort_field** | **str** | The reference field for sorting the results. | [optional] [default to 'RELEVANCE']
**sort_order** | **str** | The order in which the results are sorted. The default order when sorting by &#x60;NAME&#x60; is ascending (&#x60;ASC&#x60;). The default order when sorting by other fields is descending (&#x60;DESC&#x60;). | [optional] 
**highlights** | [**SearchHighlight**](SearchHighlight.md) |  | [optional] 
**limit** | **int** | The number of search results to present in the response. If set to &#x60;0&#x60;, only aggregations are performed. Negative values are not possible. If not set, the default limit is used. The maximum possible value is &#x60;1000&#x60;. In conjunction with &#x60;offset&#x60;, this field provides a method to paginate the results. The sum of &#x60;limit&#x60; and &#x60;offset&#x60; cannot exceed &#x60;10000&#x60;. | [optional] [default to 20]
**offset** | **int** | The number of first search results to skip in the response. Negative values are not possible. If not set or set to &#x60;0&#x60;, no results are skipped. In conjunction with &#x60;limit&#x60;, this field provides a method to paginate the results. The sum of &#x60;limit&#x60; and &#x60;offset&#x60; cannot exceed &#x60;10000&#x60;. | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

