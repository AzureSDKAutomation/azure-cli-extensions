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
from .example_steps import step_service_create
from .example_steps import step_service_list
from .example_steps import step_service_list2
from .example_steps import step_service_show
from .example_steps import step_service_update
from .example_steps import step_service_check_device
from .example_steps import step_service_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg, rg_2, rg_3, rg_4):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg, rg_2, rg_3, rg_4):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg, rg_2, rg_3, rg_4):
    setup_scenario(test, rg, rg_2, rg_3, rg_4)
    step_service_create(test, rg, rg_2, rg_3, rg_4, checks=[])
    step_service_list(test, rg, rg_2, rg_3, rg_4, checks=[])
    step_service_list2(test, rg, rg_2, rg_3, rg_4, checks=[])
    step_service_show(test, rg, rg_2, rg_3, rg_4, checks=[])
    step_service_update(test, rg, rg_2, rg_3, rg_4, checks=[])
    step_service_check_device(test, rg, rg_2, rg_3, rg_4, checks=[])
    step_service_delete(test, rg, rg_2, rg_3, rg_4, checks=[])
    cleanup_scenario(test, rg, rg_2, rg_3, rg_4)


# Test class for Scenario
@try_manual
class WindowsiotservicesScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(WindowsiotservicesScenarioTest, self).__init__(*args, **kwargs)


    @ResourceGroupPreparer(name_prefix='clitestwindowsiotservices_res6117'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestwindowsiotservices_res9407'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestwindowsiotservices_res9101'[:7], key='rg_3', parameter_name='rg_3')
    @ResourceGroupPreparer(name_prefix='clitestwindowsiotservices_res4228'[:7], key='rg_4', parameter_name='rg_4')
    def test_windowsiotservices_Scenario(self, rg, rg_2, rg_3, rg_4):
        call_scenario(self, rg, rg_2, rg_3, rg_4)
        calc_coverage(__file__)
        raise_if()

