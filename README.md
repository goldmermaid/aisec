# sec-agent-sdk
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sec_agent_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sec_agent_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import sec_agent_sdk
from sec_agent_sdk.rest import ApiException
from pprint import pprint

configuration = sec_agent_sdk.Configuration()

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = 'YOUR_API_KEY'

# Enter a context with an instance of the API client
with sec_agent_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sec_agent_sdk.DefaultApi(api_client)
    form_type = FormType.EIGHT_K # FormType | 10-K | 10-Q | 8-K | 6-K
    company = 'AA' # ticker
    date_filed = '2024-04-17' # str | date string in YYYY-mm-dd
    table = FilingTable.INCOME_STATEMENT # FilingTable | 'cash-flow-statement' | 'income-statement' | 'balance-sheet'

    try:
        # Search sec filing
        api_response = api_instance.search_sec_filing(form_type, company, date_filed, table)
        print("The response of DefaultApi->search_sec_filing:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->search_sec_filing: %s\n" % e)

```


## Documentation For Models

 - [Filing](docs/Filing.md)
 - [FilingTable](docs/FilingTable.md)
 - [FormType](docs/FormType.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LocationInner](docs/LocationInner.md)
 - [ValidationError](docs/ValidationError.md)
