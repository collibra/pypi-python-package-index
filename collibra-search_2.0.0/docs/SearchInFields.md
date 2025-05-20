# SearchInFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | The reference resource type for the filter, also known as resource category. You must also provide at least one field for each resource type. When you include more than one resource type, you must provide the same fields (if available) for all resource types.&lt;br /&gt; Possible values are &#x60;Asset&#x60;, &#x60;Domain&#x60;, &#x60;Community&#x60;, &#x60;User&#x60; and &#x60;UserGroup&#x60;.&lt;br /&gt; Use in conjunction with &#x60;fields&#x60;. | [optional] 
**fields** | **list[str]** | A list of fields for the reference resource type. Works in conjunction with &#x60;resourceType&#x60;.&lt;br /&gt; Possible values for &#x60;Asset&#x60; are  &#x60;name&#x60;, &#x60;displayName&#x60;, &#x60;comments&#x60;, &#x60;tags&#x60;, &#x60;dataClassification&#x60; and &#x60;attributes&#x60;. Note that &#x60;attributes&#x60; is a wildcard for all attribute types. To search in a specific attribute type, use the following notation: &#x60;resource_type:resource_uuid&#x60; where &#x60;resource_type&#x60; is the attribute resource type, such as &#x60;StringAttributeType&#x60; (or use the generic &#x60;attribute&#x60;) and &#x60;resource_uuid&#x60; is the UUID of the attribute type. &lt;br/&gt;Possible values for &#x60;Domain&#x60; and &#x60;Community&#x60; are &#x60;name&#x60; and &#x60;comments&#x60;.&lt;br /&gt; Possible values for &#x60;User&#x60; and &#x60;UserGroup&#x60; are &#x60;name&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

