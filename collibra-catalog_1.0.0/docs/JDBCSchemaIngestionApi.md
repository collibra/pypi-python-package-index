# collibra_catalog.JDBCSchemaIngestionApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_schema_from_jdbc**](JDBCSchemaIngestionApi.md#add_schema_from_jdbc) | **POST** /schemas/jdbc | Create a JDBC schema ingestion
[**refresh_jdbc_schema**](JDBCSchemaIngestionApi.md#refresh_jdbc_schema) | **POST** /schemas/jdbc/{assetId} | Refresh an existing JDBC schema ingestion

# **add_schema_from_jdbc**
> Job add_schema_from_jdbc(body=body)

Create a JDBC schema ingestion

Create a schema from a JDBC data source. <br />This operation is deprecated and it will be removed the next major release

### Example
```python
from __future__ import print_function
import time
import collibra_catalog
from collibra_catalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog.JDBCSchemaIngestionApi()
body = collibra_catalog.AddSchemaFromJdbcRequest() # AddSchemaFromJdbcRequest |  (optional)

try:
    # Create a JDBC schema ingestion
    api_response = api_instance.add_schema_from_jdbc(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JDBCSchemaIngestionApi->add_schema_from_jdbc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddSchemaFromJdbcRequest**](AddSchemaFromJdbcRequest.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_jdbc_schema**
> Job refresh_jdbc_schema(asset_id, body=body)

Refresh an existing JDBC schema ingestion

Refresh a schema from a JDBC data source. <br />This operation is deprecated and it will be removed the next major release

### Example
```python
from __future__ import print_function
import time
import collibra_catalog
from collibra_catalog.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog.JDBCSchemaIngestionApi()
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_catalog.RefreshJdbcSchemaRequest() # RefreshJdbcSchemaRequest |  (optional)

try:
    # Refresh an existing JDBC schema ingestion
    api_response = api_instance.refresh_jdbc_schema(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JDBCSchemaIngestionApi->refresh_jdbc_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)|  | 
 **body** | [**RefreshJdbcSchemaRequest**](RefreshJdbcSchemaRequest.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

