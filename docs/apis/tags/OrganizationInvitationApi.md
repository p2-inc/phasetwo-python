<a name="__pageTop"></a>
# phasetwo.apis.tags.organization_invitation_api.OrganizationInvitationApi

All URIs are relative to *https://app.phasetwo.io/realms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_invitation_by_id**](#get_organization_invitation_by_id) | **get** /{realm}/orgs/{orgId}/invitations/{invitationId} | Get organization invitation by ID
[**resend_organization_invitation**](#resend_organization_invitation) | **put** /{realm}/orgs/{orgId}/invitations/{invitationId}/resend-email | Resend an Organization Invitation

# **get_organization_invitation_by_id**
<a name="get_organization_invitation_by_id"></a>
> InvitationRepresentation get_organization_invitation_by_id(realmorg_idinvitation_id)

Get organization invitation by ID

Get an invitation to an organization by its uuid.

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_invitation_api
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
    api_instance = organization_invitation_api.OrganizationInvitationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
        'invitationId': "invitationId_example",
    }
    try:
        # Get organization invitation by ID
        api_response = api_instance.get_organization_invitation_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationInvitationApi->get_organization_invitation_by_id: %s\n" % e)
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
200 | [ApiResponseFor200](#get_organization_invitation_by_id.ApiResponseFor200) | success

#### get_organization_invitation_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InvitationRepresentation**](../../models/InvitationRepresentation.md) |  | 


### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **resend_organization_invitation**
<a name="resend_organization_invitation"></a>
> resend_organization_invitation(realmorg_idinvitation_id)

Resend an Organization Invitation

Resend the email for an existing Organization Invitation

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_invitation_api
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
    api_instance = organization_invitation_api.OrganizationInvitationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
        'invitationId': "invitationId_example",
    }
    try:
        # Resend an Organization Invitation
        api_response = api_instance.resend_organization_invitation(
            path_params=path_params,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationInvitationApi->resend_organization_invitation: %s\n" % e)
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
204 | [ApiResponseFor204](#resend_organization_invitation.ApiResponseFor204) | success

#### resend_organization_invitation.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

