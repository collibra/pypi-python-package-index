# collibra_management_console.NodeConfigurationApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_jvm_configuration**](NodeConfigurationApi.md#get_node_jvm_configuration) | **GET** /node/configuration/jvm/{nodeId} | Get Node&#x27;s JVM configuration. Requires super role.
[**restore_default_node_jvm_configuration**](NodeConfigurationApi.md#restore_default_node_jvm_configuration) | **POST** /node/configuration/jvm/{nodeId}/restoreDefaults | Restore Node&#x27;s JVM configuration to default. Requires super role.
[**update_node_jvm_configuration**](NodeConfigurationApi.md#update_node_jvm_configuration) | **POST** /node/configuration/jvm/{nodeId} | Update Node&#x27;s JVM configuration. Requires super role.
[**update_node_jvm_with_json**](NodeConfigurationApi.md#update_node_jvm_with_json) | **POST** /node/configuration/jvm/{nodeId}/json | Update Node&#x27;s JVM configuration with JSON. Requires super role.

# **get_node_jvm_configuration**
> get_node_jvm_configuration(node_id)

Get Node's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeConfigurationApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get Node's JVM configuration. Requires super role.
    api_instance.get_node_jvm_configuration(node_id)
except ApiException as e:
    print("Exception when calling NodeConfigurationApi->get_node_jvm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_default_node_jvm_configuration**
> restore_default_node_jvm_configuration(node_id)

Restore Node's JVM configuration to default. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeConfigurationApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Restore Node's JVM configuration to default. Requires super role.
    api_instance.restore_default_node_jvm_configuration(node_id)
except ApiException as e:
    print("Exception when calling NodeConfigurationApi->restore_default_node_jvm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_jvm_configuration**
> update_node_jvm_configuration(node_id, body=body)

Update Node's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeConfigurationApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_management_console.JvmConfiguration() # JvmConfiguration |  (optional)

try:
    # Update Node's JVM configuration. Requires super role.
    api_instance.update_node_jvm_configuration(node_id, body=body)
except ApiException as e:
    print("Exception when calling NodeConfigurationApi->update_node_jvm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)|  | 
 **body** | [**JvmConfiguration**](JvmConfiguration.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_jvm_with_json**
> update_node_jvm_with_json(node_id, body=body)

Update Node's JVM configuration with JSON. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.NodeConfigurationApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Update Node's JVM configuration with JSON. Requires super role.
    api_instance.update_node_jvm_with_json(node_id, body=body)
except ApiException as e:
    print("Exception when calling NodeConfigurationApi->update_node_jvm_with_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

