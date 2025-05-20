# collibra_core.DiagramPicturesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_diagram_picture**](DiagramPicturesApi.md#add_diagram_picture) | **POST** /diagramPictures | Adds a diagram picture.

# **add_diagram_picture**
> str add_diagram_picture(body=body)

Adds a diagram picture.

Take a diagram picture for a given asset and diagram view. A diagram picture is a copy of traceability diagram (result diagram) at a given time (for more information on traceability diagram check DGC User Guide).  The motivation behind diagram picture is to be able to reopen them at a later point in time and be able to see them them exactly as they were created. This feature is not possible for result diagram which are always showing the current situation.

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
api_instance = collibra_core.DiagramPicturesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddDiagramPictureRequest() # AddDiagramPictureRequest |  (optional)

try:
    # Adds a diagram picture.
    api_response = api_instance.add_diagram_picture(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramPicturesApi->add_diagram_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDiagramPictureRequest**](AddDiagramPictureRequest.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

