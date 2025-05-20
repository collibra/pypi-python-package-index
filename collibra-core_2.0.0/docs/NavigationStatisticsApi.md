# collibra_core.NavigationStatisticsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_most_viewed_assets**](NavigationStatisticsApi.md#find_most_viewed_assets) | **GET** /navigation/most_viewed | Find most viewed assets.
[**find_recently_viewed_assets**](NavigationStatisticsApi.md#find_recently_viewed_assets) | **GET** /navigation/recently_viewed | Find recently viewed assets.

# **find_most_viewed_assets**
> NavigationStatisticsEntryPagedResponse find_most_viewed_assets(offset=offset, limit=limit, count_limit=count_limit, period=period, is_guest_excluded=is_guest_excluded)

Find most viewed assets.

Returns the most viewed assets by all users, with navigation-related info.

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
api_instance = collibra_core.NavigationStatisticsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)
period = 0 # int | The time span for which most viewed assets should be found. This time span must be expressed in milliseconds.<br/>For instance, to get most viewed assets for last 24 hours, period would be <code>86400000</code>.<br/>If it's unset (period = 0) looks for all time most viewed assets. (optional) (default to 0)
is_guest_excluded = false # bool | Whether guest visits should be excluded from result. (optional) (default to false)

try:
    # Find most viewed assets.
    api_response = api_instance.find_most_viewed_assets(offset=offset, limit=limit, count_limit=count_limit, period=period, is_guest_excluded=is_guest_excluded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NavigationStatisticsApi->find_most_viewed_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]
 **period** | **int**| The time span for which most viewed assets should be found. This time span must be expressed in milliseconds.&lt;br/&gt;For instance, to get most viewed assets for last 24 hours, period would be &lt;code&gt;86400000&lt;/code&gt;.&lt;br/&gt;If it&#x27;s unset (period &#x3D; 0) looks for all time most viewed assets. | [optional] [default to 0]
 **is_guest_excluded** | **bool**| Whether guest visits should be excluded from result. | [optional] [default to false]

### Return type

[**NavigationStatisticsEntryPagedResponse**](NavigationStatisticsEntryPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_recently_viewed_assets**
> NavigationStatisticsEntryPagedResponse find_recently_viewed_assets(offset=offset, limit=limit, count_limit=count_limit)

Find recently viewed assets.

Returns the assets that were recently viewed by the current user.

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
api_instance = collibra_core.NavigationStatisticsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)

try:
    # Find recently viewed assets.
    api_response = api_instance.find_recently_viewed_assets(offset=offset, limit=limit, count_limit=count_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NavigationStatisticsApi->find_recently_viewed_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped | [optional] [default to -1]

### Return type

[**NavigationStatisticsEntryPagedResponse**](NavigationStatisticsEntryPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

