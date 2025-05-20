# collibra_core.ReportingApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_insights_zip**](ReportingApi.md#get_insights_zip) | **GET** /reporting/insights/download | Reporting insights download
[**get_pre_signed_insights_zip**](ReportingApi.md#get_pre_signed_insights_zip) | **GET** /reporting/insights/directDownload | Reporting insights download directly from cloud storage

# **get_insights_zip**
> str get_insights_zip(snapshot_date=snapshot_date, format=format)

Reporting insights download

Returns a Reporting Data archive (zip) file that contains Apache Parquet files with table content for each of the seven concepts (community, domain, asset, attribute, relation, responsibility and usage) for one day (=snapshot date). Please refer to the Reporting Data Layer product documentation for more information at [Working with your reporting data](https://productresources.collibra.com/docs/collibra/latest/Content/Reporting/co_working-with-data.htm).<br />Collibra Insights Data Access provides data that may be subject to access restrictions within your organization. Please ensure you follow your organization's policies and have approval to access this data.<br />This operation is deprecated and it will be removed in the future.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ReportingApi(collibra_core.ApiClient(configuration))
snapshot_date = 'snapshot_date_example' # str | Snapshot date for reporting insights data in ISO8601 format (e.g.: 2019-05-14) (optional)
format = 'zip' # str | Archive format. Currently only ZIP format is accepted (optional) (default to zip)

try:
    # Reporting insights download
    api_response = api_instance.get_insights_zip(snapshot_date=snapshot_date, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportingApi->get_insights_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_date** | **str**| Snapshot date for reporting insights data in ISO8601 format (e.g.: 2019-05-14) | [optional] 
 **format** | **str**| Archive format. Currently only ZIP format is accepted | [optional] [default to zip]

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pre_signed_insights_zip**
> get_pre_signed_insights_zip(snapshot_date=snapshot_date, format=format)

Reporting insights download directly from cloud storage

Returns a Reporting Data archive (zip) file that contains Apache Parquet files with table content for each of the seven concepts (community, domain, asset, attribute, relation, responsibility and usage) for one day (=snapshot date). Please refer to the Reporting Data Layer product documentation for more information at [Working with your reporting data](https://productresources.collibra.com/docs/collibra/latest/Content/Reporting/co_working-with-data.htm).<br />Collibra Insights Data Access provides data that may be subject to access restrictions within your organization. Please ensure you follow your organization's policies and have approval to access this data.<br />This endpoint redirects to download the Reporting Data archive (zip) file directly from cloud storage, bypassing the Collibra network. The redirect URL is temporary, valid for 60 seconds by default (see “pre-signed URL” in AWS and GCP docs for more details). You will need to allow redirects for this endpoint to work correctly.<br />Note: The \"Try it out\" button in the documentation UI might not work properly. To test this endpoint, please use curl with \"-L\" option to follow redirects. 

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ReportingApi(collibra_core.ApiClient(configuration))
snapshot_date = 'snapshot_date_example' # str | Snapshot date for reporting insights data in ISO8601 format (e.g.: 2019-05-14) (optional)
format = 'zip' # str | Archive format. Currently only ZIP format is accepted (optional) (default to zip)

try:
    # Reporting insights download directly from cloud storage
    api_instance.get_pre_signed_insights_zip(snapshot_date=snapshot_date, format=format)
except ApiException as e:
    print("Exception when calling ReportingApi->get_pre_signed_insights_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_date** | **str**| Snapshot date for reporting insights data in ISO8601 format (e.g.: 2019-05-14) | [optional] 
 **format** | **str**| Archive format. Currently only ZIP format is accepted | [optional] [default to zip]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

