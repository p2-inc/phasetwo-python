<a name="__pageTop"></a>
# phasetwo.apis.tags.organization_domains_api.OrganizationDomainsApi

All URIs are relative to *https://app.phasetwo.io/auth/realms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_domain**](#get_organization_domain) | **get** /{realm}/orgs/{orgId}/domains/{domainName} | Get details for a domain owned by an organization
[**get_organization_domains**](#get_organization_domains) | **get** /{realm}/orgs/{orgId}/domains | Get details for all domains owned by an organization
[**verify_domain**](#verify_domain) | **post** /{realm}/orgs/{orgId}/domains/{domainName}/verify | Start domain verification

# **get_organization_domain**
<a name="get_organization_domain"></a>
> OrganizationDomainRepresentation get_organization_domain(realmorg_iddomain_name)

Get details for a domain owned by an organization

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_domains_api
from phasetwo.model.organization_domain_representation import OrganizationDomainRepresentation
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
    api_instance = organization_domains_api.OrganizationDomainsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
        'domainName': "domainName_example",
    }
    try:
        # Get details for a domain owned by an organization
        api_response = api_instance.get_organization_domain(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationDomainsApi->get_organization_domain: %s\n" % e)
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
domainName | DomainNameSchema | | 

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

# DomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_organization_domain.ApiResponseFor200) | success

#### get_organization_domain.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OrganizationDomainRepresentation**](../../models/OrganizationDomainRepresentation.md) |  | 


### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_organization_domains**
<a name="get_organization_domains"></a>
> [OrganizationDomainRepresentation] get_organization_domains(realmorg_id)

Get details for all domains owned by an organization

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_domains_api
from phasetwo.model.organization_domain_representation import OrganizationDomainRepresentation
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
    api_instance = organization_domains_api.OrganizationDomainsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
    }
    try:
        # Get details for all domains owned by an organization
        api_response = api_instance.get_organization_domains(
            path_params=path_params,
        )
        pprint(api_response)
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationDomainsApi->get_organization_domains: %s\n" % e)
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
200 | [ApiResponseFor200](#get_organization_domains.ApiResponseFor200) | success

#### get_organization_domains.ApiResponseFor200
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
[**OrganizationDomainRepresentation**]({{complexTypePrefix}}OrganizationDomainRepresentation.md) | [**OrganizationDomainRepresentation**]({{complexTypePrefix}}OrganizationDomainRepresentation.md) | [**OrganizationDomainRepresentation**]({{complexTypePrefix}}OrganizationDomainRepresentation.md) |  | 

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **verify_domain**
<a name="verify_domain"></a>
> verify_domain(realmorg_iddomain_name)

Start domain verification

Initiate a verification check for the domain name owned by this organization

### Example

* Bearer Authentication (access_token):
```python
import phasetwo
from phasetwo.apis.tags import organization_domains_api
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
    api_instance = organization_domains_api.OrganizationDomainsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'realm': "realm_example",
        'orgId': "orgId_example",
        'domainName': "domainName_example",
    }
    try:
        # Start domain verification
        api_response = api_instance.verify_domain(
            path_params=path_params,
        )
    except phasetwo.ApiException as e:
        print("Exception when calling OrganizationDomainsApi->verify_domain: %s\n" % e)
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
domainName | DomainNameSchema | | 

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

# DomainNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#verify_domain.ApiResponseFor202) | success

#### verify_domain.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[access_token](../../../README.md#access_token)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

