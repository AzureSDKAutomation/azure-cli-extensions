# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import LogicManagementClientConfiguration
from .operations import WorkflowOperations
from .operations import WorkflowVersionOperations
from .operations import WorkflowTriggerOperations
from .operations import WorkflowVersionTriggerOperations
from .operations import WorkflowTriggerHistoryOperations
from .operations import WorkflowRunOperations
from .operations import WorkflowRunActionOperations
from .operations import WorkflowRunActionRepetitionOperations
from .operations import WorkflowRunActionRepetitionRequestHistoryOperations
from .operations import WorkflowRunActionRequestHistoryOperations
from .operations import WorkflowRunActionScopeRepetitionOperations
from .operations import WorkflowRunOperationOperations
from .operations import IntegrationAccountOperations
from .operations import IntegrationAccountAssemblyOperations
from .operations import IntegrationAccountBatchConfigurationOperations
from .operations import IntegrationAccountSchemaOperations
from .operations import IntegrationAccountMapOperations
from .operations import IntegrationAccountPartnerOperations
from .operations import IntegrationAccountAgreementOperations
from .operations import IntegrationAccountCertificateOperations
from .operations import IntegrationAccountSessionOperations
from .operations import IntegrationAccountUsageConfigurationOperations
from .operations import IntegrationServiceEnvironmentOperations
from .operations import IntegrationServiceEnvironmentSkuOperations
from .operations import IntegrationServiceEnvironmentNetworkHealthOperations
from .operations import IntegrationServiceEnvironmentManagedApiOperations
from .operations import IntegrationServiceEnvironmentManagedApiOperationOperations
from .operations import OperationOperations
from .. import models


class LogicManagementClient(object):
    """REST API for Azure Logic Apps.

    :ivar workflow: WorkflowOperations operations
    :vartype workflow: logic_management_client.aio.operations.WorkflowOperations
    :ivar workflow_version: WorkflowVersionOperations operations
    :vartype workflow_version: logic_management_client.aio.operations.WorkflowVersionOperations
    :ivar workflow_trigger: WorkflowTriggerOperations operations
    :vartype workflow_trigger: logic_management_client.aio.operations.WorkflowTriggerOperations
    :ivar workflow_version_trigger: WorkflowVersionTriggerOperations operations
    :vartype workflow_version_trigger: logic_management_client.aio.operations.WorkflowVersionTriggerOperations
    :ivar workflow_trigger_history: WorkflowTriggerHistoryOperations operations
    :vartype workflow_trigger_history: logic_management_client.aio.operations.WorkflowTriggerHistoryOperations
    :ivar workflow_run: WorkflowRunOperations operations
    :vartype workflow_run: logic_management_client.aio.operations.WorkflowRunOperations
    :ivar workflow_run_action: WorkflowRunActionOperations operations
    :vartype workflow_run_action: logic_management_client.aio.operations.WorkflowRunActionOperations
    :ivar workflow_run_action_repetition: WorkflowRunActionRepetitionOperations operations
    :vartype workflow_run_action_repetition: logic_management_client.aio.operations.WorkflowRunActionRepetitionOperations
    :ivar workflow_run_action_repetition_request_history: WorkflowRunActionRepetitionRequestHistoryOperations operations
    :vartype workflow_run_action_repetition_request_history: logic_management_client.aio.operations.WorkflowRunActionRepetitionRequestHistoryOperations
    :ivar workflow_run_action_request_history: WorkflowRunActionRequestHistoryOperations operations
    :vartype workflow_run_action_request_history: logic_management_client.aio.operations.WorkflowRunActionRequestHistoryOperations
    :ivar workflow_run_action_scope_repetition: WorkflowRunActionScopeRepetitionOperations operations
    :vartype workflow_run_action_scope_repetition: logic_management_client.aio.operations.WorkflowRunActionScopeRepetitionOperations
    :ivar workflow_run_operation: WorkflowRunOperationOperations operations
    :vartype workflow_run_operation: logic_management_client.aio.operations.WorkflowRunOperationOperations
    :ivar integration_account: IntegrationAccountOperations operations
    :vartype integration_account: logic_management_client.aio.operations.IntegrationAccountOperations
    :ivar integration_account_assembly: IntegrationAccountAssemblyOperations operations
    :vartype integration_account_assembly: logic_management_client.aio.operations.IntegrationAccountAssemblyOperations
    :ivar integration_account_batch_configuration: IntegrationAccountBatchConfigurationOperations operations
    :vartype integration_account_batch_configuration: logic_management_client.aio.operations.IntegrationAccountBatchConfigurationOperations
    :ivar integration_account_schema: IntegrationAccountSchemaOperations operations
    :vartype integration_account_schema: logic_management_client.aio.operations.IntegrationAccountSchemaOperations
    :ivar integration_account_map: IntegrationAccountMapOperations operations
    :vartype integration_account_map: logic_management_client.aio.operations.IntegrationAccountMapOperations
    :ivar integration_account_partner: IntegrationAccountPartnerOperations operations
    :vartype integration_account_partner: logic_management_client.aio.operations.IntegrationAccountPartnerOperations
    :ivar integration_account_agreement: IntegrationAccountAgreementOperations operations
    :vartype integration_account_agreement: logic_management_client.aio.operations.IntegrationAccountAgreementOperations
    :ivar integration_account_certificate: IntegrationAccountCertificateOperations operations
    :vartype integration_account_certificate: logic_management_client.aio.operations.IntegrationAccountCertificateOperations
    :ivar integration_account_session: IntegrationAccountSessionOperations operations
    :vartype integration_account_session: logic_management_client.aio.operations.IntegrationAccountSessionOperations
    :ivar integration_account_usage_configuration: IntegrationAccountUsageConfigurationOperations operations
    :vartype integration_account_usage_configuration: logic_management_client.aio.operations.IntegrationAccountUsageConfigurationOperations
    :ivar integration_service_environment: IntegrationServiceEnvironmentOperations operations
    :vartype integration_service_environment: logic_management_client.aio.operations.IntegrationServiceEnvironmentOperations
    :ivar integration_service_environment_sku: IntegrationServiceEnvironmentSkuOperations operations
    :vartype integration_service_environment_sku: logic_management_client.aio.operations.IntegrationServiceEnvironmentSkuOperations
    :ivar integration_service_environment_network_health: IntegrationServiceEnvironmentNetworkHealthOperations operations
    :vartype integration_service_environment_network_health: logic_management_client.aio.operations.IntegrationServiceEnvironmentNetworkHealthOperations
    :ivar integration_service_environment_managed_api: IntegrationServiceEnvironmentManagedApiOperations operations
    :vartype integration_service_environment_managed_api: logic_management_client.aio.operations.IntegrationServiceEnvironmentManagedApiOperations
    :ivar integration_service_environment_managed_api_operation: IntegrationServiceEnvironmentManagedApiOperationOperations operations
    :vartype integration_service_environment_managed_api_operation: logic_management_client.aio.operations.IntegrationServiceEnvironmentManagedApiOperationOperations
    :ivar operation: OperationOperations operations
    :vartype operation: logic_management_client.aio.operations.OperationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription id.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = LogicManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.workflow = WorkflowOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_version = WorkflowVersionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_trigger = WorkflowTriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_version_trigger = WorkflowVersionTriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_trigger_history = WorkflowTriggerHistoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run = WorkflowRunOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action = WorkflowRunActionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action_repetition = WorkflowRunActionRepetitionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action_repetition_request_history = WorkflowRunActionRepetitionRequestHistoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action_request_history = WorkflowRunActionRequestHistoryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_action_scope_repetition = WorkflowRunActionScopeRepetitionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workflow_run_operation = WorkflowRunOperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account = IntegrationAccountOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_assembly = IntegrationAccountAssemblyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_batch_configuration = IntegrationAccountBatchConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_schema = IntegrationAccountSchemaOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_map = IntegrationAccountMapOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_partner = IntegrationAccountPartnerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_agreement = IntegrationAccountAgreementOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_certificate = IntegrationAccountCertificateOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_session = IntegrationAccountSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_account_usage_configuration = IntegrationAccountUsageConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment = IntegrationServiceEnvironmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment_sku = IntegrationServiceEnvironmentSkuOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment_network_health = IntegrationServiceEnvironmentNetworkHealthOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment_managed_api = IntegrationServiceEnvironmentManagedApiOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.integration_service_environment_managed_api_operation = IntegrationServiceEnvironmentManagedApiOperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "LogicManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
