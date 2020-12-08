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

    from azext_databoxedge.generated._client_factory import cf_device
    databoxedge_device = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._device_operations#DeviceOperations.{}',
        client_factory=cf_device)
    with self.command_group('databoxedge device', databoxedge_device, client_factory=cf_device,
                            is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_device_list')
        g.custom_show_command('show', 'databoxedge_device_show')
        g.custom_command('create', 'databoxedge_device_create', supports_no_wait=True)
        g.custom_command('update', 'databoxedge_device_update')
        g.custom_command('delete', 'databoxedge_device_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('create-or-update-security-setting', 'databoxedge_device_create_or_update_security_setting',
                         supports_no_wait=True)
        g.custom_command('download-update', 'databoxedge_device_download_update', supports_no_wait=True)
        g.custom_command('get-extended-information', 'databoxedge_device_get_extended_information')
        g.custom_command('get-network-setting', 'databoxedge_device_get_network_setting')
        g.custom_command('get-update-summary', 'databoxedge_device_get_update_summary')
        g.custom_command('install-update', 'databoxedge_device_install_update', supports_no_wait=True)
        g.custom_command('scan-for-update', 'databoxedge_device_scan_for_update', supports_no_wait=True)
        g.custom_command('upload-certificate', 'databoxedge_device_upload_certificate')
        g.custom_wait_command('wait', 'databoxedge_device_show')

    from azext_databoxedge.generated._client_factory import cf_alert
    databoxedge_alert = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._alert_operations#AlertOperations.{}',
        client_factory=cf_alert)
    with self.command_group('databoxedge alert', databoxedge_alert, client_factory=cf_alert,
                            is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_alert_list')
        g.custom_show_command('show', 'databoxedge_alert_show')

    from azext_databoxedge.generated._client_factory import cf_bandwidth_schedule
    databoxedge_bandwidth_schedule = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._bandwidth_schedule_operations#Bandwidt'
        'hScheduleOperations.{}',
        client_factory=cf_bandwidth_schedule)
    with self.command_group('databoxedge bandwidth-schedule', databoxedge_bandwidth_schedule,
                            client_factory=cf_bandwidth_schedule, is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_bandwidth_schedule_list')
        g.custom_show_command('show', 'databoxedge_bandwidth_schedule_show')
        g.custom_command('create', 'databoxedge_bandwidth_schedule_create', supports_no_wait=True)
        g.custom_command('update', 'databoxedge_bandwidth_schedule_update', supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_bandwidth_schedule_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_bandwidth_schedule_show')

    from azext_databoxedge.generated._client_factory import cf_job
    databoxedge_job = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._job_operations#JobOperations.{}',
        client_factory=cf_job)
    with self.command_group('databoxedge job', databoxedge_job, client_factory=cf_job, is_experimental=True) as g:
        g.custom_show_command('show', 'databoxedge_job_show')

    from azext_databoxedge.generated._client_factory import cf_node
    databoxedge_node = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._node_operations#NodeOperations.{}',
        client_factory=cf_node)
    with self.command_group('databoxedge node', databoxedge_node, client_factory=cf_node, is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_node_list')

    from azext_databoxedge.generated._client_factory import cf_operation_status
    databoxedge_operation_status = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._operation_status_operations#OperationS'
        'tatusOperations.{}',
        client_factory=cf_operation_status)
    with self.command_group('databoxedge operation-status', databoxedge_operation_status,
                            client_factory=cf_operation_status, is_experimental=True) as g:
        g.custom_show_command('show', 'databoxedge_operation_status_show')

    from azext_databoxedge.generated._client_factory import cf_order
    databoxedge_order = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._order_operations#OrderOperations.{}',
        client_factory=cf_order)
    with self.command_group('databoxedge order', databoxedge_order, client_factory=cf_order,
                            is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_order_list')
        g.custom_show_command('show', 'databoxedge_order_show')
        g.custom_command('create', 'databoxedge_order_create', supports_no_wait=True)
        g.custom_command('update', 'databoxedge_order_update', supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_order_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_order_show')

    from azext_databoxedge.generated._client_factory import cf_role
    databoxedge_role = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._role_operations#RoleOperations.{}',
        client_factory=cf_role)
    with self.command_group('databoxedge role', databoxedge_role, client_factory=cf_role, is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_role_list')
        g.custom_show_command('show', 'databoxedge_role_show')
        g.custom_command('create', 'databoxedge_role_create', supports_no_wait=True)
        g.generic_update_command('update', setter_arg_name='role', setter_name='begin_create_or_update',
                                 custom_func_name='databoxedge_role_update', supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_role_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_role_show')

    from azext_databoxedge.generated._client_factory import cf_share
    databoxedge_share = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._share_operations#ShareOperations.{}',
        client_factory=cf_share)
    with self.command_group('databoxedge share', databoxedge_share, client_factory=cf_share,
                            is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_share_list')
        g.custom_show_command('show', 'databoxedge_share_show')
        g.custom_command('create', 'databoxedge_share_create', supports_no_wait=True)
        g.custom_command('update', 'databoxedge_share_update', supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_share_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('refresh', 'databoxedge_share_refresh', supports_no_wait=True)
        g.custom_wait_command('wait', 'databoxedge_share_show')

    from azext_databoxedge.generated._client_factory import cf_storage_account_credentials
    databoxedge_storage_account_credentials = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._storage_account_credentials_operations'
        '#StorageAccountCredentialsOperations.{}',
        client_factory=cf_storage_account_credentials)
    with self.command_group('databoxedge storage-account-credentials', databoxedge_storage_account_credentials,
                            client_factory=cf_storage_account_credentials, is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_storage_account_credentials_list')
        g.custom_show_command('show', 'databoxedge_storage_account_credentials_show')
        g.custom_command('delete', 'databoxedge_storage_account_credentials_delete', supports_no_wait=True,
                         confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_storage_account_credentials_show')

    from azext_databoxedge.generated._client_factory import cf_storage_account
    databoxedge_storage_account = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._storage_account_operations#StorageAcco'
        'untOperations.{}',
        client_factory=cf_storage_account)
    with self.command_group('databoxedge storage-account', databoxedge_storage_account,
                            client_factory=cf_storage_account, is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_storage_account_list')
        g.custom_show_command('show', 'databoxedge_storage_account_show')
        g.custom_command('delete', 'databoxedge_storage_account_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_storage_account_show')

    from azext_databoxedge.generated._client_factory import cf_container
    databoxedge_container = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._container_operations#ContainerOperatio'
        'ns.{}',
        client_factory=cf_container)
    with self.command_group('databoxedge container', databoxedge_container, client_factory=cf_container,
                            is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_container_list')
        g.custom_show_command('show', 'databoxedge_container_show')
        g.custom_command('create', 'databoxedge_container_create', supports_no_wait=True)
        g.custom_command('update', 'databoxedge_container_update', supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_container_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('refresh', 'databoxedge_container_refresh', supports_no_wait=True)
        g.custom_wait_command('wait', 'databoxedge_container_show')

    from azext_databoxedge.generated._client_factory import cf_trigger
    databoxedge_trigger = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._trigger_operations#TriggerOperations.{'
        '}',
        client_factory=cf_trigger)
    with self.command_group('databoxedge trigger', databoxedge_trigger, client_factory=cf_trigger,
                            is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_trigger_list')
        g.custom_show_command('show', 'databoxedge_trigger_show')
        g.custom_command('create', 'databoxedge_trigger_create', supports_no_wait=True)
        g.generic_update_command('update', setter_arg_name='trigger', setter_name='begin_create_or_update',
                                 custom_func_name='databoxedge_trigger_update', supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_trigger_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_trigger_show')

    from azext_databoxedge.generated._client_factory import cf_user
    databoxedge_user = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._user_operations#UserOperations.{}',
        client_factory=cf_user)
    with self.command_group('databoxedge user', databoxedge_user, client_factory=cf_user, is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_user_list')
        g.custom_show_command('show', 'databoxedge_user_show')
        g.custom_command('create', 'databoxedge_user_create', supports_no_wait=True)
        g.custom_command('update', 'databoxedge_user_update', supports_no_wait=True)
        g.custom_command('delete', 'databoxedge_user_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'databoxedge_user_show')

    from azext_databoxedge.generated._client_factory import cf_sku
    databoxedge_sku = CliCommandType(
        operations_tmpl='azext_databoxedge.vendored_sdks.databoxedge.operations._sku_operations#SkuOperations.{}',
        client_factory=cf_sku)
    with self.command_group('databoxedge sku', databoxedge_sku, client_factory=cf_sku, is_experimental=True) as g:
        g.custom_command('list', 'databoxedge_sku_list')
