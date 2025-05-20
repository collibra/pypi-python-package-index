# SearchFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field** | **str** | The reference field for the filter. You must also provide at least a value for each reference field.&lt;br /&gt; Possible values are &#x60;community&#x60;, &#x60;domain&#x60;, &#x60;domainType&#x60;, &#x60;assetType&#x60;, &#x60;status&#x60;, &#x60;createdBy&#x60;, &#x60;lastModifiedOn&#x60;, &#x60;createdOn&#x60;, &#x60;tags&#x60;.&lt;br /&gt; Use in conjunction with &#x60;values&#x60;. | [optional] 
**values** | **list[str]** | A list of values for the reference field. You must provide at least one value for each reference filed.&lt;br /&gt; Works in conjunction with &#x60;filed&#x60;.&lt;br /&gt; &lt;br /&gt; Possible values for &#x60;community&#x60;, &#x60;domain&#x60;, &#x60;domainType&#x60;, &#x60;assetType&#x60;, &#x60;status&#x60; and &#x60;createdBy&#x60; are one or more UUIDs.&lt;br /&gt; &lt;br /&gt; Possible values for &#x60;lastModifiedOn&#x60; and &#x60;createdOn&#x60; are &#x60;LAST_24H&#x60;, &#x60;LAST_7D&#x60;, &#x60;LAST_30D&#x60;, &#x60;LAST_365D&#x60;, &#x60;OLDER_THAN_365D&#x60;.&lt;br /&gt; &lt;br /&gt; Possible values for &#x60;tags&#x60; are one or more string values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

