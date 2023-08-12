<a name="__pageTop"></a>
# phasetwo.apis.tags.organization_invitations_api.OrganizationInvitationsApi

All URIs are relative to *https://app.phasetwo.io/realms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organization_invitation**](#add_organization_invitation) | **post** /{realm}/orgs/{orgId}/invitations | Create an invitation to an organization
[**get_organization_invitations**](#get_organization_invitations) | **get** /{realm}/orgs/{orgId}/invitations | Get organization invitations
[**remove_organization_invitation**](#remove_organization_invitation) | **delete** /{realm}/orgs/{orgId}/invitations/{invitationId} | Remove a pending invitation

# **add_organization_invitation**
<a name="add_organization_invitation"></a>
> add_organization_invitation(realmorg_idinvitation_request_representation)

Create an invitation to an organization

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_invitations_api
from phasetwo.model.invitation_request_representation import InvitationRequestRepresentation
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
    api_instance = organization_invitations_api.OrganizationInvitationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    body = InvitationRequestRepresentation(
        email="email_example",
        send=True,
        inviter_id="inviter_id_example",
        redirect_uri="redirect_uri_example",
        roles=[
            "roles_example"
        ],
    )
    try:
        # Create an invitation to an organization
        api_response = api_instance.add_organization_invitation(
            path_params=path_params,
            body=body,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationInvitationsApi->add_organization_invitation: %s\n" % e)
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
[**InvitationRequestRepresentation**](../../models/InvitationRequestRepresentation.md) |  | 


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
201 | [ApiResponseFor201](#add_organization_invitation.ApiResponseFor201) | success
409 | [ApiResponseFor409](#add_organization_invitation.ApiResponseFor409) | invitation already exists

#### add_organization_invitation.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### add_organization_invitation.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_organization_invitations**
<a name="get_organization_invitations"></a>
> [InvitationRepresentation] get_organization_invitations(realmorg_id)

Get organization invitations

Get a paginated list of invitations to an organization, using an optional search query for email address.

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_invitations_api
from phasetwo.model.invitation_representation import InvitationRepresentation
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
    api_instance = organization_invitations_api.OrganizationInvitationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    query_params = {
    }
    try:
        # Get organization invitations
        api_response = api_instance.get_organization_invitations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationInvitationsApi->get_organization_invitations: %s\n" % e)

    # example passing only optional values
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    query_params = {
        'search': "search_example",
        'first': 1,
        'max': 1,
    }
    try:
        # Get organization invitations
        api_response = api_instance.get_organization_invitations(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationInvitationsApi->get_organization_invitations: %s\n" % e)
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
200 | [ApiResponseFor200](#get_organization_invitations.ApiResponseFor200) | success

#### get_organization_invitations.ApiResponseFor200
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
[**InvitationRepresentation**]({{complexTypePrefix}}InvitationRepresentation.md) | [**InvitationRepresentation**]({{complexTypePrefix}}InvitationRepresentation.md) | [**InvitationRepresentation**]({{complexTypePrefix}}InvitationRepresentation.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_organization_invitation**
<a name="remove_organization_invitation"></a>
> remove_organization_invitation(realmorg_idinvitation_id)

Remove a pending invitation

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_invitations_api
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
    api_instance = organization_invitations_api.OrganizationInvitationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
        'invitationId': "invitationId_example",
    }
    try:
        # Remove a pending invitation
        api_response = api_instance.remove_organization_invitation(
            path_params=path_params,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationInvitationsApi->remove_organization_invitation: %s\n" % e)
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
invitationId | InvitationIdSchema | | 

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

# InvitationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_organization_invitation.ApiResponseFor204) | success

#### remove_organization_invitation.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

