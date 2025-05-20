# ChangeDomainTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Domain Type to be changed. Silently ignored if the ID is provided as path parameter of the request. | 
**public_id** | **str** | The new public id for the Domain Type. It must be unique within all Domain Types. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. WARNING : The public id should only be changed with extreme caution, since it can break existing customizations. The only valid use case is to change it after creation of the type, if no public id was specified, and the generated proposal is not acceptable. | [optional] 
**name** | **str** | The new name for the Domain Type. | [optional] 
**description** | **str** | The new description for the Domain Type. | [optional] 
**parent_id** | **str** | The ID of the new parent for the Domain Type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

