# collibra_management_console.UserApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add2**](UserApi.md#add2) | **POST** /user | Create a new user
[**change_role**](UserApi.md#change_role) | **PUT** /user/{userId}/role | Change the role of a user
[**find_all6**](UserApi.md#find_all6) | **GET** /user | List all users
[**get_by_id6**](UserApi.md#get_by_id6) | **GET** /user/{userId} | Get a user by ID
[**get_by_user_name**](UserApi.md#get_by_user_name) | **GET** /user/name/{userName} | Get a user by user name
[**get_password_policy**](UserApi.md#get_password_policy) | **GET** /user/passwordPolicy | Get password policy
[**get_password_policy1**](UserApi.md#get_password_policy1) | **GET** /user/passwordReset/passwordPolicy | Get password policy per token
[**remove5**](UserApi.md#remove5) | **DELETE** /user/{userId} | Delete a user
[**reset_password_request**](UserApi.md#reset_password_request) | **POST** /user/passwordReset/request | Request an email for a user to reset his password

# **add2**
> UserModel add2(body=body)

Create a new user

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()
body = collibra_management_console.UserModel() # UserModel | The model for the user to create (optional)

try:
    # Create a new user
    api_response = api_instance.add2(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->add2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserModel**](UserModel.md)| The model for the user to create | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_role**
> UserModel change_role(user_id, role=role)

Change the role of a user

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target user
role = 'role_example' # str | The new role for the target user (optional)

try:
    # Change the role of a user
    api_response = api_instance.change_role(user_id, role=role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->change_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| The ID of the target user | 
 **role** | **str**| The new role for the target user | [optional] 

### Return type

[**UserModel**](UserModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all6**
> list[UserModel] find_all6()

List all users

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()

try:
    # List all users
    api_response = api_instance.find_all6()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->find_all6: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserModel]**](UserModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id6**
> get_by_id6(user_id)

Get a user by ID

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target user

try:
    # Get a user by ID
    api_instance.get_by_id6(user_id)
except ApiException as e:
    print("Exception when calling UserApi->get_by_id6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| The ID of the target user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_user_name**
> get_by_user_name(user_name)

Get a user by user name

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()
user_name = 'user_name_example' # str | The username to look for

try:
    # Get a user by user name
    api_instance.get_by_user_name(user_name)
except ApiException as e:
    print("Exception when calling UserApi->get_by_user_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_name** | **str**| The username to look for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_policy**
> PasswordPolicyModel get_password_policy()

Get password policy

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()

try:
    # Get password policy
    api_response = api_instance.get_password_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_password_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PasswordPolicyModel**](PasswordPolicyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_policy1**
> PasswordPolicyModel get_password_policy1(token=token)

Get password policy per token

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()
token = 'token_example' # str |  (optional)

try:
    # Get password policy per token
    api_response = api_instance.get_password_policy1(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_password_policy1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | [optional] 

### Return type

[**PasswordPolicyModel**](PasswordPolicyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove5**
> remove5(user_id)

Delete a user

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the target user

try:
    # Delete a user
    api_instance.remove5(user_id)
except ApiException as e:
    print("Exception when calling UserApi->remove5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)| The ID of the target user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_request**
> reset_password_request(email=email)

Request an email for a user to reset his password

### Example
```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.UserApi()
email = 'email_example' # str |  (optional)

try:
    # Request an email for a user to reset his password
    api_instance.reset_password_request(email=email)
except ApiException as e:
    print("Exception when calling UserApi->reset_password_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

