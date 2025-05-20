# collibra_catalog_database_registration.ProfilingApi

All URIs are relative to */rest/catalogDatabase/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_multiple_schema_profiling_configurations**](ProfilingApi.md#add_multiple_schema_profiling_configurations) | **POST** /schemaProfilingConfigurations/batch | Add multiple schema profiling configurations
[**add_profiling_configuration**](ProfilingApi.md#add_profiling_configuration) | **POST** /profilingConfigurations | Add profiling and classification configuration
[**add_schema_profiling_configuration**](ProfilingApi.md#add_schema_profiling_configuration) | **POST** /schemaProfilingConfigurations | Add schema profiling and classification configuration
[**change_schema_profiling_configuration**](ProfilingApi.md#change_schema_profiling_configuration) | **PATCH** /schemaProfilingConfigurations/{schemaProfilingConfigurationId} | Update schema profiling and classification configuration
[**delete_profiling_configuration**](ProfilingApi.md#delete_profiling_configuration) | **DELETE** /profilingConfigurations/{profilingConfigurationId} | Delete profiling and classification configuration
[**delete_schema_profiling_configuration**](ProfilingApi.md#delete_schema_profiling_configuration) | **DELETE** /schemaProfilingConfigurations/{schemaProfilingConfigurationId} | Delete schema profiling and classification configuration
[**find_profiling_configurations**](ProfilingApi.md#find_profiling_configurations) | **GET** /profilingConfigurations | List profiling and classification configurations
[**find_schema_profiling_configurations**](ProfilingApi.md#find_schema_profiling_configurations) | **GET** /schemaProfilingConfigurations | List schema profiling and classification configurations
[**get_profiling_configuration**](ProfilingApi.md#get_profiling_configuration) | **GET** /profilingConfigurations/{profilingConfigurationId} | Retrieve a profiling and classification configuration
[**get_schema_profiling_configuration**](ProfilingApi.md#get_schema_profiling_configuration) | **GET** /schemaProfilingConfigurations/{schemaProfilingConfigurationId} | Retrieve schema profiling and classification configuration
[**profile_database**](ProfilingApi.md#profile_database) | **POST** /databases/{databaseId}/profile | Profile and classify a Database asset
[**update_profiling_configuration**](ProfilingApi.md#update_profiling_configuration) | **PATCH** /profilingConfigurations/{profilingConfigurationId} | Update profiling and classification configuration

# **add_multiple_schema_profiling_configurations**
> SchemaProfilingConfigurations add_multiple_schema_profiling_configurations(body=body)

Add multiple schema profiling configurations

Add multiple schema profiling configurations.  This operation is executed in a single transaction, that creates all the configurations. In case the operation fails, none of the configurations are created. 

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
body = [collibra_catalog_database_registration.AddSchemaProfilingConfigurationRequest()] # list[AddSchemaProfilingConfigurationRequest] |  (optional)

try:
    # Add multiple schema profiling configurations
    api_response = api_instance.add_multiple_schema_profiling_configurations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->add_multiple_schema_profiling_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddSchemaProfilingConfigurationRequest]**](AddSchemaProfilingConfigurationRequest.md)|  | [optional] 

### Return type

[**SchemaProfilingConfigurations**](SchemaProfilingConfigurations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_profiling_configuration**
> ProfilingConfiguration add_profiling_configuration(body=body)

Add profiling and classification configuration

Creates a profiling and classification configuration for a specific Database asset. This profiling and classification configuration provides a *default* configuration that applies to all schemas in the Database asset. You can define only a single *default* profiling and classification configuration for a specific Database asset.   To define schema-specific profiling and classification configurations, use the */schemaProfilingConfigurations* endpoints. 

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
body = collibra_catalog_database_registration.AddProfilingConfigurationRequest() # AddProfilingConfigurationRequest |  (optional)

try:
    # Add profiling and classification configuration
    api_response = api_instance.add_profiling_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->add_profiling_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddProfilingConfigurationRequest**](AddProfilingConfigurationRequest.md)|  | [optional] 

### Return type

[**ProfilingConfiguration**](ProfilingConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_schema_profiling_configuration**
> SchemaProfilingConfiguration add_schema_profiling_configuration(body=body)

Add schema profiling and classification configuration

Creates a profiling and classification configuration for a specific schema.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
body = collibra_catalog_database_registration.AddSchemaProfilingConfigurationRequest() # AddSchemaProfilingConfigurationRequest |  (optional)

try:
    # Add schema profiling and classification configuration
    api_response = api_instance.add_schema_profiling_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->add_schema_profiling_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddSchemaProfilingConfigurationRequest**](AddSchemaProfilingConfigurationRequest.md)|  | [optional] 

### Return type

[**SchemaProfilingConfiguration**](SchemaProfilingConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_schema_profiling_configuration**
> SchemaProfilingConfiguration change_schema_profiling_configuration(schema_profiling_configuration_id, body=body)

Update schema profiling and classification configuration

Updates a specific profiling and classification configuration.  You can only update some attributes of the schema profiling and classification configuration via this API. The attributes that are not provided in the request are not modified. 

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
schema_profiling_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema profiling configuration.
body = collibra_catalog_database_registration.ChangeSchemaProfilingConfigurationRequest() # ChangeSchemaProfilingConfigurationRequest |  (optional)

try:
    # Update schema profiling and classification configuration
    api_response = api_instance.change_schema_profiling_configuration(schema_profiling_configuration_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->change_schema_profiling_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_profiling_configuration_id** | [**str**](.md)| The ID of the schema profiling configuration. | 
 **body** | [**ChangeSchemaProfilingConfigurationRequest**](ChangeSchemaProfilingConfigurationRequest.md)|  | [optional] 

### Return type

[**SchemaProfilingConfiguration**](SchemaProfilingConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profiling_configuration**
> delete_profiling_configuration(profiling_configuration_id)

Delete profiling and classification configuration

Deletes a profiling and classification configuration. 

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
profiling_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the profiling configuration.

try:
    # Delete profiling and classification configuration
    api_instance.delete_profiling_configuration(profiling_configuration_id)
except ApiException as e:
    print("Exception when calling ProfilingApi->delete_profiling_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profiling_configuration_id** | [**str**](.md)| The ID of the profiling configuration. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schema_profiling_configuration**
> delete_schema_profiling_configuration(schema_profiling_configuration_id)

Delete schema profiling and classification configuration

Deletes a schema profiling and classification configuration.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi()
schema_profiling_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema profiling configuration.

try:
    # Delete schema profiling and classification configuration
    api_instance.delete_schema_profiling_configuration(schema_profiling_configuration_id)
except ApiException as e:
    print("Exception when calling ProfilingApi->delete_schema_profiling_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_profiling_configuration_id** | [**str**](.md)| The ID of the schema profiling configuration. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_profiling_configurations**
> ProfilingConfigurationPagedResponse find_profiling_configurations(database_id=database_id, offset=offset, limit=limit)

List profiling and classification configurations

Returns the profiling and classification configurations defined for the given criteria.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
database_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Database asset. (optional)
offset = 0 # int | The index of the first result to retrieve.  If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.  (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve.  If not set, the default limit  (limit = <code>0</code>) will be used. The maximum value for this parameter is <code>500<code>.  (optional) (default to 0)

try:
    # List profiling and classification configurations
    api_response = api_instance.find_profiling_configurations(database_id=database_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->find_profiling_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | [**str**](.md)| The ID of the Database asset. | [optional] 
 **offset** | **int**| The index of the first result to retrieve.  If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;.  | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve.  If not set, the default limit  (limit &#x3D; &lt;code&gt;0&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;code&gt;.  | [optional] [default to 0]

### Return type

[**ProfilingConfigurationPagedResponse**](ProfilingConfigurationPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_schema_profiling_configurations**
> SchemaProfilingConfigurationPagedResponse find_schema_profiling_configurations(schema_connection_id=schema_connection_id, database_id=database_id, offset=offset, limit=limit)

List schema profiling and classification configurations

Returns the schema-specific profiling and classification configurations defined for the given criteria. You can apply a *filter* on the schema connection or database to return only the configurations defined for a given schema or database. 

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
schema_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema connection. (optional)
database_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Database asset. (optional)
offset = 0 # int | The index of the first result to retrieve.  If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.  (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve.  If not set, the default limit  (limit = <code>0</code>) will be used. The maximum value for this parameter is <code>500<code>.  (optional) (default to 0)

try:
    # List schema profiling and classification configurations
    api_response = api_instance.find_schema_profiling_configurations(schema_connection_id=schema_connection_id, database_id=database_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->find_schema_profiling_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_connection_id** | [**str**](.md)| The ID of the schema connection. | [optional] 
 **database_id** | [**str**](.md)| The ID of the Database asset. | [optional] 
 **offset** | **int**| The index of the first result to retrieve.  If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;.  | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve.  If not set, the default limit  (limit &#x3D; &lt;code&gt;0&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;code&gt;.  | [optional] [default to 0]

### Return type

[**SchemaProfilingConfigurationPagedResponse**](SchemaProfilingConfigurationPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profiling_configuration**
> ProfilingConfiguration get_profiling_configuration(profiling_configuration_id)

Retrieve a profiling and classification configuration

Returns a profiling and classification configuration. 

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
profiling_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the profiling configuration.

try:
    # Retrieve a profiling and classification configuration
    api_response = api_instance.get_profiling_configuration(profiling_configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->get_profiling_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profiling_configuration_id** | [**str**](.md)| The ID of the profiling configuration. | 

### Return type

[**ProfilingConfiguration**](ProfilingConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_profiling_configuration**
> SchemaProfilingConfiguration get_schema_profiling_configuration(schema_profiling_configuration_id)

Retrieve schema profiling and classification configuration

Returns a specific schema profiling and classification configuration.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
schema_profiling_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema profiling configuration.

try:
    # Retrieve schema profiling and classification configuration
    api_response = api_instance.get_schema_profiling_configuration(schema_profiling_configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->get_schema_profiling_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_profiling_configuration_id** | [**str**](.md)| The ID of the schema profiling configuration. | 

### Return type

[**SchemaProfilingConfiguration**](SchemaProfilingConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_database**
> Job profile_database(database_id)

Profile and classify a Database asset

Triggers the *profiling & classification job* for a specific Database asset.  This API executes the profiling and classification as an *asynchronous job* and returns the job id of the triggered job in the response. To monitor the status of a job, use the Jobs resource of the REST Core API: GET /jobs/{jobId}. 

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
database_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Database asset.

try:
    # Profile and classify a Database asset
    api_response = api_instance.profile_database(database_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->profile_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | [**str**](.md)| The ID of the Database asset. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profiling_configuration**
> ProfilingConfiguration update_profiling_configuration(profiling_configuration_id, body=body)

Update profiling and classification configuration

Updates a profiling and classification configuration. 

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_database_registration
from collibra_catalog_database_registration.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_database_registration.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_database_registration.ProfilingApi(collibra_catalog_database_registration.ApiClient(configuration))
profiling_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the profiling configuration.
body = collibra_catalog_database_registration.ChangeProfilingConfigurationRequest() # ChangeProfilingConfigurationRequest |  (optional)

try:
    # Update profiling and classification configuration
    api_response = api_instance.update_profiling_configuration(profiling_configuration_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfilingApi->update_profiling_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profiling_configuration_id** | [**str**](.md)| The ID of the profiling configuration. | 
 **body** | [**ChangeProfilingConfigurationRequest**](ChangeProfilingConfigurationRequest.md)|  | [optional] 

### Return type

[**ProfilingConfiguration**](ProfilingConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

