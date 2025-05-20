# collibra_core.DomainsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain**](DomainsApi.md#add_domain) | **POST** /domains | Add domain
[**add_domains**](DomainsApi.md#add_domains) | **POST** /domains/bulk | Add multpile domains
[**change_domain**](DomainsApi.md#change_domain) | **PATCH** /domains/{domainId} | Change domain
[**change_domains**](DomainsApi.md#change_domains) | **PATCH** /domains/bulk | Change multiple domains
[**find_domains**](DomainsApi.md#find_domains) | **GET** /domains | Search domains
[**get_domain**](DomainsApi.md#get_domain) | **GET** /domains/{domainId} | Get domain
[**get_domain_breadcrumb**](DomainsApi.md#get_domain_breadcrumb) | **GET** /domains/{domainId}/breadcrumb | Get domain breadcrumb
[**remove_domain**](DomainsApi.md#remove_domain) | **DELETE** /domains/{domainId} | Remove domain
[**remove_domains**](DomainsApi.md#remove_domains) | **DELETE** /domains/bulk | Remove multiple domains
[**remove_domains_in_job**](DomainsApi.md#remove_domains_in_job) | **POST** /domains/removalJobs | Remove multiple domains asynchronously

# **add_domain**
> DomainImpl add_domain(body=body)

Add domain

Adds a new domain with given data into a community.

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
body = collibra_core.AddDomainRequest() # AddDomainRequest | the properties of the domain to be added (optional)

try:
    # Add domain
    api_response = api_instance.add_domain(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->add_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddDomainRequest**](AddDomainRequest.md)| the properties of the domain to be added | [optional] 

### Return type

[**DomainImpl**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_domains**
> list[DomainImpl] add_domains(body=body)

Add multpile domains

Adds multiple domains using the given parameters

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
body = [collibra_core.AddDomainRequest()] # list[AddDomainRequest] | List of the properties of the domains to be added. (optional)

try:
    # Add multpile domains
    api_response = api_instance.add_domains(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->add_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[AddDomainRequest]**](AddDomainRequest.md)| List of the properties of the domains to be added. | [optional] 

### Return type

[**list[DomainImpl]**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domain**
> DomainImpl change_domain(domain_id, body=body)

Change domain

Changes the domain with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the ID of the domain to be changed.
body = collibra_core.ChangeDomainRequest() # ChangeDomainRequest | the properties of the domain to be changed (optional)

try:
    # Change domain
    api_response = api_instance.change_domain(domain_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->change_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| the ID of the domain to be changed. | 
 **body** | [**ChangeDomainRequest**](ChangeDomainRequest.md)| the properties of the domain to be changed | [optional] 

### Return type

[**DomainImpl**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domains**
> list[DomainImpl] change_domains(body=body)

Change multiple domains

Changes multiple domains using the given parameters

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
body = [collibra_core.ChangeDomainRequest()] # list[ChangeDomainRequest] | List of the properties of the domains to be changed. (optional)

try:
    # Change multiple domains
    api_response = api_instance.change_domains(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->change_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ChangeDomainRequest]**](ChangeDomainRequest.md)| List of the properties of the domains to be changed. | [optional] 

### Return type

[**list[DomainImpl]**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_domains**
> DomainPagedResponse find_domains(offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, name=name, name_match_mode=name_match_mode, exclude_meta=exclude_meta, community_id=community_id, type_id=type_id, include_sub_communities=include_sub_communities)

Search domains

Finds the domains that match the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 domains is returned.

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. (optional) (default to -1)
cursor = 'cursor_example' # str | Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (<code>nextCursor</code> property). (optional)
name = 'name_example' # str | The name of the domain to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. If the match mode is <code>EXACT</code> the search is case-sensitive, otherwise the search is case-insensitive. (optional) (default to ANYWHERE)
exclude_meta = true # bool | The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user). (optional) (default to true)
community_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the community to find the domains in (optional)
type_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the domain type to search for. Returned domains are of this type (optional)
include_sub_communities = false # bool | The include sub-communities flag. When set to true, sub-communities (of the community indicated via the <code>communityId</code> parameter) will be searched in. (optional) (default to false)

try:
    # Search domains
    api_response = api_instance.find_domains(offset=offset, limit=limit, count_limit=count_limit, cursor=cursor, name=name, name_match_mode=name_match_mode, exclude_meta=exclude_meta, community_id=community_id, type_id=type_id, include_sub_communities=include_sub_communities)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->find_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. Cursor should be preferred over offset for better performance and stable results. It is forbidden to use both in the same request. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. The maximum allowed limit is 1000. | [optional] [default to 0]
 **count_limit** | **int**| Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped. For cursor pagination this parameter is ignored and count is skipped. | [optional] [default to -1]
 **cursor** | **str**| Cursor for the current page of results. To retrieve the first page with cursor pagination you need to pass this parameter with an empty value (must be non-null). For the next pages, the value must be taken from the response (&lt;code&gt;nextCursor&lt;/code&gt; property). | [optional] 
 **name** | **str**| The name of the domain to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. If the match mode is &lt;code&gt;EXACT&lt;/code&gt; the search is case-sensitive, otherwise the search is case-insensitive. | [optional] [default to ANYWHERE]
 **exclude_meta** | **bool**| The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user). | [optional] [default to true]
 **community_id** | [**str**](.md)| The ID of the community to find the domains in | [optional] 
 **type_id** | [**str**](.md)| The ID of the domain type to search for. Returned domains are of this type | [optional] 
 **include_sub_communities** | **bool**| The include sub-communities flag. When set to true, sub-communities (of the community indicated via the &lt;code&gt;communityId&lt;/code&gt; parameter) will be searched in. | [optional] [default to false]

### Return type

[**DomainPagedResponse**](DomainPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> DomainImpl get_domain(domain_id)

Get domain

Returns the domain with the given ID

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the ID of the domain

try:
    # Get domain
    api_response = api_instance.get_domain(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| the ID of the domain | 

### Return type

[**DomainImpl**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_breadcrumb**
> list[NamedResourceReferenceImpl] get_domain_breadcrumb(domain_id)

Get domain breadcrumb

Returns the list of resources that lead to the domain identified by the given ID.

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
domain_id = 'domain_id_example' # str | The ID of the domain

try:
    # Get domain breadcrumb
    api_response = api_instance.get_domain_breadcrumb(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domain_breadcrumb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| The ID of the domain | 

### Return type

[**list[NamedResourceReferenceImpl]**](NamedResourceReferenceImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domain**
> remove_domain(domain_id)

Remove domain

This endpoint will be removed in the future. Please use POST /domains/removalJobs.

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
domain_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | the ID of the domain to remove

try:
    # Remove domain
    api_instance.remove_domain(domain_id)
except ApiException as e:
    print("Exception when calling DomainsApi->remove_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| the ID of the domain to remove | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domains**
> remove_domains(body=body)

Remove multiple domains

This endpoint will be removed in the future. Please use POST /domains/removalJobs.

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | the IDs of the domains to be removed, i.e. ["6f685f90-1036-4d30-983a-a9bbcdd7b8f6", "6f685f90-1036-4d30-983a-a9bbcdd7b123"] (optional)

try:
    # Remove multiple domains
    api_instance.remove_domains(body=body)
except ApiException as e:
    print("Exception when calling DomainsApi->remove_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| the IDs of the domains to be removed, i.e. [&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6&quot;, &quot;6f685f90-1036-4d30-983a-a9bbcdd7b123&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domains_in_job**
> Job remove_domains_in_job(body=body)

Remove multiple domains asynchronously

Removes multiple domains with the given IDs in a job.

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
api_instance = collibra_core.DomainsApi(collibra_core.ApiClient(configuration))
body = ['body_example'] # list[str] | the IDs of the domains to be removed, i.e. ["6f685f90-1036-4d30-983a-a9bbcdd7b8f6", "6f685f90-1036-4d30-983a-a9bbcdd7b123"] (optional)

try:
    # Remove multiple domains asynchronously
    api_response = api_instance.remove_domains_in_job(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->remove_domains_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| the IDs of the domains to be removed, i.e. [&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6&quot;, &quot;6f685f90-1036-4d30-983a-a9bbcdd7b123&quot;] | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

