# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from phasetwo.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ATTRIBUTES = "Attributes"
    EVENTS = "Events"
    IDENTITY_PROVIDERS = "Identity Providers"
    ORGANIZATION_DOMAINS = "Organization Domains"
    ORGANIZATION_INVITATION = "Organization Invitation"
    ORGANIZATION_INVITATIONS = "Organization Invitations"
    ORGANIZATION_MEMBERSHIPS = "Organization Memberships"
    ORGANIZATION_ROLES = "Organization Roles"
    ORGANIZATIONS = "Organizations"
    USERS = "Users"
