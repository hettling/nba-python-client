# swagger_client.SpecimenApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_get**](SpecimenApi.md#count_get) | **GET** /specimen/count | Get the number of specimens matching a condition
[**count_postjson**](SpecimenApi.md#count_postjson) | **POST** /specimen/count | Get the number of specimens matching a condition
[**dwca_get_data_set**](SpecimenApi.md#dwca_get_data_set) | **GET** /specimen/dwca/getDataSet/{dataset} | Download dataset as Darwin Core Archive File
[**dwca_get_data_set_names**](SpecimenApi.md#dwca_get_data_set_names) | **GET** /specimen/dwca/getDataSetNames | Retrieve the names of all available datasets
[**dwca_query**](SpecimenApi.md#dwca_query) | **GET** /specimen/dwca/query | Dynamic download service: Query for specimens and return result as Darwin Core Archive File
[**exists**](SpecimenApi.md#exists) | **GET** /specimen/exists/{unitID} | Returns whether or not a unitID for a specimen exists
[**find**](SpecimenApi.md#find) | **GET** /specimen/find/{id} | Find a specimen by id
[**find_by_ids**](SpecimenApi.md#find_by_ids) | **GET** /specimen/findByIds/{ids} | Find specimens by ids
[**find_by_unit_id**](SpecimenApi.md#find_by_unit_id) | **GET** /specimen/findByUnitID/{unitID} | Find a specimen by unitID
[**get_distinct_values**](SpecimenApi.md#get_distinct_values) | **GET** /specimen/getDistinctValues/{field} | Get all different values that can be found for one field
[**get_field_info**](SpecimenApi.md#get_field_info) | **GET** /specimen/metadata/getFieldInfo | 
[**get_ids_in_collection**](SpecimenApi.md#get_ids_in_collection) | **GET** /specimen/getIdsInCollection/{name} | Retrieve all ids within a &#39;special collection&#39; of specimens
[**get_named_collections**](SpecimenApi.md#get_named_collections) | **GET** /specimen/getNamedCollections | Retrieve the names of all &#39;special collections&#39; of specimens
[**get_paths**](SpecimenApi.md#get_paths) | **GET** /specimen/metadata/getPaths | 
[**get_settings**](SpecimenApi.md#get_settings) | **GET** /specimen/metadata/getSettings | 
[**get_settings_0**](SpecimenApi.md#get_settings_0) | **GET** /specimen/metadata/getSetting/{name} | 
[**group_by_scientific_name_get**](SpecimenApi.md#group_by_scientific_name_get) | **GET** /specimen/groupByScientificName | Aggregates Taxon and Specimen documents according to their scientific names
[**is_operator_allowed**](SpecimenApi.md#is_operator_allowed) | **GET** /specimen/metadata/isOperatorAllowed/{field}/{operator} | 
[**query_get**](SpecimenApi.md#query_get) | **GET** /specimen/query | Query for specimens
[**query_postjson**](SpecimenApi.md#query_postjson) | **POST** /specimen/query | Query for specimens


# **count_get**
> int count_get()

Get the number of specimens matching a condition

Conditions given as query string

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    # Get the number of specimens matching a condition
    api_response = api_instance.count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: text/plain;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_postjson**
> int count_postjson(body=body)

Get the number of specimens matching a condition

Conditions given as querySpec JSON

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
body = swagger_client.QuerySpec() # QuerySpec | querySpec JSON (optional)

try: 
    # Get the number of specimens matching a condition
    api_response = api_instance.count_postjson(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->count_postjson: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuerySpec**](QuerySpec.md)| querySpec JSON | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: text/plain;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dwca_get_data_set**
> dwca_get_data_set(dataset)

Download dataset as Darwin Core Archive File

Available datasets can be queried with /specimen/dwca/getDataSetNames

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
dataset = 'dataset_example' # str | name of dataset

try: 
    # Download dataset as Darwin Core Archive File
    api_instance.dwca_get_data_set(dataset)
except ApiException as e:
    print("Exception when calling SpecimenApi->dwca_get_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| name of dataset | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dwca_get_data_set_names**
> list[str] dwca_get_data_set_names()

Retrieve the names of all available datasets

Individual datasets can then be downloaded with /dwca/getDataSet/{dataset}

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    # Retrieve the names of all available datasets
    api_response = api_instance.dwca_get_data_set_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->dwca_get_data_set_names: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dwca_query**
> dwca_query()

Dynamic download service: Query for specimens and return result as Darwin Core Archive File

Query can be human-readable or querySpec JSON

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    # Dynamic download service: Query for specimens and return result as Darwin Core Archive File
    api_instance.dwca_query()
except ApiException as e:
    print("Exception when calling SpecimenApi->dwca_query: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exists**
> bool exists(unit_id)

Returns whether or not a unitID for a specimen exists

Returns either true or false

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
unit_id = 'unit_id_example' # str | the unitID of the specimen to query

try: 
    # Returns whether or not a unitID for a specimen exists
    api_response = api_instance.exists(unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **str**| the unitID of the specimen to query | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find**
> Specimen find(id)

Find a specimen by id

If found, returns a single specimen

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
id = 'id_example' # str | id of specimen

try: 
    # Find a specimen by id
    api_response = api_instance.find(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of specimen | 

### Return type

[**Specimen**](Specimen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_ids**
> list[Specimen] find_by_ids(ids)

Find specimens by ids

Given multiple ids, returns a list of specimen

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
ids = 'ids_example' # str | ids of multiple specimen, separated by comma

try: 
    # Find specimens by ids
    api_response = api_instance.find_by_ids(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->find_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| ids of multiple specimen, separated by comma | 

### Return type

[**list[Specimen]**](Specimen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_unit_id**
> list[Specimen] find_by_unit_id(unit_id)

Find a specimen by unitID

Get a specimen by its unitID. Returns a list since unitIDs are not strictly unique

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
unit_id = 'unit_id_example' # str | the unitID of the specimen to query

try: 
    # Find a specimen by unitID
    api_response = api_instance.find_by_unit_id(unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->find_by_unit_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | **str**| the unitID of the specimen to query | 

### Return type

[**list[Specimen]**](Specimen.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distinct_values**
> dict(str, object) get_distinct_values(field)

Get all different values that can be found for one field

A list of all fields for specimen documents can be retrieved with /metadata/getFieldInfo

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
field = 'field_example' # str | name of field in specimen object

try: 
    # Get all different values that can be found for one field
    api_response = api_instance.get_distinct_values(field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->get_distinct_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| name of field in specimen object | 

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_info**
> dict(str, FieldInfo) get_field_info()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    api_response = api_instance.get_field_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->get_field_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, FieldInfo)**](FieldInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ids_in_collection**
> list[str] get_ids_in_collection(name)

Retrieve all ids within a 'special collection' of specimens

Available collections can be queried with /getNamedCollections

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
name = 'name_example' # str | name of dataset

try: 
    # Retrieve all ids within a 'special collection' of specimens
    api_response = api_instance.get_ids_in_collection(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->get_ids_in_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of dataset | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_named_collections**
> list[str] get_named_collections()

Retrieve the names of all 'special collections' of specimens



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    # Retrieve the names of all 'special collections' of specimens
    api_response = api_instance.get_named_collections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->get_named_collections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_paths**
> list[str] get_paths()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    api_response = api_instance.get_paths()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->get_paths: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> dict(str, object) get_settings()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_0**
> object get_settings_0(name)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
name = 'name_example' # str | 

try: 
    api_response = api_instance.get_settings_0(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->get_settings_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_by_scientific_name_get**
> QueryResult group_by_scientific_name_get()

Aggregates Taxon and Specimen documents according to their scientific names

Returns a list with ScientificNameGroups, which contain Taxon and Specimen documents that share a scientific name

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    # Aggregates Taxon and Specimen documents according to their scientific names
    api_response = api_instance.group_by_scientific_name_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->group_by_scientific_name_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_operator_allowed**
> bool is_operator_allowed(field, operator)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
field = 'field_example' # str | 
operator = 'operator_example' # str | 

try: 
    api_response = api_instance.is_operator_allowed(field, operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->is_operator_allowed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**|  | 
 **operator** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_get**
> QueryResult query_get()

Query for specimens

Search for specimen with a human-readable query or a querySpec JSON

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()

try: 
    # Query for specimens
    api_response = api_instance.query_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->query_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_postjson**
> QueryResult query_postjson(body=body)

Query for specimens

Search for specimen with a querySpec JSON

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpecimenApi()
body = swagger_client.QuerySpec() # QuerySpec | querySpec (optional)

try: 
    # Query for specimens
    api_response = api_instance.query_postjson(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpecimenApi->query_postjson: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuerySpec**](QuerySpec.md)| querySpec | [optional] 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

