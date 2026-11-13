# Phase Two Python SDK

<!-- phasetwo:banner:start - managed by p2-inc/shared-github-actions, edit there -->
[![license](https://img.shields.io/badge/license-Apache--2.0-blue)](COPYING) [![docs](https://img.shields.io/badge/docs-phasetwo.io-blue)](https://phasetwo.io/docs/api/sdks/)

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

The Phase Two Python SDK library provides access to the Phase Two API for server-side Python applications.

> [!NOTE]
> All Phase Two SDKs (Java, TypeScript, Python, Go) share the version of the Phase Two API they implement: every SDK release X.Y.* implements API X.Y, and patch releases are SDK-only fixes. While on 0.x, a new minor version can contain breaking changes from the API spec, so pin a version.

## Documentation

See the [API Reference](https://phasetwo.io/api/phase-two-admin-rest-api)

## Installation

```sh
pip install phasetwo-sdk
```

Requires Python 3.11 or later. The import name is `phasetwo`.

## Use

Get an access token for a service account (client credentials grant) with any OIDC library, for example [python-keycloak](https://python-keycloak.readthedocs.io/en/latest/), and pass it to the SDK's `Configuration`. The host is your Keycloak base URL followed by `/realms`.

```python
import json
import time

from phasetwo import (
    ApiClient,
    Configuration,
    EventRepresentation,
    EventsApi,
    OrganizationRepresentation,
    OrganizationsApi,
)

realm = "my-realm"
config = Configuration(
    host="https://my-phasetwo-host/auth/realms",
    access_token=get_access_token(),  # e.g. KeycloakOpenID(...).token(grant_type="client_credentials")["access_token"]
)

with ApiClient(config) as client:
    orgs = OrganizationsApi(client)

    # Create an organization. The new id is in the Location header.
    resp = orgs.create_organization_with_http_info(realm, OrganizationRepresentation(name="example"))
    org_id = resp.headers["Location"].rsplit("/", 1)[-1]

    # Create a link to the IdP Wizard for the organization
    link = orgs.create_portal_link(realm, org_id).link

    # Create and publish an audit event
    EventsApi(client).create_event(
        realm,
        EventRepresentation(type="foo.bar", representation=json.dumps({"orgId": org_id}), time=int(time.time() * 1000)),
    )
```

## Generated code

The API classes and models in `phasetwo/openapi` are generated from the [Phase Two OpenAPI spec](https://github.com/p2-inc/phasetwo-docs/blob/main/openapi.yaml) by [phasetwo-sdk-generator](https://github.com/p2-inc/phasetwo-sdk-generator) (generator: [python](https://openapi-generator.tech/docs/generators/python)) and re-exported from `phasetwo`. Don't edit them by hand; `sdk-generator.json` records the spec commit they came from. `phasetwo/__init__.py` and `pyproject.toml` are hand-written.

To build: `uv build`

## License

Apache License 2.0, see [COPYING](COPYING).
