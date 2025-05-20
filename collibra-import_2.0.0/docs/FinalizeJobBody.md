# FinalizeJobBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send_notification** | **bool** | Whether job status notification should be sent. &lt;b&gt;The default value&lt;/b&gt; is &lt;code&gt;false&lt;/code&gt;. | [optional] [default to False]
**batch_size** | **int** | &lt;i&gt;The batchSize parameter is now deprecated and is ignored during command execution.&lt;/i&gt; | [optional] [default to 1000]
**simulation** | **bool** | Whether the import should be triggered as a simulation. &lt;b&gt;The default value&lt;/b&gt; is &lt;code&gt;false&lt;/code&gt;.&lt;p&gt;If &lt;code&gt;true&lt;/code&gt;, the result of the import simulation will be available at the end of the job but no change will be applied to the DGC. | [optional] [default to False]
**save_result** | **bool** | Whether the import Result should be persisted or forgotten. &lt;b&gt;The default value&lt;/b&gt; is &lt;code&gt;false&lt;/code&gt;.&lt;p&gt;If &lt;code&gt;true&lt;/code&gt;, the result of the import simulation will be available at the end of the job but no change will be applied to the DGC.&lt;p&gt;&lt;b&gt;DEPRECATED:&lt;/b&gt;This parameter is deprecated and will be removed in the future.&lt;/b&gt;. | [optional] [default to False]
**finalization_strategy** | **str** | The synchronization finalization strategy used in the clean up action. This determines whether to remove, ignore or change the status of assets that no longer exist in the external system.&lt;br /&gt;Possible values are &#x60;REMOVE_RESOURCES&#x60;, &#x60;CHANGE_STATUS&#x60; and &#x60;IGNORE&#x60;.&lt;br /&gt;When you select &#x60;CHANGE_STATUS&#x60;, you must also provide a value for &#x60;missingAssetStatusId&#x60;. | [optional] [default to 'REMOVE_RESOURCES']
**missing_asset_status_id** | **str** | If &lt;b&gt;finalizationStrategy&lt;/b&gt; is set to &#x60;CHANGE_STATUS&#x60; then this parameter determines the new status ID for assets that no longer exist in the external system. | [optional] 
**finalization_parameters** | **dict(str, str)** | If you have set &#x60;finalizationStrategy&#x60; to &#x60;CHANGE_STATUS&#x60;, the status ID for the assets that no longer exist in the external system.&lt;p&gt;&lt;b&gt;NOTE:&lt;/b&gt; This parameter must be declared with an &#x27;application/json&#x27; content type.&lt;p&gt;&lt;b&gt;DEPRECATED:&lt;/b&gt; This parameter is deprecated and will be removed in the future. Please, use &lt;/b&gt;missingAssetStatusId&lt;/b&gt;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

