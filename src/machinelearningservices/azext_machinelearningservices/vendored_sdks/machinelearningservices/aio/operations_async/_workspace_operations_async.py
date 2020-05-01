# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncNoPolling, AsyncPollingMethod, async_poller
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class WorkspaceOperations:
    """WorkspaceOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get(
        self,
        resource_group_name: str,
        workspace_name: str,
        **kwargs
    ) -> "models.Workspace":
        """Gets the properties of the specified machine learning workspace.

        :param resource_group_name: Name of the resource group in which workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Workspace or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.Workspace
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Workspace"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2020-05-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.MachineLearningServiceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Workspace', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}'}

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        workspace_name: str,
        identity: Optional["models.Identity"] = None,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["models.Sku"] = None,
        description: Optional[str] = None,
        friendly_name: Optional[str] = None,
        key_vault: Optional[str] = None,
        application_insights: Optional[str] = None,
        container_registry: Optional[str] = None,
        storage_account: Optional[str] = None,
        discovery_url: Optional[str] = None,
        hbi_workspace: Optional[bool] = False,
        image_build_compute: Optional[str] = None,
        allow_public_access_when_behind_vnet: Optional[bool] = False,
        shared_private_link_resources: Optional[List["SharedPrivateLinkResource"]] = None,
        status: Optional[Union[str, "models.EncryptionStatus"]] = None,
        key_vault_properties: Optional["models.KeyVaultProperties"] = None,
        **kwargs
    ) -> "models.Workspace":
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Workspace"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _parameters = models.Workspace(identity=identity, location=location, tags=tags, sku=sku, description=description, friendly_name=friendly_name, key_vault=key_vault, application_insights=application_insights, container_registry=container_registry, storage_account=storage_account, discovery_url=discovery_url, hbi_workspace=hbi_workspace, image_build_compute=image_build_compute, allow_public_access_when_behind_vnet=allow_public_access_when_behind_vnet, shared_private_link_resources=shared_private_link_resources, status=status, key_vault_properties=key_vault_properties)
        api_version = "2020-05-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_parameters, 'Workspace')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.MachineLearningServiceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Workspace', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Workspace', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}'}

    async def create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        identity: Optional["models.Identity"] = None,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["models.Sku"] = None,
        description: Optional[str] = None,
        friendly_name: Optional[str] = None,
        key_vault: Optional[str] = None,
        application_insights: Optional[str] = None,
        container_registry: Optional[str] = None,
        storage_account: Optional[str] = None,
        discovery_url: Optional[str] = None,
        hbi_workspace: Optional[bool] = False,
        image_build_compute: Optional[str] = None,
        allow_public_access_when_behind_vnet: Optional[bool] = False,
        shared_private_link_resources: Optional[List["SharedPrivateLinkResource"]] = None,
        status: Optional[Union[str, "models.EncryptionStatus"]] = None,
        key_vault_properties: Optional["models.KeyVaultProperties"] = None,
        **kwargs
    ) -> "models.Workspace":
        """Creates or updates a workspace with the specified parameters.

        :param resource_group_name: Name of the resource group in which workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param identity: The identity of the resource.
        :type identity: ~azure.mgmt.machinelearningservices.models.Identity
        :param location: Specifies the location of the resource.
        :type location: str
        :param tags: Contains resource tags defined as key/value pairs.
        :type tags: dict[str, str]
        :param sku: The sku of the workspace.
        :type sku: ~azure.mgmt.machinelearningservices.models.Sku
        :param description: The description of this workspace.
        :type description: str
        :param friendly_name: The friendly name for this workspace. This name in mutable.
        :type friendly_name: str
        :param key_vault: ARM id of the key vault associated with this workspace. This cannot be
     changed once the workspace has been created.
        :type key_vault: str
        :param application_insights: ARM id of the application insights associated with this workspace.
     This cannot be changed once the workspace has been created.
        :type application_insights: str
        :param container_registry: ARM id of the container registry associated with this workspace.
     This cannot be changed once the workspace has been created.
        :type container_registry: str
        :param storage_account: ARM id of the storage account associated with this workspace. This
     cannot be changed once the workspace has been created.
        :type storage_account: str
        :param discovery_url: Url for the discovery service to identify regional endpoints for machine
     learning experimentation services.
        :type discovery_url: str
        :param hbi_workspace: The flag to signal HBI data in the workspace and reduce diagnostic data
     collected by the service.
        :type hbi_workspace: bool
        :param image_build_compute: The compute name for image build.
        :type image_build_compute: str
        :param allow_public_access_when_behind_vnet: The flag to indicate whether to allow public
     access when behind VNet.
        :type allow_public_access_when_behind_vnet: bool
        :param shared_private_link_resources: The list of shared private link resources in this
     workspace.
        :type shared_private_link_resources: list[~azure.mgmt.machinelearningservices.models.SharedPrivateLinkResource]
        :param status: Indicates whether or not the encryption is enabled for the workspace.
        :type status: str or ~azure.mgmt.machinelearningservices.models.EncryptionStatus
        :param key_vault_properties: Customer Key vault properties.
        :type key_vault_properties: ~azure.mgmt.machinelearningservices.models.KeyVaultProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :return: An instance of LROPoller that returns Workspace
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.machinelearningservices.models.Workspace]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Workspace"]
        raw_result = await self._create_or_update_initial(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            identity=identity,
            location=location,
            tags=tags,
            sku=sku,
            description=description,
            friendly_name=friendly_name,
            key_vault=key_vault,
            application_insights=application_insights,
            container_registry=container_registry,
            storage_account=storage_account,
            discovery_url=discovery_url,
            hbi_workspace=hbi_workspace,
            image_build_compute=image_build_compute,
            allow_public_access_when_behind_vnet=allow_public_access_when_behind_vnet,
            shared_private_link_resources=shared_private_link_resources,
            status=status,
            key_vault_properties=key_vault_properties,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Workspace', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = AsyncARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        return await async_poller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}'}

    async def delete(
        self,
        resource_group_name: str,
        workspace_name: str,
        **kwargs
    ) -> None:
        """Deletes a machine learning workspace.

        :param resource_group_name: Name of the resource group in which workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2020-05-01"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.MachineLearningServiceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}'}

    async def update(
        self,
        resource_group_name: str,
        workspace_name: str,
        tags: Optional[Dict[str, str]] = None,
        sku: Optional["models.Sku"] = None,
        description: Optional[str] = None,
        friendly_name: Optional[str] = None,
        **kwargs
    ) -> "models.Workspace":
        """Updates a machine learning workspace with the specified parameters.

        :param resource_group_name: Name of the resource group in which workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :param tags: The resource tags for the machine learning workspace.
        :type tags: dict[str, str]
        :param sku: The sku of the workspace.
        :type sku: ~azure.mgmt.machinelearningservices.models.Sku
        :param description: The description of this workspace.
        :type description: str
        :param friendly_name: The friendly name for this workspace.
        :type friendly_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Workspace or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.Workspace
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Workspace"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _parameters = models.WorkspaceUpdateParameters(tags=tags, sku=sku, description=description, friendly_name=friendly_name)
        api_version = "2020-05-01"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_parameters, 'WorkspaceUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.MachineLearningServiceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Workspace', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}'}

    def list_by_resource_group(
        self,
        resource_group_name: str,
        skiptoken: Optional[str] = None,
        **kwargs
    ) -> "models.WorkspaceListResult":
        """Lists all the available machine learning workspaces under the specified resource group.

        :param resource_group_name: Name of the resource group in which workspace is located.
        :type resource_group_name: str
        :param skiptoken: Continuation token for pagination.
        :type skiptoken: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceListResult or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.WorkspaceListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.WorkspaceListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2020-05-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if skiptoken is not None:
                query_parameters['$skiptoken'] = self._serialize.query("skiptoken", skiptoken, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('WorkspaceListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.MachineLearningServiceError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces'}

    async def list_key(
        self,
        resource_group_name: str,
        workspace_name: str,
        **kwargs
    ) -> "models.ListWorkspaceKeysResult":
        """Lists all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry.

        :param resource_group_name: Name of the resource group in which workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListWorkspaceKeysResult or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.ListWorkspaceKeysResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ListWorkspaceKeysResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2020-05-01"

        # Construct URL
        url = self.list_key.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.MachineLearningServiceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ListWorkspaceKeysResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/listKeys'}

    async def resync_key(
        self,
        resource_group_name: str,
        workspace_name: str,
        **kwargs
    ) -> None:
        """Resync all the keys associated with this workspace. This includes keys for the storage account, app insights and password for container registry.

        :param resource_group_name: Name of the resource group in which workspace is located.
        :type resource_group_name: str
        :param workspace_name: Name of Azure Machine Learning workspace.
        :type workspace_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2020-05-01"

        # Construct URL
        url = self.resync_key.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'workspaceName': self._serialize.url("workspace_name", workspace_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.MachineLearningServiceError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    resync_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/resyncKeys'}

    def list_by_subscription(
        self,
        skiptoken: Optional[str] = None,
        **kwargs
    ) -> "models.WorkspaceListResult":
        """Lists all the available machine learning workspaces under the specified subscription.

        :param skiptoken: Continuation token for pagination.
        :type skiptoken: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkspaceListResult or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.WorkspaceListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.WorkspaceListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2020-05-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if skiptoken is not None:
                query_parameters['$skiptoken'] = self._serialize.query("skiptoken", skiptoken, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('WorkspaceListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.MachineLearningServiceError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/workspaces'}
