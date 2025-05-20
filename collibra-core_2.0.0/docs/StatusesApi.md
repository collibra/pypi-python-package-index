# collibra_core.StatusesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_status**](StatusesApi.md#add_status) | **POST** /statuses | Adds a new Status.
[**add_statuses**](StatusesApi.md#add_statuses) | **POST** /statuses/bulk | Adds multiple statuses in one go.
[**change_status**](StatusesApi.md#change_status) | **PATCH** /statuses/{statusId} | Changes the status with the information that is present in the request.
[**change_statuses**](StatusesApi.md#change_statuses) | **PATCH** /statuses/bulk | Changes multiple statuses in one go.
[**find_statuses**](StatusesApi.md#find_statuses) | **GET** /statuses | Returns statuses matching the given search criteria.
[**get_status**](StatusesApi.md#get_status) | **GET** /statuses/{statusId} | Returns the Status identified by the given id.
[**get_status_by_name**](StatusesApi.md#get_status_by_name) | **GET** /statuses/name/{statusName} | Returns the Status identified by the given name.
[**remove_status**](StatusesApi.md#remove_status) | **DELETE** /statuses/{statusId} | Removes the Status identified by the given id.
[**remove_statuses**](StatusesApi.md#remove_statuses) | **DELETE** /statuses/bulk | Removes multiple statuses.

# **add_status**
> StatusImpl add_status(body=body)

Adds a new Status.

Adds a new Status.

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddStatusRequest() # AddStatusRequest |  (optional)

try:
    # Adds a new Status.
    api_response = api_instance.add_status(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->add_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddStatusRequest**](AddStatusRequest.md)|  | [optional] 

### Return type

[**StatusImpl**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_statuses**
> list[StatusImpl] add_statuses(body=body)

Adds multiple statuses in one go.

Adds multiple statuses in one go.

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddStatusRequest()] # list[AddStatusRequest] |  (optional)

try:
    # Adds multiple statuses in one go.
    api_response = api_instance.add_statuses(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->add_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddStatusRequest]**](AddStatusRequest.md)|  | [optional] 

### Return type

[**list[StatusImpl]**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_status**
> StatusImpl change_status(status_id, body=body)

Changes the status with the information that is present in the request.

Changes the status with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the status.
body = collibra_core.ChangeStatusRequest() # ChangeStatusRequest |  (optional)

try:
    # Changes the status with the information that is present in the request.
    api_response = api_instance.change_status(status_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->change_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | [**str**](.md)| The unique identifier of the status. | 
 **body** | [**ChangeStatusRequest**](ChangeStatusRequest.md)|  | [optional] 

### Return type

[**StatusImpl**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_statuses**
> list[StatusImpl] change_statuses(body=body)

Changes multiple statuses in one go.

Changes multiple statuses in one go.

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeStatusRequest()] # list[ChangeStatusRequest] |  (optional)

try:
    # Changes multiple statuses in one go.
    api_response = api_instance.change_statuses(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->change_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeStatusRequest]**](ChangeStatusRequest.md)|  | [optional] 

### Return type

[**list[StatusImpl]**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_statuses**
> StatusPagedResponse find_statuses(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, description=description)

Returns statuses matching the given search criteria.

Returns statuses matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned statuses satisfy all constraints that are specified in this search criteria. By default a result containing 1000 statuses is returned. 

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The name of the Status to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) (default to ANYWHERE)
description = 'description_example' # str | The description of the Status to search for. (optional)

try:
    # Returns statuses matching the given search criteria.
    api_response = api_instance.find_statuses(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->find_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The name of the Status to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] [default to ANYWHERE]
 **description** | **str**| The description of the Status to search for. | [optional] 

### Return type

[**StatusPagedResponse**](StatusPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> StatusImpl get_status(status_id)

Returns the Status identified by the given id.

Returns the Status identified by the given id.

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The <code>id</code> of the Status

try:
    # Returns the Status identified by the given id.
    api_response = api_instance.get_status(status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | [**str**](.md)| The &lt;code&gt;id&lt;/code&gt; of the Status | 

### Return type

[**StatusImpl**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_by_name**
> StatusImpl get_status_by_name(status_name)

Returns the Status identified by the given name.

Returns the Status identified by the given name.

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
status_name = 'status_name_example' # str | The name that identifies the Status.

try:
    # Returns the Status identified by the given name.
    api_response = api_instance.get_status_by_name(status_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->get_status_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_name** | **str**| The name that identifies the Status. | 

### Return type

[**StatusImpl**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_status**
> remove_status(status_id)

Removes the Status identified by the given id.

Removes the Status identified by the given id.

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The <code>id</code> of the Status.

try:
    # Removes the Status identified by the given id.
    api_instance.remove_status(status_id)
except ApiException as e:
    print("Exception when calling StatusesApi->remove_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | [**str**](.md)| The &lt;code&gt;id&lt;/code&gt; of the Status. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_statuses**
> remove_statuses(body=body)

Removes multiple statuses.

Removes multiple statuses.

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
api_instance = collibra_core.StatusesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | The indentifiers of the Statuses. (optional)

try:
    # Removes multiple statuses.
    api_instance.remove_statuses(body=body)
except ApiException as e:
    print("Exception when calling StatusesApi->remove_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The indentifiers of the Statuses. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

