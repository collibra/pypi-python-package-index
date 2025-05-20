# AddComplexRelationTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new Complex Relation Type. Should be unique within all Complex Relation Types.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**public_id** | **str** | The public id that will be assigned to the new Complex Relation Type. It must be unique within all Asset Types, Complex Relation Types, Domain Types and Scopes. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. If no public id is provided, a valid public id will be generated. | [optional] 
**name** | **str** | The name of the new Complex Relation Type. Should be unique within all Complex Relation Types. | 
**description** | **str** | The description of the new Complex Relation Type. | [optional] 
**color** | **str** | The color of the symbol, in a hex format e.g. &#x27;#000000&#x27;.  This format always includes the &#x27;#&#x27; and has a size of 7. | [optional] 
**symbol_type** | **str** | The symbol type. | 
**icon_code** | **str** | The icon code of the new Complex Relation Type. | [optional] 
**acronym_code** | **str** | The acronym code of the new Complex Relation Type. | [optional] 
**attribute_types** | [**list[ComplexRelationAttributeTypeRequest]**](ComplexRelationAttributeTypeRequest.md) | The list of attribute types for the new Complex Relation Type. | 
**leg_types** | [**list[ComplexRelationLegTypeRequest]**](ComplexRelationLegTypeRequest.md) | The list of leg types for the new Complex Relation Type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

