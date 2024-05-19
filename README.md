# sec-agent-sdk
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

💻 Installation

```sh
pip install git+ssh://git@github.com:CambioML/aisec.git#main

# Or

poetry add git+ssh://git@github.com:CambioML/aisec.git#main
```

🌱 Set up your AnyParser API key
Please reach out at info@cambioml.com for an API key.

📜 Examples

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
