"""Quick start for the Phase Two Python SDK. The README shows the code between the
snippet markers; CI runs this file against Phase Two Keycloak.

Environment: PHASETWO_URL (e.g. https://auth.example.com/auth), PHASETWO_REALM,
PHASETWO_CLIENT_ID, PHASETWO_CLIENT_SECRET, EXAMPLE_USER_ID (an existing user).
"""

import os

base_url = os.environ["PHASETWO_URL"]
realm = os.environ["PHASETWO_REALM"]
client_id = os.environ["PHASETWO_CLIENT_ID"]
client_secret = os.environ["PHASETWO_CLIENT_SECRET"]
user_id = os.environ["EXAMPLE_USER_ID"]

# snippet:start quickstart
import time

import urllib3

from phasetwo import (
    ApiClient,
    Configuration,
    EventRepresentation,
    EventsApi,
    OrganizationMembershipsApi,
    OrganizationRepresentation,
    OrganizationsApi,
)

# Get a token for a service account with the client credentials grant.
token = urllib3.PoolManager().request(
    "POST",
    f"{base_url}/realms/{realm}/protocol/openid-connect/token",
    fields={"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret},
    encode_multipart=False,
).json()["access_token"]

config = Configuration(host=f"{base_url}/realms", access_token=token)

with ApiClient(config) as client:
    orgs = OrganizationsApi(client)

    # Create an organization. The response is empty; the new id is in the Location header.
    created = orgs.create_organization_with_http_info(
        realm, OrganizationRepresentation(name="acme", domains=["acme.example.com"])
    )
    org_id = created.headers["Location"].rsplit("/", 1)[-1]

    # Add an existing user as a member.
    OrganizationMembershipsApi(client).add_organization_member(realm, org_id, user_id)

    # Create a link to the IdP Wizard, for the organization's admin to set up SSO.
    link = orgs.create_portal_link(realm, org_id)
    print("IdP Wizard:", link.link)

    # Record an audit event.
    EventsApi(client).create_event(
        realm, EventRepresentation(type="acme.onboarded", time=int(time.time() * 1000))
    )
    # snippet:end quickstart

    # snippet:start errors
    from phasetwo import ApiException, NotFoundException

    orgs.delete_organization(realm, org_id)
    try:
        orgs.get_organization_by_id(realm, org_id)
    except NotFoundException:
        print("Deleted:", org_id)
    except ApiException as e:  # any other non-2xx response
        print(e.status, e.reason, e.body)
    # snippet:end errors
