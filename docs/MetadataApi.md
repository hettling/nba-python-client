# swagger_client.MetadataApi

All URIs are relative to *http://localhost:8080/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allowed_date_formats**](MetadataApi.md#get_allowed_date_formats) | **GET** /metadata/getAllowedDateFormats | 
[**get_controlled_list_phase_or_stage**](MetadataApi.md#get_controlled_list_phase_or_stage) | **GET** /metadata/getControlledList/PhaseOrStage | 
[**get_controlled_list_sex**](MetadataApi.md#get_controlled_list_sex) | **GET** /metadata/getControlledList/Sex | 
[**get_controlled_list_specimen_type_status**](MetadataApi.md#get_controlled_list_specimen_type_status) | **GET** /metadata/getControlledList/SpecimenTypeStatus | 
[**get_controlled_list_taxonomic_status**](MetadataApi.md#get_controlled_list_taxonomic_status) | **GET** /metadata/getControlledList/TaxonomicStatus | 
[**get_controlled_lists**](MetadataApi.md#get_controlled_lists) | **GET** /metadata/getControlledLists | 
[**get_rest_services**](MetadataApi.md#get_rest_services) | **GET** /metadata/getRestServices | 
[**get_setting**](MetadataApi.md#get_setting) | **GET** /metadata/getSetting/{name} | 
[**get_settings**](MetadataApi.md#get_settings) | **GET** /metadata/getSettings | 
[**get_source_systems**](MetadataApi.md#get_source_systems) | **GET** /metadata/getSourceSystems | 


# **get_allowed_date_formats**
> list[str] get_allowed_date_formats()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_allowed_date_formats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_allowed_date_formats: %s\n" % e)
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

# **get_controlled_list_phase_or_stage**
> list[str] get_controlled_list_phase_or_stage()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_controlled_list_phase_or_stage()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_controlled_list_phase_or_stage: %s\n" % e)
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

# **get_controlled_list_sex**
> list[str] get_controlled_list_sex()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_controlled_list_sex()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_controlled_list_sex: %s\n" % e)
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

# **get_controlled_list_specimen_type_status**
> list[str] get_controlled_list_specimen_type_status()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_controlled_list_specimen_type_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_controlled_list_specimen_type_status: %s\n" % e)
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

# **get_controlled_list_taxonomic_status**
> list[str] get_controlled_list_taxonomic_status()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_controlled_list_taxonomic_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_controlled_list_taxonomic_status: %s\n" % e)
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

# **get_controlled_lists**
> list[str] get_controlled_lists()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_controlled_lists()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_controlled_lists: %s\n" % e)
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

# **get_rest_services**
> list[RestService] get_rest_services()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_rest_services()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_rest_services: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RestService]**](RestService.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_setting**
> object get_setting(name)



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
name = 'name_example' # str | 

try: 
    api_response = api_instance.get_setting(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_setting: %s\n" % e)
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
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_settings: %s\n" % e)
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

# **get_source_systems**
> list[SourceSystem] get_source_systems()



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try: 
    api_response = api_instance.get_source_systems()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_source_systems: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SourceSystem]**](SourceSystem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

