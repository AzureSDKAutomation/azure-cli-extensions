# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from azure.cli.testsdk import StorageAccountPreparer
from .example_steps import step_alert_list
from .example_steps import step_alert_list2
from .example_steps import step_alert_list3
from .example_steps import step_alert_list4
from .example_steps import step_alert_list_external
from .example_steps import step_alert_list_external2
from .example_steps import step_alert_list5
from .example_steps import step_alert_list6
from .example_steps import step_alert_list7
from .example_steps import step_alert_dismiss
from .example_steps import step_alert_dismiss2
from .example_steps import step_dimension_list
from .example_steps import step_dimension_list2
from .example_steps import step_dimension_list3
from .example_steps import step_dimension_list4
from .example_steps import step_dimension_list5
from .example_steps import step_dimension_list6
from .example_steps import step_dimension_list7
from .example_steps import step_dimension_list8
from .example_steps import step_dimension_list9
from .example_steps import step_dimension_list10
from .example_steps import step_dimension_list11
from .example_steps import step_dimension_list12
from .example_steps import step_dimension_list13
from .example_steps import step_dimension_list14
from .example_steps import step_dimension_list15
from .example_steps import step_dimension_list16
from .example_steps import step_dimension_list17
from .example_steps import step_dimension_list18
from .example_steps import step_dimension_by_external_cloud_provider_type
from .example_steps import step_dimension_by_external_cloud_provider_type2
from .example_steps import step_dimension_list19
from .example_steps import step_dimension_list20
from .example_steps import step_dimension_list21
from .example_steps import step_dimension_list22
from .example_steps import step_dimension_list23
from .example_steps import step_dimension_list24
from .example_steps import step_dimension_list25
from .example_steps import step_dimension_list26
from .example_steps import step_export_create
from .example_steps import step_export_create2
from .example_steps import step_export_create3
from .example_steps import step_export_create4
from .example_steps import step_export_create5
from .example_steps import step_export_create6
from .example_steps import step_export_show
from .example_steps import step_export_show2
from .example_steps import step_export_show3
from .example_steps import step_export_show4
from .example_steps import step_export_show5
from .example_steps import step_export_show6
from .example_steps import step_export_show_execution_history
from .example_steps import step_export_show_execution_history2
from .example_steps import step_export_show_execution_history3
from .example_steps import step_export_show_execution_history4
from .example_steps import step_export_show_execution_history5
from .example_steps import step_export_show_execution_history6
from .example_steps import step_export_list
from .example_steps import step_export_list2
from .example_steps import step_export_list3
from .example_steps import step_export_list4
from .example_steps import step_export_list5
from .example_steps import step_export_list6
from .example_steps import step_export_execute
from .example_steps import step_export_execute2
from .example_steps import step_export_execute3
from .example_steps import step_export_execute4
from .example_steps import step_export_execute5
from .example_steps import step_export_execute6
from .example_steps import step_export_delete
from .example_steps import step_export_delete2
from .example_steps import step_export_delete3
from .example_steps import step_export_delete4
from .example_steps import step_export_delete5
from .example_steps import step_export_delete6
from .example_steps import step_forecast_usage
from .example_steps import step_forecast_usage2
from .example_steps import step_forecast_usage3
from .example_steps import step_forecast_usage4
from .example_steps import step_forecast_external_cloud_provider_usage
from .example_steps import step_forecast_external_cloud_provider_usage2
from .example_steps import step_forecast_usage5
from .example_steps import step_forecast_usage6
from .example_steps import step_forecast_usage7
from .example_steps import step_generate_detailed_cost
from .example_steps import step_generate_detailed_cost2
from .example_steps import step_generate_detailed_cost3
from .example_steps import step_generate_detailed_cost4
from .example_steps import step_generate_detailed_cost5
from .example_steps import step_generate_detailed_cost6
from .example_steps import step_generate_detailed_cost7
from .example_steps import step_query_usage
from .example_steps import step_query_usage2
from .example_steps import step_query_usage3
from .example_steps import step_query_usage4
from .example_steps import step_query_usage5
from .example_steps import step_query_usage6
from .example_steps import step_query_usage7
from .example_steps import step_query_usage8
from .example_steps import step_query_usage9
from .example_steps import step_query_usage10
from .example_steps import step_query_usage11
from .example_steps import step_query_usage12
from .example_steps import step_query_usage_by_external_cloud_provider_type
from .example_steps import step_query_usage_by_external_cloud_provider_type2
from .example_steps import step_query_usage13
from .example_steps import step_query_usage14
from .example_steps import step_query_usage15
from .example_steps import step_query_usage16
from .example_steps import step_query_usage17
from .example_steps import step_query_usage18
from .example_steps import step_query_usage19
from .example_steps import step_query_usage20
from .example_steps import step_view_create
from .example_steps import step_view_create2
from .example_steps import step_view_show
from .example_steps import step_view_list
from .example_steps import step_view_show2
from .example_steps import step_view_list2
from .example_steps import step_view_delete
from .example_steps import step_view_delete2
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg):
    setup_scenario(test, rg)
    step_alert_list(test, rg, checks=[])
    step_alert_list2(test, rg, checks=[])
    step_alert_list3(test, rg, checks=[])
    step_alert_list4(test, rg, checks=[])
    step_alert_list_external(test, rg, checks=[])
    step_alert_list_external2(test, rg, checks=[])
    step_alert_list5(test, rg, checks=[])
    step_alert_list6(test, rg, checks=[])
    step_alert_list6(test, rg, checks=[])
    step_alert_list7(test, rg, checks=[])
    step_alert_list7(test, rg, checks=[])
    step_alert_dismiss(test, rg, checks=[])
    step_alert_dismiss2(test, rg, checks=[])
    step_dimension_list(test, rg, checks=[])
    step_dimension_list2(test, rg, checks=[])
    step_dimension_list3(test, rg, checks=[])
    step_dimension_list4(test, rg, checks=[])
    step_dimension_list5(test, rg, checks=[])
    step_dimension_list6(test, rg, checks=[])
    step_dimension_list7(test, rg, checks=[])
    step_dimension_list8(test, rg, checks=[])
    step_dimension_list9(test, rg, checks=[])
    step_dimension_list10(test, rg, checks=[])
    step_dimension_list11(test, rg, checks=[])
    step_dimension_list12(test, rg, checks=[])
    step_dimension_list13(test, rg, checks=[])
    step_dimension_list14(test, rg, checks=[])
    step_dimension_list15(test, rg, checks=[])
    step_dimension_list16(test, rg, checks=[])
    step_dimension_list17(test, rg, checks=[])
    step_dimension_list18(test, rg, checks=[])
    step_dimension_by_external_cloud_provider_type(test, rg, checks=[])
    step_dimension_by_external_cloud_provider_type2(test, rg, checks=[])
    step_dimension_list19(test, rg, checks=[])
    step_dimension_list20(test, rg, checks=[])
    step_dimension_list21(test, rg, checks=[])
    step_dimension_list22(test, rg, checks=[])
    step_dimension_list23(test, rg, checks=[])
    step_dimension_list24(test, rg, checks=[])
    step_dimension_list25(test, rg, checks=[])
    step_dimension_list26(test, rg, checks=[])
    step_export_create(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("definition.timeframe", "MonthToDate", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
        test.check("schedule.recurrence", "Weekly", case_sensitive=False),
        test.check("schedule.recurrencePeriod.from", "2020-06-01T00:00:00Z", case_sensitive=False),
        test.check("schedule.recurrencePeriod.to", "2020-10-31T00:00:00Z", case_sensitive=False),
        test.check("schedule.status", "Active", case_sensitive=False),
    ])
    step_export_create2(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("definition.timeframe", "MonthToDate", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
        test.check("schedule.recurrence", "Weekly", case_sensitive=False),
        test.check("schedule.recurrencePeriod.from", "2020-06-01T00:00:00Z", case_sensitive=False),
        test.check("schedule.recurrencePeriod.to", "2020-10-31T00:00:00Z", case_sensitive=False),
        test.check("schedule.status", "Active", case_sensitive=False),
    ])
    step_export_create3(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("definition.timeframe", "MonthToDate", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
        test.check("schedule.recurrence", "Weekly", case_sensitive=False),
        test.check("schedule.recurrencePeriod.from", "2020-06-01T00:00:00Z", case_sensitive=False),
        test.check("schedule.recurrencePeriod.to", "2020-10-31T00:00:00Z", case_sensitive=False),
        test.check("schedule.status", "Active", case_sensitive=False),
    ])
    step_export_create4(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("definition.timeframe", "MonthToDate", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
        test.check("schedule.recurrence", "Weekly", case_sensitive=False),
        test.check("schedule.recurrencePeriod.from", "2020-06-01T00:00:00Z", case_sensitive=False),
        test.check("schedule.recurrencePeriod.to", "2020-10-31T00:00:00Z", case_sensitive=False),
        test.check("schedule.status", "Active", case_sensitive=False),
    ])
    step_export_create5(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("definition.timeframe", "MonthToDate", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
        test.check("schedule.recurrence", "Weekly", case_sensitive=False),
        test.check("schedule.recurrencePeriod.from", "2020-06-01T00:00:00Z", case_sensitive=False),
        test.check("schedule.recurrencePeriod.to", "2020-10-31T00:00:00Z", case_sensitive=False),
        test.check("schedule.status", "Active", case_sensitive=False),
    ])
    step_export_create6(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("definition.timeframe", "MonthToDate", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
        test.check("schedule.recurrence", "Weekly", case_sensitive=False),
        test.check("schedule.recurrencePeriod.from", "2020-06-01T00:00:00Z", case_sensitive=False),
        test.check("schedule.recurrencePeriod.to", "2020-10-31T00:00:00Z", case_sensitive=False),
        test.check("schedule.status", "Active", case_sensitive=False),
    ])
    step_export_show(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
    ])
    step_export_show2(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
    ])
    step_export_show3(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
    ])
    step_export_show4(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
    ])
    step_export_show5(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
    ])
    step_export_show6(test, rg, checks=[
        test.check("name", "{myExport}", case_sensitive=False),
        test.check("definition.type", "ActualCost", case_sensitive=False),
        test.check("deliveryInfo.destination.container", "exports", case_sensitive=False),
        test.check("deliveryInfo.destination.resourceId", "/subscriptions/{subscription_id}/resourceGroups/{rg}/provide"
                   "rs/Microsoft.Storage/storageAccounts/{sa}", case_sensitive=False),
        test.check("deliveryInfo.destination.rootFolderPath", "ad-hoc", case_sensitive=False),
    ])
    step_export_show_execution_history(test, rg, checks=[])
    step_export_show_execution_history2(test, rg, checks=[])
    step_export_show_execution_history3(test, rg, checks=[])
    step_export_show_execution_history4(test, rg, checks=[])
    step_export_show_execution_history5(test, rg, checks=[])
    step_export_show_execution_history6(test, rg, checks=[])
    step_export_list(test, rg, checks=[])
    step_export_list2(test, rg, checks=[])
    step_export_list3(test, rg, checks=[])
    step_export_list4(test, rg, checks=[])
    step_export_list5(test, rg, checks=[])
    step_export_list6(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_export_execute(test, rg, checks=[])
    step_export_execute2(test, rg, checks=[])
    step_export_execute3(test, rg, checks=[])
    step_export_execute4(test, rg, checks=[])
    step_export_execute5(test, rg, checks=[])
    step_export_execute6(test, rg, checks=[])
    step_export_delete(test, rg, checks=[])
    step_export_delete2(test, rg, checks=[])
    step_export_delete3(test, rg, checks=[])
    step_export_delete4(test, rg, checks=[])
    step_export_delete5(test, rg, checks=[])
    step_export_delete6(test, rg, checks=[])
    step_forecast_usage(test, rg, checks=[])
    step_forecast_usage2(test, rg, checks=[])
    step_forecast_usage3(test, rg, checks=[])
    step_forecast_usage4(test, rg, checks=[])
    step_forecast_external_cloud_provider_usage(test, rg, checks=[])
    step_forecast_external_cloud_provider_usage2(test, rg, checks=[])
    step_forecast_usage5(test, rg, checks=[])
    step_forecast_usage6(test, rg, checks=[])
    step_forecast_usage7(test, rg, checks=[])
    step_generate_detailed_cost(test, rg, checks=[])
    step_generate_detailed_cost2(test, rg, checks=[])
    step_generate_detailed_cost3(test, rg, checks=[])
    step_generate_detailed_cost4(test, rg, checks=[])
    step_generate_detailed_cost5(test, rg, checks=[])
    step_generate_detailed_cost6(test, rg, checks=[])
    step_generate_detailed_cost7(test, rg, checks=[])
    step_query_usage(test, rg, checks=[])
    step_query_usage2(test, rg, checks=[])
    step_query_usage3(test, rg, checks=[])
    step_query_usage4(test, rg, checks=[])
    step_query_usage5(test, rg, checks=[])
    step_query_usage6(test, rg, checks=[])
    step_query_usage7(test, rg, checks=[])
    step_query_usage8(test, rg, checks=[])
    step_query_usage9(test, rg, checks=[])
    step_query_usage10(test, rg, checks=[])
    step_query_usage11(test, rg, checks=[])
    step_query_usage12(test, rg, checks=[])
    step_query_usage_by_external_cloud_provider_type(test, rg, checks=[])
    step_query_usage_by_external_cloud_provider_type2(test, rg, checks=[])
    step_query_usage13(test, rg, checks=[])
    step_query_usage14(test, rg, checks=[])
    step_query_usage15(test, rg, checks=[])
    step_query_usage16(test, rg, checks=[])
    step_query_usage17(test, rg, checks=[])
    step_query_usage18(test, rg, checks=[])
    step_query_usage19(test, rg, checks=[])
    step_query_usage20(test, rg, checks=[])
    step_view_create(test, rg, checks=[
        test.check("accumulated", "true", case_sensitive=False),
        test.check("chart", "Table", case_sensitive=False),
        test.check("displayName", "swagger Example", case_sensitive=False),
        test.check("metric", "ActualCost", case_sensitive=False),
        test.check("query..dataset.aggregation.totalCost.name", "PreTaxCost", case_sensitive=False),
        test.check("query..dataset.aggregation.totalCost.function", "Sum", case_sensitive=False),
        test.check("query..dataset.granularity", "Daily", case_sensitive=False),
        test.check("query.timeframe", "MonthToDate", case_sensitive=False),
        test.check("name", "{myView}", case_sensitive=False),
    ])
    step_view_create2(test, rg, checks=[
        test.check("accumulated", "true", case_sensitive=False),
        test.check("chart", "Table", case_sensitive=False),
        test.check("displayName", "swagger Example", case_sensitive=False),
        test.check("metric", "ActualCost", case_sensitive=False),
        test.check("query..dataset.aggregation.totalCost.name", "PreTaxCost", case_sensitive=False),
        test.check("query..dataset.aggregation.totalCost.function", "Sum", case_sensitive=False),
        test.check("query..dataset.granularity", "Daily", case_sensitive=False),
        test.check("query.timeframe", "MonthToDate", case_sensitive=False),
        test.check("name", "{myView}", case_sensitive=False),
    ])
    step_view_show(test, rg, checks=[
        test.check("eTag", "\"1d4ff9fe66f1d10\"", case_sensitive=False),
        test.check("accumulated", "true", case_sensitive=False),
        test.check("chart", "Table", case_sensitive=False),
        test.check("displayName", "swagger Example", case_sensitive=False),
        test.check("metric", "ActualCost", case_sensitive=False),
        test.check("query..dataset.aggregation.totalCost.name", "PreTaxCost", case_sensitive=False),
        test.check("query..dataset.aggregation.totalCost.function", "Sum", case_sensitive=False),
        test.check("query..dataset.granularity", "Daily", case_sensitive=False),
        test.check("query.timeframe", "MonthToDate", case_sensitive=False),
        test.check("name", "{myView}", case_sensitive=False),
    ])
    step_view_list(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_view_show2(test, rg, checks=[
        test.check("eTag", "\"1d4ff9fe66f1d10\"", case_sensitive=False),
        test.check("accumulated", "true", case_sensitive=False),
        test.check("chart", "Table", case_sensitive=False),
        test.check("displayName", "swagger Example", case_sensitive=False),
        test.check("metric", "ActualCost", case_sensitive=False),
        test.check("query..dataset.aggregation.totalCost.name", "PreTaxCost", case_sensitive=False),
        test.check("query..dataset.aggregation.totalCost.function", "Sum", case_sensitive=False),
        test.check("query..dataset.granularity", "Daily", case_sensitive=False),
        test.check("query.timeframe", "MonthToDate", case_sensitive=False),
        test.check("name", "{myView}", case_sensitive=False),
    ])
    step_view_list2(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_view_delete(test, rg, checks=[])
    step_view_delete2(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class CostmanagementScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(CostmanagementScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myExport': 'TestExport',
            'myView': 'swaggerExample',
            'myView2': 'TestView',
        })


    @ResourceGroupPreparer(name_prefix='clitestcostmanagement_MYDEVTESTRG'[:7], key='rg', parameter_name='rg')
    @StorageAccountPreparer(name_prefix='clitestcostmanagement_ccmeastusdiag182'[:7], key='sa',
                            resource_group_parameter_name='rg')
    def test_costmanagement_Scenario(self, rg):
        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

