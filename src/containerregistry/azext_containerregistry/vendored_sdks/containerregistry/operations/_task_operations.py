# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class TaskOperations(object):
    """TaskOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~container_registry_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.TaskListResult"]
        """Lists all the tasks for a specified container registry.

        :param resource_group_name: The name of the resource group to which the container registry
     belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TaskListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~container_registry_management_client.models.TaskListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TaskListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
                    'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('TaskListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        task_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Task"
        """Get the properties of a specified task.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param task_name: The name of the container registry task.
        :type task_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Task, or the result of cls(response)
        :rtype: ~container_registry_management_client.models.Task
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Task"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'taskName': self._serialize.url("task_name", task_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9-_]*$'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Task', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}'}  # type: ignore

    def _create_initial(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        task_name,  # type: str
        location,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        status=None,  # type: Optional[Union[str, "models.TaskStatus"]]
        platform=None,  # type: Optional["models.PlatformProperties"]
        agent_pool_name=None,  # type: Optional[str]
        timeout=3600,  # type: Optional[int]
        step=None,  # type: Optional["models.TaskStepProperties"]
        custom_registries=None,  # type: Optional[Dict[str, "models.CustomRegistryCredentials"]]
        login_mode=None,  # type: Optional[Union[str, "models.SourceRegistryLoginMode"]]
        timer_triggers=None,  # type: Optional[List["models.TimerTrigger"]]
        source_triggers=None,  # type: Optional[List["models.SourceTrigger"]]
        base_image_trigger=None,  # type: Optional["models.BaseImageTrigger"]
        cpu=None,  # type: Optional[int]
        principal_id=None,  # type: Optional[str]
        tenant_id=None,  # type: Optional[str]
        type=None,  # type: Optional[Union[str, "models.ResourceIdentityType"]]
        user_assigned_identities=None,  # type: Optional[Dict[str, "models.UserIdentityProperties"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Task"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Task"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _task_create_parameters = models.Task(location=location, tags=tags, status=status, platform=platform, agent_pool_name=agent_pool_name, timeout=timeout, step=step, custom_registries=custom_registries, login_mode=login_mode, timer_triggers=timer_triggers, source_triggers=source_triggers, base_image_trigger=base_image_trigger, cpu=cpu, principal_id=principal_id, tenant_id=tenant_id, type_identity_type=type, user_assigned_identities=user_assigned_identities)
        api_version = "2019-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'taskName': self._serialize.url("task_name", task_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9-_]*$'),
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
        body_content = self._serialize.body(_task_create_parameters, 'Task')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Task', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Task', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}'}  # type: ignore

    def begin_create(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        task_name,  # type: str
        location,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        status=None,  # type: Optional[Union[str, "models.TaskStatus"]]
        platform=None,  # type: Optional["models.PlatformProperties"]
        agent_pool_name=None,  # type: Optional[str]
        timeout=3600,  # type: Optional[int]
        step=None,  # type: Optional["models.TaskStepProperties"]
        custom_registries=None,  # type: Optional[Dict[str, "models.CustomRegistryCredentials"]]
        login_mode=None,  # type: Optional[Union[str, "models.SourceRegistryLoginMode"]]
        timer_triggers=None,  # type: Optional[List["models.TimerTrigger"]]
        source_triggers=None,  # type: Optional[List["models.SourceTrigger"]]
        base_image_trigger=None,  # type: Optional["models.BaseImageTrigger"]
        cpu=None,  # type: Optional[int]
        principal_id=None,  # type: Optional[str]
        tenant_id=None,  # type: Optional[str]
        type=None,  # type: Optional[Union[str, "models.ResourceIdentityType"]]
        user_assigned_identities=None,  # type: Optional[Dict[str, "models.UserIdentityProperties"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Creates a task for a container registry with the specified parameters.

        :param resource_group_name: The name of the resource group to which the container registry
     belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param task_name: The name of the container registry task.
        :type task_name: str
        :param location: The location of the resource. This cannot be changed after the resource is
     created.
        :type location: str
        :param tags: The tags of the resource.
        :type tags: dict[str, str]
        :param status: The current status of task.
        :type status: str or ~container_registry_management_client.models.TaskStatus
        :param platform: The platform properties against which the run has to happen.
        :type platform: ~container_registry_management_client.models.PlatformProperties
        :param agent_pool_name: The dedicated agent pool for the task.
        :type agent_pool_name: str
        :param timeout: Run timeout in seconds.
        :type timeout: int
        :param step: The properties of a task step.
        :type step: ~container_registry_management_client.models.TaskStepProperties
        :param custom_registries: Describes the credential parameters for accessing other custom
     registries. The key
         for the dictionary item will be the registry login server (myregistry.azurecr.io) and
         the value of the item will be the registry credentials for accessing the registry.
        :type custom_registries: dict[str, ~container_registry_management_client.models.CustomRegistryCredentials]
        :param login_mode: The authentication mode which determines the source registry login scope.
     The credentials for the source registry
         will be generated using the given scope. These credentials will be used to login to
         the source registry during the run.
        :type login_mode: str or ~container_registry_management_client.models.SourceRegistryLoginMode
        :param timer_triggers: The collection of timer triggers.
        :type timer_triggers: list[~container_registry_management_client.models.TimerTrigger]
        :param source_triggers: The collection of triggers based on source code repository.
        :type source_triggers: list[~container_registry_management_client.models.SourceTrigger]
        :param base_image_trigger: The trigger based on base image dependencies.
        :type base_image_trigger: ~container_registry_management_client.models.BaseImageTrigger
        :param cpu: The CPU configuration in terms of number of cores required for the run.
        :type cpu: int
        :param principal_id: The principal ID of resource identity.
        :type principal_id: str
        :param tenant_id: The tenant ID of resource.
        :type tenant_id: str
        :param type: The identity type.
        :type type: str or ~container_registry_management_client.models.ResourceIdentityType
        :param user_assigned_identities: The list of user identities associated with the resource. The
     user identity
         dictionary key references will be ARM resource ids in the form:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
             providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        :type user_assigned_identities: dict[str, ~container_registry_management_client.models.UserIdentityProperties]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either Task or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~container_registry_management_client.models.Task]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Task"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._create_initial(
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            task_name=task_name,
            location=location,
            tags=tags,
            status=status,
            platform=platform,
            agent_pool_name=agent_pool_name,
            timeout=timeout,
            step=step,
            custom_registries=custom_registries,
            login_mode=login_mode,
            timer_triggers=timer_triggers,
            source_triggers=source_triggers,
            base_image_trigger=base_image_trigger,
            cpu=cpu,
            principal_id=principal_id,
            tenant_id=tenant_id,
            type=type,
            user_assigned_identities=user_assigned_identities,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Task', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}'}  # type: ignore

    def _delete_initial(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        task_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'taskName': self._serialize.url("task_name", task_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9-_]*$'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}'}  # type: ignore

    def begin_delete(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        task_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Deletes a specified task.

        :param resource_group_name: The name of the resource group to which the container registry
     belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param task_name: The name of the container registry task.
        :type task_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            task_name=task_name,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}'}  # type: ignore

    def _update_initial(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        task_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        status=None,  # type: Optional[Union[str, "models.TaskStatus"]]
        platform=None,  # type: Optional["models.PlatformUpdateParameters"]
        agent_configuration=None,  # type: Optional["models.AgentProperties"]
        agent_pool_name=None,  # type: Optional[str]
        timeout=None,  # type: Optional[int]
        step=None,  # type: Optional["models.TaskStepUpdateParameters"]
        trigger=None,  # type: Optional["models.TriggerUpdateParameters"]
        credentials=None,  # type: Optional["models.Credentials"]
        principal_id=None,  # type: Optional[str]
        tenant_id=None,  # type: Optional[str]
        type=None,  # type: Optional[Union[str, "models.ResourceIdentityType"]]
        user_assigned_identities=None,  # type: Optional[Dict[str, "models.UserIdentityProperties"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Task"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Task"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _task_update_parameters = models.TaskUpdateParameters(tags=tags, status=status, platform=platform, agent_configuration=agent_configuration, agent_pool_name=agent_pool_name, timeout=timeout, step=step, trigger=trigger, credentials=credentials, principal_id=principal_id, tenant_id=tenant_id, type=type, user_assigned_identities=user_assigned_identities)
        api_version = "2019-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'taskName': self._serialize.url("task_name", task_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9-_]*$'),
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
        body_content = self._serialize.body(_task_update_parameters, 'TaskUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Task', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Task', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}'}  # type: ignore

    def begin_update(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        task_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        status=None,  # type: Optional[Union[str, "models.TaskStatus"]]
        platform=None,  # type: Optional["models.PlatformUpdateParameters"]
        agent_configuration=None,  # type: Optional["models.AgentProperties"]
        agent_pool_name=None,  # type: Optional[str]
        timeout=None,  # type: Optional[int]
        step=None,  # type: Optional["models.TaskStepUpdateParameters"]
        trigger=None,  # type: Optional["models.TriggerUpdateParameters"]
        credentials=None,  # type: Optional["models.Credentials"]
        principal_id=None,  # type: Optional[str]
        tenant_id=None,  # type: Optional[str]
        type=None,  # type: Optional[Union[str, "models.ResourceIdentityType"]]
        user_assigned_identities=None,  # type: Optional[Dict[str, "models.UserIdentityProperties"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Updates a task with the specified parameters.

        :param resource_group_name: The name of the resource group to which the container registry
     belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param task_name: The name of the container registry task.
        :type task_name: str
        :param tags: The ARM resource tags.
        :type tags: dict[str, str]
        :param status: The current status of task.
        :type status: str or ~container_registry_management_client.models.TaskStatus
        :param platform: The platform properties against which the run has to happen.
        :type platform: ~container_registry_management_client.models.PlatformUpdateParameters
        :param agent_configuration: The machine configuration of the run agent.
        :type agent_configuration: ~container_registry_management_client.models.AgentProperties
        :param agent_pool_name: The dedicated agent pool for the task.
        :type agent_pool_name: str
        :param timeout: Run timeout in seconds.
        :type timeout: int
        :param step: The properties for updating a task step.
        :type step: ~container_registry_management_client.models.TaskStepUpdateParameters
        :param trigger: The properties for updating trigger properties.
        :type trigger: ~container_registry_management_client.models.TriggerUpdateParameters
        :param credentials: The parameters that describes a set of credentials that will be used when
     this run is invoked.
        :type credentials: ~container_registry_management_client.models.Credentials
        :param principal_id: The principal ID of resource identity.
        :type principal_id: str
        :param tenant_id: The tenant ID of resource.
        :type tenant_id: str
        :param type: The identity type.
        :type type: str or ~container_registry_management_client.models.ResourceIdentityType
        :param user_assigned_identities: The list of user identities associated with the resource. The
     user identity
         dictionary key references will be ARM resource ids in the form:
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/
             providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        :type user_assigned_identities: dict[str, ~container_registry_management_client.models.UserIdentityProperties]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either Task or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~container_registry_management_client.models.Task]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Task"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._update_initial(
            resource_group_name=resource_group_name,
            registry_name=registry_name,
            task_name=task_name,
            tags=tags,
            status=status,
            platform=platform,
            agent_configuration=agent_configuration,
            agent_pool_name=agent_pool_name,
            timeout=timeout,
            step=step,
            trigger=trigger,
            credentials=credentials,
            principal_id=principal_id,
            tenant_id=tenant_id,
            type=type,
            user_assigned_identities=user_assigned_identities,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Task', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}'}  # type: ignore

    def get_detail(
        self,
        resource_group_name,  # type: str
        registry_name,  # type: str
        task_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Task"
        """Returns a task with extended information that includes all secrets.

        :param resource_group_name: The name of the resource group to which the container registry
         belongs.
        :type resource_group_name: str
        :param registry_name: The name of the container registry.
        :type registry_name: str
        :param task_name: The name of the container registry task.
        :type task_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Task, or the result of cls(response)
        :rtype: ~container_registry_management_client.models.Task
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Task"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-06-01-preview"

        # Construct URL
        url = self.get_detail.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', min_length=1),
            'registryName': self._serialize.url("registry_name", registry_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9]*$'),
            'taskName': self._serialize.url("task_name", task_name, 'str', max_length=50, min_length=5, pattern=r'^[a-zA-Z0-9-_]*$'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Task', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_detail.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ContainerRegistry/registries/{registryName}/tasks/{taskName}/listDetails'}  # type: ignore
