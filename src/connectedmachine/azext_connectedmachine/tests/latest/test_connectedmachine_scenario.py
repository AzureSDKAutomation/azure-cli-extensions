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
from .. import try_manual, raise_if, calc_coverage
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup
@try_manual
def setup(test, rg):
    pass


# EXAMPLE: /MachineExtensions/put/Create or Update a Machine Extension (PUT)
@try_manual
def step__machineextensions_put(test, rg):
    test.cmd('az connectedmachine extension create '
             '--machine-name "myMachine" '
             '--n "CustomScriptExtension" '
             '--location "eastus2euap" '
             '--type "CustomScriptExtension" '
             '--publisher "Microsoft.Compute" '
             '--settings "{{\\"commandToExecute\\":\\"powershell.exe -c \\\\\\"Get-Process | Where-Object {{ $_.CPU '
             '-gt 10000 }}\\\\\\"\\"}}" '
             '--type-handler-version "1.10" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /MachineExtensions/get/Get all Machine Extensions
@try_manual
def step__machineextensions_get(test, rg):
    test.cmd('az connectedmachine extension list '
             '--machine-name "myMachine" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /MachineExtensions/get/Get Machine Extension
@try_manual
def step__machineextensions_get_get_machine_extension(test, rg):
    test.cmd('az connectedmachine extension show '
             '--machine-name "myMachine" '
             '--n "CustomScriptExtension" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /MachineExtensions/patch/Create or Update a Machine Extension (PATCH)
@try_manual
def step__machineextensions_patch(test, rg):
    test.cmd('az connectedmachine extension update '
             '--machine-name "myMachine" '
             '--n "CustomScriptExtension" '
             '--type "CustomScriptExtension" '
             '--publisher "Microsoft.Compute" '
             '--settings "{{\\"commandToExecute\\":\\"powershell.exe -c \\\\\\"Get-Process | Where-Object {{ $_.CPU '
             '-lt 100 }}\\\\\\"\\"}}" '
             '--type-handler-version "1.10" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /MachineExtensions/delete/Delete a Machine Extension
@try_manual
def step__machineextensions_delete(test, rg):
    test.cmd('az connectedmachine extension delete -y '
             '--machine-name "myMachine" '
             '--n "MMA" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Machines/get/Get Machine
@try_manual
def step__machines_get_get_machine(test, rg):
    test.cmd('az connectedmachine show '
             '--name "myMachine" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Machines/get/List Machines by resource group
@try_manual
def step__machines_get_list_machines_by_resource_group(test, rg):
    test.cmd('az connectedmachine list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Machines/get/List Machines by subscription
@try_manual
def step__machines_get_list_machines_by_subscription(test, rg):
    test.cmd('az connectedmachine list '
             '-g ""',
             checks=[])


# EXAMPLE: /Machines/delete/Delete a Machine
@try_manual
def step__machines_delete_delete_a_machine(test, rg):
    test.cmd('az connectedmachine delete -y '
             '--name "myMachine" '
             '--resource-group "{rg}"',
             checks=[])


# Env cleanup
@try_manual
def cleanup(test, rg):
    pass


# Testcase
@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__machineextensions_put(test, rg)
    step__machineextensions_get(test, rg)
    step__machineextensions_get_get_machine_extension(test, rg)
    step__machineextensions_patch(test, rg)
    step__machineextensions_delete(test, rg)
    step__machines_get_get_machine(test, rg)
    step__machines_get_list_machines_by_resource_group(test, rg)
    step__machines_get_list_machines_by_subscription(test, rg)
    step__machines_delete_delete_a_machine(test, rg)
    cleanup(test, rg)


@try_manual
class ConnectedMachineScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestconnectedmachine_myResourceGroup'[:7], key='rg', parameter_name='rg')
    def test_connectedmachine(self, rg):

        call_scenario(self, rg)
        calc_coverage(__file__)
        raise_if()
