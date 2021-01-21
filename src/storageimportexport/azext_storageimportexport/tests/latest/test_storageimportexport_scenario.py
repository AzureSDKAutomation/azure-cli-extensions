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
from .example_steps import step_location_show
from .example_steps import step_bit_locker_key_list
from .example_steps import step_job_list
from .example_steps import step_job_list2
from .example_steps import step_location_list
from .example_steps import step_job_delete
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
    # STEP NOT FOUND: /Jobs/put/Create job
    # STEP NOT FOUND: /Jobs/get/Get job
    step_location_show(test, rg, checks=[])
    step_bit_locker_key_list(test, rg, checks=[])
    step_job_list(test, rg, checks=[])
    step_job_list2(test, rg, checks=[
        test.check('length(@)', 1),
    ])
    step_location_list(test, rg, checks=[])
    # STEP NOT FOUND: /Jobs/patch/Update job
    step_job_delete(test, rg, checks=[])
    cleanup_scenario(test, rg)


# Test class for Scenario
@try_manual
class StorageimportexportScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(StorageimportexportScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myLocation': 'West US',
            'myJob': 'myJob',
            'myJob2': 'myExportJob',
        })


    @ResourceGroupPreparer(name_prefix='cliteststorageimportexport_myResourceGroup'[:7], key='rg',
                           parameter_name='rg')
    @StorageAccountPreparer(name_prefix='cliteststorageimportexport_test'[:7], key='sa',
                            resource_group_parameter_name='rg')
    def test_storageimportexport_Scenario(self, rg):
        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()

