# collibra_catalog_database_registration.MetadataApi

All URIs are relative to */rest/catalogDatabase/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_multiple_schema_metadata_configurations**](MetadataApi.md#add_multiple_schema_metadata_configurations) | **POST** /schemaMetadataConfigurations/batch | Add multiple schema metadata synchronization configurations
[**add_schema_metadata_configuration**](MetadataApi.md#add_schema_metadata_configuration) | **POST** /schemaMetadataConfigurations | Add a schema metadata synchronization configuration
[**change_schema_metadata_configuration**](MetadataApi.md#change_schema_metadata_configuration) | **PUT** /schemaMetadataConfigurations/{schemaMetadataConfigurationId} | Update schema metadata synchronization configuration
[**delete_schema_metadata_configuration**](MetadataApi.md#delete_schema_metadata_configuration) | **DELETE** /schemaMetadataConfigurations/{schemaMetadataConfigurationId} | Delete schema metadata synchronization configuration
[**find_schema_metadata_configurations**](MetadataApi.md#find_schema_metadata_configurations) | **GET** /schemaMetadataConfigurations | List schema metadata synchronization configurations
[**get_schema_metadata_configuration**](MetadataApi.md#get_schema_metadata_configuration) | **GET** /schemaMetadataConfigurations/{schemaMetadataConfigurationId} | Retrieve a schema metadata synchronization configuration
[**synchronize_database_metadata**](MetadataApi.md#synchronize_database_metadata) | **POST** /databases/{databaseId}/synchronizeMetadata | Synchronize metadata for a Database asset

# **add_multiple_schema_metadata_configurations**
> SchemaMetadataConfigurations add_multiple_schema_metadata_configurations(body=body)

Add multiple schema metadata synchronization configurations

Adds multiple schema metadata synchronization configurations.  This operation is executed in a single transaction, that creates all the configurations. In case the operation fails, none of the configurations are created. 

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
api_instance = collibra_catalog_database_registration.MetadataApi(collibra_catalog_database_registration.ApiClient(configuration))
body = [collibra_catalog_database_registration.AddSchemaMetadataConfigurationRequest()] # list[AddSchemaMetadataConfigurationRequest] |  (optional)

try:
    # Add multiple schema metadata synchronization configurations
    api_response = api_instance.add_multiple_schema_metadata_configurations(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->add_multiple_schema_metadata_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddSchemaMetadataConfigurationRequest]**](AddSchemaMetadataConfigurationRequest.md)|  | [optional] 

### Return type

[**SchemaMetadataConfigurations**](SchemaMetadataConfigurations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_schema_metadata_configuration**
> SchemaMetadataConfiguration add_schema_metadata_configuration(body=body)

Add a schema metadata synchronization configuration

Creates a schema metadata configuration.  Only a single configuration can be created for a single schema connection id. 

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
api_instance = collibra_catalog_database_registration.MetadataApi(collibra_catalog_database_registration.ApiClient(configuration))
body = collibra_catalog_database_registration.AddSchemaMetadataConfigurationRequest() # AddSchemaMetadataConfigurationRequest |  (optional)

try:
    # Add a schema metadata synchronization configuration
    api_response = api_instance.add_schema_metadata_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->add_schema_metadata_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddSchemaMetadataConfigurationRequest**](AddSchemaMetadataConfigurationRequest.md)|  | [optional] 

### Return type

[**SchemaMetadataConfiguration**](SchemaMetadataConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_schema_metadata_configuration**
> SchemaMetadataConfiguration change_schema_metadata_configuration(schema_metadata_configuration_id, body=body)

Update schema metadata synchronization configuration

Updates a schema metadata synchronization configuration. 

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
api_instance = collibra_catalog_database_registration.MetadataApi(collibra_catalog_database_registration.ApiClient(configuration))
schema_metadata_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema metadata configuration.
body = collibra_catalog_database_registration.ChangeSchemaMetadataConfigurationRequest() # ChangeSchemaMetadataConfigurationRequest |  (optional)

try:
    # Update schema metadata synchronization configuration
    api_response = api_instance.change_schema_metadata_configuration(schema_metadata_configuration_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->change_schema_metadata_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_metadata_configuration_id** | [**str**](.md)| The ID of the schema metadata configuration. | 
 **body** | [**ChangeSchemaMetadataConfigurationRequest**](ChangeSchemaMetadataConfigurationRequest.md)|  | [optional] 

### Return type

[**SchemaMetadataConfiguration**](SchemaMetadataConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schema_metadata_configuration**
> delete_schema_metadata_configuration(schema_metadata_configuration_id)

Delete schema metadata synchronization configuration

Deletes a given schema metadata synchronization configuration.

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
api_instance = collibra_catalog_database_registration.MetadataApi(collibra_catalog_database_registration.ApiClient(configuration))
schema_metadata_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema metadata configuration.

try:
    # Delete schema metadata synchronization configuration
    api_instance.delete_schema_metadata_configuration(schema_metadata_configuration_id)
except ApiException as e:
    print("Exception when calling MetadataApi->delete_schema_metadata_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_metadata_configuration_id** | [**str**](.md)| The ID of the schema metadata configuration. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_schema_metadata_configurations**
> SchemaMetadataConfigurationPagedResponse find_schema_metadata_configurations(schema_connection_id=schema_connection_id, offset=offset, limit=limit)

List schema metadata synchronization configurations

Returns the schema metadata configurations defined for the given criteria.

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
api_instance = collibra_catalog_database_registration.MetadataApi(collibra_catalog_database_registration.ApiClient(configuration))
schema_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema connection. (optional)
offset = 0 # int | The index of the first result to retrieve.  If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.  (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve.  If not set, the default limit  (limit = <code>0</code>) will be used. The maximum value for this parameter is <code>500<code>.  (optional) (default to 0)

try:
    # List schema metadata synchronization configurations
    api_response = api_instance.find_schema_metadata_configurations(schema_connection_id=schema_connection_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->find_schema_metadata_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_connection_id** | [**str**](.md)| The ID of the schema connection. | [optional] 
 **offset** | **int**| The index of the first result to retrieve.  If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;.  | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve.  If not set, the default limit  (limit &#x3D; &lt;code&gt;0&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;code&gt;.  | [optional] [default to 0]

### Return type

[**SchemaMetadataConfigurationPagedResponse**](SchemaMetadataConfigurationPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_metadata_configuration**
> SchemaMetadataConfiguration get_schema_metadata_configuration(schema_metadata_configuration_id)

Retrieve a schema metadata synchronization configuration

Returns the schema metadata configuration defined for the given criteria.

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
api_instance = collibra_catalog_database_registration.MetadataApi(collibra_catalog_database_registration.ApiClient(configuration))
schema_metadata_configuration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema metadata configuration.

try:
    # Retrieve a schema metadata synchronization configuration
    api_response = api_instance.get_schema_metadata_configuration(schema_metadata_configuration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_schema_metadata_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_metadata_configuration_id** | [**str**](.md)| The ID of the schema metadata configuration. | 

### Return type

[**SchemaMetadataConfiguration**](SchemaMetadataConfiguration.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_database_metadata**
> Job synchronize_database_metadata(database_id, body=body)

Synchronize metadata for a Database asset

Triggers the database synchronization job for a list of schema connections.  This API executes the metadata synchronization as an *asynchronous job* and returns the job ID of the triggered job in the response.  To monitor the status of a job, use the Jobs resource of the REST Core API: GET /jobs/{jobId}. 

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
api_instance = collibra_catalog_database_registration.MetadataApi(collibra_catalog_database_registration.ApiClient(configuration))
database_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Database asset.
body = collibra_catalog_database_registration.DatabaseMetadataSynchronizationRequest() # DatabaseMetadataSynchronizationRequest |  (optional)

try:
    # Synchronize metadata for a Database asset
    api_response = api_instance.synchronize_database_metadata(database_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->synchronize_database_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | [**str**](.md)| The ID of the Database asset. | 
 **body** | [**DatabaseMetadataSynchronizationRequest**](DatabaseMetadataSynchronizationRequest.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

