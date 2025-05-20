# collibra_core.AuthenticationSessionsApi

All URIs are relative to */rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**current_session**](AuthenticationSessionsApi.md#current_session) | **GET** /auth/sessions/current | Get session
[**heartbeat**](AuthenticationSessionsApi.md#heartbeat) | **GET** /auth/sessions/heartbeat | Checks if the user session is active
[**login**](AuthenticationSessionsApi.md#login) | **POST** /auth/sessions | Login
[**logout**](AuthenticationSessionsApi.md#logout) | **DELETE** /auth/sessions/current | Logout

# **current_session**
> current_session(include=include)

Get session

Gets current session (checks if user is logged in).

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_core.AuthenticationSessionsApi()
include = ['include_example'] # list[str] | Specify additional objects to include in the session response. Supports 'csrfToken' and 'user'. Multiple inclusions may be specified using additional 'include' query parameters or by comma-separated list. (optional)

try:
    # Get session
    api_instance.current_session(include=include)
except ApiException as e:
    print("Exception when calling AuthenticationSessionsApi->current_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify additional objects to include in the session response. Supports &#x27;csrfToken&#x27; and &#x27;user&#x27;. Multiple inclusions may be specified using additional &#x27;include&#x27; query parameters or by comma-separated list. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **heartbeat**
> heartbeat()

Checks if the user session is active

Returns 200 if user session is active and 401 if the session is expired or doesn't exist

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_core.AuthenticationSessionsApi()

try:
    # Checks if the user session is active
    api_instance.heartbeat()
except ApiException as e:
    print("Exception when calling AuthenticationSessionsApi->heartbeat: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> DGCSession login(body=body)

Login

Authenticates a user and creates a new session on the server. Once the user is authenticated then the returned session id can be used to access DGC REST Api in subsequent requests. The method additionally returns the JSESSIONID cookie in a <code>Set-Cookie</code> header. If user already has an open session then this session will be terminated.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_core.AuthenticationSessionsApi()
body = collibra_core.LoginRequest() # LoginRequest |  (optional)

try:
    # Login
    api_response = api_instance.login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSessionsApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginRequest**](LoginRequest.md)|  | [optional] 

### Return type

[**DGCSession**](DGCSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Logout

Logs current user out and destroys the active session.

### Example
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_core.AuthenticationSessionsApi()

try:
    # Logout
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthenticationSessionsApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

