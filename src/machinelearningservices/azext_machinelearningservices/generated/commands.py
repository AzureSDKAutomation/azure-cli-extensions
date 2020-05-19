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

    from azext_machinelearningservices.generated._client_factory import cf_workspace
    machinelearningservices_workspace = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._workspace_oper'
        'ations#WorkspaceOperations.{}',
        client_factory=cf_workspace)
    with self.command_group('machinelearningservices workspace', machinelearningservices_workspace,
                            client_factory=cf_workspace, is_experimental=True) as g:
        g.custom_command('list', 'machinelearningservices_workspace_list')
        g.custom_show_command('show', 'machinelearningservices_workspace_show')
        g.custom_command('create', 'machinelearningservices_workspace_create', supports_no_wait=True)
        g.custom_command('update', 'machinelearningservices_workspace_update')
        g.custom_command('delete', 'machinelearningservices_workspace_delete')
        g.custom_command('list-key', 'machinelearningservices_workspace_list_key')
        g.custom_command('resync-key', 'machinelearningservices_workspace_resync_key')
        g.wait_command('wait')

    from azext_machinelearningservices.generated._client_factory import cf_workspace_feature
    machinelearningservices_workspace_feature = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._workspace_feat'
        'ure_operations#WorkspaceFeatureOperations.{}',
        client_factory=cf_workspace_feature)
    with self.command_group('machinelearningservices workspace-feature', machinelearningservices_workspace_feature,
                            client_factory=cf_workspace_feature, is_experimental=True) as g:
        g.custom_command('list', 'machinelearningservices_workspace_feature_list')

    from azext_machinelearningservices.generated._client_factory import cf_usage
    machinelearningservices_usage = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._usage_operatio'
        'ns#UsageOperations.{}',
        client_factory=cf_usage)
    with self.command_group('machinelearningservices usage', machinelearningservices_usage, client_factory=cf_usage,
                            is_experimental=True) as g:
        g.custom_command('list', 'machinelearningservices_usage_list')

    from azext_machinelearningservices.generated._client_factory import cf_virtual_machine_size
    machinelearningservices_virtual_machine_size = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._virtual_machin'
        'e_size_operations#VirtualMachineSizeOperations.{}',
        client_factory=cf_virtual_machine_size)
    with self.command_group('machinelearningservices virtual-machine-size',
                            machinelearningservices_virtual_machine_size, client_factory=cf_virtual_machine_size,
                            is_experimental=True) as g:
        g.custom_command('list', 'machinelearningservices_virtual_machine_size_list')

    from azext_machinelearningservices.generated._client_factory import cf_quota
    machinelearningservices_quota = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._quota_operatio'
        'ns#QuotaOperations.{}',
        client_factory=cf_quota)
    with self.command_group('machinelearningservices quota', machinelearningservices_quota, client_factory=cf_quota,
                            is_experimental=True) as g:
        g.custom_command('list', 'machinelearningservices_quota_list')
        g.custom_command('update', 'machinelearningservices_quota_update')

    from azext_machinelearningservices.generated._client_factory import cf_machine_learning_compute
    machinelearningservices_machine_learning_compute = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._machine_learni'
        'ng_compute_operations#MachineLearningComputeOperations.{}',
        client_factory=cf_machine_learning_compute)
    with self.command_group('machinelearningservices machine-learning-compute',
                            machinelearningservices_machine_learning_compute,
                            client_factory=cf_machine_learning_compute, is_experimental=True) as g:
        g.custom_command('list', 'machinelearningservices_machine_learning_compute_list')
        g.custom_show_command('show', 'machinelearningservices_machine_learning_compute_show')
        g.custom_command('aks create', 'machinelearningservices_machine_learning_compute_aks_create',
                         supports_no_wait=True)
        g.custom_command('aml-compute create', 'machinelearningservices_machine_learning_compute_aml_compute_create',
                         supports_no_wait=True)
        g.custom_command('data-factory create', 'machinelearningservices_machine_learning_compute_data_factory_create',
                          supports_no_wait=True)
        g.custom_command('data-lake-analytics create', 'machinelearningservices_machine_learning_compute_data_lake_anal'
                         'ytics_create', supports_no_wait=True)
        g.custom_command('databricks create', 'machinelearningservices_machine_learning_compute_databricks_create',
                         supports_no_wait=True)
        g.custom_command('hd-insight create', 'machinelearningservices_machine_learning_compute_hd_insight_create',
                         supports_no_wait=True)
        g.custom_command('virtual-machine create', 'machinelearningservices_machine_learning_compute_virtual_machine_cr'
                         'eate', supports_no_wait=True)
        g.custom_command('update', 'machinelearningservices_machine_learning_compute_update', supports_no_wait=True)
        g.custom_command('delete', 'machinelearningservices_machine_learning_compute_delete', supports_no_wait=True)
        g.custom_command('list-key', 'machinelearningservices_machine_learning_compute_list_key')
        g.custom_command('list-node', 'machinelearningservices_machine_learning_compute_list_node')
        g.wait_command('wait')

    from azext_machinelearningservices.generated._client_factory import cf_machinelearningservices
    machinelearningservices_ = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._model_operatio'
        'ns#ModelOperations.{}',
        client_factory=cf_machinelearningservices)
    with self.command_group('machinelearningservices ', machinelearningservices_,
                            client_factory=cf_machinelearningservices, is_experimental=True) as g:
        g.custom_command('list-sku', 'machinelearningservices__list_sku')

    from azext_machinelearningservices.generated._client_factory import cf_private_endpoint_connection
    machinelearningservices_private_endpoint_connection = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._private_endpoi'
        'nt_connection_operations#PrivateEndpointConnectionOperations.{}',
        client_factory=cf_private_endpoint_connection)
    with self.command_group('machinelearningservices private-endpoint-connection',
                            machinelearningservices_private_endpoint_connection,
                            client_factory=cf_private_endpoint_connection, is_experimental=True) as g:
        g.custom_show_command('show', 'machinelearningservices_private_endpoint_connection_show')
        g.custom_command('delete', 'machinelearningservices_private_endpoint_connection_delete')
        g.custom_command('put', 'machinelearningservices_private_endpoint_connection_put')

    from azext_machinelearningservices.generated._client_factory import cf_private_link_resource
    machinelearningservices_private_link_resource = CliCommandType(
        operations_tmpl='azext_machinelearningservices.vendored_sdks.machinelearningservices.operations._private_link_r'
        'esource_operations#PrivateLinkResourceOperations.{}',
        client_factory=cf_private_link_resource)
    with self.command_group('machinelearningservices private-link-resource',
                            machinelearningservices_private_link_resource, client_factory=cf_private_link_resource,
                            is_experimental=True) as g:
        g.custom_command('list', 'machinelearningservices_private_link_resource_list')
