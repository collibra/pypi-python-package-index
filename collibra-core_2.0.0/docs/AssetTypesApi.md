# collibra_core.AssetTypesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_type**](AssetTypesApi.md#add_asset_type) | **POST** /assetTypes | Add asset type
[**add_asset_types**](AssetTypesApi.md#add_asset_types) | **POST** /assetTypes/bulk | Add multiple asset types
[**change_asset_type**](AssetTypesApi.md#change_asset_type) | **PATCH** /assetTypes/{assetTypeId} | Change asset type
[**change_asset_types**](AssetTypesApi.md#change_asset_types) | **PATCH** /assetTypes/bulk | Change multiple asset types
[**find_asset_types**](AssetTypesApi.md#find_asset_types) | **GET** /assetTypes | Find asset types matching criteria
[**find_parent_types**](AssetTypesApi.md#find_parent_types) | **GET** /assetTypes/{assetTypeId}/parents | Find parent types
[**find_sub_asset_types**](AssetTypesApi.md#find_sub_asset_types) | **GET** /assetTypes/{assetTypeId}/subTypes | Find asset subtypes
[**get_asset_type**](AssetTypesApi.md#get_asset_type) | **GET** /assetTypes/{assetTypeId} | Get asset type by ID
[**remove_asset_type**](AssetTypesApi.md#remove_asset_type) | **DELETE** /assetTypes/{assetTypeId} | Remove asset type by ID
[**remove_asset_types**](AssetTypesApi.md#remove_asset_types) | **DELETE** /assetTypes/bulk | Remove multiple asset types

# **add_asset_type**
> AssetTypeImpl add_asset_type(body=body)

Add asset type

Adds a new asset type with the given parameters.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddAssetTypeRequest() # AddAssetTypeRequest | The properties of the asset type to be added (optional)

try:
    # Add asset type
    api_response = api_instance.add_asset_type(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->add_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddAssetTypeRequest**](AddAssetTypeRequest.md)| The properties of the asset type to be added | [optional] 

### Return type

[**AssetTypeImpl**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_asset_types**
> list[AssetTypeImpl] add_asset_types(body=body)

Add multiple asset types

Adds multiple asset types in one go.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddAssetTypeRequest()] # list[AddAssetTypeRequest] |  (optional)

try:
    # Add multiple asset types
    api_response = api_instance.add_asset_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->add_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddAssetTypeRequest]**](AddAssetTypeRequest.md)|  | [optional] 

### Return type

[**list[AssetTypeImpl]**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_asset_type**
> AssetTypeImpl change_asset_type(asset_type_id, body=body)

Change asset type

Changes the asset type using the given parameters. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the asset type
body = collibra_core.ChangeAssetTypeRequest() # ChangeAssetTypeRequest |  (optional)

try:
    # Change asset type
    api_response = api_instance.change_asset_type(asset_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->change_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The ID of the asset type | 
 **body** | [**ChangeAssetTypeRequest**](ChangeAssetTypeRequest.md)|  | [optional] 

### Return type

[**AssetTypeImpl**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_asset_types**
> list[AssetTypeImpl] change_asset_types(body=body)

Change multiple asset types

Changes multiple asset types using the given parameters.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeAssetTypeRequest()] # list[ChangeAssetTypeRequest] |  (optional)

try:
    # Change multiple asset types
    api_response = api_instance.change_asset_types(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->change_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeAssetTypeRequest]**](ChangeAssetTypeRequest.md)|  | [optional] 

### Return type

[**list[AssetTypeImpl]**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_asset_types**
> AssetTypePagedResponse find_asset_types(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, exclude_final=exclude_final, top_level=top_level, display_name_enabled=display_name_enabled)

Find asset types matching criteria

Returns asset types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 asset types is returned.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The name of the Asset Type to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) (default to ANYWHERE)
parent_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the parent to find the Asset Types in. (optional)
exclude_meta = true # bool | Whether the meta Asset Types should be excluded from the results or not. (optional) (default to true)
exclude_final = false # bool | Whether the final Asset Types should be excluded from the results or not. (optional) (default to false)
top_level = false # bool | Whether only top level Asset Types should be searched or not. (optional) (default to false)
display_name_enabled = true # bool | Whether only Asset Types with display names enabled (or disabled) should be searched. (optional)

try:
    # Find asset types matching criteria
    api_response = api_instance.find_asset_types(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, exclude_final=exclude_final, top_level=top_level, display_name_enabled=display_name_enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->find_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The name of the Asset Type to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] [default to ANYWHERE]
 **parent_id** | [**str**](.md)| The ID of the parent to find the Asset Types in. | [optional] 
 **exclude_meta** | **bool**| Whether the meta Asset Types should be excluded from the results or not. | [optional] [default to true]
 **exclude_final** | **bool**| Whether the final Asset Types should be excluded from the results or not. | [optional] [default to false]
 **top_level** | **bool**| Whether only top level Asset Types should be searched or not. | [optional] [default to false]
 **display_name_enabled** | **bool**| Whether only Asset Types with display names enabled (or disabled) should be searched. | [optional] 

### Return type

[**AssetTypePagedResponse**](AssetTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_parent_types**
> list[AssetTypeImpl] find_parent_types(asset_type_id)

Find parent types

Finds all the parent asset types of the asset with the given ID.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the AssetType.

try:
    # Find parent types
    api_response = api_instance.find_parent_types(asset_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->find_parent_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The unique identifier of the AssetType. | 

### Return type

[**list[AssetTypeImpl]**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_sub_asset_types**
> AssetTypePagedResponse find_sub_asset_types(asset_type_id, include_parent=include_parent, direct_sub_types_only=direct_sub_types_only)

Find asset subtypes

Finds all asset subtypes of an asset type, as specified by the request parameters.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the AssetType
include_parent = true # bool | Whether parent Asset Type should be included in the search result. (optional)
direct_sub_types_only = true # bool | Whether we should only list the direct subtypes, or all subtypes. (optional)

try:
    # Find asset subtypes
    api_response = api_instance.find_sub_asset_types(asset_type_id, include_parent=include_parent, direct_sub_types_only=direct_sub_types_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->find_sub_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The ID of the AssetType | 
 **include_parent** | **bool**| Whether parent Asset Type should be included in the search result. | [optional] 
 **direct_sub_types_only** | **bool**| Whether we should only list the direct subtypes, or all subtypes. | [optional] 

### Return type

[**AssetTypePagedResponse**](AssetTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_type**
> AssetTypeImpl get_asset_type(asset_type_id)

Get asset type by ID

Returns the asset type having the given ID.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the asset type

try:
    # Get asset type by ID
    api_response = api_instance.get_asset_type(asset_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->get_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The ID of the asset type | 

### Return type

[**AssetTypeImpl**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_type**
> remove_asset_type(asset_type_id)

Remove asset type by ID

Removes the asset type having the given ID.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the asset type

try:
    # Remove asset type by ID
    api_instance.remove_asset_type(asset_type_id)
except ApiException as e:
    print("Exception when calling AssetTypesApi->remove_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The ID of the asset type | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_types**
> remove_asset_types(body=body)

Remove multiple asset types

Removes multiple asset types identified by the given IDs.

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
api_instance = collibra_core.AssetTypesApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] |  (optional)

try:
    # Remove multiple asset types
    api_instance.remove_asset_types(body=body)
except ApiException as e:
    print("Exception when calling AssetTypesApi->remove_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

