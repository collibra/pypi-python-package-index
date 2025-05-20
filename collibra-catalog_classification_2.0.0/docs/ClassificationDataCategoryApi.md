# collibra_catalog_classification.ClassificationDataCategoryApi

All URIs are relative to */rest/catalogClassification/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_data_category_data_class**](ClassificationDataCategoryApi.md#connect_data_category_data_class) | **POST** /dataClasses/{dataClassId}/dataCategories | Associate data class with data category
[**disconnect_data_category_data_class**](ClassificationDataCategoryApi.md#disconnect_data_category_data_class) | **DELETE** /dataClasses/{dataClassId}/dataCategories/{dataCategoryId} | Remove existing association between a data class and a data category
[**get_association_data_class_data_category**](ClassificationDataCategoryApi.md#get_association_data_class_data_category) | **GET** /dataClasses/dataCategories | Retrieve the association with a data category and a data class.

# **connect_data_category_data_class**
> DataClassDataCategoryConnection connect_data_category_data_class(data_class_id, body=body)

Associate data class with data category

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_classification
from collibra_catalog_classification.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_classification.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_classification.ClassificationDataCategoryApi(collibra_catalog_classification.ApiClient(configuration))
data_class_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the data class to which the data category will be associated.
body = 'body_example' # str | The ID of the data category to be associated with the data class. (optional)

try:
    # Associate data class with data category
    api_response = api_instance.connect_data_category_data_class(data_class_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationDataCategoryApi->connect_data_category_data_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_class_id** | [**str**](.md)| The ID of the data class to which the data category will be associated. | 
 **body** | [**str**](str.md)| The ID of the data category to be associated with the data class. | [optional] 

### Return type

[**DataClassDataCategoryConnection**](DataClassDataCategoryConnection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_data_category_data_class**
> disconnect_data_category_data_class(data_class_id, data_category_id)

Remove existing association between a data class and a data category

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_classification
from collibra_catalog_classification.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_classification.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_classification.ClassificationDataCategoryApi(collibra_catalog_classification.ApiClient(configuration))
data_class_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the data class from which the data category will be removed.
data_category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the data category to be removed.

try:
    # Remove existing association between a data class and a data category
    api_instance.disconnect_data_category_data_class(data_class_id, data_category_id)
except ApiException as e:
    print("Exception when calling ClassificationDataCategoryApi->disconnect_data_category_data_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_class_id** | [**str**](.md)| The ID of the data class from which the data category will be removed. | 
 **data_category_id** | [**str**](.md)| The ID of the data category to be removed. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_association_data_class_data_category**
> DataClassDataCategoryConnectionsPagedResponse get_association_data_class_data_category(data_category_id=data_category_id, data_class_id=data_class_id, offset=offset, limit=limit)

Retrieve the association with a data category and a data class.

### Example
```python
from __future__ import print_function
import time
import collibra_catalog_classification
from collibra_catalog_classification.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_catalog_classification.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_catalog_classification.ClassificationDataCategoryApi(collibra_catalog_classification.ApiClient(configuration))
data_category_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the data category for which you want to see the associated data classes. (optional)
data_class_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the data class for which you want to see the associated data categories. (optional)
offset = 0 # int | The index of the first result to retrieve.  If not set (offset = <code>0</code>), results are retrieved starting from row <code>0</code>.  (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve.  If not set, the default limit  (limit = <code>0</code>) is used. The maximum value for this parameter is <code>1000<code>.  (optional) (default to 0)

try:
    # Retrieve the association with a data category and a data class.
    api_response = api_instance.get_association_data_class_data_category(data_category_id=data_category_id, data_class_id=data_class_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClassificationDataCategoryApi->get_association_data_class_data_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_category_id** | [**str**](.md)| The ID of the data category for which you want to see the associated data classes. | [optional] 
 **data_class_id** | [**str**](.md)| The ID of the data class for which you want to see the associated data categories. | [optional] 
 **offset** | **int**| The index of the first result to retrieve.  If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results are retrieved starting from row &lt;code&gt;0&lt;/code&gt;.  | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve.  If not set, the default limit  (limit &#x3D; &lt;code&gt;0&lt;/code&gt;) is used. The maximum value for this parameter is &lt;code&gt;1000&lt;code&gt;.  | [optional] [default to 0]

### Return type

[**DataClassDataCategoryConnectionsPagedResponse**](DataClassDataCategoryConnectionsPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

