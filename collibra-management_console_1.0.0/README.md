# collibra-management_console_100
Collibra Management Console public REST API \\n Please ensure that cookies are not present within the API request. Including cookies within the call will cause 403 error.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import collibra_management_console 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import collibra_management_console
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import collibra_management_console
from collibra_management_console.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment to backup
body = collibra_management_console.BackupSpecificationModel() # BackupSpecificationModel | The specification for the backup to create (optional)

try:
    # Create a backup for the specified environment
    api_response = api_instance.backup(environment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->backup: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the backup to delete

try:
    # Delete a backup
    api_instance.delete_backup(id)
except ApiException as e:
    print("Exception when calling BackupApi->delete_backup: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))

try:
    # List all backups
    api_response = api_instance.find_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->find_all: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
backup_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the backup to retrieve

try:
    # Get a backup by ID
    api_response = api_instance.get_by_id(backup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->get_by_id: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment

try:
    # Get the state of the current backup for the specified environment
    api_instance.get_current_state_map(environment_id)
except ApiException as e:
    print("Exception when calling BackupApi->get_current_state_map: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The backup id
key = 'key_example' # str |  (optional)

try:
    # Download a backup file
    api_instance.get_file(id, key=key)
except ApiException as e:
    print("Exception when calling BackupApi->get_file: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
environment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The ID of the environment

try:
    # Get the global status of the current backup for the specified environment
    api_response = api_instance.is_environment_backing_up(environment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->is_environment_backing_up: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
description = 'description_example' # str |  (optional)
name = 'name_example' # str |  (optional)

try:
    # Update name and/or description of an existing backup
    api_instance.update_backup_information(id, description=description, name=name)
except ApiException as e:
    print("Exception when calling BackupApi->update_backup_information: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
body = collibra_management_console.BackupBody() # BackupBody |  (optional)

try:
    # Upload a backup file
    api_response = api_instance.upload_backup(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackupApi->upload_backup: %s\n" % e)

# create an instance of the API class
api_instance = collibra_management_console.BackupApi(collibra_management_console.ApiClient(configuration))
body = collibra_management_console.BackupAsyncBody() # BackupAsyncBody |  (optional)

try:
    # Upload a backup file and process it asynchronously
    api_instance.upload_backup_async_validation(body=body)
except ApiException as e:
    print("Exception when calling BackupApi->upload_backup_async_validation: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BackupApi* | [**backup**](docs/BackupApi.md#backup) | **POST** /backup/{environmentId} | Create a backup for the specified environment
*BackupApi* | [**delete_backup**](docs/BackupApi.md#delete_backup) | **DELETE** /backup/file/{id} | Delete a backup
*BackupApi* | [**find_all**](docs/BackupApi.md#find_all) | **GET** /backup | List all backups
*BackupApi* | [**get_by_id**](docs/BackupApi.md#get_by_id) | **GET** /backup/id/{backupId} | Get a backup by ID
*BackupApi* | [**get_current_state_map**](docs/BackupApi.md#get_current_state_map) | **GET** /backup/{environmentId}/state | Get the state of the current backup for the specified environment
*BackupApi* | [**get_file**](docs/BackupApi.md#get_file) | **POST** /backup/file/{id} | Download a backup file
*BackupApi* | [**is_environment_backing_up**](docs/BackupApi.md#is_environment_backing_up) | **GET** /backup/{environmentId}/globalState | Get the global status of the current backup for the specified environment
*BackupApi* | [**update_backup_information**](docs/BackupApi.md#update_backup_information) | **POST** /backup/{id}/backupinformation | Update name and/or description of an existing backup
*BackupApi* | [**upload_backup**](docs/BackupApi.md#upload_backup) | **POST** /backup | Upload a backup file
*BackupApi* | [**upload_backup_async_validation**](docs/BackupApi.md#upload_backup_async_validation) | **POST** /backup/async | Upload a backup file and process it asynchronously
*BackupScheduleApi* | [**create**](docs/BackupScheduleApi.md#create) | **POST** /backupSchedule | Create a backup schedule
*BackupScheduleApi* | [**delete**](docs/BackupScheduleApi.md#delete) | **DELETE** /backupSchedule/{id} | Delete a backup schedule
*BackupScheduleApi* | [**get_all**](docs/BackupScheduleApi.md#get_all) | **GET** /backupSchedule | Retrieve all backup schedules
*BackupScheduleApi* | [**get_backups_by_schedule_id**](docs/BackupScheduleApi.md#get_backups_by_schedule_id) | **GET** /backupSchedule/{id}/backups | Retrieve all backups created by a backup schedule
*BackupScheduleApi* | [**get_by_environment_id**](docs/BackupScheduleApi.md#get_by_environment_id) | **GET** /backupSchedule/environment/{environmentId} | Retrieve all backup schedules for the given environment
*BackupScheduleApi* | [**get_by_id1**](docs/BackupScheduleApi.md#get_by_id1) | **GET** /backupSchedule/{id} | Retrieve a backup schedule
*BackupScheduleApi* | [**update**](docs/BackupScheduleApi.md#update) | **PUT** /backupSchedule/{id} | Update a backup schedule
*ConsoleConfigurationApi* | [**get_configuration**](docs/ConsoleConfigurationApi.md#get_configuration) | **GET** /console/configuration | Get the console configuration.
*ConsoleConfigurationApi* | [**get_console_jvm_configuration**](docs/ConsoleConfigurationApi.md#get_console_jvm_configuration) | **GET** /console/configuration/jvm | Get Console&#x27;s JVM configuration. Requires super role.
*ConsoleConfigurationApi* | [**restore_defaults**](docs/ConsoleConfigurationApi.md#restore_defaults) | **POST** /console/configuration/jvm/restoreDefaults | Restore Console&#x27;s JVM configuration to default. Requires super role.
*ConsoleConfigurationApi* | [**update_console_jvm_configuration**](docs/ConsoleConfigurationApi.md#update_console_jvm_configuration) | **POST** /console/configuration/jvm | Update Console&#x27;s JVM configuration. Requires super role.
*ConsoleConfigurationApi* | [**update_console_jvm_with_json**](docs/ConsoleConfigurationApi.md#update_console_jvm_with_json) | **POST** /console/configuration/jvm/json | Update Console&#x27;s JVM configuration with JSON. Requires super role.
*ConsoleSamlApi* | [**change_certificate**](docs/ConsoleSamlApi.md#change_certificate) | **POST** /samlconsole/certificate | Changes the certificate to be used with SAML
*ConsoleSamlApi* | [**delete_certificate**](docs/ConsoleSamlApi.md#delete_certificate) | **DELETE** /samlconsole/certificate | Delete the specified SAML certificate from the SAML keystore.
*ConsoleSamlApi* | [**get_file1**](docs/ConsoleSamlApi.md#get_file1) | **GET** /samlconsole | Download the saml.xml configuration file
*ConsoleSamlApi* | [**get_sp_metadata_as_string**](docs/ConsoleSamlApi.md#get_sp_metadata_as_string) | **GET** /samlconsole/metadata | Returns the SAML Service Provider metadata for this instance.
*ConsoleSamlApi* | [**remove**](docs/ConsoleSamlApi.md#remove) | **DELETE** /samlconsole | Remove the saml.xml configuration file
*ConsoleSamlApi* | [**upload_file**](docs/ConsoleSamlApi.md#upload_file) | **POST** /samlconsole | Update the saml.xml configuration by uploading a new file
*DgcConfigurationApi* | [**get_application_server_configuration1**](docs/DgcConfigurationApi.md#get_application_server_configuration1) | **GET** /dgc/configuration/applicationServer/{nodeId} | Get DGC&#x27;s Application Server configuration.
*DgcConfigurationApi* | [**get_jvm_configuration**](docs/DgcConfigurationApi.md#get_jvm_configuration) | **GET** /dgc/configuration/jvm/{managedServiceId} | Get DGC&#x27;s JVM configuration. Requires super role.
*DgcConfigurationApi* | [**restore_default_application_server_configuration1**](docs/DgcConfigurationApi.md#restore_default_application_server_configuration1) | **POST** /dgc/configuration/applicationServer/{nodeId}/restoreDefaults | Restore DGC&#x27;s Application Server configuration to default. Requires super role.
*DgcConfigurationApi* | [**restore_default_jvm_configuration**](docs/DgcConfigurationApi.md#restore_default_jvm_configuration) | **POST** /dgc/configuration/jvm/{managedServiceId}/restoreDefaults | Restore DGC&#x27;s JVM configuration to default
*DgcConfigurationApi* | [**update_application_server_configuration1**](docs/DgcConfigurationApi.md#update_application_server_configuration1) | **POST** /dgc/configuration/applicationServer/{nodeId} | Update DGC&#x27;s Application Server configuration.
*DgcConfigurationApi* | [**update_application_server_configuration_with_json1**](docs/DgcConfigurationApi.md#update_application_server_configuration_with_json1) | **POST** /dgc/configuration/applicationServer/{nodeId}/json | Update DGC&#x27;s Application Server configuration with JSON.
*DgcConfigurationApi* | [**update_jvm_configuration**](docs/DgcConfigurationApi.md#update_jvm_configuration) | **POST** /dgc/configuration/jvm/{managedServiceId} | Update DGC&#x27;s JVM configuration. Requires super role.
*DgcConfigurationApi* | [**update_jvm_configuration_with_json**](docs/DgcConfigurationApi.md#update_jvm_configuration_with_json) | **POST** /dgc/configuration/jvm/{managedServiceId}/json | Update DGC&#x27;s JVM configuration with JSON. Requires super role.
*DgcLicenseApi* | [**update_license**](docs/DgcLicenseApi.md#update_license) | **POST** /license/{environmentId}/licenseText | Update the license by providing the content of the new license file
*DgcLicenseApi* | [**update_license1**](docs/DgcLicenseApi.md#update_license1) | **POST** /license/{environmentId}/licenseFile | Update the license by uploading a new license file
*DgcLoggerApi* | [**delete_logger_level**](docs/DgcLoggerApi.md#delete_logger_level) | **DELETE** /dgcLog/{managedServiceId}/{logger} | Remove the given DGC logger
*DgcLoggerApi* | [**get_logger_level**](docs/DgcLoggerApi.md#get_logger_level) | **GET** /dgcLog/{managedServiceId}/{logger} | Retrieve the level of the given DGC logger
*DgcLoggerApi* | [**set_logger_level**](docs/DgcLoggerApi.md#set_logger_level) | **POST** /dgcLog | Adjust the level of the given DGC logger
*DgcSamlApi* | [**get_content**](docs/DgcSamlApi.md#get_content) | **GET** /saml/{environmentId} | Get the contents of the saml.xml configuration file
*DgcSamlApi* | [**get_file2**](docs/DgcSamlApi.md#get_file2) | **GET** /saml/{environmentId}/file | Download the saml.xml configuration file
*DgcSamlApi* | [**remove1**](docs/DgcSamlApi.md#remove1) | **DELETE** /saml/{environmentId} | Remove the saml.xml configuration file
*DgcSamlApi* | [**upload_file1**](docs/DgcSamlApi.md#upload_file1) | **POST** /saml/{environmentId}/file | Update the saml.xml configuration by uploading a new file
*EnvironmentApi* | [**add**](docs/EnvironmentApi.md#add) | **POST** /environment | Create a new environment
*EnvironmentApi* | [**add_service**](docs/EnvironmentApi.md#add_service) | **POST** /environment/{environmentId}/add/{managedServiceId} | Add a managed service to an environment
*EnvironmentApi* | [**add_service_provider**](docs/EnvironmentApi.md#add_service_provider) | **POST** /environment/{environmentId}/addServiceProvider/{serviceProviderId} | Add a service provider to an environment
*EnvironmentApi* | [**change**](docs/EnvironmentApi.md#change) | **PUT** /environment/{environmentId} | Change an existing environment
*EnvironmentApi* | [**find_all1**](docs/EnvironmentApi.md#find_all1) | **GET** /environment | List all environments
*EnvironmentApi* | [**get_by_id2**](docs/EnvironmentApi.md#get_by_id2) | **GET** /environment/{environmentId} | Get an environment by ID
*EnvironmentApi* | [**remove2**](docs/EnvironmentApi.md#remove2) | **DELETE** /environment/{environmentId} | Delete an environment
*EnvironmentApi* | [**remove_service**](docs/EnvironmentApi.md#remove_service) | **POST** /environment/{environmentId}/remove/{serviceProviderId} | Remove a service provider from an environment
*EnvironmentApi* | [**start**](docs/EnvironmentApi.md#start) | **POST** /environment/{environmentId}/start | Start an environment
*EnvironmentApi* | [**stop**](docs/EnvironmentApi.md#stop) | **POST** /environment/{environmentId}/stop | Stop an environment
*JobserverConfigurationApi* | [**get_jobserver_context_jvm_configuration**](docs/JobserverConfigurationApi.md#get_jobserver_context_jvm_configuration) | **GET** /spark/configuration/contextJvm/{managedServiceId} | Get Jobserver&#x27;s Monitoring JVM configuration. Requires super role.
*JobserverConfigurationApi* | [**get_jobserver_jvm_configuration**](docs/JobserverConfigurationApi.md#get_jobserver_jvm_configuration) | **GET** /spark/configuration/jvm/{managedServiceId} | Get Jobserver&#x27;s JVM configuration. Requires super role.
*JobserverConfigurationApi* | [**get_jobserver_server_configuration**](docs/JobserverConfigurationApi.md#get_jobserver_server_configuration) | **GET** /spark/configuration/server/{managedServiceId} | Get Jobserver&#x27;s Server configuration. 
*JobserverConfigurationApi* | [**get_jobserver_server_configuration_definition**](docs/JobserverConfigurationApi.md#get_jobserver_server_configuration_definition) | **GET** /spark/configuration/server/definition | Get Jobserver&#x27;s Server configuration definition. 
*JobserverConfigurationApi* | [**overwrite_jobserver_server_configuration**](docs/JobserverConfigurationApi.md#overwrite_jobserver_server_configuration) | **POST** /spark/configuration/server/{managedServiceId} | Overwrite Jobserver&#x27;s JVM configuration. Requires super role.
*JobserverConfigurationApi* | [**restore_default_jobserver_context_jvm_configuration**](docs/JobserverConfigurationApi.md#restore_default_jobserver_context_jvm_configuration) | **POST** /spark/configuration/contextJvm/{managedServiceId}/restoreDefaults | Restore Jobserver&#x27;s Monitoring JVM configuration to default. Requires super role.
*JobserverConfigurationApi* | [**restore_default_jobserver_jvm_configuration**](docs/JobserverConfigurationApi.md#restore_default_jobserver_jvm_configuration) | **POST** /spark/configuration/jvm/{managedServiceId}/restoreDefaults | Restore Jobserver&#x27;s JVM configuration to default. Requires super role.
*JobserverConfigurationApi* | [**restore_default_jobserver_server_configuration**](docs/JobserverConfigurationApi.md#restore_default_jobserver_server_configuration) | **POST** /spark/configuration/server/{managedServiceId}/restoreDefaults | Get Jobserver&#x27;s Server configuration. 
*JobserverConfigurationApi* | [**update_jobserver_context_jvm_configuration**](docs/JobserverConfigurationApi.md#update_jobserver_context_jvm_configuration) | **POST** /spark/configuration/contextJvm/{managedServiceId} | Update Jobserver&#x27;s Monitoring JVM configuration. Requires super role.
*JobserverConfigurationApi* | [**update_jobserver_context_jvm_with_json**](docs/JobserverConfigurationApi.md#update_jobserver_context_jvm_with_json) | **POST** /spark/configuration/contextJvm/{managedServiceId}/json | Update Jobserver&#x27;s Monitoring JVM configuration with JSON. Requires super role.
*JobserverConfigurationApi* | [**update_jobserver_jvm_configuration**](docs/JobserverConfigurationApi.md#update_jobserver_jvm_configuration) | **POST** /spark/configuration/jvm/{managedServiceId} | Update Jobserver&#x27;s JVM configuration. Requires super role.
*JobserverConfigurationApi* | [**update_jobserver_jvm_with_json**](docs/JobserverConfigurationApi.md#update_jobserver_jvm_with_json) | **POST** /spark/configuration/jvm/{managedServiceId}/json | Update Jobserver&#x27;s JVM configuration with JSON. Requires super role.
*JobserverConfigurationApi* | [**update_jobserver_server_configuration_with_json**](docs/JobserverConfigurationApi.md#update_jobserver_server_configuration_with_json) | **POST** /spark/configuration/server/{managedServiceId}/json | Overwrite Jobserver&#x27;s JVM configuration. Requires super role.
*JvmApi* | [**get_configuration_definition1**](docs/JvmApi.md#get_configuration_definition1) | **GET** /jvm/definition | Get JVM configuration definition
*ManagedServicesApi* | [**change1**](docs/ManagedServicesApi.md#change1) | **PUT** /service/{managedServiceId} | Change an existing managed service
*ManagedServicesApi* | [**find_all2**](docs/ManagedServicesApi.md#find_all2) | **GET** /service | List all managed services
*ManagedServicesApi* | [**get_by_id3**](docs/ManagedServicesApi.md#get_by_id3) | **GET** /service/{managedServiceId} | Get a managed service by ID
*ManagedServicesApi* | [**start1**](docs/ManagedServicesApi.md#start1) | **POST** /service/{managedServiceId}/start | Start a managed service
*ManagedServicesApi* | [**stop1**](docs/ManagedServicesApi.md#stop1) | **POST** /service/{managedServiceId}/stop | Stop a managed service
*NodeApi* | [**add1**](docs/NodeApi.md#add1) | **POST** /node | Add a node
*NodeApi* | [**change2**](docs/NodeApi.md#change2) | **PUT** /node/{nodeId} | Change an existing node
*NodeApi* | [**find_all3**](docs/NodeApi.md#find_all3) | **GET** /node | List all nodes
*NodeApi* | [**get_by_id4**](docs/NodeApi.md#get_by_id4) | **GET** /node/{nodeId} | Get a node by ID
*NodeApi* | [**remove3**](docs/NodeApi.md#remove3) | **DELETE** /node/{nodeId} | Remove a node
*NodeApi* | [**status**](docs/NodeApi.md#status) | **GET** /node/{nodeId}/status | Get the status of a node
*NodeConfigurationApi* | [**get_node_jvm_configuration**](docs/NodeConfigurationApi.md#get_node_jvm_configuration) | **GET** /node/configuration/jvm/{nodeId} | Get Node&#x27;s JVM configuration. Requires super role.
*NodeConfigurationApi* | [**restore_default_node_jvm_configuration**](docs/NodeConfigurationApi.md#restore_default_node_jvm_configuration) | **POST** /node/configuration/jvm/{nodeId}/restoreDefaults | Restore Node&#x27;s JVM configuration to default. Requires super role.
*NodeConfigurationApi* | [**update_node_jvm_configuration**](docs/NodeConfigurationApi.md#update_node_jvm_configuration) | **POST** /node/configuration/jvm/{nodeId} | Update Node&#x27;s JVM configuration. Requires super role.
*NodeConfigurationApi* | [**update_node_jvm_with_json**](docs/NodeConfigurationApi.md#update_node_jvm_with_json) | **POST** /node/configuration/jvm/{nodeId}/json | Update Node&#x27;s JVM configuration with JSON. Requires super role.
*RestoreApi* | [**cancel_restore**](docs/RestoreApi.md#cancel_restore) | **PUT** /restore/{environmentId}/cancel | Cancel a restore operation in progress
*RestoreApi* | [**restore_backup_from_id**](docs/RestoreApi.md#restore_backup_from_id) | **POST** /restore/{environmentId} | Restore a backup to an environment
*RestoreApi* | [**restore_to_factory_defaults**](docs/RestoreApi.md#restore_to_factory_defaults) | **POST** /restore/{environmentId}/factoryDefaults | Restore an environment to factory defaults
*RestoreApi* | [**state_map**](docs/RestoreApi.md#state_map) | **GET** /restore/{environmentId}/state | Retrieve the state of all steps of the restore operation on a specified environment
*ServiceProviderApi* | [**add_slave_to_repository_cluster**](docs/ServiceProviderApi.md#add_slave_to_repository_cluster) | **POST** /serviceProvider/repositorycluster/{serviceProviderId}/addSlave/{managedServiceId} | Add a slave repository to a repository cluster
*ServiceProviderApi* | [**create_repository_cluster**](docs/ServiceProviderApi.md#create_repository_cluster) | **POST** /serviceProvider/repositorycluster/create | Create a new repository cluster
*ServiceProviderApi* | [**find_all4**](docs/ServiceProviderApi.md#find_all4) | **GET** /serviceProvider | List all service providers
*ServiceProviderApi* | [**get_by_id5**](docs/ServiceProviderApi.md#get_by_id5) | **GET** /serviceProvider/{serviceProviderId} | Get a service provider by ID
*ServiceProviderApi* | [**remove4**](docs/ServiceProviderApi.md#remove4) | **DELETE** /serviceProvider/{serviceProviderId} | Delete a service provider
*ServiceProviderApi* | [**remove_from_repository_cluster**](docs/ServiceProviderApi.md#remove_from_repository_cluster) | **POST** /serviceProvider/repositorycluster/{serviceProviderId}/remove/{managedServiceId} | Remove a repository from the cluster
*ServiceProviderApi* | [**set_master_in_repository_cluster**](docs/ServiceProviderApi.md#set_master_in_repository_cluster) | **POST** /serviceProvider/repositorycluster/{serviceProviderId}/setMaster/{managedServiceId} | Set the master repository of a repository cluster
*ServiceProviderApi* | [**start2**](docs/ServiceProviderApi.md#start2) | **POST** /serviceProvider/serviceProvider/{serviceProviderId}/start | Start a service provider
*ServiceProviderApi* | [**stop2**](docs/ServiceProviderApi.md#stop2) | **POST** /serviceProvider/serviceProvider/{serviceProviderId}/stop | Stop a service provider
*SupportApi* | [**create_support_file**](docs/SupportApi.md#create_support_file) | **POST** /support/{environmentId}/zip | Create a diagnostic file for a specified environment
*SupportApi* | [**delete_support_file**](docs/SupportApi.md#delete_support_file) | **DELETE** /support/{id} | Delete a diagnostic file
*SupportApi* | [**find_all5**](docs/SupportApi.md#find_all5) | **GET** /support | List all diagnostic files
*SupportApi* | [**get_file3**](docs/SupportApi.md#get_file3) | **GET** /support/{id} | Download a diagnostic file
*UserApi* | [**add2**](docs/UserApi.md#add2) | **POST** /user | Create a new user
*UserApi* | [**change_role**](docs/UserApi.md#change_role) | **PUT** /user/{userId}/role | Change the role of a user
*UserApi* | [**find_all6**](docs/UserApi.md#find_all6) | **GET** /user | List all users
*UserApi* | [**get_by_id6**](docs/UserApi.md#get_by_id6) | **GET** /user/{userId} | Get a user by ID
*UserApi* | [**get_by_user_name**](docs/UserApi.md#get_by_user_name) | **GET** /user/name/{userName} | Get a user by user name
*UserApi* | [**get_password_policy**](docs/UserApi.md#get_password_policy) | **GET** /user/passwordPolicy | Get password policy
*UserApi* | [**get_password_policy1**](docs/UserApi.md#get_password_policy1) | **GET** /user/passwordReset/passwordPolicy | Get password policy per token
*UserApi* | [**remove5**](docs/UserApi.md#remove5) | **DELETE** /user/{userId} | Delete a user
*UserApi* | [**reset_password_request**](docs/UserApi.md#reset_password_request) | **POST** /user/passwordReset/request | Request an email for a user to reset his password

## Documentation For Models

 - [AjpConnectorConfiguration](docs/AjpConnectorConfiguration.md)
 - [ApplicationServerConfiguration](docs/ApplicationServerConfiguration.md)
 - [AttributeFields](docs/AttributeFields.md)
 - [BackupAsyncBody](docs/BackupAsyncBody.md)
 - [BackupBody](docs/BackupBody.md)
 - [BackupConfiguration](docs/BackupConfiguration.md)
 - [BackupInformationModel](docs/BackupInformationModel.md)
 - [BackupModel](docs/BackupModel.md)
 - [BackupRetryConfiguration](docs/BackupRetryConfiguration.md)
 - [BackupScheduleConfiguration](docs/BackupScheduleConfiguration.md)
 - [BackupScheduleCreateRequest](docs/BackupScheduleCreateRequest.md)
 - [BackupScheduleModel](docs/BackupScheduleModel.md)
 - [BackupScheduleModelServerTimeZoneOffset](docs/BackupScheduleModelServerTimeZoneOffset.md)
 - [BackupScheduleModelServerTimeZoneOffsetRules](docs/BackupScheduleModelServerTimeZoneOffsetRules.md)
 - [BackupScheduleModelServerTimeZoneOffsetRulesDuration](docs/BackupScheduleModelServerTimeZoneOffsetRulesDuration.md)
 - [BackupScheduleModelServerTimeZoneOffsetRulesDurationUnits](docs/BackupScheduleModelServerTimeZoneOffsetRulesDurationUnits.md)
 - [BackupScheduleModelServerTimeZoneOffsetRulesOffsetAfter](docs/BackupScheduleModelServerTimeZoneOffsetRulesOffsetAfter.md)
 - [BackupScheduleModelServerTimeZoneOffsetRulesTransitionRules](docs/BackupScheduleModelServerTimeZoneOffsetRulesTransitionRules.md)
 - [BackupScheduleModelServerTimeZoneOffsetRulesTransitions](docs/BackupScheduleModelServerTimeZoneOffsetRulesTransitions.md)
 - [BackupScheduleUpdateRequest](docs/BackupScheduleUpdateRequest.md)
 - [BackupSpecificationModel](docs/BackupSpecificationModel.md)
 - [BaseField](docs/BaseField.md)
 - [BeanDefinition](docs/BeanDefinition.md)
 - [BodyPart](docs/BodyPart.md)
 - [BodyPartHeaders](docs/BodyPartHeaders.md)
 - [BodyPartParameterizedHeaders](docs/BodyPartParameterizedHeaders.md)
 - [ConsoleConfiguration](docs/ConsoleConfiguration.md)
 - [ConsoleDataSourceConfiguration](docs/ConsoleDataSourceConfiguration.md)
 - [ConsoleLdapConfiguration](docs/ConsoleLdapConfiguration.md)
 - [ConsoleLdapServer](docs/ConsoleLdapServer.md)
 - [ConsoleLdapUserFields](docs/ConsoleLdapUserFields.md)
 - [ContentDisposition](docs/ContentDisposition.md)
 - [CsrfConfiguration](docs/CsrfConfiguration.md)
 - [DGCManagedServiceModel](docs/DGCManagedServiceModel.md)
 - [EnvironmentConfiguration](docs/EnvironmentConfiguration.md)
 - [EnvironmentModel](docs/EnvironmentModel.md)
 - [FetchBackupRequest](docs/FetchBackupRequest.md)
 - [FileIdBody](docs/FileIdBody.md)
 - [FormDataBodyPart](docs/FormDataBodyPart.md)
 - [FormDataContentDisposition](docs/FormDataContentDisposition.md)
 - [FormDataMultiPart](docs/FormDataMultiPart.md)
 - [HeadersScopeConfiguration](docs/HeadersScopeConfiguration.md)
 - [HttpConnectorConfiguration](docs/HttpConnectorConfiguration.md)
 - [HttpsConnectorConfiguration](docs/HttpsConnectorConfiguration.md)
 - [IdBackupinformationBody](docs/IdBackupinformationBody.md)
 - [JobserverSecurityConfiguration](docs/JobserverSecurityConfiguration.md)
 - [JobserverServerConfiguration](docs/JobserverServerConfiguration.md)
 - [JvmConfiguration](docs/JvmConfiguration.md)
 - [LicenseInfoModel](docs/LicenseInfoModel.md)
 - [LocalTime](docs/LocalTime.md)
 - [MailConfiguration](docs/MailConfiguration.md)
 - [ManagedServiceConfiguration](docs/ManagedServiceConfiguration.md)
 - [ManagedServiceModel](docs/ManagedServiceModel.md)
 - [ManagedServiceStatus](docs/ManagedServiceStatus.md)
 - [MediaType](docs/MediaType.md)
 - [MessageBodyWorkers](docs/MessageBodyWorkers.md)
 - [MonitoringValueModelLong](docs/MonitoringValueModelLong.md)
 - [MonitoringValueModelMutableMemoryUsage](docs/MonitoringValueModelMutableMemoryUsage.md)
 - [MultiPart](docs/MultiPart.md)
 - [MultivaluedMapStringParameterizedHeader](docs/MultivaluedMapStringParameterizedHeader.md)
 - [MultivaluedMapStringString](docs/MultivaluedMapStringString.md)
 - [MutableMemoryUsage](docs/MutableMemoryUsage.md)
 - [NodeConfiguration](docs/NodeConfiguration.md)
 - [NodeModel](docs/NodeModel.md)
 - [ParameterizedHeader](docs/ParameterizedHeader.md)
 - [PasswordConfiguration](docs/PasswordConfiguration.md)
 - [PasswordPolicyModel](docs/PasswordPolicyModel.md)
 - [PasswordResetRequestBody](docs/PasswordResetRequestBody.md)
 - [PgHbaConfiguration](docs/PgHbaConfiguration.md)
 - [PostgresqlAuthorizationFileRow](docs/PostgresqlAuthorizationFileRow.md)
 - [Providers](docs/Providers.md)
 - [ReplicationStateModel](docs/ReplicationStateModel.md)
 - [ResourcesConfiguration](docs/ResourcesConfiguration.md)
 - [RestoreSpecificationModel](docs/RestoreSpecificationModel.md)
 - [SamlConfiguration](docs/SamlConfiguration.md)
 - [SamlRequestedAuthnContextConfiguration](docs/SamlRequestedAuthnContextConfiguration.md)
 - [SamlconsoleCertificateBody](docs/SamlconsoleCertificateBody.md)
 - [SearchConfiguration](docs/SearchConfiguration.md)
 - [SecurityConfiguration](docs/SecurityConfiguration.md)
 - [SecurityHeadersConfiguration](docs/SecurityHeadersConfiguration.md)
 - [ServiceProviderModel](docs/ServiceProviderModel.md)
 - [SessionConfiguration](docs/SessionConfiguration.md)
 - [SetLoggerLevelRequest](docs/SetLoggerLevelRequest.md)
 - [SignoutConfiguration](docs/SignoutConfiguration.md)
 - [SsoConfiguration](docs/SsoConfiguration.md)
 - [StepStateModel](docs/StepStateModel.md)
 - [SupportModel](docs/SupportModel.md)
 - [SupportSpecificationModel](docs/SupportSpecificationModel.md)
 - [UiConfiguration](docs/UiConfiguration.md)
 - [UserModel](docs/UserModel.md)
 - [WhitelistConfiguration](docs/WhitelistConfiguration.md)
 - [WhitelistDomain](docs/WhitelistDomain.md)

## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author


