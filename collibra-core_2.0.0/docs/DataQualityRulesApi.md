# collibra_core.DataQualityRulesApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_quality_rule**](DataQualityRulesApi.md#add_data_quality_rule) | **POST** /dataQualityRules | Adds a new data quality rule.
[**change_data_quality_rule**](DataQualityRulesApi.md#change_data_quality_rule) | **PATCH** /dataQualityRules/{dataQualityRuleId} | Changes the data quality rule with the information that is present in the request.
[**find_data_quality_rules**](DataQualityRulesApi.md#find_data_quality_rules) | **GET** /dataQualityRules | Returns data quality rules matching the given search criteria.
[**get_data_quality_rule**](DataQualityRulesApi.md#get_data_quality_rule) | **GET** /dataQualityRules/{dataQualityRuleId} | Returns the DataQualityRule identified by given id.
[**remove_data_quality_rule**](DataQualityRulesApi.md#remove_data_quality_rule) | **DELETE** /dataQualityRules/{dataQualityRuleId} | Removes the DataQualityRule identified by the given id.

# **add_data_quality_rule**
> DataQualityRuleImpl add_data_quality_rule(body=body)

Adds a new data quality rule.

Adds a new data quality rule.

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
api_instance = collibra_core.DataQualityRulesApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddDataQualityRuleRequest() # AddDataQualityRuleRequest |  (optional)

try:
    # Adds a new data quality rule.
    api_response = api_instance.add_data_quality_rule(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->add_data_quality_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDataQualityRuleRequest**](AddDataQualityRuleRequest.md)|  | [optional] 

### Return type

[**DataQualityRuleImpl**](DataQualityRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_data_quality_rule**
> DataQualityRuleImpl change_data_quality_rule(data_quality_rule_id, body=body)

Changes the data quality rule with the information that is present in the request.

Changes the data quality rule with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.DataQualityRulesApi(collibra_core.ApiClient(configuration))
data_quality_rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the data quality rule
body = collibra_core.ChangeDataQualityRuleRequest() # ChangeDataQualityRuleRequest |  (optional)

try:
    # Changes the data quality rule with the information that is present in the request.
    api_response = api_instance.change_data_quality_rule(data_quality_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->change_data_quality_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | [**str**](.md)| the unique identifier of the data quality rule | 
 **body** | [**ChangeDataQualityRuleRequest**](ChangeDataQualityRuleRequest.md)|  | [optional] 

### Return type

[**DataQualityRuleImpl**](DataQualityRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_data_quality_rules**
> DataQualityRulePagedResponse find_data_quality_rules(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, sort_field=sort_field, sort_order=sort_order)

Returns data quality rules matching the given search criteria.

Returns data quality rules matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned data quality rules satisfy all constraints that are specified in this search criteria. By default a result containing 1000 data quality rules is returned.

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
api_instance = collibra_core.DataQualityRulesApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
name = 'name_example' # str | The name of the dataquality rule to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to ANYWHERE)
sort_field = 'NAME' # str | The field that should be used as reference for sorting. (optional) (default to NAME)
sort_order = 'ASC' # str | The order of sorting. (optional) (default to ASC)

try:
    # Returns data quality rules matching the given search criteria.
    api_response = api_instance.find_data_quality_rules(offset=offset, limit=limit, count_limit=count_limit, name=name, name_match_mode=name_match_mode, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->find_data_quality_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **name** | **str**| The name of the dataquality rule to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to ANYWHERE]
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] [default to NAME]
 **sort_order** | **str**| The order of sorting. | [optional] [default to ASC]

### Return type

[**DataQualityRulePagedResponse**](DataQualityRulePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_quality_rule**
> DataQualityRuleImpl get_data_quality_rule(data_quality_rule_id)

Returns the DataQualityRule identified by given id.

Returns the DataQualityRule identified by given id.

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
api_instance = collibra_core.DataQualityRulesApi(collibra_core.ApiClient(configuration))
data_quality_rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the data quality rule

try:
    # Returns the DataQualityRule identified by given id.
    api_response = api_instance.get_data_quality_rule(data_quality_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->get_data_quality_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | [**str**](.md)| the unique identifier of the data quality rule | 

### Return type

[**DataQualityRuleImpl**](DataQualityRuleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_data_quality_rule**
> remove_data_quality_rule(data_quality_rule_id)

Removes the DataQualityRule identified by the given id.

Removes the DataQualityRule identified by the given id.

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
api_instance = collibra_core.DataQualityRulesApi(collibra_core.ApiClient(configuration))
data_quality_rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the unique identifier of the data quality rule

try:
    # Removes the DataQualityRule identified by the given id.
    api_instance.remove_data_quality_rule(data_quality_rule_id)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->remove_data_quality_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | [**str**](.md)| the unique identifier of the data quality rule | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

