# swagger_client.TaxonApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_get**](TaxonApi.md#count_get) | **GET** /taxon/count | 
[**count_postjson**](TaxonApi.md#count_postjson) | **POST** /taxon/count | 
[**dwca_get_data_set**](TaxonApi.md#dwca_get_data_set) | **GET** /taxon/dwca/getDataSet/{dataset} | 
[**dwca_get_data_set_names**](TaxonApi.md#dwca_get_data_set_names) | **GET** /taxon/dwca/getDataSetNames | 
[**dwca_query**](TaxonApi.md#dwca_query) | **GET** /taxon/dwca/query | 
[**find**](TaxonApi.md#find) | **GET** /taxon/find/{id} | finds taxon by ID
[**find_by_ids**](TaxonApi.md#find_by_ids) | **GET** /taxon/findByIds/{ids} | 
[**get_distinct_values**](TaxonApi.md#get_distinct_values) | **GET** /taxon/getDistinctValues/{field} | 
[**get_field_info**](TaxonApi.md#get_field_info) | **GET** /taxon/metadata/getFieldInfo | 
[**get_paths**](TaxonApi.md#get_paths) | **GET** /taxon/metadata/getPaths | 
[**get_settings**](TaxonApi.md#get_settings) | **GET** /taxon/metadata/getSettings | 
[**get_settings_0**](TaxonApi.md#get_settings_0) | **GET** /taxon/metadata/getSetting/{name} | 
[**group_by_scientific_name_get**](TaxonApi.md#group_by_scientific_name_get) | **GET** /taxon/groupByScientificName | 
[**is_operator_allowed**](TaxonApi.md#is_operator_allowed) | **GET** /taxon/metadata/isOperatorAllowed/{field}/{operator} | 
[**query_get**](TaxonApi.md#query_get) | **GET** /taxon/query | 
[**query_postjson**](TaxonApi.md#query_postjson) | **POST** /taxon/query | 


# **count_get**
> int count_get()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()

try: 
    api_response = api_instance.count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->count_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_postjson**
> int count_postjson(body=body)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()
body = swagger_client.QuerySpec() # QuerySpec |  (optional)

try: 
    api_response = api_instance.count_postjson(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->count_postjson: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dwca_get_data_set**
> dwca_get_data_set(dataset)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()
dataset = 'dataset_example' # str | 

try: 
    api_instance.dwca_get_data_set(dataset)
except ApiException as e:
    print("Exception when calling TaxonApi->dwca_get_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**|  | 

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



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()

try: 
    api_response = api_instance.dwca_get_data_set_names()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->dwca_get_data_set_names: %s\n" % e)
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



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()

try: 
    api_instance.dwca_query()
except ApiException as e:
    print("Exception when calling TaxonApi->dwca_query: %s\n" % e)
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

# **find**
> Taxon find(id)

finds taxon by ID



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()
id = 'id_example' # str | 

try: 
    # finds taxon by ID
    api_response = api_instance.find(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Taxon**](Taxon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_ids**
> list[Taxon] find_by_ids(ids)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()
ids = 'ids_example' # str | 

try: 
    api_response = api_instance.find_by_ids(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->find_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

[**list[Taxon]**](Taxon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_distinct_values**
> dict(str, int) get_distinct_values(field)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()
field = 'field_example' # str | 

try: 
    api_response = api_instance.get_distinct_values(field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->get_distinct_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**|  | 

### Return type

**dict(str, int)**

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
api_instance = swagger_client.TaxonApi()

try: 
    api_response = api_instance.get_field_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->get_field_info: %s\n" % e)
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
api_instance = swagger_client.TaxonApi()

try: 
    api_response = api_instance.get_paths()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->get_paths: %s\n" % e)
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
api_instance = swagger_client.TaxonApi()

try: 
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->get_settings: %s\n" % e)
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
api_instance = swagger_client.TaxonApi()
name = 'name_example' # str | 

try: 
    api_response = api_instance.get_settings_0(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->get_settings_0: %s\n" % e)
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
> QueryResultScientificNameGroup group_by_scientific_name_get()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()

try: 
    api_response = api_instance.group_by_scientific_name_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->group_by_scientific_name_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResultScientificNameGroup**](QueryResultScientificNameGroup.md)

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
api_instance = swagger_client.TaxonApi()
field = 'field_example' # str | 
operator = 'operator_example' # str | 

try: 
    api_response = api_instance.is_operator_allowed(field, operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->is_operator_allowed: %s\n" % e)
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
> QueryResultTaxon query_get()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()

try: 
    api_response = api_instance.query_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->query_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResultTaxon**](QueryResultTaxon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_postjson**
> QueryResultTaxon query_postjson(body=body)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxonApi()
body = swagger_client.QuerySpec() # QuerySpec |  (optional)

try: 
    api_response = api_instance.query_postjson(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxonApi->query_postjson: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

[**QueryResultTaxon**](QueryResultTaxon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

