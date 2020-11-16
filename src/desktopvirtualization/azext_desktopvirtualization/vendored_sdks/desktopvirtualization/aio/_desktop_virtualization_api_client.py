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

from ._configuration import DesktopVirtualizationAPIClientConfiguration
from .operations import OperationOperations
from .operations import WorkspaceOperations
from .operations import ScalingPlanOperations
from .operations import ApplicationGroupOperations
from .operations import StartMenuItemOperations
from .operations import ApplicationOperations
from .operations import DesktopOperations
from .operations import HostPoolOperations
from .operations import UserSessionOperations
from .operations import SessionHostOperations
from .operations import MsixPackageOperations
from .operations import MsixImageOperations
from .. import models


class DesktopVirtualizationAPIClient(object):
    """DesktopVirtualizationAPIClient.

    :ivar operation: OperationOperations operations
    :vartype operation: desktop_virtualization_api_client.aio.operations.OperationOperations
    :ivar workspace: WorkspaceOperations operations
    :vartype workspace: desktop_virtualization_api_client.aio.operations.WorkspaceOperations
    :ivar scaling_plan: ScalingPlanOperations operations
    :vartype scaling_plan: desktop_virtualization_api_client.aio.operations.ScalingPlanOperations
    :ivar application_group: ApplicationGroupOperations operations
    :vartype application_group: desktop_virtualization_api_client.aio.operations.ApplicationGroupOperations
    :ivar start_menu_item: StartMenuItemOperations operations
    :vartype start_menu_item: desktop_virtualization_api_client.aio.operations.StartMenuItemOperations
    :ivar application: ApplicationOperations operations
    :vartype application: desktop_virtualization_api_client.aio.operations.ApplicationOperations
    :ivar desktop: DesktopOperations operations
    :vartype desktop: desktop_virtualization_api_client.aio.operations.DesktopOperations
    :ivar host_pool: HostPoolOperations operations
    :vartype host_pool: desktop_virtualization_api_client.aio.operations.HostPoolOperations
    :ivar user_session: UserSessionOperations operations
    :vartype user_session: desktop_virtualization_api_client.aio.operations.UserSessionOperations
    :ivar session_host: SessionHostOperations operations
    :vartype session_host: desktop_virtualization_api_client.aio.operations.SessionHostOperations
    :ivar msix_package: MsixPackageOperations operations
    :vartype msix_package: desktop_virtualization_api_client.aio.operations.MsixPackageOperations
    :ivar msix_image: MsixImageOperations operations
    :vartype msix_image: desktop_virtualization_api_client.aio.operations.MsixImageOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
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
        self._config = DesktopVirtualizationAPIClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace = WorkspaceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.scaling_plan = ScalingPlanOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application_group = ApplicationGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.start_menu_item = StartMenuItemOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.application = ApplicationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.desktop = DesktopOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.host_pool = HostPoolOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_session = UserSessionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.session_host = SessionHostOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.msix_package = MsixPackageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.msix_image = MsixImageOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DesktopVirtualizationAPIClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
