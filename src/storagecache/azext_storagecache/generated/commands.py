# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_storagecache.generated._client_factory import cf_sku
    storagecache_sku = CliCommandType(
        operations_tmpl='azext_storagecache.vendored_sdks.storagecache.operations._sku_operations#SkuOperations.{}',
        client_factory=cf_sku)
    with self.command_group('storagecache sku', storagecache_sku, client_factory=cf_sku) as g:
        g.custom_command('list', 'storagecache_sku_list')

    from azext_storagecache.generated._client_factory import cf_usage_model
    storagecache_usage_model = CliCommandType(
        operations_tmpl='azext_storagecache.vendored_sdks.storagecache.operations._usage_model_operations#UsageModelOperations.{}',
        client_factory=cf_usage_model)
    with self.command_group('storagecache usage-model', storagecache_usage_model, client_factory=cf_usage_model) as g:
        g.custom_command('list', 'storagecache_usage_model_list')

    from azext_storagecache.generated._client_factory import cf_cache
    storagecache_cache = CliCommandType(
        operations_tmpl='azext_storagecache.vendored_sdks.storagecache.operations._cache_operations#CacheOperations.{}',
        client_factory=cf_cache)
    with self.command_group('storagecache cache', storagecache_cache, client_factory=cf_cache) as g:
        g.custom_command('list', 'storagecache_cache_list')
        g.custom_show_command('show', 'storagecache_cache_show')
        g.custom_command('create', 'storagecache_cache_create', supports_no_wait=True)
        g.custom_command('update', 'storagecache_cache_update')
        g.custom_command('delete', 'storagecache_cache_delete', supports_no_wait=True)
        g.custom_command('flush', 'storagecache_cache_flush', supports_no_wait=True)
        g.custom_command('start', 'storagecache_cache_start', supports_no_wait=True)
        g.custom_command('stop', 'storagecache_cache_stop', supports_no_wait=True)
        g.custom_command('upgrade-firmware', 'storagecache_cache_upgrade_firmware', supports_no_wait=True)
        g.wait_command('wait')

    from azext_storagecache.generated._client_factory import cf_storage_target
    storagecache_storage_target = CliCommandType(
        operations_tmpl='azext_storagecache.vendored_sdks.storagecache.operations._storage_target_operations#StorageTargetOperations.{}',
        client_factory=cf_storage_target)
    with self.command_group('storagecache storage-target', storagecache_storage_target, client_factory=cf_storage_target) as g:
        g.custom_command('list', 'storagecache_storage_target_list')
        g.custom_show_command('show', 'storagecache_storage_target_show')
        g.custom_command('create', 'storagecache_storage_target_create', supports_no_wait=True)
        g.generic_update_command('update', supports_no_wait=True)
        g.custom_command('delete', 'storagecache_storage_target_delete', supports_no_wait=True)
        g.wait_command('wait')
