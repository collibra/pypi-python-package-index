# ChangeProfilingConfigurationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiling_type** | **str** | - **full**: Select to profile and classify based on all synchronized metadata. - **sample**: Select to profile and classify based on a sample of the synchronized metadata.   When you select Partial scan, you can define the maximum number of rows that you want to use for profiling and classification (as *sampleSize*). By default, the maximum number of rows is 20000.  | [optional] 
**sample_size** | **int** | If *profilingType* is defined as *sample*, this attribute defines how many rows are used for profiling. The minimum value is 100. | [optional] 
**run_after_metadata_synchronization** | **bool** | If set to *true*, it will automatically create a data profile and classify columns every time the metadata synchronization process of one or more schemas finishes.  This may take a long time. You can also add a schedule to profile and classify at regular intervals.  | [optional] 
**exclude_types** | [**ExcludeTypes**](ExcludeTypes.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

