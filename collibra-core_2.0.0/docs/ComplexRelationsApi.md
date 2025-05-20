# collibra_core.ComplexRelationsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_complex_relation**](ComplexRelationsApi.md#add_complex_relation) | **POST** /complexRelations | Adds new complex relation.
[**change_complex_relation**](ComplexRelationsApi.md#change_complex_relation) | **PATCH** /complexRelations/{complexRelationId} | Change the complex relation with the information that is present in the request.
[**export_to_csv**](ComplexRelationsApi.md#export_to_csv) | **POST** /complexRelations/export/csv-job | Export complex relations of the given type to CSV.
[**export_to_csv_without_job**](ComplexRelationsApi.md#export_to_csv_without_job) | **POST** /complexRelations/export/csv-file | Export all complex relations of the given type to a CSV file.
[**export_to_csvas_string**](ComplexRelationsApi.md#export_to_csvas_string) | **POST** /complexRelations/export/csv | Export all complex relations of the given type to CSV as a String.
[**export_to_excel**](ComplexRelationsApi.md#export_to_excel) | **POST** /complexRelations/export/excel-job | Export complex relations of the given type to Excel.
[**export_to_excel_without_job**](ComplexRelationsApi.md#export_to_excel_without_job) | **POST** /complexRelations/export/excel-file | Export all complex relations of the given type to an Excel file.
[**find_complex_relations**](ComplexRelationsApi.md#find_complex_relations) | **GET** /complexRelations | Returns complex relations matching the given search criteria.
[**get_complex_relation**](ComplexRelationsApi.md#get_complex_relation) | **GET** /complexRelations/{complexRelationId} | Returns a ComplexRelation identified by given id.
[**remove_complex_relation**](ComplexRelationsApi.md#remove_complex_relation) | **DELETE** /complexRelations/{complexRelationId} | Removes complex relation identified by given id.

# **add_complex_relation**
> ComplexRelationImpl add_complex_relation(body=body)

Adds new complex relation.

Adds new complex relation.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddComplexRelationRequest() # AddComplexRelationRequest |  (optional)

try:
    # Adds new complex relation.
    api_response = api_instance.add_complex_relation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->add_complex_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddComplexRelationRequest**](AddComplexRelationRequest.md)|  | [optional] 

### Return type

[**ComplexRelationImpl**](ComplexRelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_complex_relation**
> ComplexRelationImpl change_complex_relation(complex_relation_id, body=body)

Change the complex relation with the information that is present in the request.

Change the complex relation with the information that is present in the request.  Only properties that are specified in this request and have not <code>null</code> values are updated.  All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
complex_relation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the complex relation to be modified.
body = collibra_core.ChangeComplexRelationRequest() # ChangeComplexRelationRequest |  (optional)

try:
    # Change the complex relation with the information that is present in the request.
    api_response = api_instance.change_complex_relation(complex_relation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->change_complex_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | [**str**](.md)| the id of the complex relation to be modified. | 
 **body** | [**ChangeComplexRelationRequest**](ChangeComplexRelationRequest.md)|  | [optional] 

### Return type

[**ComplexRelationImpl**](ComplexRelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_csv**
> Job export_to_csv(body=body)

Export complex relations of the given type to CSV.

Export complex relations of the given type to CSV.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
body = collibra_core.ExportComplexRelationsToCSVRequest() # ExportComplexRelationsToCSVRequest |  (optional)

try:
    # Export complex relations of the given type to CSV.
    api_response = api_instance.export_to_csv(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->export_to_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportComplexRelationsToCSVRequest**](ExportComplexRelationsToCSVRequest.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_csv_without_job**
> FileInfoImpl export_to_csv_without_job(body=body)

Export all complex relations of the given type to a CSV file.

Export all complex relations of the given type to a CSV file.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
body = collibra_core.ExportComplexRelationsToCSVRequest() # ExportComplexRelationsToCSVRequest |  (optional)

try:
    # Export all complex relations of the given type to a CSV file.
    api_response = api_instance.export_to_csv_without_job(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->export_to_csv_without_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportComplexRelationsToCSVRequest**](ExportComplexRelationsToCSVRequest.md)|  | [optional] 

### Return type

[**FileInfoImpl**](FileInfoImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_csvas_string**
> str export_to_csvas_string(body=body)

Export all complex relations of the given type to CSV as a String.

Export all complex relations of the given type to CSV as a String.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
body = collibra_core.ExportComplexRelationsToCSVRequest() # ExportComplexRelationsToCSVRequest |  (optional)

try:
    # Export all complex relations of the given type to CSV as a String.
    api_response = api_instance.export_to_csvas_string(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->export_to_csvas_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportComplexRelationsToCSVRequest**](ExportComplexRelationsToCSVRequest.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_excel**
> Job export_to_excel(body=body)

Export complex relations of the given type to Excel.

Export complex relations of the given type to Excel.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
body = collibra_core.ExportComplexRelationsToExcelRequest() # ExportComplexRelationsToExcelRequest |  (optional)

try:
    # Export complex relations of the given type to Excel.
    api_response = api_instance.export_to_excel(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->export_to_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportComplexRelationsToExcelRequest**](ExportComplexRelationsToExcelRequest.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_excel_without_job**
> FileInfoImpl export_to_excel_without_job(body=body)

Export all complex relations of the given type to an Excel file.

Export all complex relations of the given type to an Excel file.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
body = collibra_core.ExportComplexRelationsToExcelRequest() # ExportComplexRelationsToExcelRequest |  (optional)

try:
    # Export all complex relations of the given type to an Excel file.
    api_response = api_instance.export_to_excel_without_job(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->export_to_excel_without_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportComplexRelationsToExcelRequest**](ExportComplexRelationsToExcelRequest.md)|  | [optional] 

### Return type

[**FileInfoImpl**](FileInfoImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_complex_relations**
> ComplexRelationPagedResponse find_complex_relations(offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, asset_id=asset_id, type_id=type_id)

Returns complex relations matching the given search criteria.

Returns complex relations matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.  All other parameters are ignored.  The returned complex relations satisfy all constraints that are specified in this search criteria.  By default a result containing 1000 complex relations is returned.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. (optional) (default to -1)
cursor = 'cursor_example' # str | Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (<code>nextCursor</code> property). (optional)
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the asset for which complex relations should be found. (optional)
type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the type of complex relations to search for. (optional)

try:
    # Returns complex relations matching the given search criteria.
    api_response = api_instance.find_complex_relations(offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, asset_id=asset_id, type_id=type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->find_complex_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. | [optional] [default to -1]
 **cursor** | **str**| Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (&lt;code&gt;nextCursor&lt;/code&gt; property). | [optional] 
 **asset_id** | [**str**](.md)| The ID of the asset for which complex relations should be found. | [optional] 
 **type_id** | [**str**](.md)| The ID of the type of complex relations to search for. | [optional] 

### Return type

[**ComplexRelationPagedResponse**](ComplexRelationPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complex_relation**
> ComplexRelationImpl get_complex_relation(complex_relation_id)

Returns a ComplexRelation identified by given id.

Returns a complex relation identified by given <code>id</code>.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
complex_relation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the complex relation.

try:
    # Returns a ComplexRelation identified by given id.
    api_response = api_instance.get_complex_relation(complex_relation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->get_complex_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | [**str**](.md)| the id of the complex relation. | 

### Return type

[**ComplexRelationImpl**](ComplexRelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_complex_relation**
> remove_complex_relation(complex_relation_id)

Removes complex relation identified by given id.

Removes complex relation identified by given id.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_core.ComplexRelationsApi(collibra_core.ApiClient(configuration))
complex_relation_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the id of the complex relation to be removed.

try:
    # Removes complex relation identified by given id.
    api_instance.remove_complex_relation(complex_relation_id)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->remove_complex_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | [**str**](.md)| the id of the complex relation to be removed. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

