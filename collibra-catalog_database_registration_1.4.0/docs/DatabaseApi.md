# collibra_catalog_database_registration.DatabaseApi

All URIs are relative to */rest/catalogDatabase/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_database**](DatabaseApi.md#add_database) | **POST** /databases | Create a Database asset
[**change_database**](DatabaseApi.md#change_database) | **PATCH** /databases/{databaseId} | Change a Database asset
[**find_databases**](DatabaseApi.md#find_databases) | **GET** /databases | Find Database assets
[**get_database**](DatabaseApi.md#get_database) | **GET** /databases/{databaseId} | Get a Database asset

# **add_database**
> Database add_database(body=body)

Create a Database asset

Creates a Database asset in a specific community, which then allows the ingestion, profiling and other capabilities for a specific database. 

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
api_instance = collibra_catalog_database_registration.DatabaseApi(collibra_catalog_database_registration.ApiClient(configuration))
body = collibra_catalog_database_registration.AddDatabaseRequest() # AddDatabaseRequest |  (optional)

try:
    # Create a Database asset
    api_response = api_instance.add_database(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->add_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDatabaseRequest**](AddDatabaseRequest.md)|  | [optional] 

### Return type

[**Database**](Database.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_database**
> Database change_database(database_id, body=body)

Change a Database asset

  Changes a Database asset based on its identifier and a set of properties   to change.    This is a partial update and properties that are not provided will not be changed. 

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
api_instance = collibra_catalog_database_registration.DatabaseApi(collibra_catalog_database_registration.ApiClient(configuration))
database_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Database asset.
body = collibra_catalog_database_registration.ChangeDatabaseRequest() # ChangeDatabaseRequest |  (optional)

try:
    # Change a Database asset
    api_response = api_instance.change_database(database_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->change_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | [**str**](.md)| The ID of the Database asset. | 
 **body** | [**ChangeDatabaseRequest**](ChangeDatabaseRequest.md)|  | [optional] 

### Return type

[**Database**](Database.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_databases**
> DatabasePagedResponse find_databases(parent_system_id=parent_system_id, edge_connection_id=edge_connection_id, database_connection_id=database_connection_id, offset=offset, limit=limit)

Find Database assets

Finds Databases based on the provided criteria.

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
api_instance = collibra_catalog_database_registration.DatabaseApi(collibra_catalog_database_registration.ApiClient(configuration))
parent_system_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the parent *System* asset. (optional)
edge_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Edge connection. (optional)
database_connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the database connection (optional)
offset = 0 # int | The index of the first result to retrieve.  If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.  (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve.  If not set, the default limit  (limit = <code>0</code>) will be used. The maximum value for this parameter is <code>500<code>.  (optional) (default to 0)

try:
    # Find Database assets
    api_response = api_instance.find_databases(parent_system_id=parent_system_id, edge_connection_id=edge_connection_id, database_connection_id=database_connection_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->find_databases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_system_id** | [**str**](.md)| The ID of the parent *System* asset. | [optional] 
 **edge_connection_id** | [**str**](.md)| The ID of the Edge connection. | [optional] 
 **database_connection_id** | [**str**](.md)| The ID of the database connection | [optional] 
 **offset** | **int**| The index of the first result to retrieve.  If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;.  | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve.  If not set, the default limit  (limit &#x3D; &lt;code&gt;0&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;code&gt;.  | [optional] [default to 0]

### Return type

[**DatabasePagedResponse**](DatabasePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database**
> Database get_database(database_id)

Get a Database asset

Gets a single Database asset by its identifier.

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
api_instance = collibra_catalog_database_registration.DatabaseApi(collibra_catalog_database_registration.ApiClient(configuration))
database_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the Database asset.

try:
    # Get a Database asset
    api_response = api_instance.get_database(database_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatabaseApi->get_database: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | [**str**](.md)| The ID of the Database asset. | 

### Return type

[**Database**](Database.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

