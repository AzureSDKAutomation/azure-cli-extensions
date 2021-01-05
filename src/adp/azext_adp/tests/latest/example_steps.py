# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


from .. import try_manual


# EXAMPLE: /Accounts/put/Put account
@try_manual
def step_account_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp account create '
             '--name "{myAccount}" '
             '--location "Global" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az adp account wait --created '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Accounts/get/Get account
@try_manual
def step_account_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp account show '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Accounts/get/List accounts
@try_manual
def step_account_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp account list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Accounts/get/List accounts by resource group
@try_manual
def step_account_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp account list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Accounts/patch/Patch account
@try_manual
def step_account_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp account update '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DataPools/put/Put Data Pool
@try_manual
def step_data_pool_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp data-pool create '
             '--account-name "{myAccount}" '
             '--name "{myDataPool}" '
             '--locations name="westus" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az adp data-pool wait --created '
             '--name "{myDataPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DataPools/get/Get Data Pool
@try_manual
def step_data_pool_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp data-pool show '
             '--account-name "{myAccount}" '
             '--name "{myDataPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DataPools/get/List Data Pools
@try_manual
def step_data_pool_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp data-pool list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DataPools/patch/Patch Data Pool
@try_manual
def step_data_pool_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp data-pool update '
             '--account-name "{myAccount}" '
             '--name "{myDataPool}" '
             '--locations name="westus" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DataPools/delete/Delete Data Pool
@try_manual
def step_data_pool_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp data-pool delete -y '
             '--account-name "{myAccount}" '
             '--name "{myDataPool}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Accounts/delete/Delete account
@try_manual
def step_account_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az adp account delete -y '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)

