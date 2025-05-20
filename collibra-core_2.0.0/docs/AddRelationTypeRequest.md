# AddRelationTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new Relation Type. Should be unique within all Relation Types.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**public_id** | **str** | The public id that will be assigned to the new Relation Type. It must be unique within all Relation Types. It should contain only ASCII letters and digits. It must start with an uppercase ASCII character. It must end with \&quot;_C\&quot;. If no public id is provided, a valid public id will be generated. | [optional] 
**source_type_id** | **str** | The ID of the source type for the new Relation Type. | 
**role** | **str** | The name of the role that the source plays. | 
**target_type_id** | **str** | The ID of the source type for the new Relation Type. | 
**co_role** | **str** | The name of the role that the target plays. | 
**description** | **str** | The description of the Relation Type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

