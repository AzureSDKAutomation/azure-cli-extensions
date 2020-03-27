# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class IntegrationAccountCertificateOperations:
    """IntegrationAccountCertificateOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~logic_management_client.models
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

    def list(
        self,
        resource_group_name: str,
        integration_account_name: str,
        top: Optional[int] = None,
        **kwargs
    ) -> "models.IntegrationAccountCertificateListResult":
        """Gets a list of integration account certificates.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param top: The number of items to be included in the result.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountCertificateListResult or the result of cls(response)
        :rtype: ~logic_management_client.models.IntegrationAccountCertificateListResult
        :raises: ~logic_management_client.models.ErrorResponseException:
        """
        cls: ClsType["models.IntegrationAccountCertificateListResult"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-05-01"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters: Dict[str, Any] = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
            if top is not None:
                query_parameters['$top'] = self._serialize.query("top", top, 'int')

            # Construct headers
            header_parameters: Dict[str, Any] = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('IntegrationAccountCertificateListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.ErrorResponseException.from_response(response, self._deserialize)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates'}

    async def get(
        self,
        resource_group_name: str,
        integration_account_name: str,
        certificate_name: str,
        **kwargs
    ) -> "models.IntegrationAccountCertificate":
        """Gets an integration account certificate.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param certificate_name: The integration account certificate name.
        :type certificate_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountCertificate or the result of cls(response)
        :rtype: ~logic_management_client.models.IntegrationAccountCertificate
        :raises: ~logic_management_client.models.ErrorResponseException:
        """
        cls: ClsType["models.IntegrationAccountCertificate"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-05-01"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = self._deserialize('IntegrationAccountCertificate', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName}'}

    async def create_or_update(
        self,
        resource_group_name: str,
        integration_account_name: str,
        certificate_name: str,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        metadata: Optional["models.IntegrationAccountCertificatePropertiesMetadata"] = None,
        key: Optional["models.KeyVaultKeyReference"] = None,
        public_certificate: Optional[str] = None,
        **kwargs
    ) -> "models.IntegrationAccountCertificate":
        """Creates or updates an integration account certificate.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param certificate_name: The integration account certificate name.
        :type certificate_name: str
        :param location: The resource location.
        :type location: str
        :param tags: The resource tags.
        :type tags: dict[str, str]
        :param metadata: The metadata.
        :type metadata: ~logic_management_client.models.IntegrationAccountCertificatePropertiesMetadata
        :param key: The reference to the key vault key.
        :type key: ~logic_management_client.models.KeyVaultKeyReference
        :param public_certificate: The public certificate.
        :type public_certificate: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntegrationAccountCertificate or IntegrationAccountCertificate or the result of cls(response)
        :rtype: ~logic_management_client.models.IntegrationAccountCertificate or ~logic_management_client.models.IntegrationAccountCertificate
        :raises: ~logic_management_client.models.ErrorResponseException:
        """
        cls: ClsType["models.IntegrationAccountCertificate"] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})

        certificate = models.IntegrationAccountCertificate(location=location, tags=tags, metadata=metadata, key=key, public_certificate=public_certificate)
        api_version = "2019-05-01"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(certificate, 'IntegrationAccountCertificate')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('IntegrationAccountCertificate', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('IntegrationAccountCertificate', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName}'}

    async def delete(
        self,
        resource_group_name: str,
        integration_account_name: str,
        certificate_name: str,
        **kwargs
    ) -> None:
        """Deletes an integration account certificate.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param integration_account_name: The integration account name.
        :type integration_account_name: str
        :param certificate_name: The integration account certificate name.
        :type certificate_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~logic_management_client.models.ErrorResponseException:
        """
        cls: ClsType[None] = kwargs.pop('cls', None )
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-05-01"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'integrationAccountName': self._serialize.url("integration_account_name", integration_account_name, 'str'),
            'certificateName': self._serialize.url("certificate_name", certificate_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters: Dict[str, Any] = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters: Dict[str, Any] = {}

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/certificates/{certificateName}'}
