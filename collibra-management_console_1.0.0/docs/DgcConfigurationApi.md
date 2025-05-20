# collibra_management_console.DgcConfigurationApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_server_configuration1**](DgcConfigurationApi.md#get_application_server_configuration1) | **GET** /dgc/configuration/applicationServer/{nodeId} | Get DGC&#x27;s Application Server configuration.
[**get_jvm_configuration**](DgcConfigurationApi.md#get_jvm_configuration) | **GET** /dgc/configuration/jvm/{managedServiceId} | Get DGC&#x27;s JVM configuration. Requires super role.
[**restore_default_application_server_configuration1**](DgcConfigurationApi.md#restore_default_application_server_configuration1) | **POST** /dgc/configuration/applicationServer/{nodeId}/restoreDefaults | Restore DGC&#x27;s Application Server configuration to default. Requires super role.
[**restore_default_jvm_configuration**](DgcConfigurationApi.md#restore_default_jvm_configuration) | **POST** /dgc/configuration/jvm/{managedServiceId}/restoreDefaults | Restore DGC&#x27;s JVM configuration to default
[**update_application_server_configuration1**](DgcConfigurationApi.md#update_application_server_configuration1) | **POST** /dgc/configuration/applicationServer/{nodeId} | Update DGC&#x27;s Application Server configuration.
[**update_application_server_configuration_with_json1**](DgcConfigurationApi.md#update_application_server_configuration_with_json1) | **POST** /dgc/configuration/applicationServer/{nodeId}/json | Update DGC&#x27;s Application Server configuration with JSON.
[**update_jvm_configuration**](DgcConfigurationApi.md#update_jvm_configuration) | **POST** /dgc/configuration/jvm/{managedServiceId} | Update DGC&#x27;s JVM configuration. Requires super role.
[**update_jvm_configuration_with_json**](DgcConfigurationApi.md#update_jvm_configuration_with_json) | **POST** /dgc/configuration/jvm/{managedServiceId}/json | Update DGC&#x27;s JVM configuration with JSON. Requires super role.

# **get_application_server_configuration1**
> ApplicationServerConfiguration get_application_server_configuration1(node_id)

Get DGC's Application Server configuration.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcConfigurationApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get DGC's Application Server configuration.
    api_response = api_instance.get_application_server_configuration1(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgcConfigurationApi->get_application_server_configuration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)|  | 

### Return type

[**ApplicationServerConfiguration**](ApplicationServerConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jvm_configuration**
> get_jvm_configuration(managed_service_id)

Get DGC's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get DGC's JVM configuration. Requires super role.
    api_instance.get_jvm_configuration(managed_service_id)
except ApiException as e:
    print("Exception when calling DgcConfigurationApi->get_jvm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_default_application_server_configuration1**
> ApplicationServerConfiguration restore_default_application_server_configuration1(node_id)

Restore DGC's Application Server configuration to default. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcConfigurationApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Restore DGC's Application Server configuration to default. Requires super role.
    api_response = api_instance.restore_default_application_server_configuration1(node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgcConfigurationApi->restore_default_application_server_configuration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)|  | 

### Return type

[**ApplicationServerConfiguration**](ApplicationServerConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_default_jvm_configuration**
> restore_default_jvm_configuration(managed_service_id)

Restore DGC's JVM configuration to default

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Restore DGC's JVM configuration to default
    api_instance.restore_default_jvm_configuration(managed_service_id)
except ApiException as e:
    print("Exception when calling DgcConfigurationApi->restore_default_jvm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_server_configuration1**
> ApplicationServerConfiguration update_application_server_configuration1(node_id, body=body)

Update DGC's Application Server configuration.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcConfigurationApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_management_console.ApplicationServerConfiguration() # ApplicationServerConfiguration |  (optional)

try:
    # Update DGC's Application Server configuration.
    api_response = api_instance.update_application_server_configuration1(node_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgcConfigurationApi->update_application_server_configuration1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)|  | 
 **body** | [**ApplicationServerConfiguration**](ApplicationServerConfiguration.md)|  | [optional] 

### Return type

[**ApplicationServerConfiguration**](ApplicationServerConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_application_server_configuration_with_json1**
> ApplicationServerConfiguration update_application_server_configuration_with_json1(node_id, body=body)

Update DGC's Application Server configuration with JSON.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcConfigurationApi()
node_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Update DGC's Application Server configuration with JSON.
    api_response = api_instance.update_application_server_configuration_with_json1(node_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DgcConfigurationApi->update_application_server_configuration_with_json1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | [**str**](.md)|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

[**ApplicationServerConfiguration**](ApplicationServerConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jvm_configuration**
> update_jvm_configuration(managed_service_id, body=body)

Update DGC's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_management_console.JvmConfiguration() # JvmConfiguration |  (optional)

try:
    # Update DGC's JVM configuration. Requires super role.
    api_instance.update_jvm_configuration(managed_service_id, body=body)
except ApiException as e:
    print("Exception when calling DgcConfigurationApi->update_jvm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)|  | 
 **body** | [**JvmConfiguration**](JvmConfiguration.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jvm_configuration_with_json**
> update_jvm_configuration_with_json(managed_service_id, body=body)

Update DGC's JVM configuration with JSON. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.DgcConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Update DGC's JVM configuration with JSON. Requires super role.
    api_instance.update_jvm_configuration_with_json(managed_service_id, body=body)
except ApiException as e:
    print("Exception when calling DgcConfigurationApi->update_jvm_configuration_with_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

