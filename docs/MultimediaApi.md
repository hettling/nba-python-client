# swagger_client.MultimediaApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_get**](MultimediaApi.md#count_get) | **GET** /multimedia/count | 
[**count_postjson**](MultimediaApi.md#count_postjson) | **POST** /multimedia/count | 
[**find**](MultimediaApi.md#find) | **GET** /multimedia/find/{id} | 
[**find_by_ids**](MultimediaApi.md#find_by_ids) | **GET** /multimedia/findByIds/{ids} | 
[**get_distinct_values**](MultimediaApi.md#get_distinct_values) | **GET** /multimedia/getDistinctValues/{field} | 
[**get_field_info**](MultimediaApi.md#get_field_info) | **GET** /multimedia/metadata/getFieldInfo | 
[**get_paths**](MultimediaApi.md#get_paths) | **GET** /multimedia/metadata/getPaths | 
[**get_settings**](MultimediaApi.md#get_settings) | **GET** /multimedia/metadata/getSettings | 
[**get_settings_0**](MultimediaApi.md#get_settings_0) | **GET** /multimedia/metadata/getSetting/{name} | 
[**is_operator_allowed**](MultimediaApi.md#is_operator_allowed) | **GET** /multimedia/metadata/isOperatorAllowed/{field}/{operator} | 
[**query_get**](MultimediaApi.md#query_get) | **GET** /multimedia/query | 
[**query_postjson**](MultimediaApi.md#query_postjson) | **POST** /multimedia/query | 


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
api_instance = swagger_client.MultimediaApi()

try: 
    api_response = api_instance.count_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->count_get: %s\n" % e)
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
api_instance = swagger_client.MultimediaApi()
body = swagger_client.QuerySpec() # QuerySpec |  (optional)

try: 
    api_response = api_instance.count_postjson(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->count_postjson: %s\n" % e)
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
> MultiMediaObject find(id)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MultimediaApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.find(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MultiMediaObject**](MultiMediaObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_by_ids**
> list[MultiMediaObject] find_by_ids(ids)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MultimediaApi()
ids = 'ids_example' # str | 

try: 
    api_response = api_instance.find_by_ids(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->find_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

[**list[MultiMediaObject]**](MultiMediaObject.md)

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
api_instance = swagger_client.MultimediaApi()
field = 'field_example' # str | 

try: 
    api_response = api_instance.get_distinct_values(field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->get_distinct_values: %s\n" % e)
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
api_instance = swagger_client.MultimediaApi()

try: 
    api_response = api_instance.get_field_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->get_field_info: %s\n" % e)
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
api_instance = swagger_client.MultimediaApi()

try: 
    api_response = api_instance.get_paths()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->get_paths: %s\n" % e)
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
api_instance = swagger_client.MultimediaApi()

try: 
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->get_settings: %s\n" % e)
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
api_instance = swagger_client.MultimediaApi()
name = 'name_example' # str | 

try: 
    api_response = api_instance.get_settings_0(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->get_settings_0: %s\n" % e)
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
api_instance = swagger_client.MultimediaApi()
field = 'field_example' # str | 
operator = 'operator_example' # str | 

try: 
    api_response = api_instance.is_operator_allowed(field, operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->is_operator_allowed: %s\n" % e)
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
> QueryResultMultiMediaObject query_get()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MultimediaApi()

try: 
    api_response = api_instance.query_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->query_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QueryResultMultiMediaObject**](QueryResultMultiMediaObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_postjson**
> QueryResultMultiMediaObject query_postjson(body=body)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MultimediaApi()
body = swagger_client.QuerySpec() # QuerySpec |  (optional)

try: 
    api_response = api_instance.query_postjson(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultimediaApi->query_postjson: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuerySpec**](QuerySpec.md)|  | [optional] 

### Return type

[**QueryResultMultiMediaObject**](QueryResultMultiMediaObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

