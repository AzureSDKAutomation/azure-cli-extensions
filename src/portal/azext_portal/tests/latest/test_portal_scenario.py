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
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: /Dashboards/put/Create or update a Dashboard
@try_manual
def step__dashboards_put_create_or_update_a_dashboard(test, rg):
    test.cmd('az portal dashboard create '
             '--location "eastus" '
             '--lenses "{{\\"aLens\\":{{\\"order\\":1,\\"parts\\":{{\\"aPart\\":{{\\"position\\":{{\\"colSpan\\":3,\\"r'
             'owSpan\\":4,\\"x\\":1,\\"y\\":2}}}},\\"bPart\\":{{\\"position\\":{{\\"colSpan\\":6,\\"rowSpan\\":6,\\"x\\'
             '":5,\\"y\\":5}}}}}}}},\\"bLens\\":{{\\"order\\":2,\\"parts\\":{{}}}}}}" '
             '--metadata "{{\\"metadata\\":{{\\"ColSpan\\":2,\\"RowSpan\\":1,\\"X\\":4,\\"Y\\":3}}}}" '
             '--tags aKey="aValue" anotherKey="anotherValue" '
             '--dashboard-name "{testDashboard}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Dashboards/get/Get a Dashboard
@try_manual
def step__dashboards_get_get_a_dashboard(test, rg):
    test.cmd('az portal dashboard show '
             '--dashboard-name "{testDashboard}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Dashboards/get/List all custom resource providers on the resourceGroup
@try_manual
def step__dashboards_get_list_all_custom_resource_providers_on_the_resourcegroup(test, rg):
    test.cmd('az portal dashboard list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Dashboards/get/List all custom resource providers on the subscription
@try_manual
def step__dashboards_get_list_all_custom_resource_providers_on_the_subscription(test, rg):
    test.cmd('az portal dashboard list',
             checks=[])


# EXAMPLE: /Dashboards/patch/Update a Dashboard
@try_manual
def step__dashboards_patch_update_a_dashboard(test, rg):
    test.cmd('az portal dashboard update '
             '--tags aKey="bValue" anotherKey="anotherValue2" '
             '--dashboard-name "{testDashboard}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Dashboards/delete/Delete a Dashboard
@try_manual
def step__dashboards_delete_delete_a_dashboard(test, rg):
    test.cmd('az portal dashboard delete '
             '--dashboard-name "{testDashboard}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


class PortalScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestportal_testRG'[:7], key='rg', parameter_name='rg')
    def test_portal(self, rg):

        self.kwargs.update({
            'testDashboard': self.create_random_name(prefix='clitestdashboards'[:7], length=24),
        })

        setup(self, rg)
        step__dashboards_put_create_or_update_a_dashboard(self, rg)
        step__dashboards_get_get_a_dashboard(self, rg)
        step__dashboards_get_list_all_custom_resource_providers_on_the_resourcegroup(self, rg)
        step__dashboards_get_list_all_custom_resource_providers_on_the_subscription(self, rg)
        step__dashboards_patch_update_a_dashboard(self, rg)
        step__dashboards_delete_delete_a_dashboard(self, rg)
        cleanup(self, rg)
