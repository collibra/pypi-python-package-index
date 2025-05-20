# collibra_management_console.ConsoleConfigurationApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](ConsoleConfigurationApi.md#get_configuration) | **GET** /console/configuration | Get the console configuration.
[**get_console_jvm_configuration**](ConsoleConfigurationApi.md#get_console_jvm_configuration) | **GET** /console/configuration/jvm | Get Console&#x27;s JVM configuration. Requires super role.
[**restore_defaults**](ConsoleConfigurationApi.md#restore_defaults) | **POST** /console/configuration/jvm/restoreDefaults | Restore Console&#x27;s JVM configuration to default. Requires super role.
[**update_console_jvm_configuration**](ConsoleConfigurationApi.md#update_console_jvm_configuration) | **POST** /console/configuration/jvm | Update Console&#x27;s JVM configuration. Requires super role.
[**update_console_jvm_with_json**](ConsoleConfigurationApi.md#update_console_jvm_with_json) | **POST** /console/configuration/jvm/json | Update Console&#x27;s JVM configuration with JSON. Requires super role.

# **get_configuration**
> get_configuration()

Get the console configuration.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleConfigurationApi()

try:
    # Get the console configuration.
    api_instance.get_configuration()
except ApiException as e:
    print("Exception when calling ConsoleConfigurationApi->get_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_console_jvm_configuration**
> get_console_jvm_configuration()

Get Console's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleConfigurationApi()

try:
    # Get Console's JVM configuration. Requires super role.
    api_instance.get_console_jvm_configuration()
except ApiException as e:
    print("Exception when calling ConsoleConfigurationApi->get_console_jvm_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_defaults**
> restore_defaults()

Restore Console's JVM configuration to default. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleConfigurationApi()

try:
    # Restore Console's JVM configuration to default. Requires super role.
    api_instance.restore_defaults()
except ApiException as e:
    print("Exception when calling ConsoleConfigurationApi->restore_defaults: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_console_jvm_configuration**
> update_console_jvm_configuration(body=body)

Update Console's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleConfigurationApi()
body = collibra_management_console.JvmConfiguration() # JvmConfiguration |  (optional)

try:
    # Update Console's JVM configuration. Requires super role.
    api_instance.update_console_jvm_configuration(body=body)
except ApiException as e:
    print("Exception when calling ConsoleConfigurationApi->update_console_jvm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JvmConfiguration**](JvmConfiguration.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_console_jvm_with_json**
> update_console_jvm_with_json(body=body)

Update Console's JVM configuration with JSON. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ConsoleConfigurationApi()
body = 'body_example' # str |  (optional)

try:
    # Update Console's JVM configuration with JSON. Requires super role.
    api_instance.update_console_jvm_with_json(body=body)
except ApiException as e:
    print("Exception when calling ConsoleConfigurationApi->update_console_jvm_with_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

