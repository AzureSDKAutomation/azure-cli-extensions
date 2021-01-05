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

    from azext_logic.generated._client_factory import cf_workflow
    logic_workflow = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflows_operations#WorkflowsOperations.{}',
        client_factory=cf_workflow)
    with self.command_group('logic workflow', logic_workflow, client_factory=cf_workflow) as g:
        g.custom_command('list', 'logic_workflow_list')
        g.custom_show_command('show', 'logic_workflow_show')
        g.custom_command('create', 'logic_workflow_create')
        g.custom_command('update', 'logic_workflow_update')
        g.custom_command('delete', 'logic_workflow_delete', confirmation=True)
        g.custom_command('disable', 'logic_workflow_disable')
        g.custom_command('enable', 'logic_workflow_enable')
        g.custom_command('generate-upgraded-definition', 'logic_workflow_generate_upgraded_definition')
        g.custom_command('list-callback-url', 'logic_workflow_list_callback_url')
        g.custom_command('list-swagger', 'logic_workflow_list_swagger')
        g.custom_command('move', 'logic_workflow_move', supports_no_wait=True)
        g.custom_command('regenerate-access-key', 'logic_workflow_regenerate_access_key')
        g.custom_command('validate-by-location', 'logic_workflow_validate_by_location')
        g.custom_command('validate-by-resource-group', 'logic_workflow_validate_by_resource_group')
        g.custom_wait_command('wait', 'logic_workflow_show')

    from azext_logic.generated._client_factory import cf_workflow_version
    logic_workflow_version = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_versions_operations#WorkflowVersionsOpera'
        'tions.{}',
        client_factory=cf_workflow_version)
    with self.command_group('logic workflow-version', logic_workflow_version,
                            client_factory=cf_workflow_version) as g:
        g.custom_command('list', 'logic_workflow_version_list')
        g.custom_show_command('show', 'logic_workflow_version_show')

    from azext_logic.generated._client_factory import cf_workflow_trigger
    logic_workflow_trigger = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_triggers_operations#WorkflowTriggersOpera'
        'tions.{}',
        client_factory=cf_workflow_trigger)
    with self.command_group('logic workflow-trigger', logic_workflow_trigger,
                            client_factory=cf_workflow_trigger) as g:
        g.custom_command('list', 'logic_workflow_trigger_list')
        g.custom_show_command('show', 'logic_workflow_trigger_show')
        g.custom_command('list-callback-url', 'logic_workflow_trigger_list_callback_url')
        g.custom_command('reset', 'logic_workflow_trigger_reset')
        g.custom_command('run', 'logic_workflow_trigger_run')
        g.custom_command('set-state', 'logic_workflow_trigger_set_state')
        g.custom_command('show-schema-json', 'logic_workflow_trigger_show_schema_json')

    from azext_logic.generated._client_factory import cf_workflow_version_trigger
    logic_workflow_version_trigger = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_version_triggers_operations#WorkflowVersi'
        'onTriggersOperations.{}',
        client_factory=cf_workflow_version_trigger)
    with self.command_group('logic workflow-version-trigger', logic_workflow_version_trigger,
                            client_factory=cf_workflow_version_trigger) as g:
        g.custom_command('list-callback-url', 'logic_workflow_version_trigger_list_callback_url')

    from azext_logic.generated._client_factory import cf_workflow_trigger_history
    logic_workflow_trigger_history = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_trigger_histories_operations#WorkflowTrig'
        'gerHistoriesOperations.{}',
        client_factory=cf_workflow_trigger_history)
    with self.command_group('logic workflow-trigger-history', logic_workflow_trigger_history,
                            client_factory=cf_workflow_trigger_history) as g:
        g.custom_command('list', 'logic_workflow_trigger_history_list')
        g.custom_show_command('show', 'logic_workflow_trigger_history_show')
        g.custom_command('resubmit', 'logic_workflow_trigger_history_resubmit')

    from azext_logic.generated._client_factory import cf_workflow_run
    logic_workflow_run = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_runs_operations#WorkflowRunsOperations.{}'
        '',
        client_factory=cf_workflow_run)
    with self.command_group('logic workflow-run', logic_workflow_run, client_factory=cf_workflow_run) as g:
        g.custom_command('list', 'logic_workflow_run_list')
        g.custom_show_command('show', 'logic_workflow_run_show')
        g.custom_command('cancel', 'logic_workflow_run_cancel')

    from azext_logic.generated._client_factory import cf_workflow_run_action
    logic_workflow_run_action = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_run_actions_operations#WorkflowRunActions'
        'Operations.{}',
        client_factory=cf_workflow_run_action)
    with self.command_group('logic workflow-run-action', logic_workflow_run_action,
                            client_factory=cf_workflow_run_action) as g:
        g.custom_command('list', 'logic_workflow_run_action_list')
        g.custom_show_command('show', 'logic_workflow_run_action_show')
        g.custom_command('list-expression-trace', 'logic_workflow_run_action_list_expression_trace')

    from azext_logic.generated._client_factory import cf_workflow_run_action_repetition
    logic_workflow_run_action_repetition = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_run_action_repetitions_operations#Workflo'
        'wRunActionRepetitionsOperations.{}',
        client_factory=cf_workflow_run_action_repetition)
    with self.command_group('logic workflow-run-action-repetition', logic_workflow_run_action_repetition,
                            client_factory=cf_workflow_run_action_repetition) as g:
        g.custom_command('list', 'logic_workflow_run_action_repetition_list')
        g.custom_show_command('show', 'logic_workflow_run_action_repetition_show')
        g.custom_command('list-expression-trace', 'logic_workflow_run_action_repetition_list_expression_trace')

    from azext_logic.generated._client_factory import cf_workflow_run_action_repetition_request_history
    logic_workflow_run_action_repetition_request_history = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_run_action_repetitions_request_histories_'
        'operations#WorkflowRunActionRepetitionsRequestHistoriesOperations.{}',
        client_factory=cf_workflow_run_action_repetition_request_history)
    with self.command_group('logic workflow-run-action-repetition-request-history',
                            logic_workflow_run_action_repetition_request_history,
                            client_factory=cf_workflow_run_action_repetition_request_history) as g:
        g.custom_command('list', 'logic_workflow_run_action_repetition_request_history_list')
        g.custom_show_command('show', 'logic_workflow_run_action_repetition_request_history_show')

    from azext_logic.generated._client_factory import cf_workflow_run_action_request_history
    logic_workflow_run_action_request_history = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_run_action_request_histories_operations#W'
        'orkflowRunActionRequestHistoriesOperations.{}',
        client_factory=cf_workflow_run_action_request_history)
    with self.command_group('logic workflow-run-action-request-history', logic_workflow_run_action_request_history,
                            client_factory=cf_workflow_run_action_request_history) as g:
        g.custom_command('list', 'logic_workflow_run_action_request_history_list')
        g.custom_show_command('show', 'logic_workflow_run_action_request_history_show')

    from azext_logic.generated._client_factory import cf_workflow_run_action_scope_repetition
    logic_workflow_run_action_scope_repetition = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_run_action_scope_repetitions_operations#W'
        'orkflowRunActionScopeRepetitionsOperations.{}',
        client_factory=cf_workflow_run_action_scope_repetition)
    with self.command_group('logic workflow-run-action-scope-repetition', logic_workflow_run_action_scope_repetition,
                            client_factory=cf_workflow_run_action_scope_repetition) as g:
        g.custom_command('list', 'logic_workflow_run_action_scope_repetition_list')
        g.custom_show_command('show', 'logic_workflow_run_action_scope_repetition_show')

    from azext_logic.generated._client_factory import cf_workflow_run_operation
    logic_workflow_run_operation = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._workflow_run_operations_operations#WorkflowRunOper'
        'ationsOperations.{}',
        client_factory=cf_workflow_run_operation)
    with self.command_group('logic workflow-run-operation', logic_workflow_run_operation,
                            client_factory=cf_workflow_run_operation) as g:
        g.custom_show_command('show', 'logic_workflow_run_operation_show')

    from azext_logic.generated._client_factory import cf_integration_account
    logic_integration_account = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_accounts_operations#IntegrationAccount'
        'sOperations.{}',
        client_factory=cf_integration_account)
    with self.command_group('logic integration-account', logic_integration_account,
                            client_factory=cf_integration_account) as g:
        g.custom_command('list', 'logic_integration_account_list')
        g.custom_show_command('show', 'logic_integration_account_show')
        g.custom_command('create', 'logic_integration_account_create')
        g.custom_command('update', 'logic_integration_account_update')
        g.custom_command('delete', 'logic_integration_account_delete', confirmation=True)
        g.custom_command('list-callback-url', 'logic_integration_account_list_callback_url')
        g.custom_command('list-key-vault-key', 'logic_integration_account_list_key_vault_key')
        g.custom_command('log-tracking-event', 'logic_integration_account_log_tracking_event')
        g.custom_command('regenerate-access-key', 'logic_integration_account_regenerate_access_key')

    from azext_logic.generated._client_factory import cf_integration_account_assembly
    logic_integration_account_assembly = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_account_assemblies_operations#Integrat'
        'ionAccountAssembliesOperations.{}',
        client_factory=cf_integration_account_assembly)
    with self.command_group('logic integration-account-assembly', logic_integration_account_assembly,
                            client_factory=cf_integration_account_assembly) as g:
        g.custom_command('list', 'logic_integration_account_assembly_list')
        g.custom_show_command('show', 'logic_integration_account_assembly_show')
        g.custom_command('create', 'logic_integration_account_assembly_create')
        g.generic_update_command('update', setter_arg_name='assembly_artifact',
                                 custom_func_name='logic_integration_account_assembly_update')
        g.custom_command('delete', 'logic_integration_account_assembly_delete', confirmation=True)
        g.custom_command('list-content-callback-url', 'logic_integration_account_assembly_list_content_callback_url')

    from azext_logic.generated._client_factory import cf_integration_account_batch_configuration
    logic_integration_account_batch_configuration = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_account_batch_configurations_operation'
        's#IntegrationAccountBatchConfigurationsOperations.{}',
        client_factory=cf_integration_account_batch_configuration)
    with self.command_group('logic integration-account-batch-configuration',
                            logic_integration_account_batch_configuration,
                            client_factory=cf_integration_account_batch_configuration) as g:
        g.custom_command('list', 'logic_integration_account_batch_configuration_list')
        g.custom_show_command('show', 'logic_integration_account_batch_configuration_show')
        g.custom_command('create', 'logic_integration_account_batch_configuration_create')
        g.generic_update_command('update', setter_arg_name='batch_configuration',
                                 custom_func_name='logic_integration_account_batch_configuration_update')
        g.custom_command('delete', 'logic_integration_account_batch_configuration_delete', confirmation=True)

    from azext_logic.generated._client_factory import cf_integration_account_schema
    logic_integration_account_schema = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_account_schemas_operations#Integration'
        'AccountSchemasOperations.{}',
        client_factory=cf_integration_account_schema)
    with self.command_group('logic integration-account-schema', logic_integration_account_schema,
                            client_factory=cf_integration_account_schema) as g:
        g.custom_command('list', 'logic_integration_account_schema_list')
        g.custom_show_command('show', 'logic_integration_account_schema_show')
        g.custom_command('create', 'logic_integration_account_schema_create')
        g.generic_update_command('update', setter_arg_name='schema', custom_func_name='logic_integration_account_schema'
                                 '_update')
        g.custom_command('delete', 'logic_integration_account_schema_delete', confirmation=True)
        g.custom_command('list-content-callback-url', 'logic_integration_account_schema_list_content_callback_url')

    from azext_logic.generated._client_factory import cf_integration_account_map
    logic_integration_account_map = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_account_maps_operations#IntegrationAcc'
        'ountMapsOperations.{}',
        client_factory=cf_integration_account_map)
    with self.command_group('logic integration-account-map', logic_integration_account_map,
                            client_factory=cf_integration_account_map) as g:
        g.custom_command('list', 'logic_integration_account_map_list')
        g.custom_show_command('show', 'logic_integration_account_map_show')
        g.custom_command('create', 'logic_integration_account_map_create')
        g.generic_update_command('update', setter_arg_name='map', custom_func_name='logic_integration_account_map_updat'
                                 'e')
        g.custom_command('delete', 'logic_integration_account_map_delete', confirmation=True)
        g.custom_command('list-content-callback-url', 'logic_integration_account_map_list_content_callback_url')

    from azext_logic.generated._client_factory import cf_integration_account_partner
    logic_integration_account_partner = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_account_partners_operations#Integratio'
        'nAccountPartnersOperations.{}',
        client_factory=cf_integration_account_partner)
    with self.command_group('logic integration-account-partner', logic_integration_account_partner,
                            client_factory=cf_integration_account_partner) as g:
        g.custom_command('list', 'logic_integration_account_partner_list')
        g.custom_show_command('show', 'logic_integration_account_partner_show')
        g.custom_command('create', 'logic_integration_account_partner_create')
        g.generic_update_command('update', setter_arg_name='partner', custom_func_name='logic_integration_account_partn'
                                 'er_update')
        g.custom_command('delete', 'logic_integration_account_partner_delete', confirmation=True)
        g.custom_command('list-content-callback-url', 'logic_integration_account_partner_list_content_callback_url')

    from azext_logic.generated._client_factory import cf_integration_account_agreement
    logic_integration_account_agreement = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_account_agreements_operations#Integrat'
        'ionAccountAgreementsOperations.{}',
        client_factory=cf_integration_account_agreement)
    with self.command_group('logic integration-account-agreement', logic_integration_account_agreement,
                            client_factory=cf_integration_account_agreement) as g:
        g.custom_command('list', 'logic_integration_account_agreement_list')
        g.custom_show_command('show', 'logic_integration_account_agreement_show')
        g.custom_command('create', 'logic_integration_account_agreement_create')
        g.custom_command('update', 'logic_integration_account_agreement_update')
        g.custom_command('delete', 'logic_integration_account_agreement_delete', confirmation=True)
        g.custom_command('list-content-callback-url', 'logic_integration_account_agreement_list_content_callback_url')

    from azext_logic.generated._client_factory import cf_integration_account_certificate
    logic_integration_account_certificate = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_account_certificates_operations#Integr'
        'ationAccountCertificatesOperations.{}',
        client_factory=cf_integration_account_certificate)
    with self.command_group('logic integration-account-certificate', logic_integration_account_certificate,
                            client_factory=cf_integration_account_certificate) as g:
        g.custom_command('list', 'logic_integration_account_certificate_list')
        g.custom_show_command('show', 'logic_integration_account_certificate_show')
        g.custom_command('create', 'logic_integration_account_certificate_create')
        g.generic_update_command('update', setter_arg_name='certificate',
                                 custom_func_name='logic_integration_account_certificate_update')
        g.custom_command('delete', 'logic_integration_account_certificate_delete', confirmation=True)

    from azext_logic.generated._client_factory import cf_integration_account_session
    logic_integration_account_session = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_account_sessions_operations#Integratio'
        'nAccountSessionsOperations.{}',
        client_factory=cf_integration_account_session)
    with self.command_group('logic integration-account-session', logic_integration_account_session,
                            client_factory=cf_integration_account_session) as g:
        g.custom_command('list', 'logic_integration_account_session_list')
        g.custom_show_command('show', 'logic_integration_account_session_show')
        g.custom_command('create', 'logic_integration_account_session_create')
        g.generic_update_command('update', setter_arg_name='session', custom_func_name='logic_integration_account_sessi'
                                 'on_update')
        g.custom_command('delete', 'logic_integration_account_session_delete', confirmation=True)

    from azext_logic.generated._client_factory import cf_integration_service_environment
    logic_integration_service_environment = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_service_environments_operations#Integr'
        'ationServiceEnvironmentsOperations.{}',
        client_factory=cf_integration_service_environment)
    with self.command_group('logic integration-service-environment', logic_integration_service_environment,
                            client_factory=cf_integration_service_environment) as g:
        g.custom_command('list', 'logic_integration_service_environment_list')
        g.custom_show_command('show', 'logic_integration_service_environment_show')
        g.custom_command('create', 'logic_integration_service_environment_create', supports_no_wait=True)
        g.custom_command('update', 'logic_integration_service_environment_update', supports_no_wait=True)
        g.custom_command('delete', 'logic_integration_service_environment_delete', confirmation=True)
        g.custom_command('restart', 'logic_integration_service_environment_restart')
        g.custom_wait_command('wait', 'logic_integration_service_environment_show')

    from azext_logic.generated._client_factory import cf_integration_service_environment_sku
    logic_integration_service_environment_sku = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_service_environment_skus_operations#In'
        'tegrationServiceEnvironmentSkusOperations.{}',
        client_factory=cf_integration_service_environment_sku)
    with self.command_group('logic integration-service-environment-sku', logic_integration_service_environment_sku,
                            client_factory=cf_integration_service_environment_sku) as g:
        g.custom_command('list', 'logic_integration_service_environment_sku_list')

    from azext_logic.generated._client_factory import cf_integration_service_environment_network_health
    logic_integration_service_environment_network_health = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_service_environment_network_health_ope'
        'rations#IntegrationServiceEnvironmentNetworkHealthOperations.{}',
        client_factory=cf_integration_service_environment_network_health)
    with self.command_group('logic integration-service-environment-network-health',
                            logic_integration_service_environment_network_health,
                            client_factory=cf_integration_service_environment_network_health) as g:
        g.custom_show_command('show', 'logic_integration_service_environment_network_health_show')

    from azext_logic.generated._client_factory import cf_integration_service_environment_managed_api
    logic_integration_service_environment_managed_api = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_service_environment_managed_apis_opera'
        'tions#IntegrationServiceEnvironmentManagedApisOperations.{}',
        client_factory=cf_integration_service_environment_managed_api)
    with self.command_group('logic integration-service-environment-managed-api',
                            logic_integration_service_environment_managed_api,
                            client_factory=cf_integration_service_environment_managed_api) as g:
        g.custom_command('list', 'logic_integration_service_environment_managed_api_list')
        g.custom_show_command('show', 'logic_integration_service_environment_managed_api_show')
        g.custom_command('delete', 'logic_integration_service_environment_managed_api_delete', supports_no_wait=True,
                         confirmation=True)
        g.custom_command('put', 'logic_integration_service_environment_managed_api_put', supports_no_wait=True)
        g.custom_wait_command('wait', 'logic_integration_service_environment_managed_api_show')

    from azext_logic.generated._client_factory import cf_integration_service_environment_managed_api_operation
    logic_integration_service_environment_managed_api_operation = CliCommandType(
        operations_tmpl='azext_logic.vendored_sdks.logic.operations._integration_service_environment_managed_api_operat'
        'ions_operations#IntegrationServiceEnvironmentManagedApiOperationsOperations.{}',
        client_factory=cf_integration_service_environment_managed_api_operation)
    with self.command_group('logic integration-service-environment-managed-api-operation',
                            logic_integration_service_environment_managed_api_operation,
                            client_factory=cf_integration_service_environment_managed_api_operation) as g:
        g.custom_command('list', 'logic_integration_service_environment_managed_api_operation_list')

    with self.command_group('logic', is_experimental=True):
        pass
