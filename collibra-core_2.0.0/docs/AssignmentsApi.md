# collibra_core.AssignmentsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_assignment**](AssignmentsApi.md#add_assignment) | **POST** /assignments | Adds a new Assignment.
[**change_assignment**](AssignmentsApi.md#change_assignment) | **PATCH** /assignments/{assignmentId} | Changes the assignment with the information that is provided in the request.
[**find_assignments_for_resource**](AssignmentsApi.md#find_assignments_for_resource) | **GET** /assignments/forResource | Find the assignments where a given resource is assigned.
[**get_assignments_for_asset**](AssignmentsApi.md#get_assignments_for_asset) | **GET** /assignments/asset/{assetId} | Returns the Assignment identified by the given Asset.
[**get_assignments_for_asset_type**](AssignmentsApi.md#get_assignments_for_asset_type) | **GET** /assignments/assetType/{assetTypeId} | Returns Assignments for given asset type id.
[**get_available_asset_types_for_domain**](AssignmentsApi.md#get_available_asset_types_for_domain) | **GET** /assignments/domain/{domainId}/assetTypes | Returns available asset types for domain identified by given id.
[**get_available_attribute_types_for_asset**](AssignmentsApi.md#get_available_attribute_types_for_asset) | **GET** /assignments/asset/{assetId}/attributeTypes | Returns available attribute types for asset identified by given id.
[**get_available_complex_relation_types_for_asset**](AssignmentsApi.md#get_available_complex_relation_types_for_asset) | **GET** /assignments/asset/{assetId}/complexRelationTypes | Returns the available ComplexRelationTypes for the Asset identified by the given id.
[**get_available_relation_types_for_asset**](AssignmentsApi.md#get_available_relation_types_for_asset) | **GET** /assignments/asset/{assetId}/relationTypes | Returns the available RelationTypes for the Asset identified by the given id.
[**remove_assignment**](AssignmentsApi.md#remove_assignment) | **DELETE** /assignments/{assignmentId} | Removes the Assignment identified by the given id.

# **add_assignment**
> AssignmentImpl add_assignment(body=body)

Adds a new Assignment.

Adds a new Assignment.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddAssignmentRequest() # AddAssignmentRequest |  (optional)

try:
    # Adds a new Assignment.
    api_response = api_instance.add_assignment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->add_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddAssignmentRequest**](AddAssignmentRequest.md)|  | [optional] 

### Return type

[**AssignmentImpl**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_assignment**
> AssignmentImpl change_assignment(assignment_id, body=body)

Changes the assignment with the information that is provided in the request.

Changes the assignment with the information that is provided in the request. Only properties that are specified in the request and are not NULL are updated. All other properties are ignored.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
assignment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the Assignment.
body = collibra_core.ChangeAssignmentRequest() # ChangeAssignmentRequest |  (optional)

try:
    # Changes the assignment with the information that is provided in the request.
    api_response = api_instance.change_assignment(assignment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->change_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | [**str**](.md)| The unique identifier of the Assignment. | 
 **body** | [**ChangeAssignmentRequest**](ChangeAssignmentRequest.md)|  | [optional] 

### Return type

[**AssignmentImpl**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_assignments_for_resource**
> list[AssignmentImpl] find_assignments_for_resource(resource_id=resource_id, resource_type=resource_type)

Find the assignments where a given resource is assigned.

Find the assignments where a given resource is assigned.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
resource_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the resource on which the assignment applies. (optional)
resource_type = 'resource_type_example' # str | The type of resource that is assigned. (optional)

try:
    # Find the assignments where a given resource is assigned.
    api_response = api_instance.find_assignments_for_resource(resource_id=resource_id, resource_type=resource_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->find_assignments_for_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**str**](.md)| The ID of the resource on which the assignment applies. | [optional] 
 **resource_type** | **str**| The type of resource that is assigned. | [optional] 

### Return type

[**list[AssignmentImpl]**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignments_for_asset**
> AssignmentImpl get_assignments_for_asset(asset_id)

Returns the Assignment identified by the given Asset.

Returns the Assignment identified by the given Asset.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the Asset.

try:
    # Returns the Assignment identified by the given Asset.
    api_response = api_instance.get_assignments_for_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_assignments_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| The unique identifier of the Asset. | 

### Return type

[**AssignmentImpl**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignments_for_asset_type**
> list[AssignmentImpl] get_assignments_for_asset_type(asset_type_id)

Returns Assignments for given asset type id.

Returns Assignments for given asset type id.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
asset_type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the AssetType.

try:
    # Returns Assignments for given asset type id.
    api_response = api_instance.get_assignments_for_asset_type(asset_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_assignments_for_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The unique identifier of the AssetType. | 

### Return type

[**list[AssignmentImpl]**](AssignmentImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_asset_types_for_domain**
> list[AssetTypeImpl] get_available_asset_types_for_domain(domain_id)

Returns available asset types for domain identified by given id.

Returns available asset types for domain identified by given id.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the Domain.

try:
    # Returns available asset types for domain identified by given id.
    api_response = api_instance.get_available_asset_types_for_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_available_asset_types_for_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| The unique identifier of the Domain. | 

### Return type

[**list[AssetTypeImpl]**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_attribute_types_for_asset**
> list[AttributeType] get_available_attribute_types_for_asset(asset_id)

Returns available attribute types for asset identified by given id.

Returns available attribute types for asset identified by given id.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the Asset.

try:
    # Returns available attribute types for asset identified by given id.
    api_response = api_instance.get_available_attribute_types_for_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_available_attribute_types_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| The unique identifier of the Asset. | 

### Return type

[**list[AttributeType]**](AttributeType.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_complex_relation_types_for_asset**
> list[ComplexRelationTypeImpl] get_available_complex_relation_types_for_asset(asset_id)

Returns the available ComplexRelationTypes for the Asset identified by the given id.

Returns the available ComplexRelationTypes for the Asset identified by the given id.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the Asset.

try:
    # Returns the available ComplexRelationTypes for the Asset identified by the given id.
    api_response = api_instance.get_available_complex_relation_types_for_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_available_complex_relation_types_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| The unique identifier of the Asset. | 

### Return type

[**list[ComplexRelationTypeImpl]**](ComplexRelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_relation_types_for_asset**
> list[RelationTypeImpl] get_available_relation_types_for_asset(asset_id)

Returns the available RelationTypes for the Asset identified by the given id.

Returns the available RelationTypes for the Asset identified by the given id.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
asset_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the Asset.

try:
    # Returns the available RelationTypes for the Asset identified by the given id.
    api_response = api_instance.get_available_relation_types_for_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->get_available_relation_types_for_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**str**](.md)| The unique identifier of the Asset. | 

### Return type

[**list[RelationTypeImpl]**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_assignment**
> remove_assignment(assignment_id)

Removes the Assignment identified by the given id.

Removes the Assignment identified by the given id.

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
api_instance = collibra_core.AssignmentsApi(collibra_core.ApiClient(configuration))
assignment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The unique identifier of the Assignment.

try:
    # Removes the Assignment identified by the given id.
    api_instance.remove_assignment(assignment_id)
except ApiException as e:
    print("Exception when calling AssignmentsApi->remove_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | [**str**](.md)| The unique identifier of the Assignment. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

