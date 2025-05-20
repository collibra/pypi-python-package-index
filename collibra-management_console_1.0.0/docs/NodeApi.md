# collibra_management_console.NodeApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add1**](NodeApi.md#add1) | **POST** /node | Add a node
[**change2**](NodeApi.md#change2) | **PUT** /node/{nodeId} | Change an existing node
[**find_all3**](NodeApi.md#find_all3) | **GET** /node | List all nodes
[**get_by_id4**](NodeApi.md#get_by_id4) | **GET** /node/{nodeId} | Get a node by ID
[**remove3**](NodeApi.md#remove3) | **DELETE** /node/{nodeId} | Remove a node
[**status**](NodeApi.md#status) | **GET** /node/{nodeId}/status | Get the status of a node

# **add1**
> NodeModel add1(body=body)

Add a node

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeApi()
body = collibra_management_console.NodeModel() # NodeModel | The model of the node to add (optional)

try:
    # Add a node
    api_response = api_instance.add1(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->add1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeModel**](NodeModel.md)| The model of the node to add | [optional] 

### Return type

[**NodeModel**](NodeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change2**
> NodeModel change2(node_id, body=body)

Change an existing node

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target node
body = collibra_management_console.NodeModel() # NodeModel | The new model for the node to change (optional)

try:
    # Change an existing node
    api_response = api_instance.change2(node_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->change2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)| The ID of the target node | 
 **body** | [**NodeModel**](NodeModel.md)| The new model for the node to change | [optional] 

### Return type

[**NodeModel**](NodeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all3**
> list[NodeModel] find_all3()

List all nodes

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeApi()

try:
    # List all nodes
    api_response = api_instance.find_all3()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->find_all3: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NodeModel]**](NodeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id4**
> NodeModel get_by_id4(node_id)

Get a node by ID

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target node

try:
    # Get a node by ID
    api_response = api_instance.get_by_id4(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->get_by_id4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)| The ID of the target node | 

### Return type

[**NodeModel**](NodeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove3**
> remove3(node_id)

Remove a node

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target node

try:
    # Remove a node
    api_instance.remove3(node_id)
except ApiException as e:
    print("Exception when calling NodeApi->remove3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)| The ID of the target node | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> str status(node_id)

Get the status of a node

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target node

try:
    # Get the status of a node
    api_response = api_instance.status(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)| The ID of the target node | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

