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

class TransactionNodeOperations(object):
    """TransactionNodeOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~blockchain_management_client.models
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

    def get(
        self,
        blockchain_member_name,  # type: str
        transaction_node_name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.TransactionNode"
        """Get the details of the transaction node.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param transaction_node_name: Transaction node name.
        :type transaction_node_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TransactionNode, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.TransactionNode
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TransactionNode"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'transactionNodeName': self._serialize.url("transaction_node_name", transaction_node_name, 'str'),
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

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TransactionNode', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}'}  # type: ignore

    def _create_initial(
        self,
        blockchain_member_name,  # type: str
        transaction_node_name,  # type: str
        resource_group_name,  # type: str
        location=None,  # type: Optional[str]
        password=None,  # type: Optional[str]
        firewall_rules=None,  # type: Optional[List["models.FirewallRule"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.TransactionNode"
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TransactionNode"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _transaction_node = models.TransactionNode(location=location, password=password, firewall_rules=firewall_rules)
        api_version = "2018-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self._create_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'transactionNodeName': self._serialize.url("transaction_node_name", transaction_node_name, 'str'),
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

        body_content_kwargs = {}  # type: Dict[str, Any]
        if _transaction_node is not None:
            body_content = self._serialize.body(_transaction_node, 'TransactionNode')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('TransactionNode', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('TransactionNode', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}'}  # type: ignore

    def begin_create(
        self,
        blockchain_member_name,  # type: str
        transaction_node_name,  # type: str
        resource_group_name,  # type: str
        location=None,  # type: Optional[str]
        password=None,  # type: Optional[str]
        firewall_rules=None,  # type: Optional[List["models.FirewallRule"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.TransactionNode"]
        """Create or update the transaction node.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param transaction_node_name: Transaction node name.
        :type transaction_node_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param location: Gets or sets the transaction node location.
        :type location: str
        :param password: Sets the transaction node dns endpoint basic auth password.
        :type password: str
        :param firewall_rules: Gets or sets the firewall rules.
        :type firewall_rules: list[~blockchain_management_client.models.FirewallRule]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either TransactionNode or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~blockchain_management_client.models.TransactionNode]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TransactionNode"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_initial(
                blockchain_member_name=blockchain_member_name,
                transaction_node_name=transaction_node_name,
                resource_group_name=resource_group_name,
                location=location,
                password=password,
                firewall_rules=firewall_rules,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('TransactionNode', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True: polling_method = ARMPolling(lro_delay,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}'}  # type: ignore

    def _delete_initial(
        self,
        blockchain_member_name,  # type: str
        transaction_node_name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'transactionNodeName': self._serialize.url("transaction_node_name", transaction_node_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}'}  # type: ignore

    def begin_delete(
        self,
        blockchain_member_name,  # type: str
        transaction_node_name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Delete the transaction node.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param transaction_node_name: Transaction node name.
        :type transaction_node_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
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
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(
                blockchain_member_name=blockchain_member_name,
                transaction_node_name=transaction_node_name,
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
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}'}  # type: ignore

    def update(
        self,
        blockchain_member_name,  # type: str
        transaction_node_name,  # type: str
        resource_group_name,  # type: str
        password=None,  # type: Optional[str]
        firewall_rules=None,  # type: Optional[List["models.FirewallRule"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.TransactionNode"
        """Update the transaction node.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param transaction_node_name: Transaction node name.
        :type transaction_node_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param password: Sets the transaction node dns endpoint basic auth password.
        :type password: str
        :param firewall_rules: Gets or sets the firewall rules.
        :type firewall_rules: list[~blockchain_management_client.models.FirewallRule]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TransactionNode, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.TransactionNode
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TransactionNode"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _transaction_node = models.TransactionNodeUpdate(password=password, firewall_rules=firewall_rules)
        api_version = "2018-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'transactionNodeName': self._serialize.url("transaction_node_name", transaction_node_name, 'str'),
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

        body_content_kwargs = {}  # type: Dict[str, Any]
        if _transaction_node is not None:
            body_content = self._serialize.body(_transaction_node, 'TransactionNodeUpdate')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('TransactionNode', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}'}  # type: ignore

    def list(
        self,
        blockchain_member_name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.TransactionNodeCollection"]
        """Lists the transaction nodes for a blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TransactionNodeCollection or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~blockchain_management_client.models.TransactionNodeCollection]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.TransactionNodeCollection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('TransactionNodeCollection', pipeline_response)
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
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes'}  # type: ignore

    def list_api_key(
        self,
        blockchain_member_name,  # type: str
        transaction_node_name,  # type: str
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ApiKeyCollection"
        """List the API keys for the transaction node.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param transaction_node_name: Transaction node name.
        :type transaction_node_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiKeyCollection, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.ApiKeyCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApiKeyCollection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-06-01-preview"

        # Construct URL
        url = self.list_api_key.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'transactionNodeName': self._serialize.url("transaction_node_name", transaction_node_name, 'str'),
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

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApiKeyCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_api_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}/listApiKeys'}  # type: ignore

    def regenerate_api_key(
        self,
        blockchain_member_name,  # type: str
        transaction_node_name,  # type: str
        resource_group_name,  # type: str
        key_name=None,  # type: Optional[str]
        value=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ApiKeyCollection"
        """Regenerate the API keys for the blockchain member.

        :param blockchain_member_name: Blockchain member name.
        :type blockchain_member_name: str
        :param transaction_node_name: Transaction node name.
        :type transaction_node_name: str
        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal.
        :type resource_group_name: str
        :param key_name: Gets or sets the API key name.
        :type key_name: str
        :param value: Gets or sets the API key value.
        :type value: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApiKeyCollection, or the result of cls(response)
        :rtype: ~blockchain_management_client.models.ApiKeyCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ApiKeyCollection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _api_key = models.ApiKey(key_name=key_name, value=value)
        api_version = "2018-06-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.regenerate_api_key.metadata['url']  # type: ignore
        path_format_arguments = {
            'blockchainMemberName': self._serialize.url("blockchain_member_name", blockchain_member_name, 'str'),
            'transactionNodeName': self._serialize.url("transaction_node_name", transaction_node_name, 'str'),
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

        body_content_kwargs = {}  # type: Dict[str, Any]
        if _api_key is not None:
            body_content = self._serialize.body(_api_key, 'ApiKey')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ApiKeyCollection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    regenerate_api_key.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Blockchain/blockchainMembers/{blockchainMemberName}/transactionNodes/{transactionNodeName}/regenerateApiKeys'}  # type: ignore
