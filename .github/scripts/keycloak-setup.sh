#!/usr/bin/env bash
# Prepare a fresh Phase Two Keycloak for examples/quickstart.py: a realm, a
# confidential client with a service account that can manage the realm, and a
# user to add to an organization. Prints the example's environment variables.
#
#   .github/scripts/keycloak-setup.sh http://localhost:8080/auth >> "$GITHUB_ENV"
#
# Expects the bootstrap admin admin/admin. Needs curl and jq.
set -euo pipefail

base=${1:?usage: keycloak-setup.sh <keycloak base url, e.g. http://localhost:8080/auth>}
realm=example
client_id=api-client

token=$(curl -sf "$base/realms/master/protocol/openid-connect/token" \
  -d grant_type=password -d client_id=admin-cli -d username=admin -d password=admin | jq -r .access_token)
api() { # <method> <path> [json]
  curl -sf -X "$1" "$base/admin/realms$2" -H "Authorization: Bearer $token" \
    -H 'Content-Type: application/json' ${3:+-d "$3"}
}

api POST "" "{\"realm\":\"$realm\",\"enabled\":true}"
api POST "/$realm/clients" "{\"clientId\":\"$client_id\",\"publicClient\":false,\"serviceAccountsEnabled\":true,\"standardFlowEnabled\":false}"
cid=$(api GET "/$realm/clients?clientId=$client_id" | jq -r '.[0].id')
secret=$(api GET "/$realm/clients/$cid/client-secret" | jq -r .value)

# Let the service account manage the realm (including Phase Two organizations).
sa=$(api GET "/$realm/clients/$cid/service-account-user" | jq -r .id)
rm_id=$(api GET "/$realm/clients?clientId=realm-management" | jq -r '.[0].id')
role=$(api GET "/$realm/clients/$rm_id/roles/realm-admin")
api POST "/$realm/users/$sa/role-mappings/clients/$rm_id" "[$role]"

api POST "/$realm/users" '{"username":"jdoe","email":"jdoe@example.com","enabled":true}'
user=$(api GET "/$realm/users?username=jdoe&exact=true" | jq -r '.[0].id')

cat <<EOF
PHASETWO_URL=$base
PHASETWO_REALM=$realm
PHASETWO_CLIENT_ID=$client_id
PHASETWO_CLIENT_SECRET=$secret
EXAMPLE_USER_ID=$user
EOF
