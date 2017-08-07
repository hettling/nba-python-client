# swagger_client.GeoApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_get**](GeoApi.md#count_get) | **GET** /geo/count | 
[**count_postjson**](GeoApi.md#count_postjson) | **POST** /geo/count | 
[**find**](GeoApi.md#find) | **GET** /geo/find/{id} | 
[**find_by_ids**](GeoApi.md#find_by_ids) | **GET** /geo/findByIds/{ids} | 
[**get_distinct_values**](GeoApi.md#get_distinct_values) | **GET** /geo/getDistinctValues/{field} | 
[**get_field_info**](GeoApi.md#get_field_info) | **GET** /geo/metadata/getFieldInfo | 
[**get_geo_json_for_locality**](GeoApi.md#get_geo_json_for_locality) | **GET** /geo/getGeoJsonForLocality/{locality} | 
[**get_paths**](GeoApi.md#get_paths) | **GET** /geo/metadata/getPaths | 
[**get_settings**](GeoApi.md#get_settings) | **GET** /geo/metadata/getSettings | 
[**get_settings_0**](GeoApi.md#get_settings_0) | **GET** /geo/metadata/getSetting/{name} | 
[**is_operator_allowed**](GeoApi.md#is_operator_allowed) | **GET** /geo/metadata/isOperatorAllowed/{field}/{operator} | 
[**query**](GeoApi.md#query) | **GET** /geo/query | 


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
api_instance = swagger_client.GeoApi()

try: 
    api_response = api_instance.count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->count_get: %s\n" % e)
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
api_instance = swagger_client.GeoApi()
body = swagger_client.QuerySpec() # QuerySpec |  (optional)

try: 
    api_response = api_instance.count_postjson(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->count_postjson: %s\n" % e)
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

# **find**
> GeoArea find(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeoApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.find(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GeoArea**](GeoArea.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_ids**
> list[GeoArea] find_by_ids(ids)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeoApi()
ids = 'ids_example' # str | 

try: 
    api_response = api_instance.find_by_ids(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->find_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

[**list[GeoArea]**](GeoArea.md)

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
api_instance = swagger_client.GeoApi()
field = 'field_example' # str | 

try: 
    api_response = api_instance.get_distinct_values(field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->get_distinct_values: %s\n" % e)
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
api_instance = swagger_client.GeoApi()

try: 
    api_response = api_instance.get_field_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->get_field_info: %s\n" % e)
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

# **get_geo_json_for_locality**
> GeoJsonObject get_geo_json_for_locality(locality)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeoApi()
locality = 'locality_example' # str | 

try: 
    api_response = api_instance.get_geo_json_for_locality(locality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->get_geo_json_for_locality: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locality** | **str**|  | 

### Return type

[**GeoJsonObject**](GeoJsonObject.md)

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
api_instance = swagger_client.GeoApi()

try: 
    api_response = api_instance.get_paths()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->get_paths: %s\n" % e)
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
api_instance = swagger_client.GeoApi()

try: 
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->get_settings: %s\n" % e)
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
api_instance = swagger_client.GeoApi()
name = 'name_example' # str | 

try: 
    api_response = api_instance.get_settings_0(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->get_settings_0: %s\n" % e)
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
api_instance = swagger_client.GeoApi()
field = 'field_example' # str | 
operator = 'operator_example' # str | 

try: 
    api_response = api_instance.is_operator_allowed(field, operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->is_operator_allowed: %s\n" % e)
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

# **query**
> QueryResultGeoArea query()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GeoApi()

try: 
    api_response = api_instance.query()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeoApi->query: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResultGeoArea**](QueryResultGeoArea.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

