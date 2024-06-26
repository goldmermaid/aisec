# AI Agent for SEC Fillings
The library is an experiment to extract SEC fillings data in real-time.

## Requirements.

Python 3.7+

💻 Installation

```sh
pip install git+ssh://git@github.com:CambioML/aisec.git#main

# Or

pip install git+https://github.com/CambioML/aisec.git

# Or

poetry add git+ssh://git@github.com:CambioML/aisec.git#main
```

🌱 Set up your CambioML API key for AI SEC
Please reach out at info@cambioml.com for an API key.

📜 Examples

```python
import os
import sec_agent_sdk
from sec_agent_sdk import FormType, FilingTable
from sec_agent_sdk.rest import ApiException
from pprint import pprint

configuration = sec_agent_sdk.Configuration()

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Enter a context with an instance of the API client
with sec_agent_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sec_agent_sdk.DefaultApi(api_client)
    form_type = FormType.EIGHT_K # FormType | 10-K | 10-Q | 8-K | 6-K
    company = 'AA' # ticker
    table = FilingTable.BALANCE_SHEET # FilingTable | 'cash-flow-statement' | 'income-statement' | 'balance-sheet' | 'business-segments-and-kpis'
    date_filed = '2024-04-17' # optional str (date string in YYYY-mm-dd) or None(the latest filing will be retrieved)

    try:
        # Search sec filing
        api_response = api_instance.search_sec_filing(form_type, company, table, date_filed)
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
