# ChangeComplexRelationTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_id** | **str** | The new public id for the Complex Relation Type. It must be unique within all Asset Types, Complex Relation Types, Domain Types and Scopes. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. WARNING : The public id should only be changed with extreme caution, since it can break existing customizations. The only valid use case is to change it after creation of the type, if no public id was specified, and the generated proposal is not acceptable. | [optional] 
**name** | **str** | The new name for the Complex Relation Type. | [optional] 
**description** | **str** | The new description for the Complex Relation Type. | [optional] 
**color** | **str** | The color of the symbol, in a hex format e.g. &#x27;#000000&#x27;.  This format always includes the &#x27;#&#x27; and has a size of 7. | [optional] 
**symbol_type** | **str** | The new symbol type. | [optional] 
**icon_code** | **str** | The new icon code for the Complex Relation Type. | [optional] 
**acronym_code** | **str** | The new acronym code for the Complex Relation Type. | [optional] 
**attribute_types** | [**list[ComplexRelationAttributeTypeRequest]**](ComplexRelationAttributeTypeRequest.md) | The new list of attribute types for the Complex Relation Type. | [optional] 
**leg_types** | [**list[ComplexRelationLegTypeRequest]**](ComplexRelationLegTypeRequest.md) | The new list of leg types for the Complex Relation Type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

