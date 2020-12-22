# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GenerateDetailedCostReportOperations:
    """GenerateDetailedCostReportOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~cost_management_client.models
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

    async def _create_operation_initial(
        self,
        scope: str,
        metric: Optional[Union[str, "models.GenerateDetailedCostReportMetricType"]] = None,
        time_period: Optional["models.GenerateDetailedCostReportTimePeriod"] = None,
        billing_period: Optional[str] = None,
        invoice_id: Optional[str] = None,
        customer_id: Optional[str] = None,
        **kwargs
    ) -> Optional["models.GenerateDetailedCostReportOperationResult"]:
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.GenerateDetailedCostReportOperationResult"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        parameters = models.GenerateDetailedCostReportDefinition(metric=metric, time_period=time_period, billing_period=billing_period, invoice_id=invoice_id, customer_id=customer_id)
        api_version = "2020-06-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._create_operation_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
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
        body_content = self._serialize.body(parameters, 'GenerateDetailedCostReportDefinition')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.GenerateDetailedCostReportErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('GenerateDetailedCostReportOperationResult', pipeline_response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Azure-Consumption-AsyncOperation']=self._deserialize('str', response.headers.get('Azure-Consumption-AsyncOperation'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    _create_operation_initial.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/generateDetailedCostReport'}  # type: ignore

    async def begin_create_operation(
        self,
        scope: str,
        metric: Optional[Union[str, "models.GenerateDetailedCostReportMetricType"]] = None,
        time_period: Optional["models.GenerateDetailedCostReportTimePeriod"] = None,
        billing_period: Optional[str] = None,
        invoice_id: Optional[str] = None,
        customer_id: Optional[str] = None,
        **kwargs
    ) -> AsyncLROPoller["models.GenerateDetailedCostReportOperationResult"]:
        """Generates the detailed cost report for provided date range, billing period(Only enterprise
        customers) or Invoice Id asynchronously at a certain scope.

        :param scope: The scope associated with usage details operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         '/providers/Microsoft.Billing/departments/{departmentId}' for Department scope,
         '/providers/Microsoft.Billing/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount
         scope. Also, Modern Commerce Account scopes are
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for billingAccount scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners.
        :type scope: str
        :param metric: The type of the detailed report. By default ActualCost is provided.
        :type metric: str or ~cost_management_client.models.GenerateDetailedCostReportMetricType
        :param time_period: Has time period for pulling data for the cost detailed report. Can only
         have one of either timePeriod or invoiceId or billingPeriod parameters. If none provided
         current month cost is provided.
        :type time_period: ~cost_management_client.models.GenerateDetailedCostReportTimePeriod
        :param billing_period: Billing Period in YearMonth(e.g. 202008) format. Only for legacy
         enterprise customers can use this. Can only have one of either timePeriod or invoiceId or
         billingPeriod parameters. If none provided current month cost is provided.
        :type billing_period: str
        :param invoice_id: Invoice Id for PayAsYouGo customers and Modern billing profile scope. Can
         only have one of either timePeriod or invoiceId or billingPeriod parameters. If none provided
         current month cost is provided.
        :type invoice_id: str
        :param customer_id: Customer Id for Modern (Invoice Id and billing profile is also required for
         this).
        :type customer_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either GenerateDetailedCostReportOperationResult or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~cost_management_client.models.GenerateDetailedCostReportOperationResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, AsyncPollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["models.GenerateDetailedCostReportOperationResult"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_operation_initial(
                scope=scope,
                metric=metric,
                time_period=time_period,
                billing_period=billing_period,
                invoice_id=invoice_id,
                customer_id=customer_id,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('GenerateDetailedCostReportOperationResult', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str', skip_quote=True),
        }

        if polling is True: polling_method = AsyncARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = AsyncNoPolling()
        else: polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_operation.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/generateDetailedCostReport'}  # type: ignore
