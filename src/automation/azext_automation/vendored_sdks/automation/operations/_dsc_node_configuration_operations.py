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
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DscNodeConfigurationOperations(object):
    """DscNodeConfigurationOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.automation.models
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

    def delete(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        node_configuration_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete the Dsc node configurations by node configuration.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param node_configuration_name: The Dsc node configuration name.
        :type node_configuration_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-01-15"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
            'nodeConfigurationName': self._serialize.url("node_configuration_name", node_configuration_name, 'str'),
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName}'}

    def get(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        node_configuration_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DscNodeConfiguration"
        """Retrieve the Dsc node configurations by node configuration.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param node_configuration_name: The Dsc node configuration name.
        :type node_configuration_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DscNodeConfiguration or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.DscNodeConfiguration
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DscNodeConfiguration"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-01-15"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
            'nodeConfigurationName': self._serialize.url("node_configuration_name", node_configuration_name, 'str'),
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

        deserialized = self._deserialize('DscNodeConfiguration', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName}'}

    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        node_configuration_name,  # type: str
        name=None,  # type: Optional[str]
        tags=None,  # type: Optional[Dict[str, str]]
        source=None,  # type: Optional["models.ContentSource"]
        configuration=None,  # type: Optional["models.DscConfigurationAssociationProperty"]
        increment_node_configuration_build=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DscNodeConfiguration"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DscNodeConfiguration"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _parameters = models.DscNodeConfigurationCreateOrUpdateParameters(name=name, tags=tags, source=source, configuration=configuration, increment_node_configuration_build=increment_node_configuration_build)
        api_version = "2018-01-15"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
            'nodeConfigurationName': self._serialize.url("node_configuration_name", node_configuration_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
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
        body_content = self._serialize.body(_parameters, 'DscNodeConfigurationCreateOrUpdateParameters')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 201:
            deserialized = self._deserialize('DscNodeConfiguration', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName}'}

    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        node_configuration_name,  # type: str
        name=None,  # type: Optional[str]
        tags=None,  # type: Optional[Dict[str, str]]
        source=None,  # type: Optional["models.ContentSource"]
        configuration=None,  # type: Optional["models.DscConfigurationAssociationProperty"]
        increment_node_configuration_build=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DscNodeConfiguration"
        """Create the node configuration identified by node configuration name.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param node_configuration_name: The Dsc node configuration name.
        :type node_configuration_name: str
        :param name: Name of the node configuration.
        :type name: str
        :param tags: Gets or sets the tags attached to the resource.
        :type tags: dict[str, str]
        :param source: Gets or sets the source.
        :type source: ~azure.mgmt.automation.models.ContentSource
        :param configuration: Gets or sets the configuration of the node.
        :type configuration: ~azure.mgmt.automation.models.DscConfigurationAssociationProperty
        :param increment_node_configuration_build: If a new build version of NodeConfiguration is
     required.
        :type increment_node_configuration_build: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :return: An instance of LROPoller that returns None
        :rtype: ~azure.core.polling.LROPoller[None]

        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DscNodeConfiguration"]
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            node_configuration_name=node_configuration_name,
            name=name,
            tags=tags,
            source=source,
            configuration=configuration,
            increment_node_configuration_build=increment_node_configuration_build,
            cls=lambda x,y,z: x,
            **kwargs
        )

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('DscNodeConfiguration', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        lro_delay = kwargs.get(
            'polling_interval',
            self._config.polling_interval
        )
        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations/{nodeConfigurationName}'}

    def list_by_automation_account(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        filter=None,  # type: Optional[str]
        skip=None,  # type: Optional[int]
        top=None,  # type: Optional[int]
        inlinecount=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DscNodeConfigurationListResult"
        """Retrieve a list of dsc node configurations.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param filter: The filter to apply on the operation.
        :type filter: str
        :param skip: The number of rows to skip.
        :type skip: int
        :param top: The number of rows to take.
        :type top: int
        :param inlinecount: Return total rows.
        :type inlinecount: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DscNodeConfigurationListResult or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.DscNodeConfigurationListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.DscNodeConfigurationListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-01-15"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_automation_account.metadata['url']
                path_format_arguments = {
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
                    'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}  # type: Dict[str, Any]
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if filter is not None:
                query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
            if skip is not None:
                query_parameters['$skip'] = self._serialize.query("skip", skip, 'int')
            if top is not None:
                query_parameters['$top'] = self._serialize.query("top", top, 'int')
            if inlinecount is not None:
                query_parameters['$inlinecount'] = self._serialize.query("inlinecount", inlinecount, 'str')

            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('DscNodeConfigurationListResult', pipeline_response)
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
    list_by_automation_account.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodeConfigurations'}
