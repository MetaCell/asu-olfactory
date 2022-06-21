# cloudharness_cli.pub_chem_index.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_molecule**](DefaultApi.md#create_molecule) | **POST** /molecules | Create a Molecule
[**delete_molecule**](DefaultApi.md#delete_molecule) | **DELETE** /molecules/{moleculeId} | Delete a Molecule
[**get_molecule**](DefaultApi.md#get_molecule) | **GET** /molecules/{moleculeId} | Get a Molecule
[**get_molecules**](DefaultApi.md#get_molecules) | **GET** /molecules | List All Molecules
[**update_molecule**](DefaultApi.md#update_molecule) | **PUT** /molecules/{moleculeId} | Update a Molecule


# **create_molecule**
> create_molecule(molecule)

Create a Molecule

Creates a new instance of a `Molecule`.

### Example

```python
import time
import cloudharness_cli.pub_chem_index
from cloudharness_cli.pub_chem_index.api import default_api
from cloudharness_cli.pub_chem_index.model.molecule import Molecule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudharness_cli.pub_chem_index.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cloudharness_cli.pub_chem_index.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    molecule = Molecule(
        cid=1,
        synonyms=[
            "synonyms_example",
        ],
    ) # Molecule | A new `Molecule` to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create a Molecule
        api_instance.create_molecule(molecule)
    except cloudharness_cli.pub_chem_index.ApiException as e:
        print("Exception when calling DefaultApi->create_molecule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **molecule** | [**Molecule**](Molecule.md)| A new &#x60;Molecule&#x60; to be created. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_molecule**
> delete_molecule(molecule_id)

Delete a Molecule

Deletes an existing `Molecule`.

### Example

```python
import time
import cloudharness_cli.pub_chem_index
from cloudharness_cli.pub_chem_index.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudharness_cli.pub_chem_index.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cloudharness_cli.pub_chem_index.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    molecule_id = "moleculeId_example" # str | A unique identifier for a `Molecule`.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Molecule
        api_instance.delete_molecule(molecule_id)
    except cloudharness_cli.pub_chem_index.ApiException as e:
        print("Exception when calling DefaultApi->delete_molecule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **molecule_id** | **str**| A unique identifier for a &#x60;Molecule&#x60;. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_molecule**
> Molecule get_molecule(molecule_id)

Get a Molecule

Gets the details of a single instance of a `Molecule`.

### Example

```python
import time
import cloudharness_cli.pub_chem_index
from cloudharness_cli.pub_chem_index.api import default_api
from cloudharness_cli.pub_chem_index.model.molecule import Molecule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudharness_cli.pub_chem_index.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cloudharness_cli.pub_chem_index.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    molecule_id = "moleculeId_example" # str | A unique identifier for a `Molecule`.

    # example passing only required values which don't have defaults set
    try:
        # Get a Molecule
        api_response = api_instance.get_molecule(molecule_id)
        pprint(api_response)
    except cloudharness_cli.pub_chem_index.ApiException as e:
        print("Exception when calling DefaultApi->get_molecule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **molecule_id** | **str**| A unique identifier for a &#x60;Molecule&#x60;. |

### Return type

[**Molecule**](Molecule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns a single &#x60;Molecule&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_molecules**
> [Molecule] get_molecules()

List All Molecules

Gets a list of all `Molecule` entities.

### Example

```python
import time
import cloudharness_cli.pub_chem_index
from cloudharness_cli.pub_chem_index.api import default_api
from cloudharness_cli.pub_chem_index.model.molecule import Molecule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudharness_cli.pub_chem_index.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cloudharness_cli.pub_chem_index.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List All Molecules
        api_response = api_instance.get_molecules()
        pprint(api_response)
    except cloudharness_cli.pub_chem_index.ApiException as e:
        print("Exception when calling DefaultApi->get_molecules: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Molecule]**](Molecule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response - returns an array of &#x60;Molecule&#x60; entities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_molecule**
> update_molecule(molecule_id, molecule)

Update a Molecule

Updates an existing `Molecule`.

### Example

```python
import time
import cloudharness_cli.pub_chem_index
from cloudharness_cli.pub_chem_index.api import default_api
from cloudharness_cli.pub_chem_index.model.molecule import Molecule
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cloudharness_cli.pub_chem_index.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cloudharness_cli.pub_chem_index.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    molecule_id = "moleculeId_example" # str | A unique identifier for a `Molecule`.
    molecule = Molecule(
        cid=1,
        synonyms=[
            "synonyms_example",
        ],
    ) # Molecule | Updated `Molecule` information.

    # example passing only required values which don't have defaults set
    try:
        # Update a Molecule
        api_instance.update_molecule(molecule_id, molecule)
    except cloudharness_cli.pub_chem_index.ApiException as e:
        print("Exception when calling DefaultApi->update_molecule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **molecule_id** | **str**| A unique identifier for a &#x60;Molecule&#x60;. |
 **molecule** | [**Molecule**](Molecule.md)| Updated &#x60;Molecule&#x60; information. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

