# collibra_management_console.ServiceProviderApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_slave_to_repository_cluster**](ServiceProviderApi.md#add_slave_to_repository_cluster) | **POST** /serviceProvider/repositorycluster/{serviceProviderId}/addSlave/{managedServiceId} | Add a slave repository to a repository cluster
[**create_repository_cluster**](ServiceProviderApi.md#create_repository_cluster) | **POST** /serviceProvider/repositorycluster/create | Create a new repository cluster
[**find_all4**](ServiceProviderApi.md#find_all4) | **GET** /serviceProvider | List all service providers
[**get_by_id5**](ServiceProviderApi.md#get_by_id5) | **GET** /serviceProvider/{serviceProviderId} | Get a service provider by ID
[**remove4**](ServiceProviderApi.md#remove4) | **DELETE** /serviceProvider/{serviceProviderId} | Delete a service provider
[**remove_from_repository_cluster**](ServiceProviderApi.md#remove_from_repository_cluster) | **POST** /serviceProvider/repositorycluster/{serviceProviderId}/remove/{managedServiceId} | Remove a repository from the cluster
[**set_master_in_repository_cluster**](ServiceProviderApi.md#set_master_in_repository_cluster) | **POST** /serviceProvider/repositorycluster/{serviceProviderId}/setMaster/{managedServiceId} | Set the master repository of a repository cluster
[**start2**](ServiceProviderApi.md#start2) | **POST** /serviceProvider/serviceProvider/{serviceProviderId}/start | Start a service provider
[**stop2**](ServiceProviderApi.md#stop2) | **POST** /serviceProvider/serviceProvider/{serviceProviderId}/stop | Stop a service provider

# **add_slave_to_repository_cluster**
> add_slave_to_repository_cluster(service_provider_id, managed_service_id)

Add a slave repository to a repository cluster

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the target cluster
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the repository managed service

try:
    # Add a slave repository to a repository cluster
    api_instance.add_slave_to_repository_cluster(service_provider_id, managed_service_id)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->add_slave_to_repository_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider_id** | [**str**](.md)| The id of the target cluster | 
 **managed_service_id** | [**str**](.md)| The id of the repository managed service | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_cluster**
> ServiceProviderModel create_repository_cluster(body=body)

Create a new repository cluster

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()
body = 'body_example' # str | The name of the cluster to create (optional)

try:
    # Create a new repository cluster
    api_response = api_instance.create_repository_cluster(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->create_repository_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The name of the cluster to create | [optional] 

### Return type

[**ServiceProviderModel**](ServiceProviderModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all4**
> list[ServiceProviderModel] find_all4()

List all service providers

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()

try:
    # List all service providers
    api_response = api_instance.find_all4()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->find_all4: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ServiceProviderModel]**](ServiceProviderModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id5**
> ServiceProviderModel get_by_id5(service_provider_id)

Get a service provider by ID

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the service provider

try:
    # Get a service provider by ID
    api_response = api_instance.get_by_id5(service_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->get_by_id5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider_id** | [**str**](.md)| The ID of the service provider | 

### Return type

[**ServiceProviderModel**](ServiceProviderModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove4**
> remove4(service_provider_id)

Delete a service provider

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the service provider to delete

try:
    # Delete a service provider
    api_instance.remove4(service_provider_id)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->remove4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider_id** | [**str**](.md)| The id of the service provider to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_from_repository_cluster**
> remove_from_repository_cluster(service_provider_id, managed_service_id)

Remove a repository from the cluster

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the target cluster
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the repository managed service

try:
    # Remove a repository from the cluster
    api_instance.remove_from_repository_cluster(service_provider_id, managed_service_id)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->remove_from_repository_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider_id** | [**str**](.md)| The id of the target cluster | 
 **managed_service_id** | [**str**](.md)| The id of the repository managed service | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_master_in_repository_cluster**
> set_master_in_repository_cluster(service_provider_id, managed_service_id)

Set the master repository of a repository cluster

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the target cluster
managed_service_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the repository managed service

try:
    # Set the master repository of a repository cluster
    api_instance.set_master_in_repository_cluster(service_provider_id, managed_service_id)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->set_master_in_repository_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider_id** | [**str**](.md)| The id of the target cluster | 
 **managed_service_id** | [**str**](.md)| The id of the repository managed service | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start2**
> start2(service_provider_id)

Start a service provider

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the service provider to start

try:
    # Start a service provider
    api_instance.start2(service_provider_id)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->start2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider_id** | [**str**](.md)| The ID of the service provider to start | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop2**
> stop2(service_provider_id)

Stop a service provider

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.ServiceProviderApi()
service_provider_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the service provider to stop

try:
    # Stop a service provider
    api_instance.stop2(service_provider_id)
except ApiException as e:
    print("Exception when calling ServiceProviderApi->stop2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_provider_id** | [**str**](.md)| The ID of the service provider to stop | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

