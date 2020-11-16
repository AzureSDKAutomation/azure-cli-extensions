# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_desktopvirtualization_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.desktopvirtualization import DesktopVirtualizationAPIClient
    return get_mgmt_service_client(cli_ctx,
                                   DesktopVirtualizationAPIClient)


def cf_workspace(cli_ctx, *_):
    return cf_desktopvirtualization_cl(cli_ctx).workspace


def cf_application_group(cli_ctx, *_):
    return cf_desktopvirtualization_cl(cli_ctx).application_group


def cf_host_pool(cli_ctx, *_):
    return cf_desktopvirtualization_cl(cli_ctx).host_pool


def cf_msix_package(cli_ctx, *_):
    return cf_desktopvirtualization_cl(cli_ctx).msix_package


def cf_msix_image(cli_ctx, *_):
    return cf_desktopvirtualization_cl(cli_ctx).msix_image
