# AddDatabaseRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_connection_id** | **str** | The ID of the database connection. The name of a database connection becomes the name of Database asset.  | 
**community_id** | **str** | The ID of the parent community in which the initial domain and database asset will be created. | 
**parent_system_id** | **str** | The ID of the parent *System* asset. After registering a database, a relation of type *Technology Asset groups / is grouped by technology Asset* is created between the System asset and the Database asset. | 
**owner_ids** | **list[str]** | The IDs of the users that are assigned as the Owner of the automatically created domain containing the Database asset.  | 
**description** | **str** | A description of the database. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

