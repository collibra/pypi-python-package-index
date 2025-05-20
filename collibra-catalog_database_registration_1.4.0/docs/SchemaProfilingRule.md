# SchemaProfilingRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiling_type** | **str** | - **full**: Select to profile and classify based on all synchronized metadata. - **sample**: Select to profile and classify based on a sample of the synchronized metadata.   When you select Partial scan, you can define the maximum number of rows that you want to use for profiling and classification (as *sampleSize*). By default, the maximum number of rows is 20000.  | [default to 'sample']
**sample_size** | [**SampleSize**](SampleSize.md) |  | [optional] 
**include** | **str** | A comma-separated list of the table names you want to profile. You can use &#x60;*&#x60; as a wildcard. If not defined, all the tables are included by default.  | [optional] [default to '*']
**exclude** | **str** | A comma-separated list of table names to be excluded during profiling. You can use &#x60;*&#x60; as a wildcard. If not defined, no table will be excluded and all tables defined in &#x60;include&#x60; will be profiled.  You can use this table rule to:  1. Profile all tables in a schema except the ones defined in the &#x60;exclude&#x60; field.  2. Profile only tables as defined in the &#x60;include&#x60; field, with the exception of tables that are listed    in the &#x60;exclude&#x60; field.  | [optional] [default to '']
**exclude_types** | [**ExcludeTypes**](ExcludeTypes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

