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
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SoftwareUpdateConfigurationMachineRunOperations(object):
    """SoftwareUpdateConfigurationMachineRunOperations operations.

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

    def get_by_id(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        software_update_configuration_machine_run_id,  # type: str
        client_request_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SoftwareUpdateConfigurationMachineRun"
        """Get a single software update configuration machine run by Id.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param software_update_configuration_machine_run_id: The Id of the software update
         configuration machine run.
        :type software_update_configuration_machine_run_id: str
        :param client_request_id: Identifies this specific client request.
        :type client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SoftwareUpdateConfigurationMachineRun or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.SoftwareUpdateConfigurationMachineRun
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SoftwareUpdateConfigurationMachineRun"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-05-15-preview"

        # Construct URL
        url = self.get_by_id.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
            'softwareUpdateConfigurationMachineRunId': self._serialize.url("software_update_configuration_machine_run_id", software_update_configuration_machine_run_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if client_request_id is not None:
            header_parameters['clientRequestId'] = self._serialize.header("client_request_id", client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SoftwareUpdateConfigurationMachineRun', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_by_id.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationMachineRuns/{softwareUpdateConfigurationMachineRunId}'}

    def list(
        self,
        resource_group_name,  # type: str
        automation_account_name,  # type: str
        client_request_id=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        skip=None,  # type: Optional[str]
        top=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SoftwareUpdateConfigurationMachineRunListResult"
        """Return list of software update configuration machine runs.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param client_request_id: Identifies this specific client request.
        :type client_request_id: str
        :param filter: The filter to apply on the operation. You can use the following filters:
         'properties/osType', 'properties/status', 'properties/startTime', and
         'properties/softwareUpdateConfiguration/name'.
        :type filter: str
        :param skip: number of entries you skip before returning results.
        :type skip: str
        :param top: Maximum number of entries returned in the results collection.
        :type top: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SoftwareUpdateConfigurationMachineRunListResult or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.SoftwareUpdateConfigurationMachineRunListResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SoftwareUpdateConfigurationMachineRunListResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2017-05-15-preview"

        # Construct URL
        url = self.list.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._]+$'),
            'automationAccountName': self._serialize.url("automation_account_name", automation_account_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query("skip", skip, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query("top", top, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if client_request_id is not None:
            header_parameters['clientRequestId'] = self._serialize.header("client_request_id", client_request_id, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SoftwareUpdateConfigurationMachineRunListResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationMachineRuns'}
