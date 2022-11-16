from phasetwo.paths.realm_attributes_attribute_key.get import ApiForget
from phasetwo.paths.realm_attributes_attribute_key.put import ApiForput
from phasetwo.paths.realm_attributes_attribute_key.delete import ApiFordelete


class RealmAttributesAttributeKey(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
