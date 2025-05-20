# collibra_catalog_cloud_ingestions.GENERICApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_generic_schedule**](GENERICApi.md#add_generic_schedule) | **POST** /genericIntegration/{ingestibleId}/schedule | Add a schedule
[**cancel_capability_job**](GENERICApi.md#cancel_capability_job) | **DELETE** /genericIntegration/{ingestibleId}/cancel | Cancel a synchronization
[**delete_config**](GENERICApi.md#delete_config) | **DELETE** /genericIntegration/{ingestibleId}/configuration | Delete a generic configuration
[**delete_generic_schedule**](GENERICApi.md#delete_generic_schedule) | **DELETE** /genericIntegration/{ingestibleId}/schedule | Delete a schedule
[**get_config**](GENERICApi.md#get_config) | **GET** /genericIntegration/{ingestibleId}/configuration | Retrieve a generic configuration
[**get_generic_schedule**](GENERICApi.md#get_generic_schedule) | **GET** /genericIntegration/{ingestibleId}/schedule | Retrieve a schedule
[**get_schema**](GENERICApi.md#get_schema) | **GET** /genericIntegration/{ingestibleId}/configuration/schema | Retrieve data schema as part of generic configuration
[**save_config**](GENERICApi.md#save_config) | **PUT** /genericIntegration/{ingestibleId}/configuration | Create or update a generic configuration
[**start_capability_job**](GENERICApi.md#start_capability_job) | **POST** /genericIntegration/{ingestibleId}/run | Starts capability on Edge.
[**update_generic_schedule**](GENERICApi.md#update_generic_schedule) | **PUT** /genericIntegration/{ingestibleId}/schedule | Update a schedule

# **add_generic_schedule**
> Schedule add_generic_schedule(ingestible_id, body=body)

Add a schedule

Adds a schedule for the generic Edge capability with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_cloud_ingestions.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_catalog_cloud_ingestions.AddGenericScheduleRequest() # AddGenericScheduleRequest |  (optional)

try:
    # Add a schedule
    api_response = api_instance.add_generic_schedule(ingestible_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GENERICApi->add_generic_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 
 **body** | [**AddGenericScheduleRequest**](AddGenericScheduleRequest.md)|  | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_capability_job**
> cancel_capability_job(ingestible_id)

Cancel a synchronization

Cancel the synchronization of the generic Edge capability with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_cloud_ingestions.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Cancel a synchronization
    api_instance.cancel_capability_job(ingestible_id)
except ApiException as e:
    print("Exception when calling GENERICApi->cancel_capability_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config**
> GenericConfiguration delete_config(ingestible_id)

Delete a generic configuration

Deletes a generic configuration from the integration instance with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi()
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a generic configuration
    api_response = api_instance.delete_config(ingestible_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GENERICApi->delete_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 

### Return type

[**GenericConfiguration**](GenericConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_generic_schedule**
> delete_generic_schedule(ingestible_id)

Delete a schedule

Deletes the schedule from the generic Edge capability with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_cloud_ingestions.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Delete a schedule
    api_instance.delete_generic_schedule(ingestible_id)
except ApiException as e:
    print("Exception when calling GENERICApi->delete_generic_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config**
> GenericConfiguration get_config(ingestible_id)

Retrieve a generic configuration

Returns the generic configuration for the integration instance with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi()
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve a generic configuration
    api_response = api_instance.get_config(ingestible_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GENERICApi->get_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 

### Return type

[**GenericConfiguration**](GenericConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_generic_schedule**
> Schedule get_generic_schedule(ingestible_id)

Retrieve a schedule

Returns the schedule for the generic Edge capability with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_cloud_ingestions.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve a schedule
    api_response = api_instance.get_generic_schedule(ingestible_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GENERICApi->get_generic_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schema**
> str get_schema(ingestible_id)

Retrieve data schema as part of generic configuration

Returns data schema for the integration instance with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi()
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve data schema as part of generic configuration
    api_response = api_instance.get_schema(ingestible_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GENERICApi->get_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_config**
> GenericConfiguration save_config(body, ingestible_id)

Create or update a generic configuration

Creates or updates a generic configuration for the integration instance with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi()
body = collibra_catalog_cloud_ingestions.SaveGenericConfigRequest() # SaveGenericConfigRequest | Generic configuration to save.
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Create or update a generic configuration
    api_response = api_instance.save_config(body, ingestible_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GENERICApi->save_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SaveGenericConfigRequest**](SaveGenericConfigRequest.md)| Generic configuration to save. | 
 **ingestible_id** | [**str**](.md)|  | 

### Return type

[**GenericConfiguration**](GenericConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_capability_job**
> Job start_capability_job(ingestible_id)

Starts capability on Edge.

Starts an Edge based capability job

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_cloud_ingestions.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Starts capability on Edge.
    api_response = api_instance.start_capability_job(ingestible_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GENERICApi->start_capability_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_generic_schedule**
> Schedule update_generic_schedule(ingestible_id, body=body)

Update a schedule

Updates the schedule for the generic Edge capability with the specified ID.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_cloud_ingestions
from collibra_catalog_cloud_ingestions.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_cloud_ingestions.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_cloud_ingestions.GENERICApi(collibra_catalog_cloud_ingestions.ApiClient(configuration))
ingestible_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = collibra_catalog_cloud_ingestions.ChangeGenericScheduleRequest() # ChangeGenericScheduleRequest |  (optional)

try:
    # Update a schedule
    api_response = api_instance.update_generic_schedule(ingestible_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GENERICApi->update_generic_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestible_id** | [**str**](.md)|  | 
 **body** | [**ChangeGenericScheduleRequest**](ChangeGenericScheduleRequest.md)|  | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

