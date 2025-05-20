# collibra_catalog_sampling.SamplesApi

All URIs are relative to */rest/catalogSampling/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_samples**](SamplesApi.md#read_samples) | **GET** /samples/{assetId} | Read sample data from the Collibra cloud repository or Edge cache
[**request_samples**](SamplesApi.md#request_samples) | **POST** /samples/{assetId}/request | Create a request to collect and cache sample data for an Edge data source

# **read_samples**
> ReadSamplesResponse read_samples(asset_id, column_limit=column_limit, column_offset=column_offset)

Read sample data from the Collibra cloud repository or Edge cache

Reads the available sample data from the Collibra cloud repository or Edge cache depending on how the data is collected.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_sampling
from collibra_catalog_sampling.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_sampling.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_sampling.SamplesApi(collibra_catalog_sampling.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Asset identifier
column_limit = 0 # int | The maximum number of columns to retrieve. If not set (columnLimit = <code>0</code>), the default column limit will be used. Maximum is set to 1500. (optional) (default to 0)
column_offset = 0 # int | The index of the fist column to retrieve. If not set (columnOffset = <code>0</code>), results will be retrieved starting from column <code>0</code>. (optional) (default to 0)

try:
    # Read sample data from the Collibra cloud repository or Edge cache
    api_response = api_instance.read_samples(asset_id, column_limit=column_limit, column_offset=column_offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesApi->read_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Asset identifier | 
 **column_limit** | **int**| The maximum number of columns to retrieve. If not set (columnLimit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default column limit will be used. Maximum is set to 1500. | [optional] [default to 0]
 **column_offset** | **int**| The index of the fist column to retrieve. If not set (columnOffset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from column &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]

### Return type

[**ReadSamplesResponse**](ReadSamplesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_samples**
> RequestSamplesResponse request_samples(asset_id)

Create a request to collect and cache sample data for an Edge data source

Creates a request to collect sample data from an Edge data source for the asset with the specified ID and temporarily makes it available in the Edge cache.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_sampling
from collibra_catalog_sampling.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_sampling.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_sampling.SamplesApi(collibra_catalog_sampling.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Asset identifier

try:
    # Create a request to collect and cache sample data for an Edge data source
    api_response = api_instance.request_samples(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamplesApi->request_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| Asset identifier | 

### Return type

[**RequestSamplesResponse**](RequestSamplesResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

