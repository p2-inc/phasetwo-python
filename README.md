# Phase Two Python SDK

<!-- phasetwo:banner:start - managed by p2-inc/shared-github-actions, edit there -->
[![PyPI](https://img.shields.io/pypi/v/phasetwo-sdk)](https://pypi.org/project/phasetwo-sdk/) [![license](https://img.shields.io/badge/license-Apache--2.0-blue)](COPYING) [![docs](https://img.shields.io/badge/docs-phasetwo.io-blue)](https://phasetwo.io/docs/api/sdks/)

📚 [Documentation](https://phasetwo.io/docs/api/sdks/) • 🚀 [Hosted Keycloak](https://dash.phasetwo.io/?utm_source=github&utm_medium=readme&utm_campaign=phasetwo-python) • 🤖 [Keycloak Skills](https://github.com/p2-inc/keycloak-skills) • 💬 [Support](mailto:support@phasetwo.io)

> [!TIP]
> **Run this in our cloud, no setup needed.** Phase Two hosts Keycloak with all of our extensions built in. [Try it free with your own cluster →](https://dash.phasetwo.io/?utm_source=github&utm_medium=readme&utm_campaign=phasetwo-python)
>
> **Using a coding agent?** Add the Phase Two Keycloak skills ([launch post](https://phasetwo.io/blog/keycloak-skills-mcp-launch)) to Claude Code, Cursor or Codex so your agent can set up passwordless login, SSO, organizations and clusters for you:
>
> ```sh
> # Install the skills (connects to our hosted MCP server)
> claude plugin marketplace add p2-inc/keycloak-skills
> claude plugin install phasetwo@keycloak-skills
> # Or connect to the MCP server directly
> claude mcp add --transport http keycloak https://mcp.phasetwo.io/mcp
> ```
<!-- phasetwo:banner:end -->

Python client for the [Phase Two Admin API](https://phasetwo.io/api/phase-two-admin-rest-api): organizations, members, roles, domains, identity providers, invitations, SCIM, webhooks and events, realm attributes and magic links. For the core Keycloak Admin API (users, clients, realms), use the official admin client for your language; for Python, [python-keycloak](https://python-keycloak.readthedocs.io/).

> [!NOTE]
> Pre-1.0: minor versions can include breaking changes. All Phase Two SDKs share a version: release X.Y.* implements Phase Two API X.Y.

## Installation

```sh
pip install phasetwo-sdk
# or
uv add phasetwo-sdk
```

Requires Python 3.11 or later (tested on 3.11 to 3.14). The package is `phasetwo-sdk`; the import name is `phasetwo`.

## Quick start

Create an organization, add a member, create an IdP Wizard link for the organization's admin, and record an audit event. This is [`examples/quickstart.py`](examples/quickstart.py), which CI runs against Phase Two Keycloak.

<!-- phasetwo:snippet quickstart examples/quickstart.py -->
```python
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
```
<!-- /phasetwo:snippet -->

`base_url` is your Keycloak URL including `/auth` (for example `https://auth.example.com/auth`); the SDK's `host` is that plus `/realms`.

## Authentication

Every request needs an access token in `Configuration(access_token=...)`. We recommend a [service account](https://phasetwo.io/docs/api/service-accounts): a confidential client with *Service accounts* enabled and the `realm-management` roles it needs (for example `manage-organizations`), using the client credentials grant as in the quick start. Any HTTP or OIDC library can get the token:

- [python-keycloak](https://python-keycloak.readthedocs.io/): `KeycloakOpenID(server_url=..., realm_name=..., client_id=..., client_secret_key=...).token(grant_type="client_credentials")["access_token"]`
- `httpx` or `requests`: `POST {base_url}/realms/{realm}/protocol/openid-connect/token` with form fields `grant_type=client_credentials`, `client_id`, `client_secret`.

Tokens expire (5 minutes by default). For long-running processes, get a new token before it expires and set `config.access_token` again.

## Usage

- There is one API class per area (`OrganizationsApi`, `OrganizationMembershipsApi`, `EventsApi`, ...), created from a shared `ApiClient`. Use `with ApiClient(config) as client:` so the connection pool is closed.
- Methods are named after the API operation (`createOrganization` → `create_organization`) and take the realm name first, then path parameters, then the request body. Optional query parameters are keyword arguments.
- Request and response bodies are pydantic models (`OrganizationRepresentation`, ...).
- Each method has a `*_with_http_info` variant that also returns the status code and headers. Creates return `201` with an empty body and the new resource's URL in `Location`; read the id from there, as the quick start does.

### Errors

Any non-2xx response raises an `ApiException`, with `status`, `reason`, `headers` and `body`. Common statuses have their own subclass: `BadRequestException` (400), `UnauthorizedException` (401), `ForbiddenException` (403), `NotFoundException` (404), `ConflictException` (409), `UnprocessableEntityException` (422) and `ServiceException` (5xx). All are importable from `phasetwo`.

<!-- phasetwo:snippet errors examples/quickstart.py -->
```python
from phasetwo import ApiException, NotFoundException

orgs.delete_organization(realm, org_id)
try:
    orgs.get_organization_by_id(realm, org_id)
except NotFoundException:
    print("Deleted:", org_id)
except ApiException as e:  # any other non-2xx response
    print(e.status, e.reason, e.body)
```
<!-- /phasetwo:snippet -->

## Compatibility

| SDK | Phase Two API | Tested against |
|---|---|---|
| 0.2.x | 0.2 | `quay.io/phasetwo/phasetwo-keycloak:26.5.6` |

The API version and the exact spec commit the code was generated from are in [`sdk-generator.json`](sdk-generator.json).

## API reference

- [Phase Two Admin REST API reference](https://phasetwo.io/api/phase-two-admin-rest-api): every operation, with request and response schemas.
- The API classes and models have docstrings generated from the same spec; use your editor's help or `help(phasetwo.OrganizationsApi)`.

## Generated code

The API classes and models in `phasetwo/openapi/` are generated from the [Phase Two OpenAPI spec](https://github.com/p2-inc/phasetwo-docs/blob/main/openapi.yaml) by [phasetwo-sdk-generator](https://github.com/p2-inc/phasetwo-sdk-generator) and re-exported from `phasetwo`. Don't edit them by hand: changes come from the spec or the generator, and CI fails if the generated code doesn't match. The README code blocks are copied from `examples/` by the same tool.

## License

Apache License 2.0, see [COPYING](COPYING).
