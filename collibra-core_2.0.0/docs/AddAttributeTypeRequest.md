# AddAttributeTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new Attribute Type. Should be unique within all Attribute Types.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**public_id** | **str** | The public id that will be assigned to the new Attribute Type. It must be unique within all Attribute Types. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. If no public id is provided, a valid public id will be generated. | [optional] 
**name** | **str** | The name of the new Attribute Type. Should be unique within all Attribute Types. | 
**description** | **str** | The description of the new Attribute Type. | [optional] 
**kind** | **str** | The kind of the new Attribute Type. | 
**language** | **str** | The language of the new Attribute Type. This property is only applicable to Attribute Types of kind \&quot;Script\&quot;. | [optional] 
**statistics_enabled** | **bool** | Whether statistics should be enabled. This property is only applicable to Attribute Types of kind \&quot;Numeric\&quot; or \&quot;Boolean\&quot;. | [optional] 
**allowed_values** | **list[str]** | List of allowed values. This property is only applicable to Attribute Types of kind \&quot;Single Value List\&quot; or \&quot;Multi Value List\&quot;. | [optional] 
**string_type** | **str** | Rich text or plain text This property is only applicable to Attribute Types of kind \&quot;String\&quot;. | [optional] 
**id_string** | **str** | The ID of the Attribute Type. This field will be removed in the future. | [optional] 
**is_integer** | **bool** | Whether Attribute Type holds an integer value. This property is only applicable to Attribute Types of kind \&quot;Numeric\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

