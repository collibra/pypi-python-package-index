# AddAssetTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The UUID that will be assigned to the new Asset Type. It should be unique within all Asset Types, and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**public_id** | **str** | The public id that will be assigned to the new Asset Type. It must be unique within all Asset Types, Complex Relation Types, Domain Types and Scopes. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. If no public id is provided, a valid public id will be generated. | [optional] 
**name** | **str** | The name of the new Asset Type. Should be unique within all Asset Types. | 
**description** | **str** | The description of the new Asset Type. | [optional] 
**color** | **str** | The color of the symbol in hex format. | [optional] 
**symbol_type** | **str** | The symbol type. | 
**icon_code** | **str** | The icon code, a code representing the icon that should be shown. | [optional] 
**acronym_code** | **str** | A code representing the acronym that should be shown. | [optional] 
**parent_id** | **str** | The ID of the parent for the new Asset Type. | [optional] 
**display_name_enabled** | **bool** | Whether the display name should be enabled for all Assets of the type being created. | 
**rating_enabled** | **bool** | Whether ratings should be enabled for all Assets of the type being created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

