# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_datadog_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_datadog.vendored_sdks.datadog import MicrosoftDatadogClient
    return get_mgmt_service_client(cli_ctx,
                                   MicrosoftDatadogClient)


def cf_marketplace_agreement(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).marketplace_agreements


def cf_api_key(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).api_keys


def cf_host(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).hosts


def cf_linked_resource(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).linked_resources


def cf_monitored_resource(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).monitored_resources


def cf_monitor(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).monitors


def cf_refresh_set_password(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).refresh_set_password


def cf_tag_rule(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).tag_rules


def cf_single_sign_on_configuration(cli_ctx, *_):
    return cf_datadog_cl(cli_ctx).single_sign_on_configurations
