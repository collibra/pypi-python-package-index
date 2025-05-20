# collibra_management_console.JobserverConfigurationApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_jobserver_context_jvm_configuration**](JobserverConfigurationApi.md#get_jobserver_context_jvm_configuration) | **GET** /spark/configuration/contextJvm/{managedServiceId} | Get Jobserver&#x27;s Monitoring JVM configuration. Requires super role.
[**get_jobserver_jvm_configuration**](JobserverConfigurationApi.md#get_jobserver_jvm_configuration) | **GET** /spark/configuration/jvm/{managedServiceId} | Get Jobserver&#x27;s JVM configuration. Requires super role.
[**get_jobserver_server_configuration**](JobserverConfigurationApi.md#get_jobserver_server_configuration) | **GET** /spark/configuration/server/{managedServiceId} | Get Jobserver&#x27;s Server configuration. 
[**get_jobserver_server_configuration_definition**](JobserverConfigurationApi.md#get_jobserver_server_configuration_definition) | **GET** /spark/configuration/server/definition | Get Jobserver&#x27;s Server configuration definition. 
[**overwrite_jobserver_server_configuration**](JobserverConfigurationApi.md#overwrite_jobserver_server_configuration) | **POST** /spark/configuration/server/{managedServiceId} | Overwrite Jobserver&#x27;s JVM configuration. Requires super role.
[**restore_default_jobserver_context_jvm_configuration**](JobserverConfigurationApi.md#restore_default_jobserver_context_jvm_configuration) | **POST** /spark/configuration/contextJvm/{managedServiceId}/restoreDefaults | Restore Jobserver&#x27;s Monitoring JVM configuration to default. Requires super role.
[**restore_default_jobserver_jvm_configuration**](JobserverConfigurationApi.md#restore_default_jobserver_jvm_configuration) | **POST** /spark/configuration/jvm/{managedServiceId}/restoreDefaults | Restore Jobserver&#x27;s JVM configuration to default. Requires super role.
[**restore_default_jobserver_server_configuration**](JobserverConfigurationApi.md#restore_default_jobserver_server_configuration) | **POST** /spark/configuration/server/{managedServiceId}/restoreDefaults | Get Jobserver&#x27;s Server configuration. 
[**update_jobserver_context_jvm_configuration**](JobserverConfigurationApi.md#update_jobserver_context_jvm_configuration) | **POST** /spark/configuration/contextJvm/{managedServiceId} | Update Jobserver&#x27;s Monitoring JVM configuration. Requires super role.
[**update_jobserver_context_jvm_with_json**](JobserverConfigurationApi.md#update_jobserver_context_jvm_with_json) | **POST** /spark/configuration/contextJvm/{managedServiceId}/json | Update Jobserver&#x27;s Monitoring JVM configuration with JSON. Requires super role.
[**update_jobserver_jvm_configuration**](JobserverConfigurationApi.md#update_jobserver_jvm_configuration) | **POST** /spark/configuration/jvm/{managedServiceId} | Update Jobserver&#x27;s JVM configuration. Requires super role.
[**update_jobserver_jvm_with_json**](JobserverConfigurationApi.md#update_jobserver_jvm_with_json) | **POST** /spark/configuration/jvm/{managedServiceId}/json | Update Jobserver&#x27;s JVM configuration with JSON. Requires super role.
[**update_jobserver_server_configuration_with_json**](JobserverConfigurationApi.md#update_jobserver_server_configuration_with_json) | **POST** /spark/configuration/server/{managedServiceId}/json | Overwrite Jobserver&#x27;s JVM configuration. Requires super role.

# **get_jobserver_context_jvm_configuration**
> get_jobserver_context_jvm_configuration(managed_service_id)

Get Jobserver's Monitoring JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get Jobserver's Monitoring JVM configuration. Requires super role.
    api_instance.get_jobserver_context_jvm_configuration(managed_service_id)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->get_jobserver_context_jvm_configuration: %s\n" % e)
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

# **get_jobserver_jvm_configuration**
> get_jobserver_jvm_configuration(managed_service_id)

Get Jobserver's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get Jobserver's JVM configuration. Requires super role.
    api_instance.get_jobserver_jvm_configuration(managed_service_id)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->get_jobserver_jvm_configuration: %s\n" % e)
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

# **get_jobserver_server_configuration**
> get_jobserver_server_configuration(managed_service_id)

Get Jobserver's Server configuration. 

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get Jobserver's Server configuration. 
    api_instance.get_jobserver_server_configuration(managed_service_id)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->get_jobserver_server_configuration: %s\n" % e)
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

# **get_jobserver_server_configuration_definition**
> get_jobserver_server_configuration_definition()

Get Jobserver's Server configuration definition. 

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()

try:
    # Get Jobserver's Server configuration definition. 
    api_instance.get_jobserver_server_configuration_definition()
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->get_jobserver_server_configuration_definition: %s\n" % e)
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

# **overwrite_jobserver_server_configuration**
> overwrite_jobserver_server_configuration(managed_service_id, body=body)

Overwrite Jobserver's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_management_console.JobserverServerConfiguration() # JobserverServerConfiguration |  (optional)

try:
    # Overwrite Jobserver's JVM configuration. Requires super role.
    api_instance.overwrite_jobserver_server_configuration(managed_service_id, body=body)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->overwrite_jobserver_server_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed_service_id** | [**str**](.md)|  | 
 **body** | [**JobserverServerConfiguration**](JobserverServerConfiguration.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_default_jobserver_context_jvm_configuration**
> restore_default_jobserver_context_jvm_configuration(managed_service_id)

Restore Jobserver's Monitoring JVM configuration to default. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Restore Jobserver's Monitoring JVM configuration to default. Requires super role.
    api_instance.restore_default_jobserver_context_jvm_configuration(managed_service_id)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->restore_default_jobserver_context_jvm_configuration: %s\n" % e)
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

# **restore_default_jobserver_jvm_configuration**
> restore_default_jobserver_jvm_configuration(managed_service_id)

Restore Jobserver's JVM configuration to default. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Restore Jobserver's JVM configuration to default. Requires super role.
    api_instance.restore_default_jobserver_jvm_configuration(managed_service_id)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->restore_default_jobserver_jvm_configuration: %s\n" % e)
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

# **restore_default_jobserver_server_configuration**
> restore_default_jobserver_server_configuration(managed_service_id)

Get Jobserver's Server configuration. 

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Get Jobserver's Server configuration. 
    api_instance.restore_default_jobserver_server_configuration(managed_service_id)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->restore_default_jobserver_server_configuration: %s\n" % e)
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

# **update_jobserver_context_jvm_configuration**
> update_jobserver_context_jvm_configuration(managed_service_id, body=body)

Update Jobserver's Monitoring JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_management_console.JvmConfiguration() # JvmConfiguration |  (optional)

try:
    # Update Jobserver's Monitoring JVM configuration. Requires super role.
    api_instance.update_jobserver_context_jvm_configuration(managed_service_id, body=body)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->update_jobserver_context_jvm_configuration: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jobserver_context_jvm_with_json**
> update_jobserver_context_jvm_with_json(managed_service_id, body=body)

Update Jobserver's Monitoring JVM configuration with JSON. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Update Jobserver's Monitoring JVM configuration with JSON. Requires super role.
    api_instance.update_jobserver_context_jvm_with_json(managed_service_id, body=body)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->update_jobserver_context_jvm_with_json: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jobserver_jvm_configuration**
> update_jobserver_jvm_configuration(managed_service_id, body=body)

Update Jobserver's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_management_console.JvmConfiguration() # JvmConfiguration |  (optional)

try:
    # Update Jobserver's JVM configuration. Requires super role.
    api_instance.update_jobserver_jvm_configuration(managed_service_id, body=body)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->update_jobserver_jvm_configuration: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jobserver_jvm_with_json**
> update_jobserver_jvm_with_json(managed_service_id, body=body)

Update Jobserver's JVM configuration with JSON. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Update Jobserver's JVM configuration with JSON. Requires super role.
    api_instance.update_jobserver_jvm_with_json(managed_service_id, body=body)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->update_jobserver_jvm_with_json: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jobserver_server_configuration_with_json**
> update_jobserver_server_configuration_with_json(managed_service_id, body=body)

Overwrite Jobserver's JVM configuration. Requires super role.

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.JobserverConfigurationApi()
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Overwrite Jobserver's JVM configuration. Requires super role.
    api_instance.update_jobserver_server_configuration_with_json(managed_service_id, body=body)
except ApiException as e:
    print("Exception when calling JobserverConfigurationApi->update_jobserver_server_configuration_with_json: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

