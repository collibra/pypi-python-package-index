# ChangeUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The new enabled flag for the user | [optional] 
**username** | **str** | The new username for the user | [optional] 
**first_name** | **str** | The new first name for the user | [optional] 
**last_name** | **str** | The new last name for the user | [optional] 
**email** | **str** | The new e-mail address for the user | [optional] 
**gender** | **str** | The new gender for the user | [optional] 
**language** | **str** | The new language for the user | [optional] 
**license_type** | **str** | The license type of the user. This represents the given license which is no longer used. | [optional] 
**addresses** | [**list[Address]**](Address.md) | The postal addresses of the user | [optional] 
**phones** | [**list[PhoneNumber]**](PhoneNumber.md) | The phone numbers of the user | [optional] 
**additional_email_addresses** | [**list[Email]**](Email.md) | The additional e-mail addresses of the user | [optional] 
**instant_messaging_accounts** | [**list[InstantMessagingAccount]**](InstantMessagingAccount.md) | The instant messaging accounts of the user | [optional] 
**websites** | [**list[Website]**](Website.md) | The websites of the user | [optional] 
**password_confirmation** | **str** | The password confirmation for the user when changing their own email. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

