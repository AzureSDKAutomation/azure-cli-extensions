# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_account_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_account.vendored_sdks.subscription import SubscriptionClient
    return get_mgmt_service_client(cli_ctx,
                                   SubscriptionClient)


def cf_subscription(cli_ctx, *_):
    return cf_account_cl(cli_ctx).subscriptions


def cf_tenant(cli_ctx, *_):
    return cf_account_cl(cli_ctx).tenants


def cf_subscription(cli_ctx, *_):
    return cf_account_cl(cli_ctx).subscription


def cf_subscription_operation(cli_ctx, *_):
    return cf_account_cl(cli_ctx).subscription_operation


def cf_subscription_policy(cli_ctx, *_):
    return cf_account_cl(cli_ctx).subscription_policy


def cf_billing_account(cli_ctx, *_):
    return cf_account_cl(cli_ctx).billing_account
