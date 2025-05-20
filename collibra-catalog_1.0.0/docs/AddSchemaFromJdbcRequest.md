# AddSchemaFromJdbcRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_name** | **str** | The schema name | 
**jdbc_driver_id** | **str** | The UUID of the JdbcDriver to use to connect to a JDBC source for ingestion. | 
**properties** | **dict(str, str)** | The properties that will be passed to the JDBC driver to connect to the source. | 
**user** | **str** | The username for the connection. If the user is not requested, specify an empty String | 
**password** | **list[str]** | The password for the connection. It can be specified as array of char (more secure) or as a String | [optional] 
**jdbc_connection_string** | **str** | The connection string that will be used instead of the one from the JdbcDriver. | [optional] 
**description** | **str** | The description of the schema to be added. | [optional] 
**owner_id** | **str** | The id of the user who will be assigned as the owner of the produced domain. | 
**store_credentials** | **bool** | Specify if the credentials should be stored into the database. | [optional] 
**cron_expression** | **str** | The cron expression to enable the automatic refresh. If not set, it will delete the cron job if one was present.&lt;br /&gt;It requires storeCredential to be set to true.&lt;br /&gt;For the syntax, see http://www.quartz-scheduler.org/documentation/quartz-2.x/tutorials/crontrigger.html | [optional] 
**cron_time_zone** | **str** | The cron time zone. If a cron expression is set, a time zone is mandatory. | [optional] 
**extract_data_sample** | **bool** | Specify if sampleData should be extracted from the database. | [optional] 
**execute_profiling** | **bool** | Specify if profiling should be executed. | [optional] 
**detect_advanced_data_types** | **bool** | Specify if advanced data types should be detected. | [optional] 
**tables_to_skip** | **list[str]** | The list table names that shouldn&#x27;t be ingested. The names can contain * wildcards toskip multiple tables with similar names. | [optional] 
**job_server** | **str** | Specify the jobserver id where to submit the ingestion. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

