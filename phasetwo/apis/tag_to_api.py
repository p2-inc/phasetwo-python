import typing_extensions

from phasetwo.apis.tags import TagValues
from phasetwo.apis.tags.attributes_api import AttributesApi
from phasetwo.apis.tags.events_api import EventsApi
from phasetwo.apis.tags.identity_providers_api import IdentityProvidersApi
from phasetwo.apis.tags.organization_domains_api import OrganizationDomainsApi
from phasetwo.apis.tags.organization_invitation_api import OrganizationInvitationApi
from phasetwo.apis.tags.organization_invitations_api import OrganizationInvitationsApi
from phasetwo.apis.tags.organization_memberships_api import OrganizationMembershipsApi
from phasetwo.apis.tags.organization_roles_api import OrganizationRolesApi
from phasetwo.apis.tags.organizations_api import OrganizationsApi
from phasetwo.apis.tags.users_api import UsersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ATTRIBUTES: AttributesApi,
        TagValues.EVENTS: EventsApi,
        TagValues.IDENTITY_PROVIDERS: IdentityProvidersApi,
        TagValues.ORGANIZATION_DOMAINS: OrganizationDomainsApi,
        TagValues.ORGANIZATION_INVITATION: OrganizationInvitationApi,
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
        TagValues.ORGANIZATION_INVITATION: OrganizationInvitationApi,
        TagValues.ORGANIZATION_INVITATIONS: OrganizationInvitationsApi,
        TagValues.ORGANIZATION_MEMBERSHIPS: OrganizationMembershipsApi,
        TagValues.ORGANIZATION_ROLES: OrganizationRolesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.USERS: UsersApi,
    }
)
