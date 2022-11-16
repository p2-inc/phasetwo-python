from phasetwo_client.paths.realm_webhooks_webhook_id.get import ApiForget
from phasetwo_client.paths.realm_webhooks_webhook_id.put import ApiForput
from phasetwo_client.paths.realm_webhooks_webhook_id.delete import ApiFordelete


class RealmWebhooksWebhookId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
