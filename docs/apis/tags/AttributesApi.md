<a name="__pageTop"></a>
# phasetwo.apis.tags.attributes_api.AttributesApi

All URIs are relative to *https://app.phasetwo.io/realms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_realm_attribute**](#create_realm_attribute) | **post** /{realm}/attributes | Create a new realm attribute
[**delete_realm_attribute**](#delete_realm_attribute) | **delete** /{realm}/attributes/{attributeKey} | Delete the realm attribute
[**get_realm_attribute_by_key**](#get_realm_attribute_by_key) | **get** /{realm}/attributes/{attributeKey} | Get realm attribute by key
[**get_realm_attributes**](#get_realm_attributes) | **get** /{realm}/attributes | Get realm attributes
[**update_realm_attribute_by_key**](#update_realm_attribute_by_key) | **put** /{realm}/attributes/{attributeKey} | Update realm attribute by key

# **create_realm_attribute**
<a name="create_realm_attribute"></a>
> create_realm_attribute(realmrealm_attribute_representation)

Create a new realm attribute

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import attributes_api
from phasetwo.model.realm_attribute_representation import RealmAttributeRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
    }
    body = RealmAttributeRepresentation(
        name="name_example",
        value="value_example",
        realm="realm_example",
    )
    try:
        # Create a new realm attribute
        api_response = api_instance.create_realm_attribute(
            path_params=path_params,
            body=body,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling AttributesApi->create_realm_attribute: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RealmAttributeRepresentation**](../../models/RealmAttributeRepresentation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_realm_attribute.ApiResponseFor201) | Attribute created
400 | [ApiResponseFor400](#create_realm_attribute.ApiResponseFor400) | Malformed attribute

#### create_realm_attribute.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_realm_attribute.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_realm_attribute**
<a name="delete_realm_attribute"></a>
> delete_realm_attribute(realmattribute_key)

Delete the realm attribute

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import attributes_api
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'attributeKey': "attributeKey_example",
    }
    try:
        # Delete the realm attribute
        api_response = api_instance.delete_realm_attribute(
            path_params=path_params,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling AttributesApi->delete_realm_attribute: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
attributeKey | AttributeKeySchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AttributeKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_realm_attribute.ApiResponseFor204) | success
404 | [ApiResponseFor404](#delete_realm_attribute.ApiResponseFor404) | Realm attribute doesn&#x27;t exist

#### delete_realm_attribute.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_realm_attribute.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_realm_attribute_by_key**
<a name="get_realm_attribute_by_key"></a>
> RealmAttributeRepresentation get_realm_attribute_by_key(realmattribute_key)

Get realm attribute by key

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import attributes_api
from phasetwo.model.realm_attribute_representation import RealmAttributeRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'attributeKey': "attributeKey_example",
    }
    try:
        # Get realm attribute by key
        api_response = api_instance.get_realm_attribute_by_key(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling AttributesApi->get_realm_attribute_by_key: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
attributeKey | AttributeKeySchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AttributeKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_realm_attribute_by_key.ApiResponseFor200) | success
404 | [ApiResponseFor404](#get_realm_attribute_by_key.ApiResponseFor404) | Realm attribute doesn&#x27;t exist

#### get_realm_attribute_by_key.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RealmAttributeRepresentation**](../../models/RealmAttributeRepresentation.md) |  | 


#### get_realm_attribute_by_key.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_realm_attributes**
<a name="get_realm_attributes"></a>
> [KeyedRealmAttributeRepresentation] get_realm_attributes(realm)

Get realm attributes

Get a list of attributes for this realm

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import attributes_api
from phasetwo.model.keyed_realm_attribute_representation import KeyedRealmAttributeRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
    }
    try:
        # Get realm attributes
        api_response = api_instance.get_realm_attributes(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling AttributesApi->get_realm_attributes: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_realm_attributes.ApiResponseFor200) | success

#### get_realm_attributes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**KeyedRealmAttributeRepresentation**]({{complexTypePrefix}}KeyedRealmAttributeRepresentation.md) | [**KeyedRealmAttributeRepresentation**]({{complexTypePrefix}}KeyedRealmAttributeRepresentation.md) | [**KeyedRealmAttributeRepresentation**]({{complexTypePrefix}}KeyedRealmAttributeRepresentation.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_realm_attribute_by_key**
<a name="update_realm_attribute_by_key"></a>
> update_realm_attribute_by_key(realmattribute_keyrealm_attribute_representation)

Update realm attribute by key

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import attributes_api
from phasetwo.model.realm_attribute_representation import RealmAttributeRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/realms"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: access_token
configuration = phasetwo.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with phasetwo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attributes_api.AttributesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'attributeKey': "attributeKey_example",
    }
    body = RealmAttributeRepresentation(
        name="name_example",
        value="value_example",
        realm="realm_example",
    )
    try:
        # Update realm attribute by key
        api_response = api_instance.update_realm_attribute_by_key(
            path_params=path_params,
            body=body,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling AttributesApi->update_realm_attribute_by_key: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RealmAttributeRepresentation**](../../models/RealmAttributeRepresentation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
attributeKey | AttributeKeySchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AttributeKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_realm_attribute_by_key.ApiResponseFor204) | success
404 | [ApiResponseFor404](#update_realm_attribute_by_key.ApiResponseFor404) | Realm attribute doesn&#x27;t exist

#### update_realm_attribute_by_key.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_realm_attribute_by_key.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

