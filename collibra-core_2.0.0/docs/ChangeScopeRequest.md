# ChangeScopeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_id** | **str** | The new public id for the Scope. It must be unique within all Asset Types, Complex Relation Types, Domain Types and Scopes. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. WARNING : The public id should only be changed with extreme caution, since it can break existing customizations. The only valid use case is to change it after creation of the type, if no public id was specified, and the generated proposal is not acceptable. | [optional] 
**name** | **str** | The new name for the scope | [optional] 
**description** | **str** | The new description for the scope | [optional] 
**domain_ids** | **list[str]** | The new list of IDs of domains that should included in the scope | [optional] 
**community_ids** | **list[str]** | The new list of IDs of communities that should included in the scope | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

