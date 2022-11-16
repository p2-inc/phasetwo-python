> :bug: **This is alpha software**

# Python SDK for Phase Two API

The Phase Two Python SDK library provides access to the Phase Two API for server-side Python applications.

## Documentation

See the [API Reference](https://phasetwo.io/api/) and [PyPI](https://pypi.org/project/phasetwo-sdk/).

## Installation

todo

## Use

The Python SDK assumes the use of the [Python Keycloak](https://python-keycloak.readthedocs.io/en/latest/) library for authentication.

### Examples

```python
import time
import phasetwo
from keycloak import KeycloakAdmin
from phasetwo.apis.tags import attributes_api
from phasetwo.model.realm_attribute_representation import RealmAttributeRepresentation

realm = "my-realm"

keycloak_admin = KeycloakAdmin(server_url="https://my-keycloak-host/auth/",
                               username='admin',
                               password='password',
                               realm_name=realm,
                               client_id='admin-cli',
                               verify=True)

configuration = phasetwo.Configuration(
    host = "https://app.phasetwo.io/auth/realms"
    access_token = keycloak_admin.token()
)

client = phasetwo.ApiClient(configuration)

# Create a new realm attribute
attr_api = attributes_api.AttributesApi(client)
attr = RealmAttributeRepresentation(name="foo", value="bar", realm=realm)
try:
    attr_api.create_realm_attribute(attr)
except phasetwo.ApiException as e:
    print("Exception when calling AttributesApi->create_realm_attribute: %s\n" % e)

# Create an Organization

# Create an Admin Portal link for the Organization

# Create and publish an Audit Event

```

---

## Developers

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import phasetwo
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import phasetwo
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import phasetwo
from pprint import pprint
from phasetwo.apis.tags import attributes_api
from phasetwo.model.keyed_realm_attribute_representation import KeyedRealmAttributeRepresentation
from phasetwo.model.realm_attribute_representation import RealmAttributeRepresentation
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
    api_instance = attributes_api.AttributesApi(api_client)
    realm = "realm_example" # str | realm name (not id!)
realm_attribute_representation = RealmAttributeRepresentation(
        name="name_example",
        value="value_example",
        realm="realm_example",
    ) # RealmAttributeRepresentation | JSON body

    try:
        # Create a new realm attribute
        api_instance.create_realm_attribute(realmrealm_attribute_representation)
    except phasetwo.ApiException as e:
        print("Exception when calling AttributesApi->create_realm_attribute: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.phasetwo.io/auth/realms*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttributesApi* | [**create_realm_attribute**](docs/apis/tags/AttributesApi.md#create_realm_attribute) | **post** /{realm}/attributes | Create a new realm attribute
*AttributesApi* | [**delete_realm_attribute**](docs/apis/tags/AttributesApi.md#delete_realm_attribute) | **delete** /{realm}/attributes/{attributeKey} | Delete the realm attribute
*AttributesApi* | [**get_realm_attribute_by_key**](docs/apis/tags/AttributesApi.md#get_realm_attribute_by_key) | **get** /{realm}/attributes/{attributeKey} | Get realm attribute by key
*AttributesApi* | [**get_realm_attributes**](docs/apis/tags/AttributesApi.md#get_realm_attributes) | **get** /{realm}/attributes | Get realm attributes
*AttributesApi* | [**update_realm_attribute_by_key**](docs/apis/tags/AttributesApi.md#update_realm_attribute_by_key) | **put** /{realm}/attributes/{attributeKey} | Update realm attribute by key
*EventsApi* | [**create_event**](docs/apis/tags/EventsApi.md#create_event) | **post** /{realm}/events | Create a new audit log event
*EventsApi* | [**create_webhook**](docs/apis/tags/EventsApi.md#create_webhook) | **post** /{realm}/webhooks | Create a new webhook
*EventsApi* | [**delete_webhook**](docs/apis/tags/EventsApi.md#delete_webhook) | **delete** /{realm}/webhooks/{webhookId} | Delete the webhook
*EventsApi* | [**get_webhook_by_id**](docs/apis/tags/EventsApi.md#get_webhook_by_id) | **get** /{realm}/webhooks/{webhookId} | Get webhook by id
*EventsApi* | [**get_webhooks**](docs/apis/tags/EventsApi.md#get_webhooks) | **get** /{realm}/webhooks | Get webhooks
*EventsApi* | [**update_webhook**](docs/apis/tags/EventsApi.md#update_webhook) | **put** /{realm}/webhooks/{webhookId} | Update this webhook by id
*IdentityProvidersApi* | [**add_idp_mapper**](docs/apis/tags/IdentityProvidersApi.md#add_idp_mapper) | **post** /{realm}/orgs/{orgId}/idps/{alias}/mappers | Add a mapper to identity provider
*IdentityProvidersApi* | [**create_idp**](docs/apis/tags/IdentityProvidersApi.md#create_idp) | **post** /{realm}/orgs/{orgId}/idps | Create a new identity provider for this organization
*IdentityProvidersApi* | [**delete_idp**](docs/apis/tags/IdentityProvidersApi.md#delete_idp) | **delete** /{realm}/orgs/{orgId}/idps/{alias} | Delete the identity provider
*IdentityProvidersApi* | [**delete_idp_mapper**](docs/apis/tags/IdentityProvidersApi.md#delete_idp_mapper) | **delete** /{realm}/orgs/{orgId}/idps/{alias}/mappers/{id} | Delete a mapper for the identity provider
*IdentityProvidersApi* | [**get_idp**](docs/apis/tags/IdentityProvidersApi.md#get_idp) | **get** /{realm}/orgs/{orgId}/idps/{alias} | Get identity provider for this organization by alias
*IdentityProvidersApi* | [**get_idp_mapper**](docs/apis/tags/IdentityProvidersApi.md#get_idp_mapper) | **get** /{realm}/orgs/{orgId}/idps/{alias}/mappers/{id} | Get mapper by id for the identity provider
*IdentityProvidersApi* | [**get_idp_mappers**](docs/apis/tags/IdentityProvidersApi.md#get_idp_mappers) | **get** /{realm}/orgs/{orgId}/idps/{alias}/mappers | Get mappers for identity provider
*IdentityProvidersApi* | [**get_idps**](docs/apis/tags/IdentityProvidersApi.md#get_idps) | **get** /{realm}/orgs/{orgId}/idps | Get identity providers for this organization
*IdentityProvidersApi* | [**import_idp_json**](docs/apis/tags/IdentityProvidersApi.md#import_idp_json) | **post** /{realm}/orgs/{orgId}/idps/import-config | Import identity provider from uploaded JSON file
*IdentityProvidersApi* | [**update_idp**](docs/apis/tags/IdentityProvidersApi.md#update_idp) | **put** /{realm}/orgs/{orgId}/idps/{alias} | Update identity provider for this organization by alias
*IdentityProvidersApi* | [**update_idp_mapper**](docs/apis/tags/IdentityProvidersApi.md#update_idp_mapper) | **put** /{realm}/orgs/{orgId}/idps/{alias}/mappers/{id} | Update a mapper for the identity provider
*OrganizationDomainsApi* | [**get_organization_domain**](docs/apis/tags/OrganizationDomainsApi.md#get_organization_domain) | **get** /{realm}/orgs/{orgId}/domains/{domainName} | Get details for a domain owned by an organization
*OrganizationDomainsApi* | [**get_organization_domains**](docs/apis/tags/OrganizationDomainsApi.md#get_organization_domains) | **get** /{realm}/orgs/{orgId}/domains | Get details for all domains owned by an organization
*OrganizationDomainsApi* | [**verify_domain**](docs/apis/tags/OrganizationDomainsApi.md#verify_domain) | **post** /{realm}/orgs/{orgId}/domains/{domainName}/verify | Start domain verification
*OrganizationInvitationsApi* | [**add_organization_invitation**](docs/apis/tags/OrganizationInvitationsApi.md#add_organization_invitation) | **post** /{realm}/orgs/{orgId}/invitations | Create an invitation to an organization
*OrganizationInvitationsApi* | [**get_organization_invitations**](docs/apis/tags/OrganizationInvitationsApi.md#get_organization_invitations) | **get** /{realm}/orgs/{orgId}/invitations | Get organization invitations
*OrganizationInvitationsApi* | [**remove_organization_invitation**](docs/apis/tags/OrganizationInvitationsApi.md#remove_organization_invitation) | **delete** /{realm}/orgs/{orgId}/invitations/{invitationId} | Remove a pending invitation
*OrganizationMembershipsApi* | [**add_organization_member**](docs/apis/tags/OrganizationMembershipsApi.md#add_organization_member) | **put** /{realm}/orgs/{orgId}/members/{userId} | Add an organization member
*OrganizationMembershipsApi* | [**check_organization_membership**](docs/apis/tags/OrganizationMembershipsApi.md#check_organization_membership) | **get** /{realm}/orgs/{orgId}/members/{userId} | Check if a user is a member of an organization
*OrganizationMembershipsApi* | [**get_organization_memberships**](docs/apis/tags/OrganizationMembershipsApi.md#get_organization_memberships) | **get** /{realm}/orgs/{orgId}/members | Get organization memberships
*OrganizationMembershipsApi* | [**remove_organization_member**](docs/apis/tags/OrganizationMembershipsApi.md#remove_organization_member) | **delete** /{realm}/orgs/{orgId}/members/{userId} | Remove an organization member
*OrganizationRolesApi* | [**check_user_organization_role**](docs/apis/tags/OrganizationRolesApi.md#check_user_organization_role) | **get** /{realm}/orgs/{orgId}/roles/{name}/users/{userId} | Check if a user has an organization role
*OrganizationRolesApi* | [**create_organization_role**](docs/apis/tags/OrganizationRolesApi.md#create_organization_role) | **post** /{realm}/orgs/{orgId}/roles | Create a new role for this organization
*OrganizationRolesApi* | [**delete_organization_role**](docs/apis/tags/OrganizationRolesApi.md#delete_organization_role) | **delete** /{realm}/orgs/{orgId}/roles/{name} | Delete this organization role
*OrganizationRolesApi* | [**get_organization_role**](docs/apis/tags/OrganizationRolesApi.md#get_organization_role) | **get** /{realm}/orgs/{orgId}/roles/{name} | Get role for this organization by name
*OrganizationRolesApi* | [**get_organization_roles**](docs/apis/tags/OrganizationRolesApi.md#get_organization_roles) | **get** /{realm}/orgs/{orgId}/roles | Get roles for this organization
*OrganizationRolesApi* | [**get_user_organization_roles**](docs/apis/tags/OrganizationRolesApi.md#get_user_organization_roles) | **get** /{realm}/orgs/{orgId}/roles/{name}/users | Get users with this organization role
*OrganizationRolesApi* | [**grant_user_organization_role**](docs/apis/tags/OrganizationRolesApi.md#grant_user_organization_role) | **put** /{realm}/orgs/{orgId}/roles/{name}/users/{userId} | Grant a user an organization role
*OrganizationRolesApi* | [**revoke_user_organization_role**](docs/apis/tags/OrganizationRolesApi.md#revoke_user_organization_role) | **delete** /{realm}/orgs/{orgId}/roles/{name}/users/{userId} | Revoke an organization role from a user
*OrganizationRolesApi* | [**update_organization_role**](docs/apis/tags/OrganizationRolesApi.md#update_organization_role) | **put** /{realm}/orgs/{orgId}/roles/{name} | Update role for this organization
*OrganizationsApi* | [**create_organization**](docs/apis/tags/OrganizationsApi.md#create_organization) | **post** /{realm}/orgs | Create a new organization
*OrganizationsApi* | [**create_portal_link**](docs/apis/tags/OrganizationsApi.md#create_portal_link) | **post** /{realm}/orgs/{orgId}/portal-link | Create a link for the organization&#x27;s admin portal
*OrganizationsApi* | [**delete_organization**](docs/apis/tags/OrganizationsApi.md#delete_organization) | **delete** /{realm}/orgs/{orgId} | Delete the organization
*OrganizationsApi* | [**get_organization_by_id**](docs/apis/tags/OrganizationsApi.md#get_organization_by_id) | **get** /{realm}/orgs/{orgId} | Get organization by id
*OrganizationsApi* | [**get_organizations**](docs/apis/tags/OrganizationsApi.md#get_organizations) | **get** /{realm}/orgs | Get organizations
*OrganizationsApi* | [**update_organization**](docs/apis/tags/OrganizationsApi.md#update_organization) | **put** /{realm}/orgs/{orgId} | Update this organization by id
*UsersApi* | [**create_magic_link**](docs/apis/tags/UsersApi.md#create_magic_link) | **post** /{realm}/magic-link | Create a magic link to log in a user
*UsersApi* | [**realm_users_user_id_orgs_get**](docs/apis/tags/UsersApi.md#realm_users_user_id_orgs_get) | **get** /{realm}/users/{userId}/orgs | List organizations for the given user
*UsersApi* | [**realm_users_user_id_orgs_org_id_roles_get**](docs/apis/tags/UsersApi.md#realm_users_user_id_orgs_org_id_roles_get) | **get** /{realm}/users/{userId}/orgs/{orgId}/roles | List organization roles for the given user and org

## Documentation For Models

 - [AuthDetailsRepresentation](docs/models/AuthDetailsRepresentation.md)
 - [EventRepresentation](docs/models/EventRepresentation.md)
 - [IdentityProviderMapperRepresentation](docs/models/IdentityProviderMapperRepresentation.md)
 - [IdentityProviderRepresentation](docs/models/IdentityProviderRepresentation.md)
 - [InvitationRepresentation](docs/models/InvitationRepresentation.md)
 - [InvitationRequestRepresentation](docs/models/InvitationRequestRepresentation.md)
 - [KeyedRealmAttributeRepresentation](docs/models/KeyedRealmAttributeRepresentation.md)
 - [MagicLinkRepresentation](docs/models/MagicLinkRepresentation.md)
 - [OrganizationDomainRepresentation](docs/models/OrganizationDomainRepresentation.md)
 - [OrganizationRepresentation](docs/models/OrganizationRepresentation.md)
 - [OrganizationRoleRepresentation](docs/models/OrganizationRoleRepresentation.md)
 - [PortalLinkRepresentation](docs/models/PortalLinkRepresentation.md)
 - [RealmAttributeRepresentation](docs/models/RealmAttributeRepresentation.md)
 - [UserRepresentation](docs/models/UserRepresentation.md)
 - [WebhookRepresentation](docs/models/WebhookRepresentation.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## access_token

- **Type**: Bearer authentication

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in phasetwo.apis and phasetwo.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from phasetwo.apis.default_api import DefaultApi`
- `from phasetwo.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import phasetwo
from phasetwo.apis import *
from phasetwo.models import *
```

---

All documentation, source code and other files in this repository are Copyright 2022 Phase Two, Inc.
