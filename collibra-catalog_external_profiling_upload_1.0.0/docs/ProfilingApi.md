# collibra_catalog_external_profiling_upload.ProfilingApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_columns_profiling_data**](ProfilingApi.md#update_columns_profiling_data) | **PATCH** /profiling/columns | Updates column profiles.

# **update_columns_profiling_data**
> DataProfilingResponse update_columns_profiling_data(body=body)

Updates column profiles.

A value is updated only if the relative property is supplied. In order to delete a value, its property must be set to null in the request.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_external_profiling_upload
from collibra_catalog_external_profiling_upload.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_external_profiling_upload.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_external_profiling_upload.ProfilingApi(collibra_catalog_external_profiling_upload.ApiClient(configuration))
body = collibra_catalog_external_profiling_upload.DataProfilingRequest() # DataProfilingRequest | The column profiles to update.
If a property is not set it's ignored (not updated)
If a property is set to null it's deleted.

A valid assetIdentifer contains one of the following combinations:
- id
- assetName, domainId
- communityName, assetName, domainName

Strings containing numeric value must use `.` as decimal separator. No thousands separator should be used. In scientific notation, an `E` should separate the mantissa from the exponent, with no other extra character. (optional)

try:
    # Updates column profiles.
    api_response = api_instance.update_columns_profiling_data(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->update_columns_profiling_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataProfilingRequest**](DataProfilingRequest.md)| The column profiles to update.
If a property is not set it&#x27;s ignored (not updated)
If a property is set to null it&#x27;s deleted.

A valid assetIdentifer contains one of the following combinations:
- id
- assetName, domainId
- communityName, assetName, domainName

Strings containing numeric value must use &#x60;.&#x60; as decimal separator. No thousands separator should be used. In scientific notation, an &#x60;E&#x60; should separate the mantissa from the exponent, with no other extra character. | [optional] 

### Return type

[**DataProfilingResponse**](DataProfilingResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

