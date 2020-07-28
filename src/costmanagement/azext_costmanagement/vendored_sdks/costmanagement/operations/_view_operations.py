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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ViewOperations(object):
    """ViewOperations operations.

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

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ViewListResult"]
        """Lists all views by tenant and object.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ViewListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~cost_management_client.models.ViewListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ViewListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('ViewListResult', pipeline_response)
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
    list.metadata = {'url': '/providers/Microsoft.CostManagement/views'}  # type: ignore

    def list_by_scope(
        self,
        scope,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ViewListResult"]
        """Lists all views at the given scope.

        :param scope: The scope associated with view operations. This includes
     'subscriptions/{subscriptionId}' for subscription scope,
     'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for
     Department scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
     for EnrollmentAccount scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
     for BillingProfile scope,
     'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}'
     for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}'
     for Management Group scope,
     'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for
     External Billing Account scope and
     'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for
     External Subscription scope.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ViewListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~cost_management_client.models.ViewListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ViewListResult"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_scope.metadata['url']  # type: ignore
                path_format_arguments = {
                    'scope': self._serialize.url("scope", scope, 'str'),
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
            deserialized = self._deserialize('ViewListResult', pipeline_response)
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
    list_by_scope.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/views'}  # type: ignore

    def get(
        self,
        view_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.View"
        """Gets the view by view name.

        :param view_name: View name.
        :type view_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: View, or the result of cls(response)
        :rtype: ~cost_management_client.models.View
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.View"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'viewName': self._serialize.url("view_name", view_name, 'str'),
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

        deserialized = self._deserialize('View', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.CostManagement/views/{viewName}'}  # type: ignore

    def create_or_update(
        self,
        view_name,  # type: str
        e_tag=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        scope=None,  # type: Optional[str]
        chart=None,  # type: Optional[Union[str, "models.ChartType"]]
        accumulated=None,  # type: Optional[Union[str, "models.AccumulatedType"]]
        metric=None,  # type: Optional[Union[str, "models.MetricType"]]
        kpis=None,  # type: Optional[List["models.KpiProperties"]]
        pivots=None,  # type: Optional[List["models.PivotProperties"]]
        timeframe=None,  # type: Optional[Union[str, "models.ReportTimeframeType"]]
        time_period=None,  # type: Optional["models.ReportConfigTimePeriod"]
        dataset=None,  # type: Optional["models.ReportConfigDataset"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.View"
        """The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

        :param view_name: View name.
        :type view_name: str
        :param e_tag: eTag of the resource. To handle concurrent update scenario, this field will be
         used to determine whether the user is updating the latest version or not.
        :type e_tag: str
        :param display_name: User input name of the view. Required.
        :type display_name: str
        :param scope: Cost Management scope to save the view on. This includes
         'subscriptions/{subscriptionId}' for subscription scope,
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for
         Department scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for BillingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}'
         for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}'
         for Management Group scope,
         '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for
         ExternalBillingAccount scope, and
         '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for
         ExternalSubscription scope.
        :type scope: str
        :param chart: Chart type of the main view in Cost Analysis. Required.
        :type chart: str or ~cost_management_client.models.ChartType
        :param accumulated: Show costs accumulated over time.
        :type accumulated: str or ~cost_management_client.models.AccumulatedType
        :param metric: Metric to use when displaying costs.
        :type metric: str or ~cost_management_client.models.MetricType
        :param kpis: List of KPIs to show in Cost Analysis UI.
        :type kpis: list[~cost_management_client.models.KpiProperties]
        :param pivots: Configuration of 3 sub-views in the Cost Analysis UI.
        :type pivots: list[~cost_management_client.models.PivotProperties]
        :param timeframe: The time frame for pulling data for the report. If custom, then a specific
         time period must be provided.
        :type timeframe: str or ~cost_management_client.models.ReportTimeframeType
        :param time_period: Has time period for pulling data for the report.
        :type time_period: ~cost_management_client.models.ReportConfigTimePeriod
        :param dataset: Has definition for data in this report config.
        :type dataset: ~cost_management_client.models.ReportConfigDataset
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: View, or the result of cls(response)
        :rtype: ~cost_management_client.models.View
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.View"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _parameters = models.View(e_tag=e_tag, display_name=display_name, scope=scope, chart=chart, accumulated=accumulated, metric=metric, kpis=kpis, pivots=pivots, timeframe=timeframe, time_period=time_period, dataset=dataset)
        api_version = "2020-08-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'viewName': self._serialize.url("view_name", view_name, 'str'),
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
        body_content = self._serialize.body(_parameters, 'View')
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
            deserialized = self._deserialize('View', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('View', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/providers/Microsoft.CostManagement/views/{viewName}'}  # type: ignore

    def delete(
        self,
        view_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """The operation to delete a view.

        :param view_name: View name.
        :type view_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-01-preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'viewName': self._serialize.url("view_name", view_name, 'str'),
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
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/providers/Microsoft.CostManagement/views/{viewName}'}  # type: ignore

    def get_by_scope(
        self,
        scope,  # type: str
        view_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.View"
        """Gets the view for the defined scope by view name.

        :param scope: The scope associated with view operations. This includes
         'subscriptions/{subscriptionId}' for subscription scope,
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for
         Department scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for BillingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}'
         for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}'
         for Management Group scope,
         'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for
         External Billing Account scope and
         'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for
         External Subscription scope.
        :type scope: str
        :param view_name: View name.
        :type view_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: View, or the result of cls(response)
        :rtype: ~cost_management_client.models.View
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.View"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-01-preview"

        # Construct URL
        url = self.get_by_scope.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'viewName': self._serialize.url("view_name", view_name, 'str'),
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

        deserialized = self._deserialize('View', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_by_scope.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/views/{viewName}'}  # type: ignore

    def create_or_update_by_scope(
        self,
        scope,  # type: str
        view_name,  # type: str
        e_tag=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        view_properties_scope=None,  # type: Optional[str]
        chart=None,  # type: Optional[Union[str, "models.ChartType"]]
        accumulated=None,  # type: Optional[Union[str, "models.AccumulatedType"]]
        metric=None,  # type: Optional[Union[str, "models.MetricType"]]
        kpis=None,  # type: Optional[List["models.KpiProperties"]]
        pivots=None,  # type: Optional[List["models.PivotProperties"]]
        timeframe=None,  # type: Optional[Union[str, "models.ReportTimeframeType"]]
        time_period=None,  # type: Optional["models.ReportConfigTimePeriod"]
        dataset=None,  # type: Optional["models.ReportConfigDataset"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.View"
        """The operation to create or update a view. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

        :param scope: The scope associated with view operations. This includes
         'subscriptions/{subscriptionId}' for subscription scope,
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for
         Department scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for BillingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}'
         for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}'
         for Management Group scope,
         'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for
         External Billing Account scope and
         'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for
         External Subscription scope.
        :type scope: str
        :param view_name: View name.
        :type view_name: str
        :param e_tag: eTag of the resource. To handle concurrent update scenario, this field will be
         used to determine whether the user is updating the latest version or not.
        :type e_tag: str
        :param display_name: User input name of the view. Required.
        :type display_name: str
        :param view_properties_scope: Cost Management scope to save the view on. This includes
         'subscriptions/{subscriptionId}' for subscription scope,
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for
         Department scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for BillingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}'
         for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}'
         for Management Group scope,
         '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for
         ExternalBillingAccount scope, and
         '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for
         ExternalSubscription scope.
        :type view_properties_scope: str
        :param chart: Chart type of the main view in Cost Analysis. Required.
        :type chart: str or ~cost_management_client.models.ChartType
        :param accumulated: Show costs accumulated over time.
        :type accumulated: str or ~cost_management_client.models.AccumulatedType
        :param metric: Metric to use when displaying costs.
        :type metric: str or ~cost_management_client.models.MetricType
        :param kpis: List of KPIs to show in Cost Analysis UI.
        :type kpis: list[~cost_management_client.models.KpiProperties]
        :param pivots: Configuration of 3 sub-views in the Cost Analysis UI.
        :type pivots: list[~cost_management_client.models.PivotProperties]
        :param timeframe: The time frame for pulling data for the report. If custom, then a specific
         time period must be provided.
        :type timeframe: str or ~cost_management_client.models.ReportTimeframeType
        :param time_period: Has time period for pulling data for the report.
        :type time_period: ~cost_management_client.models.ReportConfigTimePeriod
        :param dataset: Has definition for data in this report config.
        :type dataset: ~cost_management_client.models.ReportConfigDataset
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: View, or the result of cls(response)
        :rtype: ~cost_management_client.models.View
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.View"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _parameters = models.View(e_tag=e_tag, display_name=display_name, scope=view_properties_scope, chart=chart, accumulated=accumulated, metric=metric, kpis=kpis, pivots=pivots, timeframe=timeframe, time_period=time_period, dataset=dataset)
        api_version = "2020-08-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update_by_scope.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'viewName': self._serialize.url("view_name", view_name, 'str'),
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
        body_content = self._serialize.body(_parameters, 'View')
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
            deserialized = self._deserialize('View', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('View', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update_by_scope.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/views/{viewName}'}  # type: ignore

    def delete_by_scope(
        self,
        scope,  # type: str
        view_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """The operation to delete a view.

        :param scope: The scope associated with view operations. This includes
         'subscriptions/{subscriptionId}' for subscription scope,
         'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for
         Department scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for BillingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}'
         for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}'
         for Management Group scope,
         'providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for
         External Billing Account scope and
         'providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for
         External Subscription scope.
        :type scope: str
        :param view_name: View name.
        :type view_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-08-01-preview"

        # Construct URL
        url = self.delete_by_scope.metadata['url']  # type: ignore
        path_format_arguments = {
            'scope': self._serialize.url("scope", scope, 'str'),
            'viewName': self._serialize.url("view_name", view_name, 'str'),
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
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_by_scope.metadata = {'url': '/{scope}/providers/Microsoft.CostManagement/views/{viewName}'}  # type: ignore
