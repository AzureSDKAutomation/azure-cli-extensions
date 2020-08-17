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
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PipelineOperations(object):
    """PipelineOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure_dev_ops.models
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

    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        pipeline_name,  # type: str
        id,  # type: str
        name,  # type: str
        organization_reference_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        location=None,  # type: Optional[str]
        parameters=None,  # type: Optional[Dict[str, str]]
        repository_type=None,  # type: Optional[Union[str, "models.CodeRepositoryType"]]
        code_repository_id=None,  # type: Optional[str]
        default_branch=None,  # type: Optional[str]
        properties=None,  # type: Optional[Dict[str, str]]
        authorization_parameters=None,  # type: Optional[Dict[str, str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Pipeline"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Pipeline"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _create_operation_parameters = models.Pipeline(tags=tags, location=location, id_properties_bootstrap_configuration_template_id=id, parameters_properties_bootstrap_configuration_template_parameters=parameters, repository_type=repository_type, id_properties_bootstrap_configuration_repository_id=code_repository_id, default_branch=default_branch, properties=properties, parameters_properties_bootstrap_configuration_repository_authorization_parameters=authorization_parameters, name_properties_project_name=name, name_properties_organization_name=organization_reference_name)
        api_version = "2019-07-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str'),
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
        body_content = self._serialize.body(_create_operation_parameters, 'Pipeline')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Pipeline', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName}'}  # type: ignore

    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        pipeline_name,  # type: str
        id,  # type: str
        name,  # type: str
        organization_reference_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        location=None,  # type: Optional[str]
        parameters=None,  # type: Optional[Dict[str, str]]
        repository_type=None,  # type: Optional[Union[str, "models.CodeRepositoryType"]]
        code_repository_id=None,  # type: Optional[str]
        default_branch=None,  # type: Optional[str]
        properties=None,  # type: Optional[Dict[str, str]]
        authorization_parameters=None,  # type: Optional[Dict[str, str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Creates or updates an Azure Pipeline.

        :param resource_group_name: Name of the resource group within the Azure subscription.
        :type resource_group_name: str
        :param pipeline_name: The name of the Azure Pipeline resource in ARM.
        :type pipeline_name: str
        :param id: Unique identifier of the pipeline template.
        :type id: str
        :param name: Name of the Azure DevOps Project.
        :type name: str
        :param organization_reference_name: Name of the Azure DevOps Organization.
        :type organization_reference_name: str
        :param tags: Resource Tags.
        :type tags: dict[str, str]
        :param location: Resource Location.
        :type location: str
        :param parameters: Dictionary of input parameters used in the pipeline template.
        :type parameters: dict[str, str]
        :param repository_type: Type of code repository.
        :type repository_type: str or ~azure_dev_ops.models.CodeRepositoryType
        :param code_repository_id: Unique immutable identifier of the code repository.
        :type code_repository_id: str
        :param default_branch: Default branch used to configure Continuous Integration (CI) in the
     pipeline.
        :type default_branch: str
        :param properties: Repository-specific properties.
        :type properties: dict[str, str]
        :param authorization_parameters: Authorization parameters corresponding to the authorization
     type.
        :type authorization_parameters: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either Pipeline or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure_dev_ops.models.Pipeline]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Pipeline"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            pipeline_name=pipeline_name,
            id=id,
            name=name,
            organization_reference_name=organization_reference_name,
            tags=tags,
            location=location,
            parameters=parameters,
            repository_type=repository_type,
            code_repository_id=code_repository_id,
            default_branch=default_branch,
            properties=properties,
            authorization_parameters=authorization_parameters,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Pipeline', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName}'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        pipeline_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Pipeline"
        """Gets an existing Azure Pipeline.

        :param resource_group_name: Name of the resource group within the Azure subscription.
        :type resource_group_name: str
        :param pipeline_name: The name of the Azure Pipeline resource in ARM.
        :type pipeline_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pipeline, or the result of cls(response)
        :rtype: ~azure_dev_ops.models.Pipeline
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Pipeline"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-07-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str'),
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Pipeline', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName}'}  # type: ignore

    def update(
        self,
        resource_group_name,  # type: str
        pipeline_name,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Pipeline"
        """Updates the properties of an Azure Pipeline. Currently, only tags can be updated.

        :param resource_group_name: Name of the resource group within the Azure subscription.
        :type resource_group_name: str
        :param pipeline_name: The name of the Azure Pipeline resource.
        :type pipeline_name: str
        :param tags: Dictionary of key-value pairs to be set as tags on the Azure Pipeline. This will
         overwrite any existing tags.
        :type tags: dict[str, str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pipeline, or the result of cls(response)
        :rtype: ~azure_dev_ops.models.Pipeline
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Pipeline"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _update_operation_parameters = models.PipelineUpdateParameters(tags=tags)
        api_version = "2019-07-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str'),
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
        body_content = self._serialize.body(_update_operation_parameters, 'PipelineUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Pipeline', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        pipeline_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes an Azure Pipeline.

        :param resource_group_name: Name of the resource group within the Azure subscription.
        :type resource_group_name: str
        :param pipeline_name: The name of the Azure Pipeline resource.
        :type pipeline_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-07-01-preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'pipelineName': self._serialize.url("pipeline_name", pipeline_name, 'str'),
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines/{pipelineName}'}  # type: ignore

    def list_by_resource_group(
        self,
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.PipelineListResult"]
        """Lists all Azure Pipelines under the specified resource group.

        :param resource_group_name: Name of the resource group within the Azure subscription.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PipelineListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure_dev_ops.models.PipelineListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PipelineListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-07-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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
            deserialized = self._deserialize('PipelineListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevOps/pipelines'}  # type: ignore

    def list_by_subscription(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.PipelineListResult"]
        """Lists all Azure Pipelines under the specified subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PipelineListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure_dev_ops.models.PipelineListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.PipelineListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-07-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
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
            deserialized = self._deserialize('PipelineListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DevOps/pipelines'}  # type: ignore
