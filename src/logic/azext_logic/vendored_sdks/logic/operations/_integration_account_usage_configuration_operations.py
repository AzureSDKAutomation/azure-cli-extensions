# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class IntegrationAccountUsageConfigurationOperations(object):
    """IntegrationAccountUsageConfigurationOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~logic_management_client.models
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
        integration_account_name,  # type: str
        top=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.IntegrationAccountUsageConfigurationListResult"]
        """Gets a list of integration account usage configurations.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param top: The number of items to be included in the result.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either IntegrationAccountUsageConfigurationListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~logic_management_client.models.IntegrationAccountUsageConfigurationListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationAccountUsageConfigurationListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('IntegrationAccountUsageConfigurationListResult', pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/usageConfigurations'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        integration_account_name,  # type: str
        usage_configuration_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IntegrationAccountUsageConfiguration"
        """Gets an integration account usage configuration.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param usage_configuration_name: The integration account usage configuration name.
        :type usage_configuration_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountUsageConfiguration, or the result of cls(response)
        :rtype: ~logic_management_client.models.IntegrationAccountUsageConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationAccountUsageConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
            'usageConfigurationName': self._serialize.url("usage_configuration_name", usage_configuration_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('IntegrationAccountUsageConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/usageConfigurations/{usageConfigurationName}'}  # type: ignore

    def create_or_update(
        self,
        resource_group_name,  # type: str
        integration_account_name,  # type: str
        usage_configuration_name,  # type: str
        location=None,  # type: Optional[str]
        tags=None,  # type: Optional[Dict[str, str]]
        disable_override=None,  # type: Optional[bool]
        throttles=None,  # type: Optional[Dict[str, "models.UsageConfigurationThrottle"]]
        metadata=None,  # type: Optional[object]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IntegrationAccountUsageConfiguration"
        """Creates or updates an integration account usage configuration.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param usage_configuration_name: The integration account usage configuration name.
        :type usage_configuration_name: str
        :param location: The resource location.
        :type location: str
        :param tags: The resource tags.
        :type tags: dict[str, str]
        :param disable_override: Whether to disable runtime override of the usage configuration.
        :type disable_override: bool
        :param throttles: The usage configuration throttles.
        :type throttles: dict[str, ~logic_management_client.models.UsageConfigurationThrottle]
        :param metadata: The metadata.
        :type metadata: object
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountUsageConfiguration, or the result of cls(response)
        :rtype: ~logic_management_client.models.IntegrationAccountUsageConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.IntegrationAccountUsageConfiguration"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        usage_configuration = models.IntegrationAccountUsageConfiguration(location=location, tags=tags, disable_override=disable_override, throttles=throttles, metadata=metadata)
        api_version = "2019-05-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
            'usageConfigurationName': self._serialize.url("usage_configuration_name", usage_configuration_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(usage_configuration, 'IntegrationAccountUsageConfiguration')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('IntegrationAccountUsageConfiguration', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('IntegrationAccountUsageConfiguration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/usageConfigurations/{usageConfigurationName}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        integration_account_name,  # type: str
        usage_configuration_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes an integration account usage configuration.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param usage_configuration_name: The integration account usage configuration name.
        :type usage_configuration_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-05-01"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
            'usageConfigurationName': self._serialize.url("usage_configuration_name", usage_configuration_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/usageConfigurations/{usageConfigurationName}'}  # type: ignore

    def list_callback_url(
        self,
        resource_group_name,  # type: str
        integration_account_name,  # type: str
        usage_configuration_name,  # type: str
        not_after=None,  # type: Optional[datetime.datetime]
        key_type=None,  # type: Optional[Union[str, "models.KeyType"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.WorkflowTriggerCallbackUrl"
        """Get the callback url.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param usage_configuration_name: The integration account usage configuration name.
        :type usage_configuration_name: str
        :param not_after: The expiry time.
        :type not_after: ~datetime.datetime
        :param key_type: The key type.
        :type key_type: str or ~logic_management_client.models.KeyType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WorkflowTriggerCallbackUrl, or the result of cls(response)
        :rtype: ~logic_management_client.models.WorkflowTriggerCallbackUrl
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.WorkflowTriggerCallbackUrl"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        list_callback_url = models.GetCallbackUrlParameters(not_after=not_after, key_type=key_type)
        api_version = "2019-05-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.list_callback_url.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
            'usageConfigurationName': self._serialize.url("usage_configuration_name", usage_configuration_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(list_callback_url, 'GetCallbackUrlParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('WorkflowTriggerCallbackUrl', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_callback_url.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/usageConfigurations/{usageConfigurationName}/listCallbackUrl'}  # type: ignore
