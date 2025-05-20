# ChangeAttributeTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Attribute Type to be changed. Silently ignored if the ID is provided as path parameter of the request. | 
**public_id** | **str** | The new public id for the Attribute Type. It must be unique within all Attribute Types. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. WARNING : The public id should only be changed with extreme caution, since it can break existing customizations. The only valid use case is to change it after creation of the type, if no public id was specified, and the generated proposal is not acceptable. | [optional] 
**name** | **str** | The new name for the Attribute Type. | [optional] 
**description** | **str** | The new description for the Attribute Type. | [optional] 
**language** | **str** | The new language for the Attribute Type. This property is only applicable to Attribute Types of kind \&quot;Script\&quot;, and specifies the language of the script. | [optional] 
**statistics_enabled** | **bool** | Whether statistics should be enabled. This property is only applicable to Attribute Types of kind \&quot;Numeric\&quot; or \&quot;Boolean\&quot;. | [optional] 
**is_integer** | **bool** | Whether Attribute Type holds integer value. This property is only applicable to Attribute Types of kind \&quot;Numeric\&quot;. | [optional] 
**allowed_values** | **list[str]** | List of allowed values. This property is only applicable to Attribute Types of kind \&quot;Single Value List\&quot; or \&quot;Multi Value List\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

