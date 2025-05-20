# collibra_catalog_database_registration.DatabaseConnectionApi

All URIs are relative to */rest/catalogDatabase/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_database_connections**](DatabaseConnectionApi.md#find_database_connections) | **GET** /databaseConnections | List database connections
[**get_database_connection**](DatabaseConnectionApi.md#get_database_connection) | **GET** /databaseConnections/{databaseConnectionId} | Retrieve a database connection
[**refresh_database_connections**](DatabaseConnectionApi.md#refresh_database_connections) | **POST** /databaseConnections/refresh | Refresh database connections from the data source

# **find_database_connections**
> DatabaseConnectionPagedResponse find_database_connections(edge_connection_id=edge_connection_id, schema_connection_id=schema_connection_id, offset=offset, limit=limit)

List database connections

Returns a list of available database connections, which you can use to register Database assets.  This API only returns the connections that have already been synchronized with the catalog. If a specific database connection is missing, the */databaseConnections/refresh* API can be called to refresh the database connections available in the catalog with the data source. 

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
api_instance = collibra_catalog_database_registration.DatabaseConnectionApi(collibra_catalog_database_registration.ApiClient(configuration))
edge_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Edge connection. (optional)
schema_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the schema connection. (optional)
offset = 0 # int | The index of the first result to retrieve.  If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.  (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve.  If not set, the default limit  (limit = <code>0</code>) will be used. The maximum value for this parameter is <code>500<code>.  (optional) (default to 0)

try:
    # List database connections
    api_response = api_instance.find_database_connections(edge_connection_id=edge_connection_id, schema_connection_id=schema_connection_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseConnectionApi->find_database_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_connection_id** | [**str**](.md)| The ID of the Edge connection. | [optional] 
 **schema_connection_id** | [**str**](.md)| The ID of the schema connection. | [optional] 
 **offset** | **int**| The index of the first result to retrieve.  If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;.  | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve.  If not set, the default limit  (limit &#x3D; &lt;code&gt;0&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;code&gt;.  | [optional] [default to 0]

### Return type

[**DatabaseConnectionPagedResponse**](DatabaseConnectionPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_connection**
> DatabaseConnection get_database_connection(database_connection_id)

Retrieve a database connection

Returns a specific database schema connection.

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
api_instance = collibra_catalog_database_registration.DatabaseConnectionApi(collibra_catalog_database_registration.ApiClient(configuration))
database_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the database connection.

try:
    # Retrieve a database connection
    api_response = api_instance.get_database_connection(database_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseConnectionApi->get_database_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_connection_id** | [**str**](.md)| The ID of the database connection. | 

### Return type

[**DatabaseConnection**](DatabaseConnection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_database_connections**
> Job refresh_database_connections(edge_connection_id)

Refresh database connections from the data source

Retrieve the database connections linked to a specific Edge connection and create the new database connections in Catalog.  This is an *asynchronous API* since it needs to reach out to the data source via Edge to retrieve the list of available database connections, which can take some time. 

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
api_instance = collibra_catalog_database_registration.DatabaseConnectionApi(collibra_catalog_database_registration.ApiClient(configuration))
edge_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Edge connection.

try:
    # Refresh database connections from the data source
    api_response = api_instance.refresh_database_connections(edge_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseConnectionApi->refresh_database_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edge_connection_id** | [**str**](.md)| The ID of the Edge connection. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

