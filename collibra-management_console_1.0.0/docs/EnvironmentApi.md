# collibra_management_console.EnvironmentApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](EnvironmentApi.md#add) | **POST** /environment | Create a new environment
[**add_service**](EnvironmentApi.md#add_service) | **POST** /environment/{environmentId}/add/{managedServiceId} | Add a managed service to an environment
[**add_service_provider**](EnvironmentApi.md#add_service_provider) | **POST** /environment/{environmentId}/addServiceProvider/{serviceProviderId} | Add a service provider to an environment
[**change**](EnvironmentApi.md#change) | **PUT** /environment/{environmentId} | Change an existing environment
[**find_all1**](EnvironmentApi.md#find_all1) | **GET** /environment | List all environments
[**get_by_id2**](EnvironmentApi.md#get_by_id2) | **GET** /environment/{environmentId} | Get an environment by ID
[**remove2**](EnvironmentApi.md#remove2) | **DELETE** /environment/{environmentId} | Delete an environment
[**remove_service**](EnvironmentApi.md#remove_service) | **POST** /environment/{environmentId}/remove/{serviceProviderId} | Remove a service provider from an environment
[**start**](EnvironmentApi.md#start) | **POST** /environment/{environmentId}/start | Start an environment
[**stop**](EnvironmentApi.md#stop) | **POST** /environment/{environmentId}/stop | Stop an environment

# **add**
> EnvironmentModel add(body=body)

Create a new environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
body = collibra_management_console.EnvironmentModel() # EnvironmentModel | The model of the environment to create (optional)

try:
    # Create a new environment
    api_response = api_instance.add(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnvironmentModel**](EnvironmentModel.md)| The model of the environment to create | [optional] 

### Return type

[**EnvironmentModel**](EnvironmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service**
> EnvironmentModel add_service(environment_id, managed_service_id)

Add a managed service to an environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the managed service to add to the environment

try:
    # Add a managed service to an environment
    api_response = api_instance.add_service(environment_id, managed_service_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->add_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 
 **managed_service_id** | [**str**](.md)| The ID of the managed service to add to the environment | 

### Return type

[**EnvironmentModel**](EnvironmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_service_provider**
> EnvironmentModel add_service_provider(environment_id, service_provider_id)

Add a service provider to an environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the service provider to add to the environment

try:
    # Add a service provider to an environment
    api_response = api_instance.add_service_provider(environment_id, service_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->add_service_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 
 **service_provider_id** | [**str**](.md)| The ID of the service provider to add to the environment | 

### Return type

[**EnvironmentModel**](EnvironmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change**
> EnvironmentModel change(environment_id, body=body)

Change an existing environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment to change
body = collibra_management_console.EnvironmentModel() # EnvironmentModel | The new model for the environment to change (optional)

try:
    # Change an existing environment
    api_response = api_instance.change(environment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the environment to change | 
 **body** | [**EnvironmentModel**](EnvironmentModel.md)| The new model for the environment to change | [optional] 

### Return type

[**EnvironmentModel**](EnvironmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all1**
> find_all1()

List all environments

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()

try:
    # List all environments
    api_instance.find_all1()
except ApiException as e:
    print("Exception when calling EnvironmentApi->find_all1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id2**
> EnvironmentModel get_by_id2(environment_id)

Get an environment by ID

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment to retrieve

try:
    # Get an environment by ID
    api_response = api_instance.get_by_id2(environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->get_by_id2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the environment to retrieve | 

### Return type

[**EnvironmentModel**](EnvironmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove2**
> remove2(environment_id)

Delete an environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment to delete

try:
    # Delete an environment
    api_instance.remove2(environment_id)
except ApiException as e:
    print("Exception when calling EnvironmentApi->remove2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the environment to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_service**
> EnvironmentModel remove_service(environment_id, service_provider_id)

Remove a service provider from an environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target environment
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the service provider to remove from the environment

try:
    # Remove a service provider from an environment
    api_response = api_instance.remove_service(environment_id, service_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentApi->remove_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the target environment | 
 **service_provider_id** | [**str**](.md)| The ID of the service provider to remove from the environment | 

### Return type

[**EnvironmentModel**](EnvironmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(environment_id)

Start an environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment to start

try:
    # Start an environment
    api_instance.start(environment_id)
except ApiException as e:
    print("Exception when calling EnvironmentApi->start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the environment to start | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> stop(environment_id)

Stop an environment

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.EnvironmentApi()
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment to stop

try:
    # Stop an environment
    api_instance.stop(environment_id)
except ApiException as e:
    print("Exception when calling EnvironmentApi->stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | [**str**](.md)| The ID of the environment to stop | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

