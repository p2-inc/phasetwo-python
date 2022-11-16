from phasetwo_client.paths.realm_orgs_org_id.get import ApiForget
from phasetwo_client.paths.realm_orgs_org_id.put import ApiForput
from phasetwo_client.paths.realm_orgs_org_id.delete import ApiFordelete


class RealmOrgsOrgId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
