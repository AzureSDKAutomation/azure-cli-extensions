# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_managementgroup.generated._client_factory import cf_management_group
    managementgroup_management_group = CliCommandType(
        operations_tmpl='azext_managementgroup.vendored_sdks.managementgroup.operations._management_group_operations#Ma'
        'nagementGroupOperations.{}',
        client_factory=cf_management_group)
    with self.command_group('managementgroup management-group', managementgroup_management_group,
                            client_factory=cf_management_group, is_experimental=True) as g:
        g.custom_command('list', 'managementgroup_management_group_list')
        g.custom_show_command('show', 'managementgroup_management_group_show')
        g.custom_command('create', 'managementgroup_management_group_create', supports_no_wait=True)
        g.custom_command('update', 'managementgroup_management_group_update')
        g.custom_command('delete', 'managementgroup_management_group_delete', supports_no_wait=True)
        g.custom_command('get-descendant', 'managementgroup_management_group_get_descendant')
        g.custom_wait_command('wait', 'managementgroup_management_group_show')

    from azext_managementgroup.generated._client_factory import cf_management_group_subscription
    managementgroup_management_group_subscription = CliCommandType(
        operations_tmpl='azext_managementgroup.vendored_sdks.managementgroup.operations._management_group_subscription_'
        'operations#ManagementGroupSubscriptionOperations.{}',
        client_factory=cf_management_group_subscription)
    with self.command_group('managementgroup management-group-subscription',
                            managementgroup_management_group_subscription,
                            client_factory=cf_management_group_subscription, is_experimental=True) as g:
        g.custom_command('create', 'managementgroup_management_group_subscription_create')
        g.custom_command('delete', 'managementgroup_management_group_subscription_delete')
        g.custom_command('get-subscription', 'managementgroup_management_group_subscription_get_subscription')
        g.custom_command('get-subscription-under-management-group', 'managementgroup_management_group_subscription_get_'
                         'subscription_under_management_group')

    from azext_managementgroup.generated._client_factory import cf_hierarchy_setting
    managementgroup_hierarchy_setting = CliCommandType(
        operations_tmpl='azext_managementgroup.vendored_sdks.managementgroup.operations._hierarchy_setting_operations#H'
        'ierarchySettingOperations.{}',
        client_factory=cf_hierarchy_setting)
    with self.command_group('managementgroup hierarchy-setting', managementgroup_hierarchy_setting,
                            client_factory=cf_hierarchy_setting, is_experimental=True) as g:
        g.custom_command('list', 'managementgroup_hierarchy_setting_list')
        g.custom_show_command('show', 'managementgroup_hierarchy_setting_show')
        g.custom_command('create', 'managementgroup_hierarchy_setting_create')
        g.custom_command('update', 'managementgroup_hierarchy_setting_update')
        g.custom_command('delete', 'managementgroup_hierarchy_setting_delete')

    from azext_managementgroup.generated._client_factory import cf_managementgroup
    managementgroup_ = CliCommandType(
        operations_tmpl='azext_managementgroup.vendored_sdks.managementgroup.operations._model_operations#ModelOperatio'
        'ns.{}',
        client_factory=cf_managementgroup)
    with self.command_group('managementgroup ', managementgroup_, client_factory=cf_managementgroup,
                            is_experimental=True) as g:
        g.custom_command('start-tenant-backfill', 'managementgroup__start_tenant_backfill')
        g.custom_command('tenant-backfill-status', 'managementgroup__tenant_backfill_status')

    from azext_managementgroup.generated._client_factory import cf_entity
    managementgroup_entity = CliCommandType(
        operations_tmpl='azext_managementgroup.vendored_sdks.managementgroup.operations._entity_operations#EntityOperat'
        'ions.{}',
        client_factory=cf_entity)
    with self.command_group('managementgroup entity', managementgroup_entity, client_factory=cf_entity,
                            is_experimental=True) as g:
        g.custom_command('list', 'managementgroup_entity_list')
