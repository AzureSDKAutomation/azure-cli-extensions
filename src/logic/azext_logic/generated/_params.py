# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azext_logic.action import (
    AddIntegrationAccount,
    AddIntegrationServiceEnvironment,
    AddDefinition,
    AddSku,
    AddKeyVault,
    AddProperties,
    AddMetadata,
    AddParametersSchema,
    AddHostIdentity,
    AddGuestIdentity,
    AddContent
)


def load_arguments(self, _):

    with self.argument_context('logic workflow list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic workflow show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')

    with self.argument_context('logic workflow create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_state', arg_type=get_enum_type(['NotSpecified', 'Completed', 'Enabled', 'Disabled', 'Deleted', 'Suspended']), help='The workflow state.')
        c.argument('properties_endpoints_configuration', arg_type=CLIArgumentType(options_list=['--properties-endpoints-configuration'], help='The endpoints configuration.'))
        c.argument('properties_integration_account', action=AddIntegrationAccount, nargs='+', help='The resource reference.')
        c.argument('properties_integration_service_environment', action=AddIntegrationServiceEnvironment, nargs='+', help='The resource reference.')
        c.argument('properties_definition', action=AddDefinition, nargs='+', help='')
        c.argument('properties_parameters', arg_type=CLIArgumentType(options_list=['--properties-parameters'], help='The parameters.'))

    with self.argument_context('logic workflow update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_state', arg_type=get_enum_type(['NotSpecified', 'Completed', 'Enabled', 'Disabled', 'Deleted', 'Suspended']), help='The workflow state.')
        c.argument('properties_endpoints_configuration', arg_type=CLIArgumentType(options_list=['--properties-endpoints-configuration'], help='The endpoints configuration.'))
        c.argument('properties_integration_account', action=AddIntegrationAccount, nargs='+', help='The resource reference.')
        c.argument('properties_integration_service_environment', action=AddIntegrationServiceEnvironment, nargs='+', help='The resource reference.')
        c.argument('properties_definition', action=AddDefinition, nargs='+', help='')
        c.argument('properties_parameters', arg_type=CLIArgumentType(options_list=['--properties-parameters'], help='The parameters.'))

    with self.argument_context('logic workflow delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')

    with self.argument_context('logic workflow move') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_state', arg_type=get_enum_type(['NotSpecified', 'Completed', 'Enabled', 'Disabled', 'Deleted', 'Suspended']), help='The workflow state.')
        c.argument('properties_endpoints_configuration', arg_type=CLIArgumentType(options_list=['--properties-endpoints-configuration'], help='The endpoints configuration.'))
        c.argument('properties_integration_account', action=AddIntegrationAccount, nargs='+', help='The resource reference.')
        c.argument('properties_integration_service_environment', action=AddIntegrationServiceEnvironment, nargs='+', help='The resource reference.')
        c.argument('properties_definition', action=AddDefinition, nargs='+', help='')
        c.argument('properties_parameters', arg_type=CLIArgumentType(options_list=['--properties-parameters'], help='The parameters.'))

    with self.argument_context('logic workflow validate-by-resource-group') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_state', arg_type=get_enum_type(['NotSpecified', 'Completed', 'Enabled', 'Disabled', 'Deleted', 'Suspended']), help='The workflow state.')
        c.argument('properties_endpoints_configuration', arg_type=CLIArgumentType(options_list=['--properties-endpoints-configuration'], help='The endpoints configuration.'))
        c.argument('properties_integration_account', action=AddIntegrationAccount, nargs='+', help='The resource reference.')
        c.argument('properties_integration_service_environment', action=AddIntegrationServiceEnvironment, nargs='+', help='The resource reference.')
        c.argument('properties_definition', action=AddDefinition, nargs='+', help='')
        c.argument('properties_parameters', arg_type=CLIArgumentType(options_list=['--properties-parameters'], help='The parameters.'))

    with self.argument_context('logic workflow list-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('not_after', help='The expiry time.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic workflow generate-upgraded-definition') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('target_schema_version', help='The target schema version.')

    with self.argument_context('logic workflow regenerate-access-key') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic workflow validate-by-location') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The workflow location.')
        c.argument('workflow_name', help='The workflow name.')

    with self.argument_context('logic workflow disable') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')

    with self.argument_context('logic workflow enable') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')

    with self.argument_context('logic workflow list-swagger') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')

    with self.argument_context('logic workflow-version list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('top', help='The number of items to be included in the result.')

    with self.argument_context('logic workflow-version show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('version_id', help='The workflow versionId.')

    with self.argument_context('logic workflow-trigger list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic workflow-trigger show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('trigger_name', help='The workflow trigger name.')

    with self.argument_context('logic workflow-trigger reset') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('trigger_name', help='The workflow trigger name.')
        c.argument('source', arg_type=CLIArgumentType(options_list=['--source'], help='The workflow trigger.'))

    with self.argument_context('logic workflow-trigger run') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('trigger_name', help='The workflow trigger name.')

    with self.argument_context('logic workflow-trigger list-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('trigger_name', help='The workflow trigger name.')

    with self.argument_context('logic workflow-version-trigger list-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('version_id', help='The workflow versionId.')
        c.argument('trigger_name', help='The workflow trigger name.')
        c.argument('not_after', help='The expiry time.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic workflow-trigger-history list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('trigger_name', help='The workflow trigger name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic workflow-trigger-history show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('trigger_name', help='The workflow trigger name.')
        c.argument('history_name', help='The workflow trigger history name. Corresponds to the run name for triggers that resulted in a run.')

    with self.argument_context('logic workflow-trigger-history resubmit') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('trigger_name', help='The workflow trigger name.')
        c.argument('history_name', help='The workflow trigger history name. Corresponds to the run name for triggers that resulted in a run.')

    with self.argument_context('logic workflow-run list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic workflow-run show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')

    with self.argument_context('logic workflow-run cancel') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')

    with self.argument_context('logic workflow-run-action list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic workflow-run-action show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')

    with self.argument_context('logic workflow-run-action list-expression-trace') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')

    with self.argument_context('logic workflow-run-action-repetition list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')

    with self.argument_context('logic workflow-run-action-repetition show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')
        c.argument('repetition_name', help='The workflow repetition.')

    with self.argument_context('logic workflow-run-action-repetition list-expression-trace') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')
        c.argument('repetition_name', help='The workflow repetition.')

    with self.argument_context('logic workflow-run-action-repetition-request-history list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')
        c.argument('repetition_name', help='The workflow repetition.')

    with self.argument_context('logic workflow-run-action-repetition-request-history show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')
        c.argument('repetition_name', help='The workflow repetition.')
        c.argument('request_history_name', help='The request history name.')

    with self.argument_context('logic workflow-run-action-request-history list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')

    with self.argument_context('logic workflow-run-action-request-history show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')
        c.argument('request_history_name', help='The request history name.')

    with self.argument_context('logic workflow-run-action-scope-repetition list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')

    with self.argument_context('logic workflow-run-action-scope-repetition show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('action_name', help='The workflow action name.')
        c.argument('repetition_name', help='The workflow repetition.')

    with self.argument_context('logic workflow-run-operation show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('workflow_name', help='The workflow name.')
        c.argument('run_name', help='The workflow run name.')
        c.argument('operation_id', help='The workflow operation id.')

    with self.argument_context('logic integration-account list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('top', help='The number of items to be included in the result.')

    with self.argument_context('logic integration-account show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')

    with self.argument_context('logic integration-account create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('sku', action=AddSku, nargs='+', help='The integration account sku.')
        c.argument('properties_integration_service_environment', arg_type=CLIArgumentType(options_list=['--properties-integration-service-environment'], help='The integration service environment.'))
        c.argument('properties_state', arg_type=get_enum_type(['NotSpecified', 'Completed', 'Enabled', 'Disabled', 'Deleted', 'Suspended']), help='The workflow state.')

    with self.argument_context('logic integration-account update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('sku', action=AddSku, nargs='+', help='The integration account sku.')
        c.argument('properties_integration_service_environment', arg_type=CLIArgumentType(options_list=['--properties-integration-service-environment'], help='The integration service environment.'))
        c.argument('properties_state', arg_type=get_enum_type(['NotSpecified', 'Completed', 'Enabled', 'Disabled', 'Deleted', 'Suspended']), help='The workflow state.')

    with self.argument_context('logic integration-account delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')

    with self.argument_context('logic integration-account log-tracking-event') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('source_type', help='The source type.')
        c.argument('track_events_options', arg_type=get_enum_type(['None', 'DisableSourceInfoEnrich']), help='The track events operation options.')
        c.argument('events', arg_type=CLIArgumentType(options_list=['--events'], help='The events.'))

    with self.argument_context('logic integration-account list-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('not_after', help='The expiry time.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic integration-account list-key-vault-key') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('key_vault', action=AddKeyVault, nargs='+', help='The key vault reference.')
        c.argument('skip_token', help='The skip token.')

    with self.argument_context('logic integration-account regenerate-access-key') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic integration-account-assembly list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')

    with self.argument_context('logic integration-account-assembly show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('assembly_artifact_name', help='The assembly artifact name.')

    with self.argument_context('logic integration-account-assembly create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('assembly_artifact_name', help='The assembly artifact name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties', action=AddProperties, nargs='+', help='The assembly properties definition.')

    with self.argument_context('logic integration-account-assembly update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('assembly_artifact_name', help='The assembly artifact name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties', action=AddProperties, nargs='+', help='The assembly properties definition.')

    with self.argument_context('logic integration-account-assembly delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('assembly_artifact_name', help='The assembly artifact name.')

    with self.argument_context('logic integration-account-assembly list-content-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('assembly_artifact_name', help='The assembly artifact name.')

    with self.argument_context('logic integration-account-batch-configuration list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')

    with self.argument_context('logic integration-account-batch-configuration show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('batch_configuration_name', help='The batch configuration name.')

    with self.argument_context('logic integration-account-batch-configuration create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('batch_configuration_name', help='The batch configuration name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='The batch configuration properties definition.'))

    with self.argument_context('logic integration-account-batch-configuration update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('batch_configuration_name', help='The batch configuration name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='The batch configuration properties definition.'))

    with self.argument_context('logic integration-account-batch-configuration delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('batch_configuration_name', help='The batch configuration name.')

    with self.argument_context('logic integration-account-schema list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic integration-account-schema show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('schema_name', help='The integration account schema name.')

    with self.argument_context('logic integration-account-schema create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('schema_name', help='The integration account schema name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_schema_type', arg_type=get_enum_type(['NotSpecified', 'Xml']), help='The schema type.')
        c.argument('properties_target_namespace', help='The target namespace of the schema.')
        c.argument('properties_document_name', help='The document name.')
        c.argument('properties_file_name', help='The file name.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')
        c.argument('properties_content', help='The content.')
        c.argument('properties_content_type', help='The content type.')

    with self.argument_context('logic integration-account-schema update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('schema_name', help='The integration account schema name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_schema_type', arg_type=get_enum_type(['NotSpecified', 'Xml']), help='The schema type.')
        c.argument('properties_target_namespace', help='The target namespace of the schema.')
        c.argument('properties_document_name', help='The document name.')
        c.argument('properties_file_name', help='The file name.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')
        c.argument('properties_content', help='The content.')
        c.argument('properties_content_type', help='The content type.')

    with self.argument_context('logic integration-account-schema delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('schema_name', help='The integration account schema name.')

    with self.argument_context('logic integration-account-schema list-content-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('schema_name', help='The integration account schema name.')
        c.argument('not_after', help='The expiry time.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic integration-account-map list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic integration-account-map show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('map_name', help='The integration account map name.')

    with self.argument_context('logic integration-account-map create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('map_name', help='The integration account map name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_map_type', arg_type=get_enum_type(['NotSpecified', 'Xslt', 'Xslt20', 'Xslt30', 'Liquid']), help='The map type.')
        c.argument('properties_parameters_schema', action=AddParametersSchema, nargs='+', help='The parameters schema of integration account map.')
        c.argument('properties_content', help='The content.')
        c.argument('properties_content_type', help='The content type.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')

    with self.argument_context('logic integration-account-map update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('map_name', help='The integration account map name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_map_type', arg_type=get_enum_type(['NotSpecified', 'Xslt', 'Xslt20', 'Xslt30', 'Liquid']), help='The map type.')
        c.argument('properties_parameters_schema', action=AddParametersSchema, nargs='+', help='The parameters schema of integration account map.')
        c.argument('properties_content', help='The content.')
        c.argument('properties_content_type', help='The content type.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')

    with self.argument_context('logic integration-account-map delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('map_name', help='The integration account map name.')

    with self.argument_context('logic integration-account-map list-content-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('map_name', help='The integration account map name.')
        c.argument('not_after', help='The expiry time.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic integration-account-partner list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic integration-account-partner show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('partner_name', help='The integration account partner name.')

    with self.argument_context('logic integration-account-partner create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('partner_name', help='The integration account partner name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_partner_type', arg_type=get_enum_type(['NotSpecified', 'B2B']), help='The partner type.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')
        c.argument('properties_content', arg_type=CLIArgumentType(options_list=['--properties-content'], help='The integration account partner content.'))

    with self.argument_context('logic integration-account-partner update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('partner_name', help='The integration account partner name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_partner_type', arg_type=get_enum_type(['NotSpecified', 'B2B']), help='The partner type.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')
        c.argument('properties_content', arg_type=CLIArgumentType(options_list=['--properties-content'], help='The integration account partner content.'))

    with self.argument_context('logic integration-account-partner delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('partner_name', help='The integration account partner name.')

    with self.argument_context('logic integration-account-partner list-content-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('partner_name', help='The integration account partner name.')
        c.argument('not_after', help='The expiry time.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic integration-account-agreement list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic integration-account-agreement show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('agreement_name', help='The integration account agreement name.')

    with self.argument_context('logic integration-account-agreement create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('agreement_name', help='The integration account agreement name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')
        c.argument('properties_agreement_type', arg_type=get_enum_type(['NotSpecified', 'AS2', 'X12', 'Edifact']), help='The agreement type.')
        c.argument('properties_host_partner', help='The integration account partner that is set as host partner for this agreement.')
        c.argument('properties_guest_partner', help='The integration account partner that is set as guest partner for this agreement.')
        c.argument('properties_host_identity', action=AddHostIdentity, nargs='+', help='The integration account partner\'s business identity.')
        c.argument('properties_guest_identity', action=AddGuestIdentity, nargs='+', help='The integration account partner\'s business identity.')
        c.argument('properties_content', arg_type=CLIArgumentType(options_list=['--properties-content'], help='The integration account agreement content.'))

    with self.argument_context('logic integration-account-agreement update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('agreement_name', help='The integration account agreement name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')
        c.argument('properties_agreement_type', arg_type=get_enum_type(['NotSpecified', 'AS2', 'X12', 'Edifact']), help='The agreement type.')
        c.argument('properties_host_partner', help='The integration account partner that is set as host partner for this agreement.')
        c.argument('properties_guest_partner', help='The integration account partner that is set as guest partner for this agreement.')
        c.argument('properties_host_identity', action=AddHostIdentity, nargs='+', help='The integration account partner\'s business identity.')
        c.argument('properties_guest_identity', action=AddGuestIdentity, nargs='+', help='The integration account partner\'s business identity.')
        c.argument('properties_content', arg_type=CLIArgumentType(options_list=['--properties-content'], help='The integration account agreement content.'))

    with self.argument_context('logic integration-account-agreement delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('agreement_name', help='The integration account agreement name.')

    with self.argument_context('logic integration-account-agreement list-content-callback-url') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('agreement_name', help='The integration account agreement name.')
        c.argument('not_after', help='The expiry time.')
        c.argument('key_type', arg_type=get_enum_type(['NotSpecified', 'Primary', 'Secondary']), help='The key type.')

    with self.argument_context('logic integration-account-certificate list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('top', help='The number of items to be included in the result.')

    with self.argument_context('logic integration-account-certificate show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('certificate_name', help='The integration account certificate name.')

    with self.argument_context('logic integration-account-certificate create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('certificate_name', help='The integration account certificate name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')
        c.argument('properties_key', arg_type=CLIArgumentType(options_list=['--properties-key'], help='The reference to the key vault key.'))
        c.argument('properties_public_certificate', help='The public certificate.')

    with self.argument_context('logic integration-account-certificate update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('certificate_name', help='The integration account certificate name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_metadata', action=AddMetadata, nargs='+', help='The metadata.')
        c.argument('properties_key', arg_type=CLIArgumentType(options_list=['--properties-key'], help='The reference to the key vault key.'))
        c.argument('properties_public_certificate', help='The public certificate.')

    with self.argument_context('logic integration-account-certificate delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('certificate_name', help='The integration account certificate name.')

    with self.argument_context('logic integration-account-session list') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('top', help='The number of items to be included in the result.')
        c.argument('filter', help='The filter to apply on the operation. Options for filters include: State, Trigger, and ReferencedResourceId.')

    with self.argument_context('logic integration-account-session show') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('session_name', help='The integration account session name.')

    with self.argument_context('logic integration-account-session create') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('session_name', help='The integration account session name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_content', action=AddContent, nargs='+', help='')

    with self.argument_context('logic integration-account-session update') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('session_name', help='The integration account session name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties_content', action=AddContent, nargs='+', help='')

    with self.argument_context('logic integration-account-session delete') as c:
        c.argument('resource_group_name', resource_group_name_type, help='The resource group name.')
        c.argument('integration_account_name', help='The integration account name.')
        c.argument('session_name', help='The integration account session name.')

    with self.argument_context('logic integration-service-environment list') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('top', help='The number of items to be included in the result.')

    with self.argument_context('logic integration-service-environment show') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')

    with self.argument_context('logic integration-service-environment create') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='The integration service environment properties.'))
        c.argument('sku', action=AddSku, nargs='+', help='The integration service environment sku.')

    with self.argument_context('logic integration-service-environment update') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), help='The resource location.')
        c.argument('tags', tags_type, help='The resource tags.')
        c.argument('properties', arg_type=CLIArgumentType(options_list=['--properties'], help='The integration service environment properties.'))
        c.argument('sku', action=AddSku, nargs='+', help='The integration service environment sku.')

    with self.argument_context('logic integration-service-environment delete') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')

    with self.argument_context('logic integration-service-environment restart') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')

    with self.argument_context('logic integration-service-environment-sku list') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')

    with self.argument_context('logic integration-service-environment-network-health show') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')

    with self.argument_context('logic integration-service-environment-managed-api list') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')

    with self.argument_context('logic integration-service-environment-managed-api show') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')
        c.argument('api_name', help='The api name.')

    with self.argument_context('logic integration-service-environment-managed-api delete') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')
        c.argument('api_name', help='The api name.')

    with self.argument_context('logic integration-service-environment-managed-api put') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')
        c.argument('api_name', help='The api name.')

    with self.argument_context('logic integration-service-environment-managed-api-operation list') as c:
        c.argument('resource_group', help='The resource group.')
        c.argument('integration_service_environment_name', help='The integration service environment name.')
        c.argument('api_name', help='The api name.')
