# collibra_protect_api_partner.SynchronizationsApi

All URIs are relative to */rest/protect/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_synchronization_by_data_source**](SynchronizationsApi.md#get_synchronization_by_data_source) | **GET** /synchronizations/byDataSource | Returns the details of the synchronization for the provided data source.

# **get_synchronization_by_data_source**
> Synchronization get_synchronization_by_data_source(data_source)

Returns the details of the synchronization for the provided data source.

### Example
```python
from __future__ import print_function
import time
import collibra_protect_api_partner
from collibra_protect_api_partner.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect_api_partner.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect_api_partner.SynchronizationsApi(collibra_protect_api_partner.ApiClient(configuration))
data_source = 'data_source_example' # str | Name of the data source

try:
    # Returns the details of the synchronization for the provided data source.
    api_response = api_instance.get_synchronization_by_data_source(data_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SynchronizationsApi->get_synchronization_by_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source** | **str**| Name of the data source | 

### Return type

[**Synchronization**](Synchronization.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

