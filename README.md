# Collibra Python Package Index

This repository contains Python client libraries for various Collibra APIs, automatically generated using Swagger Codegen.

## Repository Structure

- Each subdirectory (e.g., `collibra-core_2.0.0/`, `collibra-catalog_1.0.0/`, etc.) contains a Python package for a specific Collibra API or module.
- Each package includes:
  - Auto-generated Python client code
  - Documentation (`README.md`, `docs/`)
  - Example usage

## Available Packages

- **collibra-core_2.0.0**: Core Collibra REST API
- **collibra-catalog_1.0.0**: Catalog API for ingestion and management
- **collibra-catalog_classification_1.0.0**: Data classification API
- **collibra-catalog_cloud_ingestions_1.0.0**: Cloud ingestion endpoints (ADLS, S3, GCS, etc.)
- **collibra-catalog_database_registration_1.4.0**: Database registration and profiling
- **collibra-catalog_external_profiling_upload_1.0.0**: Manual profiling data upload
- **collibra-catalog_sampling_1.0.0**: Data sampling endpoints
- **collibra-catalog_technical_lineage_1.0.0**: Technical lineage integration
- **collibra-core_2.0.0**: Core platform endpoints
- **collibra-import_2.0.0**: Import and synchronization APIs
- **collibra-management_console_1.0.0**: Management Console API
- **collibra-protect_1.0.0**: Data protection and masking APIs
- **collibra-protect_api_partner**: Partner API for data protection

## Installation

Each package can be installed independently. For example:

```sh
cd collibra-core_2.0.0
pip install .
```

Or install directly from the repository:

```sh
pip install /path/to/collibra-core_2.0.0
```

## Usage

Each package contains a `README.md` with detailed usage instructions and code examples. Here is a general example:

```python
import collibra_core_2_0_0
from collibra_core_2_0_0.rest import ApiException

configuration = collibra_core_2_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

api_instance = collibra_core_2_0_0.UsersApi(collibra_core_2_0_0.ApiClient(configuration))

try:
    users = api_instance.find_users()
    print(users)
except ApiException as e:
    print("Exception when calling UsersApi->find_users: %s\n" % e)
```

## Authentication

Most APIs use HTTP Basic Authentication. Set your username and password in the configuration object as shown above.

## Documentation

- Each package contains its own `README.md` and `docs/` directory with API endpoint and model documentation.
- Refer to the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) documentation for more details on the generated code.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

This repository is a "Community Offering" available under the [Collibra Marketplace License agreement](https://www.collibra.com/us/en/legal/documents/collibra-marketplace-license-agreement).