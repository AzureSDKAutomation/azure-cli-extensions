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

from ._configuration import KustoManagementClientConfiguration
from .operations import ClusterOperations
from .operations import ClusterPrincipalAssignmentOperations
from .operations import DatabaseOperations
from .operations import DatabasePrincipalAssignmentOperations
from .operations import AttachedDatabaseConfigurationOperations
from .operations import DataConnectionOperations
from .operations import OperationOperations
from .. import models


class KustoManagementClient(object):
    """The Azure Kusto management API provides a RESTful set of web services that interact with Azure Kusto services to manage your clusters and databases. The API enables you to create, update, and delete clusters and databases.

    :ivar cluster: ClusterOperations operations
    :vartype cluster: kusto_management_client.aio.operations.ClusterOperations
    :ivar cluster_principal_assignment: ClusterPrincipalAssignmentOperations operations
    :vartype cluster_principal_assignment: kusto_management_client.aio.operations.ClusterPrincipalAssignmentOperations
    :ivar database: DatabaseOperations operations
    :vartype database: kusto_management_client.aio.operations.DatabaseOperations
    :ivar database_principal_assignment: DatabasePrincipalAssignmentOperations operations
    :vartype database_principal_assignment: kusto_management_client.aio.operations.DatabasePrincipalAssignmentOperations
    :ivar attached_database_configuration: AttachedDatabaseConfigurationOperations operations
    :vartype attached_database_configuration: kusto_management_client.aio.operations.AttachedDatabaseConfigurationOperations
    :ivar data_connection: DataConnectionOperations operations
    :vartype data_connection: kusto_management_client.aio.operations.DataConnectionOperations
    :ivar operation: OperationOperations operations
    :vartype operation: kusto_management_client.aio.operations.OperationOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
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
        self._config = KustoManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.cluster = ClusterOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.cluster_principal_assignment = ClusterPrincipalAssignmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.database = DatabaseOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.database_principal_assignment = DatabasePrincipalAssignmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.attached_database_configuration = AttachedDatabaseConfigurationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_connection = DataConnectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "KustoManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
