# collibra_protect.PrescriptivePathsApi

All URIs are relative to */rest/protect/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_prescriptive_path**](PrescriptivePathsApi.md#add_prescriptive_path) | **POST** /prescriptivePaths | Add a new prescriptive path
[**delete_prescriptive_path**](PrescriptivePathsApi.md#delete_prescriptive_path) | **DELETE** /prescriptivePaths/{assetTypeId} | Delete a prescriptive path
[**get_prescriptive_path**](PrescriptivePathsApi.md#get_prescriptive_path) | **GET** /prescriptivePaths/{assetTypeId} | Retrieve a prescriptive path
[**list_asset_types**](PrescriptivePathsApi.md#list_asset_types) | **GET** /prescriptivePaths/assetTypes | List asset types supported by Protect
[**list_prescriptive_paths**](PrescriptivePathsApi.md#list_prescriptive_paths) | **GET** /prescriptivePaths | Lists all available prescriptive paths
[**patch_prescriptive_path**](PrescriptivePathsApi.md#patch_prescriptive_path) | **PATCH** /prescriptivePaths/{assetTypeId} | Update a prescriptive path

# **add_prescriptive_path**
> PrescriptivePath add_prescriptive_path(body)

Add a new prescriptive path

Adds a new prescriptive path.

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
api_instance = collibra_protect.PrescriptivePathsApi(collibra_protect.ApiClient(configuration))
body = collibra_protect.AddPrescriptivePathRequest() # AddPrescriptivePathRequest | The prescriptive path to add.

try:
    # Add a new prescriptive path
    api_response = api_instance.add_prescriptive_path(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrescriptivePathsApi->add_prescriptive_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddPrescriptivePathRequest**](AddPrescriptivePathRequest.md)| The prescriptive path to add. | 

### Return type

[**PrescriptivePath**](PrescriptivePath.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_prescriptive_path**
> delete_prescriptive_path(asset_type_id)

Delete a prescriptive path

Deletes the prescriptive path for the asset type with the specified ID.

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
api_instance = collibra_protect.PrescriptivePathsApi(collibra_protect.ApiClient(configuration))
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the asset type.

try:
    # Delete a prescriptive path
    api_instance.delete_prescriptive_path(asset_type_id)
except ApiException as e:
    print("Exception when calling PrescriptivePathsApi->delete_prescriptive_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The universally unique identifier (UUID) of the asset type. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prescriptive_path**
> PrescriptivePath get_prescriptive_path(asset_type_id)

Retrieve a prescriptive path

Returns the prescriptive path information for the asset type with the specified ID.

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
api_instance = collibra_protect.PrescriptivePathsApi(collibra_protect.ApiClient(configuration))
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the asset type.

try:
    # Retrieve a prescriptive path
    api_response = api_instance.get_prescriptive_path(asset_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrescriptivePathsApi->get_prescriptive_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The universally unique identifier (UUID) of the asset type. | 

### Return type

[**PrescriptivePath**](PrescriptivePath.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_asset_types**
> AssetTypeIds list_asset_types()

List asset types supported by Protect

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
api_instance = collibra_protect.PrescriptivePathsApi(collibra_protect.ApiClient(configuration))

try:
    # List asset types supported by Protect
    api_response = api_instance.list_asset_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrescriptivePathsApi->list_asset_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssetTypeIds**](AssetTypeIds.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_prescriptive_paths**
> PrescriptivePaths list_prescriptive_paths()

Lists all available prescriptive paths

Returns the prescriptive path information for the asset type with the specified ID.

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
api_instance = collibra_protect.PrescriptivePathsApi(collibra_protect.ApiClient(configuration))

try:
    # Lists all available prescriptive paths
    api_response = api_instance.list_prescriptive_paths()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrescriptivePathsApi->list_prescriptive_paths: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PrescriptivePaths**](PrescriptivePaths.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_prescriptive_path**
> PrescriptivePath patch_prescriptive_path(body, asset_type_id)

Update a prescriptive path

Updates the prescriptive path for the asset type with the specified ID.

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
api_instance = collibra_protect.PrescriptivePathsApi(collibra_protect.ApiClient(configuration))
body = collibra_protect.ChangePrescriptivePathRequest() # ChangePrescriptivePathRequest | The changes that need to be applied to the prescriptive path.
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The universally unique identifier (UUID) of the asset type.

try:
    # Update a prescriptive path
    api_response = api_instance.patch_prescriptive_path(body, asset_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrescriptivePathsApi->patch_prescriptive_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangePrescriptivePathRequest**](ChangePrescriptivePathRequest.md)| The changes that need to be applied to the prescriptive path. | 
 **asset_type_id** | [**str**](.md)| The universally unique identifier (UUID) of the asset type. | 

### Return type

[**PrescriptivePath**](PrescriptivePath.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

