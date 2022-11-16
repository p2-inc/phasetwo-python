import typing_extensions

from phasetwo_client.paths import PathValues
from phasetwo_client.apis.paths.realm_orgs import RealmOrgs
from phasetwo_client.apis.paths.realm_orgs_org_id import RealmOrgsOrgId
from phasetwo_client.apis.paths.realm_orgs_org_id_portal_link import RealmOrgsOrgIdPortalLink
from phasetwo_client.apis.paths.realm_orgs_org_id_members import RealmOrgsOrgIdMembers
from phasetwo_client.apis.paths.realm_orgs_org_id_domains import RealmOrgsOrgIdDomains
from phasetwo_client.apis.paths.realm_orgs_org_id_domains_domain_name import RealmOrgsOrgIdDomainsDomainName
from phasetwo_client.apis.paths.realm_orgs_org_id_domains_domain_name_verify import RealmOrgsOrgIdDomainsDomainNameVerify
from phasetwo_client.apis.paths.realm_orgs_org_id_members_user_id import RealmOrgsOrgIdMembersUserId
from phasetwo_client.apis.paths.realm_orgs_org_id_invitations import RealmOrgsOrgIdInvitations
from phasetwo_client.apis.paths.realm_orgs_org_id_invitations_invitation_id import RealmOrgsOrgIdInvitationsInvitationId
from phasetwo_client.apis.paths.realm_orgs_org_id_roles import RealmOrgsOrgIdRoles
from phasetwo_client.apis.paths.realm_orgs_org_id_roles_name import RealmOrgsOrgIdRolesName
from phasetwo_client.apis.paths.realm_orgs_org_id_roles_name_users import RealmOrgsOrgIdRolesNameUsers
from phasetwo_client.apis.paths.realm_orgs_org_id_roles_name_users_user_id import RealmOrgsOrgIdRolesNameUsersUserId
from phasetwo_client.apis.paths.realm_orgs_org_id_idps_import_config import RealmOrgsOrgIdIdpsImportConfig
from phasetwo_client.apis.paths.realm_orgs_org_id_idps import RealmOrgsOrgIdIdps
from phasetwo_client.apis.paths.realm_orgs_org_id_idps_alias import RealmOrgsOrgIdIdpsAlias
from phasetwo_client.apis.paths.realm_orgs_org_id_idps_alias_mappers import RealmOrgsOrgIdIdpsAliasMappers
from phasetwo_client.apis.paths.realm_orgs_org_id_idps_alias_mappers_id import RealmOrgsOrgIdIdpsAliasMappersId
from phasetwo_client.apis.paths.realm_users_user_id_orgs import RealmUsersUserIdOrgs
from phasetwo_client.apis.paths.realm_users_user_id_orgs_org_id_roles import RealmUsersUserIdOrgsOrgIdRoles
from phasetwo_client.apis.paths.realm_events import RealmEvents
from phasetwo_client.apis.paths.realm_attributes import RealmAttributes
from phasetwo_client.apis.paths.realm_attributes_attribute_key import RealmAttributesAttributeKey
from phasetwo_client.apis.paths.realm_webhooks import RealmWebhooks
from phasetwo_client.apis.paths.realm_webhooks_webhook_id import RealmWebhooksWebhookId
from phasetwo_client.apis.paths.realm_magic_link import RealmMagicLink

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.REALM_ORGS: RealmOrgs,
        PathValues.REALM_ORGS_ORG_ID: RealmOrgsOrgId,
        PathValues.REALM_ORGS_ORG_ID_PORTALLINK: RealmOrgsOrgIdPortalLink,
        PathValues.REALM_ORGS_ORG_ID_MEMBERS: RealmOrgsOrgIdMembers,
        PathValues.REALM_ORGS_ORG_ID_DOMAINS: RealmOrgsOrgIdDomains,
        PathValues.REALM_ORGS_ORG_ID_DOMAINS_DOMAIN_NAME: RealmOrgsOrgIdDomainsDomainName,
        PathValues.REALM_ORGS_ORG_ID_DOMAINS_DOMAIN_NAME_VERIFY: RealmOrgsOrgIdDomainsDomainNameVerify,
        PathValues.REALM_ORGS_ORG_ID_MEMBERS_USER_ID: RealmOrgsOrgIdMembersUserId,
        PathValues.REALM_ORGS_ORG_ID_INVITATIONS: RealmOrgsOrgIdInvitations,
        PathValues.REALM_ORGS_ORG_ID_INVITATIONS_INVITATION_ID: RealmOrgsOrgIdInvitationsInvitationId,
        PathValues.REALM_ORGS_ORG_ID_ROLES: RealmOrgsOrgIdRoles,
        PathValues.REALM_ORGS_ORG_ID_ROLES_NAME: RealmOrgsOrgIdRolesName,
        PathValues.REALM_ORGS_ORG_ID_ROLES_NAME_USERS: RealmOrgsOrgIdRolesNameUsers,
        PathValues.REALM_ORGS_ORG_ID_ROLES_NAME_USERS_USER_ID: RealmOrgsOrgIdRolesNameUsersUserId,
        PathValues.REALM_ORGS_ORG_ID_IDPS_IMPORTCONFIG: RealmOrgsOrgIdIdpsImportConfig,
        PathValues.REALM_ORGS_ORG_ID_IDPS: RealmOrgsOrgIdIdps,
        PathValues.REALM_ORGS_ORG_ID_IDPS_ALIAS: RealmOrgsOrgIdIdpsAlias,
        PathValues.REALM_ORGS_ORG_ID_IDPS_ALIAS_MAPPERS: RealmOrgsOrgIdIdpsAliasMappers,
        PathValues.REALM_ORGS_ORG_ID_IDPS_ALIAS_MAPPERS_ID: RealmOrgsOrgIdIdpsAliasMappersId,
        PathValues.REALM_USERS_USER_ID_ORGS: RealmUsersUserIdOrgs,
        PathValues.REALM_USERS_USER_ID_ORGS_ORG_ID_ROLES: RealmUsersUserIdOrgsOrgIdRoles,
        PathValues.REALM_EVENTS: RealmEvents,
        PathValues.REALM_ATTRIBUTES: RealmAttributes,
        PathValues.REALM_ATTRIBUTES_ATTRIBUTE_KEY: RealmAttributesAttributeKey,
        PathValues.REALM_WEBHOOKS: RealmWebhooks,
        PathValues.REALM_WEBHOOKS_WEBHOOK_ID: RealmWebhooksWebhookId,
        PathValues.REALM_MAGICLINK: RealmMagicLink,
    }
)

path_to_api = PathToApi(
    {
        PathValues.REALM_ORGS: RealmOrgs,
        PathValues.REALM_ORGS_ORG_ID: RealmOrgsOrgId,
        PathValues.REALM_ORGS_ORG_ID_PORTALLINK: RealmOrgsOrgIdPortalLink,
        PathValues.REALM_ORGS_ORG_ID_MEMBERS: RealmOrgsOrgIdMembers,
        PathValues.REALM_ORGS_ORG_ID_DOMAINS: RealmOrgsOrgIdDomains,
        PathValues.REALM_ORGS_ORG_ID_DOMAINS_DOMAIN_NAME: RealmOrgsOrgIdDomainsDomainName,
        PathValues.REALM_ORGS_ORG_ID_DOMAINS_DOMAIN_NAME_VERIFY: RealmOrgsOrgIdDomainsDomainNameVerify,
        PathValues.REALM_ORGS_ORG_ID_MEMBERS_USER_ID: RealmOrgsOrgIdMembersUserId,
        PathValues.REALM_ORGS_ORG_ID_INVITATIONS: RealmOrgsOrgIdInvitations,
        PathValues.REALM_ORGS_ORG_ID_INVITATIONS_INVITATION_ID: RealmOrgsOrgIdInvitationsInvitationId,
        PathValues.REALM_ORGS_ORG_ID_ROLES: RealmOrgsOrgIdRoles,
        PathValues.REALM_ORGS_ORG_ID_ROLES_NAME: RealmOrgsOrgIdRolesName,
        PathValues.REALM_ORGS_ORG_ID_ROLES_NAME_USERS: RealmOrgsOrgIdRolesNameUsers,
        PathValues.REALM_ORGS_ORG_ID_ROLES_NAME_USERS_USER_ID: RealmOrgsOrgIdRolesNameUsersUserId,
        PathValues.REALM_ORGS_ORG_ID_IDPS_IMPORTCONFIG: RealmOrgsOrgIdIdpsImportConfig,
        PathValues.REALM_ORGS_ORG_ID_IDPS: RealmOrgsOrgIdIdps,
        PathValues.REALM_ORGS_ORG_ID_IDPS_ALIAS: RealmOrgsOrgIdIdpsAlias,
        PathValues.REALM_ORGS_ORG_ID_IDPS_ALIAS_MAPPERS: RealmOrgsOrgIdIdpsAliasMappers,
        PathValues.REALM_ORGS_ORG_ID_IDPS_ALIAS_MAPPERS_ID: RealmOrgsOrgIdIdpsAliasMappersId,
        PathValues.REALM_USERS_USER_ID_ORGS: RealmUsersUserIdOrgs,
        PathValues.REALM_USERS_USER_ID_ORGS_ORG_ID_ROLES: RealmUsersUserIdOrgsOrgIdRoles,
        PathValues.REALM_EVENTS: RealmEvents,
        PathValues.REALM_ATTRIBUTES: RealmAttributes,
        PathValues.REALM_ATTRIBUTES_ATTRIBUTE_KEY: RealmAttributesAttributeKey,
        PathValues.REALM_WEBHOOKS: RealmWebhooks,
        PathValues.REALM_WEBHOOKS_WEBHOOK_ID: RealmWebhooksWebhookId,
        PathValues.REALM_MAGICLINK: RealmMagicLink,
    }
)
