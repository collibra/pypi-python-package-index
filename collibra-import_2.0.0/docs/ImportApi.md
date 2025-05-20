# collibra_import.ImportApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evict_synchronization_cache**](ImportApi.md#evict_synchronization_cache) | **DELETE** /import/synchronize/{synchronizationId}/evict | Removes all cache entries corresponding to the provided synchronization id.
[**exists**](ImportApi.md#exists) | **GET** /import/synchronize/exists/{synchronizationId} | Checks whether given synchronization id already exists.
[**find_synchronization_infos**](ImportApi.md#find_synchronization_infos) | **GET** /import/synchronize | Returns synchronization information matching the given search criteria.
[**import_csv_in_job**](ImportApi.md#import_csv_in_job) | **POST** /import/csv-job | Starts import from the CSV file in job (asynchronously).
[**import_excel_in_job**](ImportApi.md#import_excel_in_job) | **POST** /import/excel-job | Starts import from the Excel file in job (asynchronously).
[**import_json_in_job**](ImportApi.md#import_json_in_job) | **POST** /import/json-job | Starts import from the JSON file in job (asynchronously).
[**remove_synchronization**](ImportApi.md#remove_synchronization) | **DELETE** /import/synchronize/{synchronizationId} | Removes all information about synchronization process corresponding to provided synchronization id.
[**synchronize_batch_csv_in_job**](ImportApi.md#synchronize_batch_csv_in_job) | **POST** /import/synchronize/{synchronizationId}/batch/csv-job | Starts batch synchronization from the CSV file in job (asynchronously).
[**synchronize_batch_excel_in_job**](ImportApi.md#synchronize_batch_excel_in_job) | **POST** /import/synchronize/{synchronizationId}/batch/excel-job | Starts batch synchronization from the Excel file in job (asynchronously).
[**synchronize_batch_json_in_job**](ImportApi.md#synchronize_batch_json_in_job) | **POST** /import/synchronize/{synchronizationId}/batch/json-job | Starts batch synchronization from the JSON file in job (asynchronously).
[**synchronize_csv_in_job**](ImportApi.md#synchronize_csv_in_job) | **POST** /import/synchronize/{synchronizationId}/csv-job | Starts full synchronization from the CSV file in job (asynchronously).
[**synchronize_excel_in_job**](ImportApi.md#synchronize_excel_in_job) | **POST** /import/synchronize/{synchronizationId}/excel-job | Starts full synchronization from the Excel file in job (asynchronously).
[**synchronize_finalize_in_job**](ImportApi.md#synchronize_finalize_in_job) | **POST** /import/synchronize/{synchronizationId}/finalize/job | Starts synchronization finalization in job (asynchronously).
[**synchronize_json_in_job**](ImportApi.md#synchronize_json_in_job) | **POST** /import/synchronize/{synchronizationId}/json-job | Starts full synchronization from the JSON file in job (asynchronously).

# **evict_synchronization_cache**
> evict_synchronization_cache(synchronization_id)

Removes all cache entries corresponding to the provided synchronization id.

Removes all cache entries corresponding to the provided synchronization <code>id</code>.<p>The synchronization component is optimized to only execute commands that differ from cycle to cycle. Call this method to clear the command cache and force the execution of all commands in this cycle.</p><p>Note: this operation does not stop the tracking of the resources identified by the provided synchronization <code>id</code>. The next synchronization process usingthe same <code>id</code> will still be able to detect resources that should be removed.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id of the operation.

try:
    # Removes all cache entries corresponding to the provided synchronization id.
    api_instance.evict_synchronization_cache(synchronization_id)
except ApiException as e:
    print("Exception when calling ImportApi->evict_synchronization_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id of the operation. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exists**
> bool exists(synchronization_id)

Checks whether given synchronization id already exists.

Checks whether given synchronization <code>id</code> already exists.

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id of the operation.

try:
    # Checks whether given synchronization id already exists.
    api_response = api_instance.exists(synchronization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id of the operation. | 

### Return type

**bool**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_synchronization_infos**
> PagedResponseSynchronizationInfo find_synchronization_infos(offset=offset, limit=limit, count_limit=count_limit)

Returns synchronization information matching the given search criteria.

Returns synchronization information matching the given search criteria.<p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.</p><p>The returned synchronization information satisfies all constraints that are specified in this search criteria. By default a result containing 1000 synchronization infos is returned.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)

try:
    # Returns synchronization information matching the given search criteria.
    api_response = api_instance.find_synchronization_infos(offset=offset, limit=limit, count_limit=count_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->find_synchronization_infos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]

### Return type

[**PagedResponseSynchronizationInfo**](PagedResponseSynchronizationInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_csv_in_job**
> Job import_csv_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)

Starts import from the CSV file in job (asynchronously).

Starts import from the CSV file in job (asynchronously).  <br/><p>Request can either accept <code>id</code> of the uploaded file that contains CSV input which should be used for import - or the file itself.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
separator = 'separator_example' # str |  (optional)
quote = 'quote_example' # str |  (optional)
escape = 'escape_example' # str |  (optional)
strict_quotes = true # bool |  (optional)
ignore_leading_whitespace = true # bool |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts import from the CSV file in job (asynchronously).
    api_response = api_instance.import_csv_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_csv_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **separator** | **str**|  | [optional] 
 **quote** | **str**|  | [optional] 
 **escape** | **str**|  | [optional] 
 **strict_quotes** | **bool**|  | [optional] 
 **ignore_leading_whitespace** | **bool**|  | [optional] 
 **header_row** | **bool**|  | [optional] 
 **template** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_excel_in_job**
> Job import_excel_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)

Starts import from the Excel file in job (asynchronously).

Starts import from the Excel file in job (asynchronously).  <br/><p>Request can either accept <code>id</code> of the uploaded file that contains Excel input which should be used for import - or the file itself.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
sheet_name = 'sheet_name_example' # str |  (optional)
sheet_index = 56 # int |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts import from the Excel file in job (asynchronously).
    api_response = api_instance.import_excel_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_excel_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **sheet_name** | **str**|  | [optional] 
 **sheet_index** | **int**|  | [optional] 
 **header_row** | **bool**|  | [optional] 
 **template** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_json_in_job**
> Job import_json_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, relations_action=relations_action)

Starts import from the JSON file in job (asynchronously).

Starts import from the JSON file in job (asynchronously).  <br/><p>Request can either accept <code>id</code> of the uploaded file that contains JSON input which should be used for import - or the file itself.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
relations_action = 'relations_action_example' # str |  (optional)

try:
    # Starts import from the JSON file in job (asynchronously).
    api_response = api_instance.import_json_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, relations_action=relations_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_json_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **relations_action** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_synchronization**
> remove_synchronization(synchronization_id)

Removes all information about synchronization process corresponding to provided synchronization id.

Removes all information about synchronization process corresponding to provided synchronization <code>id</code>.<p>This operation stops tracking of synchronization identified by provided synchronization <code>id</code>. The next synchronization process specified with this <code>id</code> will not be able to detect resources that should be removed.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id of the operation.

try:
    # Removes all information about synchronization process corresponding to provided synchronization id.
    api_instance.remove_synchronization(synchronization_id)
except ApiException as e:
    print("Exception when calling ImportApi->remove_synchronization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id of the operation. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_batch_csv_in_job**
> Job synchronize_batch_csv_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)

Starts batch synchronization from the CSV file in job (asynchronously).

Starts batch synchronization from the CSV file in job (asynchronously).<p>Request can either accept <code>id</code> of the uploaded file that contains CSV input which should be used for import or the file itself. The input file is treated as a part (batch) of synchronization process. After last batch, finalization (cleanup) process should be called.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
separator = 'separator_example' # str |  (optional)
quote = 'quote_example' # str |  (optional)
escape = 'escape_example' # str |  (optional)
strict_quotes = true # bool |  (optional)
ignore_leading_whitespace = true # bool |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts batch synchronization from the CSV file in job (asynchronously).
    api_response = api_instance.synchronize_batch_csv_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_batch_csv_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id used to distinguish different synchronizations. | 
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **separator** | **str**|  | [optional] 
 **quote** | **str**|  | [optional] 
 **escape** | **str**|  | [optional] 
 **strict_quotes** | **bool**|  | [optional] 
 **ignore_leading_whitespace** | **bool**|  | [optional] 
 **header_row** | **bool**|  | [optional] 
 **template** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_batch_excel_in_job**
> Job synchronize_batch_excel_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)

Starts batch synchronization from the Excel file in job (asynchronously).

Starts batch synchronization from the Excel file in job (asynchronously).<p>Request can either accept <code>id</code> of the uploaded file that contains Excel input which should be used for import or the file itself. The input file is treated as a part (batch) of synchronization process. After last batch, finalization (cleanup) process should be called.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
sheet_name = 'sheet_name_example' # str |  (optional)
sheet_index = 56 # int |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts batch synchronization from the Excel file in job (asynchronously).
    api_response = api_instance.synchronize_batch_excel_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_batch_excel_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id used to distinguish different synchronizations. | 
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **sheet_name** | **str**|  | [optional] 
 **sheet_index** | **int**|  | [optional] 
 **header_row** | **bool**|  | [optional] 
 **template** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_batch_json_in_job**
> Job synchronize_batch_json_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, relations_action=relations_action)

Starts batch synchronization from the JSON file in job (asynchronously).

Starts batch synchronization from the JSON file in job (asynchronously).<p>Request can either accept <code>id</code> of the uploaded file that contains JSON input which should be used for import or the file itself. The input file is treated as a part (batch) of synchronization process. After last batch, finalization (cleanup) process should be called.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
relations_action = 'relations_action_example' # str |  (optional)

try:
    # Starts batch synchronization from the JSON file in job (asynchronously).
    api_response = api_instance.synchronize_batch_json_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, relations_action=relations_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_batch_json_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id used to distinguish different synchronizations. | 
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **relations_action** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_csv_in_job**
> Job synchronize_csv_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)

Starts full synchronization from the CSV file in job (asynchronously).

Starts full synchronization from the CSV file in job (asynchronously).<p>Request can either accept <code>id</code> of the uploaded file that contains CSV input which should be used for import or the file itself. The input file is treated as a full input of synchronization process.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
finalization_strategy = 'finalization_strategy_example' # str |  (optional)
missing_asset_status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
separator = 'separator_example' # str |  (optional)
quote = 'quote_example' # str |  (optional)
escape = 'escape_example' # str |  (optional)
strict_quotes = true # bool |  (optional)
ignore_leading_whitespace = true # bool |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts full synchronization from the CSV file in job (asynchronously).
    api_response = api_instance.synchronize_csv_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_csv_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id used to distinguish different synchronizations. | 
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **finalization_strategy** | **str**|  | [optional] 
 **missing_asset_status_id** | [**str**](.md)|  | [optional] 
 **separator** | **str**|  | [optional] 
 **quote** | **str**|  | [optional] 
 **escape** | **str**|  | [optional] 
 **strict_quotes** | **bool**|  | [optional] 
 **ignore_leading_whitespace** | **bool**|  | [optional] 
 **header_row** | **bool**|  | [optional] 
 **template** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_excel_in_job**
> Job synchronize_excel_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)

Starts full synchronization from the Excel file in job (asynchronously).

Starts full synchronization from the Excel file in job (asynchronously).<p>Request can either accept <code>id</code> of the uploaded file that contains Excel input which should be used for import or the file itself. The input file is treated as a full input of synchronization process.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
finalization_strategy = 'finalization_strategy_example' # str |  (optional)
missing_asset_status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
sheet_name = 'sheet_name_example' # str |  (optional)
sheet_index = 56 # int |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts full synchronization from the Excel file in job (asynchronously).
    api_response = api_instance.synchronize_excel_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_excel_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id used to distinguish different synchronizations. | 
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **finalization_strategy** | **str**|  | [optional] 
 **missing_asset_status_id** | [**str**](.md)|  | [optional] 
 **sheet_name** | **str**|  | [optional] 
 **sheet_index** | **int**|  | [optional] 
 **header_row** | **bool**|  | [optional] 
 **template** | **str**|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_finalize_in_job**
> Job synchronize_finalize_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, finalization_parameters=finalization_parameters)

Starts synchronization finalization in job (asynchronously).

Starts synchronization finalization in job (asynchronously).<p>Note that while the only mandatory parameter is <code>synchronizationId</code>, requests that omit all optional parameters fail because the multipart-based setup requires at least one part to be present in the body. To meet this requirement and still use all the default values, you can pass a dummy part, for example <code>-F 'foo=bar'</code> if using <code>curl</code>.

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization ID used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
finalization_strategy = 'finalization_strategy_example' # str |  (optional)
missing_asset_status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
finalization_parameters = {'key': 'finalization_parameters_example'} # dict(str, str) |  (optional)

try:
    # Starts synchronization finalization in job (asynchronously).
    api_response = api_instance.synchronize_finalize_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, finalization_parameters=finalization_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_finalize_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization ID used to distinguish different synchronizations. | 
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **finalization_strategy** | **str**|  | [optional] 
 **missing_asset_status_id** | [**str**](.md)|  | [optional] 
 **finalization_parameters** | [**dict(str, str)**](str.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **synchronize_json_in_job**
> Job synchronize_json_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id)

Starts full synchronization from the JSON file in job (asynchronously).

Starts full synchronization from the JSON file in job (asynchronously).<p>Request can either accept <code>id</code> of the uploaded file that contains JSON input which should be used for import or the file itself. The input file is treated as a full input of synchronization process.</p>

### Example
```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
finalization_strategy = 'finalization_strategy_example' # str |  (optional)
missing_asset_status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Starts full synchronization from the JSON file in job (asynchronously).
    api_response = api_instance.synchronize_json_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_json_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **synchronization_id** | **str**| The synchronization id used to distinguish different synchronizations. | 
 **send_notification** | **bool**|  | [optional] 
 **batch_size** | **int**|  | [optional] 
 **simulation** | **bool**|  | [optional] 
 **save_result** | **bool**|  | [optional] 
 **file_id** | [**str**](.md)|  | [optional] 
 **file** | **str**|  | [optional] 
 **file_name** | **str**|  | [optional] 
 **delete_file** | **bool**|  | [optional] 
 **continue_on_error** | **bool**|  | [optional] 
 **finalization_strategy** | **str**|  | [optional] 
 **missing_asset_status_id** | [**str**](.md)|  | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

