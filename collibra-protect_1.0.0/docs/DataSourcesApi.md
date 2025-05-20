# collibra_protect.DataSourcesApi

All URIs are relative to */rest/protect/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_source**](DataSourcesApi.md#add_data_source) | **POST** /dataSources | Add a new data source
[**delete_data_source**](DataSourcesApi.md#delete_data_source) | **DELETE** /dataSources/{id} | Delete a data source
[**get_data_source**](DataSourcesApi.md#get_data_source) | **GET** /dataSources/{id} | Retrieve a data source
[**list_data_sources**](DataSourcesApi.md#list_data_sources) | **GET** /dataSources | List data sources
[**patch_data_source**](DataSourcesApi.md#patch_data_source) | **PATCH** /dataSources/{id} | Update a data source

# **add_data_source**
> DataSource add_data_source(body)

Add a new data source

Adds a new data source.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.DataSourcesApi(collibra_protect.ApiClient(configuration))
body = collibra_protect.AddDataSourceRequest() # AddDataSourceRequest | The new data source you want to add.

try:
    # Add a new data source
    api_response = api_instance.add_data_source(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->add_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDataSourceRequest**](AddDataSourceRequest.md)| The new data source you want to add. | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_source**
> delete_data_source(id)

Delete a data source

Deletes the data source with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.DataSourcesApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the data source.

try:
    # Delete a data source
    api_instance.delete_data_source(id)
except ApiException as e:
    print("Exception when calling DataSourcesApi->delete_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the data source. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source**
> DataSource get_data_source(id)

Retrieve a data source

Returns information about the data source with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.DataSourcesApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the data source.

try:
    # Retrieve a data source
    api_response = api_instance.get_data_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the data source. | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_sources**
> PagedDataSources list_data_sources(limit=limit, after=after)

List data sources

Lists all data sources.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.DataSourcesApi(collibra_protect.ApiClient(configuration))
limit = 25 # int | This is the maximum number of results that may be returned. Fewer may be returned than the value of <code>limit</code>.  Do not depend on the number of results being fewer than the <code>limit</code> value to indicate that your query reached the end of the list of data, use the absence of <code>after</code> (see Cursors) instead. For example, if you set <code>limit</code> to 10 and 9 results are returned, there may be more data available.  If not set, the default limit (limit = <code>25</code>) will be used. The maximum value for this parameter is <code>500</code>.  (optional) (default to 25)
after = 'after_example' # str | This is the cursor that points to the end of the page of data that has been returned. (optional)

try:
    # List data sources
    api_response = api_instance.list_data_sources(limit=limit, after=after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->list_data_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| This is the maximum number of results that may be returned. Fewer may be returned than the value of &lt;code&gt;limit&lt;/code&gt;.  Do not depend on the number of results being fewer than the &lt;code&gt;limit&lt;/code&gt; value to indicate that your query reached the end of the list of data, use the absence of &lt;code&gt;after&lt;/code&gt; (see Cursors) instead. For example, if you set &lt;code&gt;limit&lt;/code&gt; to 10 and 9 results are returned, there may be more data available.  If not set, the default limit (limit &#x3D; &lt;code&gt;25&lt;/code&gt;) will be used. The maximum value for this parameter is &lt;code&gt;500&lt;/code&gt;.  | [optional] [default to 25]
 **after** | **str**| This is the cursor that points to the end of the page of data that has been returned. | [optional] 

### Return type

[**PagedDataSources**](PagedDataSources.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_data_source**
> DataSource patch_data_source(id, body=body)

Update a data source

Updates the data source with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_protect
from collibra_protect.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_protect.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_protect.DataSourcesApi(collibra_protect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the data source.
body = collibra_protect.ChangeDataSourceRequest() # ChangeDataSourceRequest | The changes that need to be applied to the data source. (optional)

try:
    # Update a data source
    api_response = api_instance.patch_data_source(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->patch_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The universally unique identifier (UUID) of the data source. | 
 **body** | [**ChangeDataSourceRequest**](ChangeDataSourceRequest.md)| The changes that need to be applied to the data source. | [optional] 

### Return type

[**DataSource**](DataSource.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

