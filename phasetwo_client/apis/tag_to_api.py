import typing_extensions

from phasetwo_client.apis.tags import TagValues
from phasetwo_client.apis.tags.attributes_api import AttributesApi
from phasetwo_client.apis.tags.events_api import EventsApi
from phasetwo_client.apis.tags.identity_providers_api import IdentityProvidersApi
from phasetwo_client.apis.tags.organization_domains_api import OrganizationDomainsApi
from phasetwo_client.apis.tags.organization_invitations_api import OrganizationInvitationsApi
from phasetwo_client.apis.tags.organization_memberships_api import OrganizationMembershipsApi
from phasetwo_client.apis.tags.organization_roles_api import OrganizationRolesApi
from phasetwo_client.apis.tags.organizations_api import OrganizationsApi
from phasetwo_client.apis.tags.users_api import UsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ATTRIBUTES: AttributesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.IDENTITY_PROVIDERS: IdentityProvidersApi,
        TagValues.ORGANIZATION_DOMAINS: OrganizationDomainsApi,
        TagValues.ORGANIZATION_INVITATIONS: OrganizationInvitationsApi,
        TagValues.ORGANIZATION_MEMBERSHIPS: OrganizationMembershipsApi,
        TagValues.ORGANIZATION_ROLES: OrganizationRolesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.USERS: UsersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ATTRIBUTES: AttributesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.IDENTITY_PROVIDERS: IdentityProvidersApi,
        TagValues.ORGANIZATION_DOMAINS: OrganizationDomainsApi,
        TagValues.ORGANIZATION_INVITATIONS: OrganizationInvitationsApi,
        TagValues.ORGANIZATION_MEMBERSHIPS: OrganizationMembershipsApi,
        TagValues.ORGANIZATION_ROLES: OrganizationRolesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.USERS: UsersApi,
    }
)
