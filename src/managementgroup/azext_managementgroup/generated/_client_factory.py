# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_managementgroup(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.managementgroup import ManagementGroupsAPI
    return get_mgmt_service_client(cli_ctx, ManagementGroupsAPI,
                                   subscription_bound=False,
                                   base_url_bound=True)


def cf_management_group(cli_ctx, *_):
    return cf_managementgroup(cli_ctx).management_group


def cf_management_group_subscription(cli_ctx, *_):
    return cf_managementgroup(cli_ctx).management_group_subscription


def cf_hierarchy_setting(cli_ctx, *_):
    return cf_managementgroup(cli_ctx).hierarchy_setting


def cf_entity(cli_ctx, *_):
    return cf_managementgroup(cli_ctx).entity
