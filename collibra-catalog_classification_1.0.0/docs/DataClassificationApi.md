# collibra_catalog_classification.DataClassificationApi

All URIs are relative to */rest/catalog/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_classification**](DataClassificationApi.md#add_classification) | **POST** /dataClassification/classifications | Adds new Classification
[**add_classification_match**](DataClassificationApi.md#add_classification_match) | **POST** /dataClassification/classificationMatches | Adds new Classification Match
[**add_classification_matches**](DataClassificationApi.md#add_classification_matches) | **POST** /dataClassification/classificationMatches/bulk | Adds new Classification Matches
[**change_classification**](DataClassificationApi.md#change_classification) | **PATCH** /dataClassification/classifications/{classificationId} | Changes existing Classification
[**change_classification_match**](DataClassificationApi.md#change_classification_match) | **PATCH** /dataClassification/classificationMatches/{classificationMatchId} | Changes a Classification Match
[**change_classification_matches**](DataClassificationApi.md#change_classification_matches) | **PATCH** /dataClassification/classificationMatches/bulk | Changes multiple Classification Matches
[**classify**](DataClassificationApi.md#classify) | **POST** /dataClassification/classifications/classify | Starts a job that classifies datasets, databases, schemas, tables or columns by external service based on sample data.
[**find_classification_matches**](DataClassificationApi.md#find_classification_matches) | **GET** /dataClassification/classificationMatches | Finds Classification Matches
[**find_classification_matches_with_params**](DataClassificationApi.md#find_classification_matches_with_params) | **GET** /dataClassification/classificationMatches/bulk | Finds Classification Matches
[**find_classifications**](DataClassificationApi.md#find_classifications) | **GET** /dataClassification/classifications | Finds Classifications
[**find_classifications_bulk**](DataClassificationApi.md#find_classifications_bulk) | **GET** /dataClassification/classifications/bulk | Finds Classifications
[**get_classification**](DataClassificationApi.md#get_classification) | **GET** /dataClassification/classifications/{classificationId} | Gets existing Classification by id.
[**get_classification_match**](DataClassificationApi.md#get_classification_match) | **GET** /dataClassification/classificationMatches/{classificationMatchId} | Gets existing Classification Match by id.
[**remove_classification**](DataClassificationApi.md#remove_classification) | **DELETE** /dataClassification/classifications/{classificationId} | Removes existing Classification. WARNING: This will also remove all ClassificationMatches that are joined with this Classification!
[**remove_classification_match**](DataClassificationApi.md#remove_classification_match) | **DELETE** /dataClassification/classificationMatches/{classificationMatchId} | Removes existing Classification Match.
[**remove_classification_matches**](DataClassificationApi.md#remove_classification_matches) | **DELETE** /dataClassification/classificationMatches/bulk | Removes multiple Classification Matches

# **add_classification**
> Classification add_classification(body=body)

Adds new Classification

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
body = collibra_catalog_classification.AddClassificationRequest() # AddClassificationRequest | The request with data needed for creation of new classification. (optional)

try:
    # Adds new Classification
    api_response = api_instance.add_classification(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->add_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClassificationRequest**](AddClassificationRequest.md)| The request with data needed for creation of new classification. | [optional] 

### Return type

[**Classification**](Classification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_classification_match**
> ClassificationMatch add_classification_match(body=body)

Adds new Classification Match

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
body = collibra_catalog_classification.AddClassificationMatchRequest() # AddClassificationMatchRequest | The request with data needed for creation of new classification match. (optional)

try:
    # Adds new Classification Match
    api_response = api_instance.add_classification_match(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->add_classification_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClassificationMatchRequest**](AddClassificationMatchRequest.md)| The request with data needed for creation of new classification match. | [optional] 

### Return type

[**ClassificationMatch**](ClassificationMatch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_classification_matches**
> ClassificationMatch add_classification_matches(body=body)

Adds new Classification Matches

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
body = collibra_catalog_classification.AddClassificationMatchesRequest() # AddClassificationMatchesRequest | The request with data needed for creation of new classification matches. (optional)

try:
    # Adds new Classification Matches
    api_response = api_instance.add_classification_matches(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->add_classification_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClassificationMatchesRequest**](AddClassificationMatchesRequest.md)| The request with data needed for creation of new classification matches. | [optional] 

### Return type

[**ClassificationMatch**](ClassificationMatch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_classification**
> Classification change_classification(classification_id, body=body)

Changes existing Classification

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
classification_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the Classification to be changed
body = collibra_catalog_classification.ChangeClassificationRequest() # ChangeClassificationRequest | The properties of the Classification to be changed. (optional)

try:
    # Changes existing Classification
    api_response = api_instance.change_classification(classification_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->change_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_id** | [**str**](.md)| The id of the Classification to be changed | 
 **body** | [**ChangeClassificationRequest**](ChangeClassificationRequest.md)| The properties of the Classification to be changed. | [optional] 

### Return type

[**Classification**](Classification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_classification_match**
> ClassificationMatch change_classification_match(classification_match_id, body=body)

Changes a Classification Match

Changes the Classification Match with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
classification_match_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the Classification Match to be changed
body = collibra_catalog_classification.ChangeClassificationMatchRequest() # ChangeClassificationMatchRequest | The properties of the Classification Match to be changed. (optional)

try:
    # Changes a Classification Match
    api_response = api_instance.change_classification_match(classification_match_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->change_classification_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_match_id** | [**str**](.md)| The id of the Classification Match to be changed | 
 **body** | [**ChangeClassificationMatchRequest**](ChangeClassificationMatchRequest.md)| The properties of the Classification Match to be changed. | [optional] 

### Return type

[**ClassificationMatch**](ClassificationMatch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_classification_matches**
> list[ClassificationMatch] change_classification_matches(body=body)

Changes multiple Classification Matches

Changes multiple Classification Matches with the information that is present in the requests. Only properties that are specified in the requests and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
body = [collibra_catalog_classification.ChangeClassificationMatchRequest()] # list[ChangeClassificationMatchRequest] | The list of properties of the Classification Matches to be changed. (optional)

try:
    # Changes multiple Classification Matches
    api_response = api_instance.change_classification_matches(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->change_classification_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeClassificationMatchRequest]**](ChangeClassificationMatchRequest.md)| The list of properties of the Classification Matches to be changed. | [optional] 

### Return type

[**list[ClassificationMatch]**](ClassificationMatch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **classify**
> classify(body=body)

Starts a job that classifies datasets, databases, schemas, tables or columns by external service based on sample data.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
body = collibra_catalog_classification.ClassifyRequest() # ClassifyRequest | The request with data needed for running classification job. (optional)

try:
    # Starts a job that classifies datasets, databases, schemas, tables or columns by external service based on sample data.
    api_instance.classify(body=body)
except ApiException as e:
    print("Exception when calling DataClassificationApi->classify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClassifyRequest**](ClassifyRequest.md)| The request with data needed for running classification job. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_classification_matches**
> PagedResponseClassificationMatch find_classification_matches(body=body)

Finds Classification Matches

Returns Classification Matches matching the given search criteria defined by request. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned Classification Matches satisfy all constraints that are specified in this search criteria. This endpoint will be removed in the next major release. Please, use GET /bulk

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
body = collibra_catalog_classification.FindClassificationMatchesRequest() # FindClassificationMatchesRequest | The search criteria of the Classification Matches to be found. (optional)

try:
    # Finds Classification Matches
    api_response = api_instance.find_classification_matches(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->find_classification_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindClassificationMatchesRequest**](FindClassificationMatchesRequest.md)| The search criteria of the Classification Matches to be found. | [optional] 

### Return type

[**PagedResponseClassificationMatch**](PagedResponseClassificationMatch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_classification_matches_with_params**
> PagedResponseClassificationMatch find_classification_matches_with_params(offset=offset, limit=limit, count_limit=count_limit, asset_ids=asset_ids, statuses=statuses, classification_ids=classification_ids, asset_type_ids=asset_type_ids)

Finds Classification Matches

Returns Classification Matches matching the given search criteria defined by query params that form the request. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned Classification Matches satisfy all constraints that are specified in this search criteria.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
asset_ids = ['asset_ids_example'] # list[str] | The <code>id</code>s of the assets (with Column types) to filter by the search results (optional)
statuses = ['statuses_example'] # list[str] | The list of classification match statuses to filter by the search results. (optional)
classification_ids = ['classification_ids_example'] # list[str] | The list of classification ids to filter by the search results. (optional)
asset_type_ids = ['asset_type_ids_example'] # list[str] | The list of asset type ids to filter by the search results. (optional)

try:
    # Finds Classification Matches
    api_response = api_instance.find_classification_matches_with_params(offset=offset, limit=limit, count_limit=count_limit, asset_ids=asset_ids, statuses=statuses, classification_ids=classification_ids, asset_type_ids=asset_type_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->find_classification_matches_with_params: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **asset_ids** | [**list[str]**](str.md)| The &lt;code&gt;id&lt;/code&gt;s of the assets (with Column types) to filter by the search results | [optional] 
 **statuses** | [**list[str]**](str.md)| The list of classification match statuses to filter by the search results. | [optional] 
 **classification_ids** | [**list[str]**](str.md)| The list of classification ids to filter by the search results. | [optional] 
 **asset_type_ids** | [**list[str]**](str.md)| The list of asset type ids to filter by the search results. | [optional] 

### Return type

[**PagedResponseClassificationMatch**](PagedResponseClassificationMatch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_classifications**
> PagedResponseClassification find_classifications(body=body)

Finds Classifications

Returns Classifications matching the given search criteria defined by request. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned Classifications satisfy all constraints that are specified in this search criteria. This endpoint will be removed in the next major release. Please, use GET /bulk

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
body = collibra_catalog_classification.FindClassificationsRequest() # FindClassificationsRequest | The search criteria of the Classifications to be found. (optional)

try:
    # Finds Classifications
    api_response = api_instance.find_classifications(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->find_classifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FindClassificationsRequest**](FindClassificationsRequest.md)| The search criteria of the Classifications to be found. | [optional] 

### Return type

[**PagedResponseClassification**](PagedResponseClassification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_classifications_bulk**
> PagedResponseClassification find_classifications_bulk(offset=offset, limit=limit, count_limit=count_limit, name=name)

Finds Classifications

Returns Classifications matching the given search criteria defined by query params that form the request. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned Classifications satisfy all constraints that are specified in this search criteria.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The exact name of classification to filter by the search results. (optional)

try:
    # Finds Classifications
    api_response = api_instance.find_classifications_bulk(offset=offset, limit=limit, count_limit=count_limit, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClassificationApi->find_classifications_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The exact name of classification to filter by the search results. | [optional] 

### Return type

[**PagedResponseClassification**](PagedResponseClassification.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification**
> get_classification(classification_id)

Gets existing Classification by id.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
classification_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Gets existing Classification by id.
    api_instance.get_classification(classification_id)
except ApiException as e:
    print("Exception when calling DataClassificationApi->get_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classification_match**
> get_classification_match(classification_match_id)

Gets existing Classification Match by id.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
classification_match_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the Classification Match to be fetched

try:
    # Gets existing Classification Match by id.
    api_instance.get_classification_match(classification_match_id)
except ApiException as e:
    print("Exception when calling DataClassificationApi->get_classification_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_match_id** | [**str**](.md)| The id of the Classification Match to be fetched | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_classification**
> remove_classification(classification_id)

Removes existing Classification. WARNING: This will also remove all ClassificationMatches that are joined with this Classification!

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
classification_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Removes existing Classification. WARNING: This will also remove all ClassificationMatches that are joined with this Classification!
    api_instance.remove_classification(classification_id)
except ApiException as e:
    print("Exception when calling DataClassificationApi->remove_classification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_classification_match**
> remove_classification_match(classification_match_id)

Removes existing Classification Match.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
classification_match_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The id of the Classification Match to be deleted

try:
    # Removes existing Classification Match.
    api_instance.remove_classification_match(classification_match_id)
except ApiException as e:
    print("Exception when calling DataClassificationApi->remove_classification_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classification_match_id** | [**str**](.md)| The id of the Classification Match to be deleted | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_classification_matches**
> remove_classification_matches(body=body)

Removes multiple Classification Matches

Removes multiple Classification Matches with IDs provided in request body.

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
api_instance = collibra_catalog_classification.DataClassificationApi(collibra_catalog_classification.ApiClient(configuration))
body = collibra_catalog_classification.DeleteClassificationMatchesRequest() # DeleteClassificationMatchesRequest | The list of Classification Match IDs to be deleted. (optional)

try:
    # Removes multiple Classification Matches
    api_instance.remove_classification_matches(body=body)
except ApiException as e:
    print("Exception when calling DataClassificationApi->remove_classification_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteClassificationMatchesRequest**](DeleteClassificationMatchesRequest.md)| The list of Classification Match IDs to be deleted. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

