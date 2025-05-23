# collibra-import_200
<p>The Import API is an efficient way to load large volumes of data into the Collibra Data Governance Center. The API can automatically differentiate between creating and updating data.</p>

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0
- Package version: 2.0.0
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
import collibra_import 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import collibra_import
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import collibra_import
from collibra_import.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id of the operation.

try:
    # Removes all cache entries corresponding to the provided synchronization id.
    api_instance.evict_synchronization_cache(synchronization_id)
except ApiException as e:
    print("Exception when calling ImportApi->evict_synchronization_cache: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id of the operation.

try:
    # Checks whether given synchronization id already exists.
    api_response = api_instance.exists(synchronization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->exists: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. The maximum allowed limit is 1000. (optional) (default to 0)
count_limit = -1 # int | Allows to limit the number of elements that will be counted. -1 will count everything and 0 will cause the count to be skipped (optional) (default to -1)

try:
    # Returns synchronization information matching the given search criteria.
    api_response = api_instance.find_synchronization_infos(offset=offset, limit=limit, count_limit=count_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->find_synchronization_infos: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
separator = 'separator_example' # str |  (optional)
quote = 'quote_example' # str |  (optional)
escape = 'escape_example' # str |  (optional)
strict_quotes = true # bool |  (optional)
ignore_leading_whitespace = true # bool |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts import from the CSV file in job (asynchronously).
    api_response = api_instance.import_csv_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_csv_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
sheet_name = 'sheet_name_example' # str |  (optional)
sheet_index = 56 # int |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts import from the Excel file in job (asynchronously).
    api_response = api_instance.import_excel_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_excel_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
relations_action = 'relations_action_example' # str |  (optional)

try:
    # Starts import from the JSON file in job (asynchronously).
    api_response = api_instance.import_json_in_job(send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, relations_action=relations_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->import_json_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id of the operation.

try:
    # Removes all information about synchronization process corresponding to provided synchronization id.
    api_instance.remove_synchronization(synchronization_id)
except ApiException as e:
    print("Exception when calling ImportApi->remove_synchronization: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
separator = 'separator_example' # str |  (optional)
quote = 'quote_example' # str |  (optional)
escape = 'escape_example' # str |  (optional)
strict_quotes = true # bool |  (optional)
ignore_leading_whitespace = true # bool |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts batch synchronization from the CSV file in job (asynchronously).
    api_response = api_instance.synchronize_batch_csv_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_batch_csv_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
sheet_name = 'sheet_name_example' # str |  (optional)
sheet_index = 56 # int |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts batch synchronization from the Excel file in job (asynchronously).
    api_response = api_instance.synchronize_batch_excel_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_batch_excel_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
relations_action = 'relations_action_example' # str |  (optional)

try:
    # Starts batch synchronization from the JSON file in job (asynchronously).
    api_response = api_instance.synchronize_batch_json_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, relations_action=relations_action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_batch_json_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
finalization_strategy = 'finalization_strategy_example' # str |  (optional)
missing_asset_status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
separator = 'separator_example' # str |  (optional)
quote = 'quote_example' # str |  (optional)
escape = 'escape_example' # str |  (optional)
strict_quotes = true # bool |  (optional)
ignore_leading_whitespace = true # bool |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts full synchronization from the CSV file in job (asynchronously).
    api_response = api_instance.synchronize_csv_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, separator=separator, quote=quote, escape=escape, strict_quotes=strict_quotes, ignore_leading_whitespace=ignore_leading_whitespace, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_csv_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
finalization_strategy = 'finalization_strategy_example' # str |  (optional)
missing_asset_status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
sheet_name = 'sheet_name_example' # str |  (optional)
sheet_index = 56 # int |  (optional)
header_row = true # bool |  (optional)
template = 'template_example' # str |  (optional)

try:
    # Starts full synchronization from the Excel file in job (asynchronously).
    api_response = api_instance.synchronize_excel_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, sheet_name=sheet_name, sheet_index=sheet_index, header_row=header_row, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_excel_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization ID used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
finalization_strategy = 'finalization_strategy_example' # str |  (optional)
missing_asset_status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
finalization_parameters = {'key': 'finalization_parameters_example'} # dict(str, str) |  (optional)

try:
    # Starts synchronization finalization in job (asynchronously).
    api_response = api_instance.synchronize_finalize_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id, finalization_parameters=finalization_parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_finalize_in_job: %s\n" % e)
# Configure HTTP basic authorization: basicAuth
configuration = collibra_import.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = collibra_import.ImportApi(collibra_import.ApiClient(configuration))
synchronization_id = 'synchronization_id_example' # str | The synchronization id used to distinguish different synchronizations.
send_notification = true # bool |  (optional)
batch_size = 56 # int |  (optional)
simulation = true # bool |  (optional)
save_result = true # bool |  (optional)
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
file = 'file_example' # str |  (optional)
file_name = 'file_name_example' # str |  (optional)
delete_file = true # bool |  (optional)
continue_on_error = true # bool |  (optional)
finalization_strategy = 'finalization_strategy_example' # str |  (optional)
missing_asset_status_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)

try:
    # Starts full synchronization from the JSON file in job (asynchronously).
    api_response = api_instance.synchronize_json_in_job(synchronization_id, send_notification=send_notification, batch_size=batch_size, simulation=simulation, save_result=save_result, file_id=file_id, file=file, file_name=file_name, delete_file=delete_file, continue_on_error=continue_on_error, finalization_strategy=finalization_strategy, missing_asset_status_id=missing_asset_status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportApi->synchronize_json_in_job: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */rest/2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ImportApi* | [**evict_synchronization_cache**](docs/ImportApi.md#evict_synchronization_cache) | **DELETE** /import/synchronize/{synchronizationId}/evict | Removes all cache entries corresponding to the provided synchronization id.
*ImportApi* | [**exists**](docs/ImportApi.md#exists) | **GET** /import/synchronize/exists/{synchronizationId} | Checks whether given synchronization id already exists.
*ImportApi* | [**find_synchronization_infos**](docs/ImportApi.md#find_synchronization_infos) | **GET** /import/synchronize | Returns synchronization information matching the given search criteria.
*ImportApi* | [**import_csv_in_job**](docs/ImportApi.md#import_csv_in_job) | **POST** /import/csv-job | Starts import from the CSV file in job (asynchronously).
*ImportApi* | [**import_excel_in_job**](docs/ImportApi.md#import_excel_in_job) | **POST** /import/excel-job | Starts import from the Excel file in job (asynchronously).
*ImportApi* | [**import_json_in_job**](docs/ImportApi.md#import_json_in_job) | **POST** /import/json-job | Starts import from the JSON file in job (asynchronously).
*ImportApi* | [**remove_synchronization**](docs/ImportApi.md#remove_synchronization) | **DELETE** /import/synchronize/{synchronizationId} | Removes all information about synchronization process corresponding to provided synchronization id.
*ImportApi* | [**synchronize_batch_csv_in_job**](docs/ImportApi.md#synchronize_batch_csv_in_job) | **POST** /import/synchronize/{synchronizationId}/batch/csv-job | Starts batch synchronization from the CSV file in job (asynchronously).
*ImportApi* | [**synchronize_batch_excel_in_job**](docs/ImportApi.md#synchronize_batch_excel_in_job) | **POST** /import/synchronize/{synchronizationId}/batch/excel-job | Starts batch synchronization from the Excel file in job (asynchronously).
*ImportApi* | [**synchronize_batch_json_in_job**](docs/ImportApi.md#synchronize_batch_json_in_job) | **POST** /import/synchronize/{synchronizationId}/batch/json-job | Starts batch synchronization from the JSON file in job (asynchronously).
*ImportApi* | [**synchronize_csv_in_job**](docs/ImportApi.md#synchronize_csv_in_job) | **POST** /import/synchronize/{synchronizationId}/csv-job | Starts full synchronization from the CSV file in job (asynchronously).
*ImportApi* | [**synchronize_excel_in_job**](docs/ImportApi.md#synchronize_excel_in_job) | **POST** /import/synchronize/{synchronizationId}/excel-job | Starts full synchronization from the Excel file in job (asynchronously).
*ImportApi* | [**synchronize_finalize_in_job**](docs/ImportApi.md#synchronize_finalize_in_job) | **POST** /import/synchronize/{synchronizationId}/finalize/job | Starts synchronization finalization in job (asynchronously).
*ImportApi* | [**synchronize_json_in_job**](docs/ImportApi.md#synchronize_json_in_job) | **POST** /import/synchronize/{synchronizationId}/json-job | Starts full synchronization from the JSON file in job (asynchronously).
*ImportResultsApi* | [**find_import_errors**](docs/ImportResultsApi.md#find_import_errors) | **GET** /import/results/{jobId}/errors | List the errors of a finished import job
*ImportResultsApi* | [**get_import_job_summary**](docs/ImportResultsApi.md#get_import_job_summary) | **GET** /import/results/{jobId}/summary | Retrieve a summary of a finished import job

## Documentation For Models

 - [AnyOfImportJsonInJobRequest](docs/AnyOfImportJsonInJobRequest.md)
 - [AssetIdentifier](docs/AssetIdentifier.md)
 - [AssetImportCommand](docs/AssetImportCommand.md)
 - [AssetTypeIdentifier](docs/AssetTypeIdentifier.md)
 - [AttributeValue](docs/AttributeValue.md)
 - [BatchCsvjobBody](docs/BatchCsvjobBody.md)
 - [BatchExceljobBody](docs/BatchExceljobBody.md)
 - [BatchJsonjobBody](docs/BatchJsonjobBody.md)
 - [CategoryReference](docs/CategoryReference.md)
 - [CommunityIdentifier](docs/CommunityIdentifier.md)
 - [CommunityImportCommand](docs/CommunityImportCommand.md)
 - [ComplexRelationIdentifier](docs/ComplexRelationIdentifier.md)
 - [ComplexRelationImportCommand](docs/ComplexRelationImportCommand.md)
 - [ComplexRelationTypeIdentifier](docs/ComplexRelationTypeIdentifier.md)
 - [DomainIdentifier](docs/DomainIdentifier.md)
 - [DomainImportCommand](docs/DomainImportCommand.md)
 - [DomainTypeIdentifier](docs/DomainTypeIdentifier.md)
 - [ExternalIdentifier](docs/ExternalIdentifier.md)
 - [FinalizeJobBody](docs/FinalizeJobBody.md)
 - [FindSynchronizationRequest](docs/FindSynchronizationRequest.md)
 - [ImportCommandReference](docs/ImportCommandReference.md)
 - [ImportCounters](docs/ImportCounters.md)
 - [ImportCsvInJobRequest](docs/ImportCsvInJobRequest.md)
 - [ImportCsvjobBody](docs/ImportCsvjobBody.md)
 - [ImportError](docs/ImportError.md)
 - [ImportErrorPagedResponse](docs/ImportErrorPagedResponse.md)
 - [ImportExcelInJobRequest](docs/ImportExcelInJobRequest.md)
 - [ImportExceljobBody](docs/ImportExceljobBody.md)
 - [ImportJsonInJobRequest](docs/ImportJsonInJobRequest.md)
 - [ImportJsonjobBody](docs/ImportJsonjobBody.md)
 - [ImportSummary](docs/ImportSummary.md)
 - [Job](docs/Job.md)
 - [MappingIdentifier](docs/MappingIdentifier.md)
 - [MappingImportCommand](docs/MappingImportCommand.md)
 - [Owner](docs/Owner.md)
 - [PagedResponseImportError](docs/PagedResponseImportError.md)
 - [PagedResponseSynchronizationInfo](docs/PagedResponseSynchronizationInfo.md)
 - [ResourceTypeSummary](docs/ResourceTypeSummary.md)
 - [StatusIdentifier](docs/StatusIdentifier.md)
 - [SubcategorySummary](docs/SubcategorySummary.md)
 - [SynchronizationBatchCsvInJobRequest](docs/SynchronizationBatchCsvInJobRequest.md)
 - [SynchronizationBatchExcelInJobRequest](docs/SynchronizationBatchExcelInJobRequest.md)
 - [SynchronizationBatchJsonInJobRequest](docs/SynchronizationBatchJsonInJobRequest.md)
 - [SynchronizationCsvInJobRequest](docs/SynchronizationCsvInJobRequest.md)
 - [SynchronizationExcelInJobRequest](docs/SynchronizationExcelInJobRequest.md)
 - [SynchronizationFinalizationRequest](docs/SynchronizationFinalizationRequest.md)
 - [SynchronizationIdCsvjobBody](docs/SynchronizationIdCsvjobBody.md)
 - [SynchronizationIdExceljobBody](docs/SynchronizationIdExceljobBody.md)
 - [SynchronizationIdJsonjobBody](docs/SynchronizationIdJsonjobBody.md)
 - [SynchronizationInfo](docs/SynchronizationInfo.md)
 - [SynchronizationJsonInJobRequest](docs/SynchronizationJsonInJobRequest.md)
 - [UserGroupIdentifier](docs/UserGroupIdentifier.md)
 - [UserIdentifier](docs/UserIdentifier.md)

## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author


