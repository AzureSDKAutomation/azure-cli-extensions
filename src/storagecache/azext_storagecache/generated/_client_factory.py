# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_storagecache(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.storagecache import StorageCacheManagementClient
    return get_mgmt_service_client(cli_ctx, StorageCacheManagementClient)


def cf_sku(cli_ctx, *_):
    return cf_storagecache(cli_ctx).sku


def cf_usage_model(cli_ctx, *_):
    return cf_storagecache(cli_ctx).usage_model


def cf_asc_operation(cli_ctx, *_):
    return cf_storagecache(cli_ctx).asc_operation


def cf_cache(cli_ctx, *_):
    return cf_storagecache(cli_ctx).cache


def cf_storage_target(cli_ctx, *_):
    return cf_storagecache(cli_ctx).storage_target
