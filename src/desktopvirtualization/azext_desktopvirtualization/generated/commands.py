# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_desktopvirtualization.generated._client_factory import cf_workspace
    desktopvirtualization_workspace = CliCommandType(
        operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._workspace_operatio'
        'ns#WorkspaceOperations.{}',
        client_factory=cf_workspace)
    with self.command_group('desktopvirtualization workspace', desktopvirtualization_workspace,
                            client_factory=cf_workspace, is_experimental=True) as g:
        g.custom_command('list', 'desktopvirtualization_workspace_list')
        g.custom_show_command('show', 'desktopvirtualization_workspace_show')
        g.custom_command('create', 'desktopvirtualization_workspace_create')
        g.custom_command('update', 'desktopvirtualization_workspace_update')
        g.custom_command('delete', 'desktopvirtualization_workspace_delete', confirmation=True)

    from azext_desktopvirtualization.generated._client_factory import cf_application_group
    desktopvirtualization_application_group = CliCommandType(
        operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._application_group_'
        'operations#ApplicationGroupOperations.{}',
        client_factory=cf_application_group)
    with self.command_group('desktopvirtualization applicationgroup', desktopvirtualization_application_group,
                            client_factory=cf_application_group, is_experimental=True) as g:
        g.custom_command('list', 'desktopvirtualization_applicationgroup_list')
        g.custom_show_command('show', 'desktopvirtualization_applicationgroup_show')
        g.custom_command('create', 'desktopvirtualization_applicationgroup_create')
        g.custom_command('update', 'desktopvirtualization_applicationgroup_update')
        g.custom_command('delete', 'desktopvirtualization_applicationgroup_delete', confirmation=True)

    from azext_desktopvirtualization.generated._client_factory import cf_host_pool
    desktopvirtualization_host_pool = CliCommandType(
        operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._host_pool_operatio'
        'ns#HostPoolOperations.{}',
        client_factory=cf_host_pool)
    with self.command_group('desktopvirtualization hostpool', desktopvirtualization_host_pool,
                            client_factory=cf_host_pool, is_experimental=True) as g:
        g.custom_command('list', 'desktopvirtualization_hostpool_list')
        g.custom_show_command('show', 'desktopvirtualization_hostpool_show')
        g.custom_command('create', 'desktopvirtualization_hostpool_create')
        g.custom_command('update', 'desktopvirtualization_hostpool_update')
        g.custom_command('delete', 'desktopvirtualization_hostpool_delete', confirmation=True)

    from azext_desktopvirtualization.generated._client_factory import cf_msix_package
    desktopvirtualization_msix_package = CliCommandType(
        operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._msix_package_opera'
        'tions#MsixPackageOperations.{}',
        client_factory=cf_msix_package)
    with self.command_group('desktopvirtualization msix-package', desktopvirtualization_msix_package,
                            client_factory=cf_msix_package, is_experimental=True) as g:
        g.custom_command('list', 'desktopvirtualization_msix_package_list')
        g.custom_show_command('show', 'desktopvirtualization_msix_package_show')
        g.custom_command('create', 'desktopvirtualization_msix_package_create')
        g.custom_command('update', 'desktopvirtualization_msix_package_update')
        g.custom_command('delete', 'desktopvirtualization_msix_package_delete', confirmation=True)

    from azext_desktopvirtualization.generated._client_factory import cf_msix_image
    desktopvirtualization_msix_image = CliCommandType(
        operations_tmpl='azext_desktopvirtualization.vendored_sdks.desktopvirtualization.operations._msix_image_operati'
        'ons#MsixImageOperations.{}',
        client_factory=cf_msix_image)
    with self.command_group('desktopvirtualization msix-image', desktopvirtualization_msix_image,
                            client_factory=cf_msix_image, is_experimental=True) as g:
        g.custom_command('expand', 'desktopvirtualization_msix_image_expand')
