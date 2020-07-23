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

class ShareOperations(object):
    """ShareOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~data_box_edge_management_client.models
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

    def list_by_data_box_edge_device(
        self,
        device_name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ShareList"]
        """Lists all the shares in a Data Box Edge/Data Box Gateway device.

        Lists all the shares in a Data Box Edge/Data Box Gateway device.

        :param device_name: The device name.
        :type device_name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ShareList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~data_box_edge_management_client.models.ShareList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ShareList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-07-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_data_box_edge_device.metadata['url']  # type: ignore
                path_format_arguments = {
                    'deviceName': self._serialize.url("device_name", device_name, 'str'),
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
            deserialized = self._deserialize('ShareList', pipeline_response)
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
    list_by_data_box_edge_device.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares'}  # type: ignore

    def get(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Share"
        """Gets a share by name.

        Gets a share by name.

        :param device_name: The device name.
        :type device_name: str
        :param name: The share name.
        :type name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Share, or the result of cls(response)
        :rtype: ~data_box_edge_management_client.models.Share
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Share"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-07-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceName': self._serialize.url("device_name", device_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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

        deserialized = self._deserialize('Share', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}'}  # type: ignore

    def _create_or_update_initial(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        share_status,  # type: Union[str, "models.ShareStatus"]
        monitoring_status,  # type: Union[str, "models.MonitoringStatus"]
        access_protocol,  # type: Union[str, "models.ShareAccessProtocol"]
        description=None,  # type: Optional[str]
        azure_container_info=None,  # type: Optional["models.AzureContainerInfo"]
        user_access_rights=None,  # type: Optional[List["models.UserAccessRight"]]
        client_access_rights=None,  # type: Optional[List["models.ClientAccessRight"]]
        refresh_details=None,  # type: Optional["models.RefreshDetails"]
        data_policy=None,  # type: Optional[Union[str, "models.DataPolicy"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Share"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Share"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _share = models.Share(description=description, share_status=share_status, monitoring_status=monitoring_status, azure_container_info=azure_container_info, access_protocol=access_protocol, user_access_rights=user_access_rights, client_access_rights=client_access_rights, refresh_details=refresh_details, data_policy=data_policy)
        api_version = "2020-07-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceName': self._serialize.url("device_name", device_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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
        body_content = self._serialize.body(_share, 'Share')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Share', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}'}  # type: ignore

    def begin_create_or_update(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        share_status,  # type: Union[str, "models.ShareStatus"]
        monitoring_status,  # type: Union[str, "models.MonitoringStatus"]
        access_protocol,  # type: Union[str, "models.ShareAccessProtocol"]
        description=None,  # type: Optional[str]
        azure_container_info=None,  # type: Optional["models.AzureContainerInfo"]
        user_access_rights=None,  # type: Optional[List["models.UserAccessRight"]]
        client_access_rights=None,  # type: Optional[List["models.ClientAccessRight"]]
        refresh_details=None,  # type: Optional["models.RefreshDetails"]
        data_policy=None,  # type: Optional[Union[str, "models.DataPolicy"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Creates a new share or updates an existing share on the device.

        Creates a new share or updates an existing share on the device.

        :param device_name: The device name.
        :type device_name: str
        :param name: The share name.
        :type name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param share_status: Current status of the share.
        :type share_status: str or ~data_box_edge_management_client.models.ShareStatus
        :param monitoring_status: Current monitoring status of the share.
        :type monitoring_status: str or ~data_box_edge_management_client.models.MonitoringStatus
        :param access_protocol: Access protocol to be used by the share.
        :type access_protocol: str or ~data_box_edge_management_client.models.ShareAccessProtocol
        :param description: Description for the share.
        :type description: str
        :param azure_container_info: Azure container mapping for the share.
        :type azure_container_info: ~data_box_edge_management_client.models.AzureContainerInfo
        :param user_access_rights: Mapping of users and corresponding access rights on the share
     (required for SMB protocol).
        :type user_access_rights: list[~data_box_edge_management_client.models.UserAccessRight]
        :param client_access_rights: List of IP addresses and corresponding access rights on the
     share(required for NFS protocol).
        :type client_access_rights: list[~data_box_edge_management_client.models.ClientAccessRight]
        :param refresh_details: Details of the refresh job on this share.
        :type refresh_details: ~data_box_edge_management_client.models.RefreshDetails
        :param data_policy: Data policy of the share.
        :type data_policy: str or ~data_box_edge_management_client.models.DataPolicy
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either Share or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~data_box_edge_management_client.models.Share]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Share"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        raw_result = self._create_or_update_initial(
            device_name=device_name,
            name=name,
            resource_group_name=resource_group_name,
            share_status=share_status,
            monitoring_status=monitoring_status,
            access_protocol=access_protocol,
            description=description,
            azure_container_info=azure_container_info,
            user_access_rights=user_access_rights,
            client_access_rights=client_access_rights,
            refresh_details=refresh_details,
            data_policy=data_policy,
            cls=lambda x,y,z: x,
            **kwargs
        )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('Share', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}'}  # type: ignore

    def _delete_initial(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-07-01-preview"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceName': self._serialize.url("device_name", device_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}'}  # type: ignore

    def begin_delete(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Deletes the share on the Data Box Edge/Data Box Gateway device.

        :param device_name: The device name.
        :type device_name: str
        :param name: The share name.
        :type name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
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
            device_name=device_name,
            name=name,
            resource_group_name=resource_group_name,
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
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}'}  # type: ignore

    def _refresh_initial(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-07-01-preview"

        # Construct URL
        url = self._refresh_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'deviceName': self._serialize.url("device_name", device_name, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _refresh_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}/refresh'}  # type: ignore

    def begin_refresh(
        self,
        device_name,  # type: str
        name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller
        """Refreshes the share metadata with the data from the cloud.

        Refreshes the share metadata with the data from the cloud.

        :param device_name: The device name.
        :type device_name: str
        :param name: The share name.
        :type name: str
        :param resource_group_name: The resource group name.
        :type resource_group_name: str
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
        raw_result = self._refresh_initial(
            device_name=device_name,
            name=name,
            resource_group_name=resource_group_name,
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
    begin_refresh.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataBoxEdge/dataBoxEdgeDevices/{deviceName}/shares/{name}/refresh'}  # type: ignore
