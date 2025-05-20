# collibra_catalog_classification.ClassificationProcessApi

All URIs are relative to */rest/catalogClassification/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_classification_process**](ClassificationProcessApi.md#start_classification_process) | **POST** /classify | Starts a process that classifies requested assets.

# **start_classification_process**
> ClassificationProcessResponse start_classification_process(body=body)

Starts a process that classifies requested assets.

API to start a process of classification.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_classification
from collibra_catalog_classification.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_classification.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_classification.ClassificationProcessApi(collibra_catalog_classification.ApiClient(configuration))
body = collibra_catalog_classification.ClassificationProcessRequest() # ClassificationProcessRequest |  (optional)

try:
    # Starts a process that classifies requested assets.
    api_response = api_instance.start_classification_process(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationProcessApi->start_classification_process: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClassificationProcessRequest**](ClassificationProcessRequest.md)|  | [optional] 

### Return type

[**ClassificationProcessResponse**](ClassificationProcessResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

