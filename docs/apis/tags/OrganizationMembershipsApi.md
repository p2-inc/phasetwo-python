<a name="__pageTop"></a>
# phasetwo.apis.tags.organization_memberships_api.OrganizationMembershipsApi

All URIs are relative to *https://app.phasetwo.io/auth/realms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organization_member**](#add_organization_member) | **put** /{realm}/orgs/{orgId}/members/{userId} | Add an organization member
[**check_organization_membership**](#check_organization_membership) | **get** /{realm}/orgs/{orgId}/members/{userId} | Check if a user is a member of an organization
[**get_organization_memberships**](#get_organization_memberships) | **get** /{realm}/orgs/{orgId}/members | Get organization memberships
[**remove_organization_member**](#remove_organization_member) | **delete** /{realm}/orgs/{orgId}/members/{userId} | Remove an organization member

# **add_organization_member**
<a name="add_organization_member"></a>
> add_organization_member(realmorg_iduser_id)

Add an organization member

Add the specified user to the specified organization as a member

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_memberships_api
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/auth/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/auth/realms"
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
    api_instance = organization_memberships_api.OrganizationMembershipsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
        'userId': "userId_example",
    }
    try:
        # Add an organization member
        api_response = api_instance.add_organization_member(
            path_params=path_params,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationMembershipsApi->add_organization_member: %s\n" % e)
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
userId | UserIdSchema | | 

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

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#add_organization_member.ApiResponseFor201) | success

#### add_organization_member.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **check_organization_membership**
<a name="check_organization_membership"></a>
> check_organization_membership(realmorg_iduser_id)

Check if a user is a member of an organization

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_memberships_api
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/auth/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/auth/realms"
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
    api_instance = organization_memberships_api.OrganizationMembershipsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
        'userId': "userId_example",
    }
    try:
        # Check if a user is a member of an organization
        api_response = api_instance.check_organization_membership(
            path_params=path_params,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationMembershipsApi->check_organization_membership: %s\n" % e)
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
userId | UserIdSchema | | 

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

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#check_organization_membership.ApiResponseFor204) | success

#### check_organization_membership.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_organization_memberships**
<a name="get_organization_memberships"></a>
> [UserRepresentation] get_organization_memberships(realmorg_id)

Get organization memberships

Get a paginated list of users who are a member of the specified organization.

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_memberships_api
from phasetwo.model.user_representation import UserRepresentation
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/auth/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/auth/realms"
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
    api_instance = organization_memberships_api.OrganizationMembershipsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    query_params = {
    }
    try:
        # Get organization memberships
        api_response = api_instance.get_organization_memberships(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationMembershipsApi->get_organization_memberships: %s\n" % e)

    # example passing only optional values
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    query_params = {
        'first': 1,
        'max': 1,
    }
    try:
        # Get organization memberships
        api_response = api_instance.get_organization_memberships(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationMembershipsApi->get_organization_memberships: %s\n" % e)
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
first | FirstSchema | | optional
max | MaxSchema | | optional


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
200 | [ApiResponseFor200](#get_organization_memberships.ApiResponseFor200) | success

#### get_organization_memberships.ApiResponseFor200
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
[**UserRepresentation**]({{complexTypePrefix}}UserRepresentation.md) | [**UserRepresentation**]({{complexTypePrefix}}UserRepresentation.md) | [**UserRepresentation**]({{complexTypePrefix}}UserRepresentation.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_organization_member**
<a name="remove_organization_member"></a>
> remove_organization_member(realmorg_iduser_id)

Remove an organization member

Remove the specified user from the specified organization as a member

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_memberships_api
from pprint import pprint
# Defining the host is optional and defaults to https://app.phasetwo.io/auth/realms
# See configuration.py for a list of all supported configuration parameters.
configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/auth/realms"
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
    api_instance = organization_memberships_api.OrganizationMembershipsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
        'userId': "userId_example",
    }
    try:
        # Remove an organization member
        api_response = api_instance.remove_organization_member(
            path_params=path_params,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationMembershipsApi->remove_organization_member: %s\n" % e)
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
userId | UserIdSchema | | 

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

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_organization_member.ApiResponseFor204) | success

#### remove_organization_member.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

