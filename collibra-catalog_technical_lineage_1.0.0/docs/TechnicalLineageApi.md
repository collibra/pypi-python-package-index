# collibra_catalog_technical_lineage.TechnicalLineageApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_harvester**](TechnicalLineageApi.md#trigger_harvester) | **POST** /technicalLineage/harvester/{assetId} | Starts technical lineage harvester

# **trigger_harvester**
> trigger_harvester(asset_id)

Starts technical lineage harvester

Starts technical lineage harvester for database asset id provided in request.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_technical_lineage
from collibra_catalog_technical_lineage.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog_technical_lineage.TechnicalLineageApi()
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Starts technical lineage harvester
    api_instance.trigger_harvester(asset_id)
except ApiException as e:
    print("Exception when calling TechnicalLineageApi->trigger_harvester: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

