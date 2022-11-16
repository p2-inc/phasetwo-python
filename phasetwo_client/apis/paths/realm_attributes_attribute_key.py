from phasetwo_client.paths.realm_attributes_attribute_key.get import ApiForget
from phasetwo_client.paths.realm_attributes_attribute_key.put import ApiForput
from phasetwo_client.paths.realm_attributes_attribute_key.delete import ApiFordelete


class RealmAttributesAttributeKey(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
