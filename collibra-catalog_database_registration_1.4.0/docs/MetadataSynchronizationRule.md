# MetadataSynchronizationRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **str** | A comma-separated list of the names of the tables you want to synchronize. You can use &#x27;*&#x27; as a wildcard. If no value is defined, all the tables are included by default.  | [optional] [default to '*']
**exclude** | **str** | A comma-separated list of the names of the tables you do not want to synchronize. You can use this table rule to do the following:   1. Synchronize all tables in a schema except the ones defined in the Exclude field.   2. Synchronize only tables as defined in the Include field, with the exception of tables that are listed      in the Exclude field.  | [optional] [default to '']
**target_domain_id** | **str** | The ID of a target domain in which the assets are created. If no domain is specified the assets are created in the automatically created domain for that schema.  | [optional] 
**skip_views** | **bool** | A property to exclude database views from the synchronization process. If true, no assets of the type Database View are created.  | [optional] [default to False]
**register_source_tags** | **bool** | A property to register source tags when it is supported by the driver.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

