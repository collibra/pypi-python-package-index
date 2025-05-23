# collibra-catalog_classification_200
Version 2 of the Catalog Classification API offers functionality related to the classification process and facilitates searching for and managing the associations between a data class and a data category. Use version 1 of the API for managing classifications and legacy data classes. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0-unstable
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
import collibra_catalog_classification 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import collibra_catalog_classification
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to */rest/catalogClassification/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClassificationDataCategoryApi* | [**connect_data_category_data_class**](docs/ClassificationDataCategoryApi.md#connect_data_category_data_class) | **POST** /dataClasses/{dataClassId}/dataCategories | Associate data class with data category
*ClassificationDataCategoryApi* | [**disconnect_data_category_data_class**](docs/ClassificationDataCategoryApi.md#disconnect_data_category_data_class) | **DELETE** /dataClasses/{dataClassId}/dataCategories/{dataCategoryId} | Remove existing association between a data class and a data category
*ClassificationDataCategoryApi* | [**get_association_data_class_data_category**](docs/ClassificationDataCategoryApi.md#get_association_data_class_data_category) | **GET** /dataClasses/dataCategories | Retrieve the association with a data category and a data class.
*ClassificationProcessApi* | [**start_classification_process**](docs/ClassificationProcessApi.md#start_classification_process) | **POST** /classify | Starts a process that classifies requested assets.

## Documentation For Models

 - [Classification](docs/Classification.md)
 - [ClassificationProcessRequest](docs/ClassificationProcessRequest.md)
 - [ClassificationProcessResponse](docs/ClassificationProcessResponse.md)
 - [DataClassDataCategoryConnection](docs/DataClassDataCategoryConnection.md)
 - [DataClassDataCategoryConnectionsPagedResponse](docs/DataClassDataCategoryConnectionsPagedResponse.md)
 - [NamedResourceReferenceImpl](docs/NamedResourceReferenceImpl.md)
 - [ResourceType](docs/ResourceType.md)
 - [StandardErrorResponse](docs/StandardErrorResponse.md)

## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author


