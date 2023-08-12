<a name="__pageTop"></a>
# phasetwo.apis.tags.organizations_api.OrganizationsApi

All URIs are relative to *https://app.phasetwo.io/realms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](#create_organization) | **post** /{realm}/orgs | Create a new organization
[**create_portal_link**](#create_portal_link) | **post** /{realm}/orgs/{orgId}/portal-link | Create a link for the organization&#x27;s admin portal
[**delete_organization**](#delete_organization) | **delete** /{realm}/orgs/{orgId} | Delete the organization
[**get_me**](#get_me) | **get** /{realm}/orgs/me | Get orgs and roles for authenticated user
[**get_organization_by_id**](#get_organization_by_id) | **get** /{realm}/orgs/{orgId} | Get organization by id
[**get_organizations**](#get_organizations) | **get** /{realm}/orgs | Get organizations
[**get_organizations_count**](#get_organizations_count) | **get** /{realm}/orgs/count | Get organizations count
[**update_organization**](#update_organization) | **put** /{realm}/orgs/{orgId} | Update this organization by id

# **create_organization**
<a name="create_organization"></a>
> create_organization(realmorganization_representation)

Create a new organization

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organizations_api
from phasetwo.model.organization_representation import OrganizationRepresentation
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
    }
    body = OrganizationRepresentation(
        id="id_example",
        name="name_example",
        display_name="display_name_example",
        url="url_example",
        realm="realm_example",
        domains=[
            "domains_example"
        ],
        attributes=dict(
,
        ),
    )
    try:
        # Create a new organization
        api_response = api_instance.create_organization(
            path_params=path_params,
            body=body,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
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
[**OrganizationRepresentation**](../../models/OrganizationRepresentation.md) |  | 


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
201 | [ApiResponseFor201](#create_organization.ApiResponseFor201) | success

#### create_organization.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Location | LocationSchema | | optional

# LocationSchema

URI indicating the ID of the new resource.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | URI indicating the ID of the new resource. | 


### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_portal_link**
<a name="create_portal_link"></a>
> PortalLinkRepresentation create_portal_link(realmorg_id)

Create a link for the organization's admin portal

Create a link for this organizations admin portal. This link encodes an action token on behalf of the organization's default admin user, or the user that is optionally specified in this request. The user specified must be a member of this organization, and have full organization admin roles.

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organizations_api
from phasetwo.model.portal_link_representation import PortalLinkRepresentation
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    try:
        # Create a link for the organization's admin portal
        api_response = api_instance.create_portal_link(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->create_portal_link: %s\n" % e)

    # example passing only optional values
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    body = dict(
        user_id="user_id_example",
    )
    try:
        # Create a link for the organization's admin portal
        api_response = api_instance.create_portal_link(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->create_portal_link: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**userId** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
orgId | OrgIdSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_portal_link.ApiResponseFor200) | success

#### create_portal_link.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PortalLinkRepresentation**](../../models/PortalLinkRepresentation.md) |  | 


### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_organization**
<a name="delete_organization"></a>
> delete_organization(realmorg_id)

Delete the organization

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    try:
        # Delete the organization
        api_response = api_instance.delete_organization(
            path_params=path_params,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->delete_organization: %s\n" % e)
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
orgId | OrgIdSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_organization.ApiResponseFor204) | success

#### delete_organization.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_me**
<a name="get_me"></a>
> MyOrganizationsRepresentation get_me(realm)

Get orgs and roles for authenticated user

Get a list of all organizations that the user is a member and their roles in those organizations. Similar idea to /userinfo in OIDC.

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organizations_api
from phasetwo.model.my_organizations_representation import MyOrganizationsRepresentation
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
    }
    try:
        # Get orgs and roles for authenticated user
        api_response = api_instance.get_me(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->get_me: %s\n" % e)
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
200 | [ApiResponseFor200](#get_me.ApiResponseFor200) | success

#### get_me.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MyOrganizationsRepresentation**](../../models/MyOrganizationsRepresentation.md) |  | 


### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_organization_by_id**
<a name="get_organization_by_id"></a>
> OrganizationRepresentation get_organization_by_id(realmorg_id)

Get organization by id

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organizations_api
from phasetwo.model.organization_representation import OrganizationRepresentation
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    try:
        # Get organization by id
        api_response = api_instance.get_organization_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organization_by_id: %s\n" % e)
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
orgId | OrgIdSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_organization_by_id.ApiResponseFor200) | success

#### get_organization_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationRepresentation**](../../models/OrganizationRepresentation.md) |  | 


### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_organizations**
<a name="get_organizations"></a>
> [OrganizationRepresentation] get_organizations(realm)

Get organizations

Get a paginated list of organizations using optional search query parameters.

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organizations_api
from phasetwo.model.organization_representation import OrganizationRepresentation
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
    }
    query_params = {
    }
    try:
        # Get organizations
        api_response = api_instance.get_organizations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organizations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'realm': "realm_example",
    }
    query_params = {
        'search': "search_example",
        'first': 1,
        'max': 1,
        'q': "q_example",
    }
    try:
        # Get organizations
        api_response = api_instance.get_organizations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organizations: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
search | SearchSchema | | optional
first | FirstSchema | | optional
max | MaxSchema | | optional
q | QSchema | | optional


# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FirstSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# MaxSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# QSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_organizations.ApiResponseFor200) | success

#### get_organizations.ApiResponseFor200
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
[**OrganizationRepresentation**]({{complexTypePrefix}}OrganizationRepresentation.md) | [**OrganizationRepresentation**]({{complexTypePrefix}}OrganizationRepresentation.md) | [**OrganizationRepresentation**]({{complexTypePrefix}}OrganizationRepresentation.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_organizations_count**
<a name="get_organizations_count"></a>
> int get_organizations_count(realm)

Get organizations count

Get a count of organizations using an optional search query.

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organizations_api
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
    }
    query_params = {
    }
    try:
        # Get organizations count
        api_response = api_instance.get_organizations_count(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organizations_count: %s\n" % e)

    # example passing only optional values
    path_params = {
        'realm': "realm_example",
    }
    query_params = {
        'search': "search_example",
    }
    try:
        # Get organizations count
        api_response = api_instance.get_organizations_count(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->get_organizations_count: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
search | SearchSchema | | optional


# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_organizations_count.ApiResponseFor200) | success

#### get_organizations_count.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_organization**
<a name="update_organization"></a>
> update_organization(realmorg_idorganization_representation)

Update this organization by id

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organizations_api
from phasetwo.model.organization_representation import OrganizationRepresentation
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
    api_instance = organizations_api.OrganizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    body = OrganizationRepresentation(
        id="id_example",
        name="name_example",
        display_name="display_name_example",
        url="url_example",
        realm="realm_example",
        domains=[
            "domains_example"
        ],
        attributes=dict(
,
        ),
    )
    try:
        # Update this organization by id
        api_response = api_instance.update_organization(
            path_params=path_params,
            body=body,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationsApi->update_organization: %s\n" % e)
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
[**OrganizationRepresentation**](../../models/OrganizationRepresentation.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
realm | RealmSchema | | 
orgId | OrgIdSchema | | 

# RealmSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_organization.ApiResponseFor204) | success

#### update_organization.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

