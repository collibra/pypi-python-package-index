# ChangeAssetTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Asset Type to be changed. Silently ignored if the ID is provided as path parameter of the request. | 
**public_id** | **str** | The new public id for the Asset Type. It must be unique within all Asset Types, Complex Relation Types, Domain Types and Scopes. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. WARNING : The public id should only be changed with extreme caution, since it can break existing customizations. The only valid use case is to change it after creation of the type, if no public id was specified, and the generated proposal is not acceptable. | [optional] 
**name** | **str** | The new name for the Asset Type. | [optional] 
**description** | **str** | The new description for the Asset Type. | [optional] 
**parent_id** | **str** | The ID of the new parent for the Asset Type. | [optional] 
**color** | **str** | The color of the symbol, in a hex format e.g. &#x27;#000000&#x27;. This format always includes the &#x27;#&#x27; and has a size of 7. | [optional] 
**symbol_type** | **str** | The symbol type. | [optional] 
**icon_code** | **str** | The icon code, a code representing the icon that should be shown. | [optional] 
**acronym_code** | **str** | The acronym code, a code representing the acronym that should be shown. | [optional] 
**display_name_enabled** | **bool** | Whether display name should be enabled for all Assets of changed type. | [optional] 
**rating_enabled** | **bool** | Whether rating should be enabled for all Assets of given type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

