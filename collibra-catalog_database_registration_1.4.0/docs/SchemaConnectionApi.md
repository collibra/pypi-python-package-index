# collibra_catalog_database_registration.SchemaConnectionApi

All URIs are relative to */rest/catalogDatabase/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_schema_connections**](SchemaConnectionApi.md#find_schema_connections) | **GET** /schemaConnections | List schema connections
[**get_schema_connection**](SchemaConnectionApi.md#get_schema_connection) | **GET** /schemaConnections/{schemaConnectionId} | Retrieve a schema connection
[**refresh_schema_connections**](SchemaConnectionApi.md#refresh_schema_connections) | **POST** /schemaConnections/refresh | Refresh schema connections from the data source

# **find_schema_connections**
> SchemaConnectionPagedResponse find_schema_connections(database_connection_id=database_connection_id, schema_id=schema_id, offset=offset, limit=limit)

List schema connections

Returns a list of available schema connections, which you can use to define metadata synchronization configurations for schemas.  This API only returns the connections that have already been synchronized with the catalog. If a specific schema connection is missing, you can call the */schemaConnections/refresh* API to synchronize the schema connections available in Catalog with the data source. 

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
api_instance = collibra_catalog_database_registration.SchemaConnectionApi(collibra_catalog_database_registration.ApiClient(configuration))
database_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the database connection. (optional)
schema_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Schema asset. (optional)
offset = 0 # int | The index of the first result to retrieve.  If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.  (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve.  If not set, the default limit  (limit = <code>0</code>) will be used. The maximum value for this parameter is <code>500<code>.  (optional) (default to 0)

try:
    # List schema connections
    api_response = api_instance.find_schema_connections(database_connection_id=database_connection_id, schema_id=schema_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaConnectionApi->find_schema_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_connection_id** | [**str**](.md)| The ID of the database connection. | [optional] 
 **schema_id** | [**str**](.md)| The ID of the Schema asset. | [optional] 
 **offset** | **int**| The index of the first result to retrieve.  If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;.  | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve.  If not set, the default limit  (limit &#x3D; &lt;code&gt;0&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;code&gt;.  | [optional] [default to 0]

### Return type

[**SchemaConnectionPagedResponse**](SchemaConnectionPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema_connection**
> SchemaConnection get_schema_connection(schema_connection_id)

Retrieve a schema connection

Returns a specific schema connection.

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
api_instance = collibra_catalog_database_registration.SchemaConnectionApi(collibra_catalog_database_registration.ApiClient(configuration))
schema_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema connection.

try:
    # Retrieve a schema connection
    api_response = api_instance.get_schema_connection(schema_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaConnectionApi->get_schema_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_connection_id** | [**str**](.md)| The ID of the schema connection. | 

### Return type

[**SchemaConnection**](SchemaConnection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_schema_connections**
> Job refresh_schema_connections(database_connection_id)

Refresh schema connections from the data source

Refresh the schema connections for a given database connection.  This is an *asynchronous API* since it needs to reach out to the data source via Edge to retrieve the list of available schema connections , which can take some time. 

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
api_instance = collibra_catalog_database_registration.SchemaConnectionApi(collibra_catalog_database_registration.ApiClient(configuration))
database_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the database connection.

try:
    # Refresh schema connections from the data source
    api_response = api_instance.refresh_schema_connections(database_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaConnectionApi->refresh_schema_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_connection_id** | [**str**](.md)| The ID of the database connection. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

