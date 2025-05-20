# AddDomainTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new Domain Type. Should be unique within all Domain Types.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**public_id** | **str** | The public id that will be assigned to the new Domain Type. It must be unique within all Domain Types. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. If no public id is provided, a valid public id will be generated. | [optional] 
**name** | **str** | The name of the new Domain Type. Should be unique within all Domain Types. | 
**description** | **str** | The description of the new Domain Type. | [optional] 
**parent_id** | **str** | The ID of the parent of the new Domain Type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

