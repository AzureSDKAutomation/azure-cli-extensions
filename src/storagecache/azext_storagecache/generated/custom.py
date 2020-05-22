# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

import json


def storagecache_sku_list(cmd, client):
    return client.list()


def storagecache_usage_model_list(cmd, client):
    return client.list()


def storagecache_cache_list(cmd, client,
                            resource_group_name=None):
    if resource_group_name is not None:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def storagecache_cache_show(cmd, client,
                            resource_group_name,
                            cache_name):
    return client.get(resource_group_name=resource_group_name,
                      cache_name=cache_name)


def storagecache_cache_create(cmd, client,
                              resource_group_name,
                              cache_name,
                              tags=None,
                              location=None,
                              identity=None,
                              sku=None,
                              cache_size_gb=None,
                              provisioning_state=None,
                              subnet=None,
                              upgrade_status=None,
                              network_settings=None,
                              encryption_settings=None,
                              security_settings=None):
    if isinstance(tags, str):
        tags = json.loads(tags)
    if isinstance(encryption_settings, str):
        encryption_settings = json.loads(encryption_settings)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         cache_name=cache_name,
                                         tags=tags,
                                         location=location,
                                         identity=identity,
                                         sku=sku,
                                         cache_size_gb=cache_size_gb,
                                         provisioning_state=provisioning_state,
                                         subnet=subnet,
                                         upgrade_status=upgrade_status,
                                         network_settings=network_settings,
                                         encryption_settings=encryption_settings,
                                         security_settings=security_settings)


def storagecache_cache_update(cmd, client,
                              resource_group_name,
                              cache_name,
                              tags=None,
                              location=None,
                              identity=None,
                              sku=None,
                              cache_size_gb=None,
                              provisioning_state=None,
                              subnet=None,
                              upgrade_status=None,
                              network_settings=None,
                              encryption_settings=None,
                              security_settings=None):
    if isinstance(tags, str):
        tags = json.loads(tags)
    if isinstance(encryption_settings, str):
        encryption_settings = json.loads(encryption_settings)
    return client.update(resource_group_name=resource_group_name,
                         cache_name=cache_name,
                         tags=tags,
                         location=location,
                         identity=identity,
                         sku=sku,
                         cache_size_gb=cache_size_gb,
                         provisioning_state=provisioning_state,
                         subnet=subnet,
                         upgrade_status=upgrade_status,
                         network_settings=network_settings,
                         encryption_settings=encryption_settings,
                         security_settings=security_settings)


def storagecache_cache_delete(cmd, client,
                              resource_group_name,
                              cache_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               cache_name=cache_name)


def storagecache_cache_flush(cmd, client,
                             resource_group_name,
                             cache_name):
    return client.begin_flush(resource_group_name=resource_group_name,
                              cache_name=cache_name)


def storagecache_cache_start(cmd, client,
                             resource_group_name,
                             cache_name):
    return client.begin_start(resource_group_name=resource_group_name,
                              cache_name=cache_name)


def storagecache_cache_stop(cmd, client,
                            resource_group_name,
                            cache_name):
    return client.begin_stop(resource_group_name=resource_group_name,
                             cache_name=cache_name)


def storagecache_cache_upgrade_firmware(cmd, client,
                                        resource_group_name,
                                        cache_name):
    return client.begin_upgrade_firmware(resource_group_name=resource_group_name,
                                         cache_name=cache_name)


def storagecache_storage_target_list(cmd, client,
                                     resource_group_name,
                                     cache_name):
    return client.list_by_cache(resource_group_name=resource_group_name,
                                cache_name=cache_name)


def storagecache_storage_target_show(cmd, client,
                                     resource_group_name,
                                     cache_name,
                                     storage_target_name):
    return client.get(resource_group_name=resource_group_name,
                      cache_name=cache_name,
                      storage_target_name=storage_target_name)


def storagecache_storage_target_create(cmd, client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name,
                                       target_base_type=None,
                                       junctions=None,
                                       target_type=None,
                                       provisioning_state=None,
                                       nfs3=None,
                                       clfs=None,
                                       unknown=None):
    if isinstance(unknown, str):
        unknown = json.loads(unknown)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         cache_name=cache_name,
                                         storage_target_name=storage_target_name,
                                         target_base_type=target_base_type,
                                         junctions=junctions,
                                         target_type=target_type,
                                         provisioning_state=provisioning_state,
                                         nfs3=nfs3,
                                         clfs=clfs,
                                         unknown=unknown)


def storagecache_storage_target_update(cmd, client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name,
                                       target_base_type=None,
                                       junctions=None,
                                       target_type=None,
                                       provisioning_state=None,
                                       nfs3=None,
                                       clfs=None,
                                       unknown=None):
    if isinstance(unknown, str):
        unknown = json.loads(unknown)
    return client.begin_create_or_update(resource_group_name=resource_group_name,
                                         cache_name=cache_name,
                                         storage_target_name=storage_target_name,
                                         target_base_type=target_base_type,
                                         junctions=junctions,
                                         target_type=target_type,
                                         provisioning_state=provisioning_state,
                                         nfs3=nfs3,
                                         clfs=clfs,
                                         unknown=unknown)


def storagecache_storage_target_delete(cmd, client,
                                       resource_group_name,
                                       cache_name,
                                       storage_target_name):
    return client.begin_delete(resource_group_name=resource_group_name,
                               cache_name=cache_name,
                               storage_target_name=storage_target_name)
