# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from phasetwo.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    REALM_ORGS = "/{realm}/orgs"
    REALM_ORGS_ORG_ID = "/{realm}/orgs/{orgId}"
    REALM_ORGS_ORG_ID_PORTALLINK = "/{realm}/orgs/{orgId}/portal-link"
    REALM_ORGS_ORG_ID_MEMBERS = "/{realm}/orgs/{orgId}/members"
    REALM_ORGS_ORG_ID_DOMAINS = "/{realm}/orgs/{orgId}/domains"
    REALM_ORGS_ORG_ID_DOMAINS_DOMAIN_NAME = "/{realm}/orgs/{orgId}/domains/{domainName}"
    REALM_ORGS_ORG_ID_DOMAINS_DOMAIN_NAME_VERIFY = "/{realm}/orgs/{orgId}/domains/{domainName}/verify"
    REALM_ORGS_ORG_ID_MEMBERS_USER_ID = "/{realm}/orgs/{orgId}/members/{userId}"
    REALM_ORGS_ORG_ID_INVITATIONS = "/{realm}/orgs/{orgId}/invitations"
    REALM_ORGS_ORG_ID_INVITATIONS_INVITATION_ID = "/{realm}/orgs/{orgId}/invitations/{invitationId}"
    REALM_ORGS_ORG_ID_ROLES = "/{realm}/orgs/{orgId}/roles"
    REALM_ORGS_ORG_ID_ROLES_NAME = "/{realm}/orgs/{orgId}/roles/{name}"
    REALM_ORGS_ORG_ID_ROLES_NAME_USERS = "/{realm}/orgs/{orgId}/roles/{name}/users"
    REALM_ORGS_ORG_ID_ROLES_NAME_USERS_USER_ID = "/{realm}/orgs/{orgId}/roles/{name}/users/{userId}"
    REALM_ORGS_ORG_ID_IDPS_IMPORTCONFIG = "/{realm}/orgs/{orgId}/idps/import-config"
    REALM_ORGS_ORG_ID_IDPS = "/{realm}/orgs/{orgId}/idps"
    REALM_ORGS_ORG_ID_IDPS_ALIAS = "/{realm}/orgs/{orgId}/idps/{alias}"
    REALM_ORGS_ORG_ID_IDPS_ALIAS_MAPPERS = "/{realm}/orgs/{orgId}/idps/{alias}/mappers"
    REALM_ORGS_ORG_ID_IDPS_ALIAS_MAPPERS_ID = "/{realm}/orgs/{orgId}/idps/{alias}/mappers/{id}"
    REALM_USERS_USER_ID_ORGS = "/{realm}/users/{userId}/orgs"
    REALM_USERS_USER_ID_ORGS_ORG_ID_ROLES = "/{realm}/users/{userId}/orgs/{orgId}/roles"
    REALM_EVENTS = "/{realm}/events"
    REALM_ATTRIBUTES = "/{realm}/attributes"
    REALM_ATTRIBUTES_ATTRIBUTE_KEY = "/{realm}/attributes/{attributeKey}"
    REALM_WEBHOOKS = "/{realm}/webhooks"
    REALM_WEBHOOKS_WEBHOOK_ID = "/{realm}/webhooks/{webhookId}"
    REALM_MAGICLINK = "/{realm}/magic-link"
