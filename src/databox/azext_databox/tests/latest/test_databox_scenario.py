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
from azure.cli.testsdk import StorageAccountPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    pass


# EXAMPLE: JobsCreate
@try_manual
def step_jobscreate(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job create '
             '--name "{myJob}" '
             '--location "westus" '
             '--transfer-type "ImportToAzure" '
             '--details "{{\\"contactDetails\\":{{\\"contactName\\":\\"Public SDK Test\\",\\"emailList\\":[\\"testing@m'
             'icrosoft.com\\"],\\"phone\\":\\"1234567890\\",\\"phoneExtension\\":\\"1234\\"}},\\"dataImportDetails\\":['
             '{{\\"accountDetails\\":{{\\"dataAccountType\\":\\"StorageAccount\\",\\"storageAccountId\\":\\"/subscripti'
             'ons/{subscription_id}/resourcegroups/{rg_4}/providers/Microsoft.Storage/storageAccounts/{sa}\\"}}}}],\\"j'
             'obDetailsType\\":\\"DataBox\\",\\"shippingAddress\\":{{\\"addressType\\":\\"Commercial\\",\\"city\\":\\"S'
             'an Francisco\\",\\"companyName\\":\\"Microsoft\\",\\"country\\":\\"US\\",\\"postalCode\\":\\"94107\\",\\"'
             'stateOrProvince\\":\\"CA\\",\\"streetAddress1\\":\\"16 TOWNSEND ST\\",\\"streetAddress2\\":\\"Unit '
             '1\\"}}}}" '
             '--sku name="DataBox" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myJob}", case_sensitive=False),
                 test.check("location", "westus", case_sensitive=False),
                 test.check("transferType", "ImportToAzure", case_sensitive=False),
                 test.check("sku.name", "DataBox", case_sensitive=False),
             ])


# EXAMPLE: JobsGet5
@try_manual
def step_jobsget5(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: JobsGet4
@try_manual
def step_jobsget4(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: JobsGet3
@try_manual
def step_jobsget3(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: JobsGet2
@try_manual
def step_jobsget2(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: JobsGet1
@try_manual
def step_jobsget1(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: JobsGet
@try_manual
def step_jobsget(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job show '
             '--expand "details" '
             '--name "{myJob}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myJob}", case_sensitive=False),
                 test.check("location", "westus", case_sensitive=False),
                 test.check("transferType", "ImportToAzure", case_sensitive=False),
                 test.check("sku.name", "DataBox", case_sensitive=False),
             ])


# EXAMPLE: JobsListByResourceGroup
@try_manual
def step_jobslistbyresourcegroup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job list '
             '--resource-group "{rg}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: JobsList
@try_manual
def step_jobslist(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job list '
             '-g ""',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: OperationsGet
@try_manual
def step_operationsget(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: ServiceValidateInputsByResourceGroup
@try_manual
def step_servicevalidateinputsbyresourcegroup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: AvailableSkusByResourceGroup
@try_manual
def step_availableskusbyresourcegroup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: BookShipmentPickupPost
@try_manual
def step_bookshipmentpickuppost(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job book-shipment-pick-up '
             '--name "{myJob5}" '
             '--resource-group "{rg_8}" '
             '--end-time "2019-09-22T18:30:00Z" '
             '--shipment-location "Front desk" '
             '--start-time "2019-09-20T18:30:00Z"',
             checks=[])


# EXAMPLE: JobsListCredentials
@try_manual
def step_jobslistcredentials(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job list-credentials '
             '--name "{myJob5}" '
             '--resource-group "{rg_8}"',
             checks=[])


# EXAMPLE: JobsCancelPost
@try_manual
def step_jobscancelpost(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job cancel '
             '--reason "CancelTest" '
             '--name "{myJob}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: JobsPatch
@try_manual
def step_jobspatch(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job update '
             '--name "{myJob}" '
             '--details "{{\\"contactDetails\\":{{\\"contactName\\":\\"Update Job\\",\\"emailList\\":[\\"testing@micros'
             'oft.com\\"],\\"phone\\":\\"1234567890\\",\\"phoneExtension\\":\\"1234\\"}},\\"shippingAddress\\":{{\\"add'
             'ressType\\":\\"Commercial\\",\\"city\\":\\"San Francisco\\",\\"companyName\\":\\"Microsoft\\",\\"country'
             '\\":\\"US\\",\\"postalCode\\":\\"94107\\",\\"stateOrProvince\\":\\"CA\\",\\"streetAddress1\\":\\"16 '
             'TOWNSEND ST\\",\\"streetAddress2\\":\\"Unit 1\\"}}}}" '
             '--resource-group "{rg}"',
             checks=[
                 test.check("name", "{myJob}", case_sensitive=False),
             ])


# EXAMPLE: ServiceRegionConfiguration
@try_manual
def step_serviceregionconfiguration(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: ValidateAddressPost
@try_manual
def step_validateaddresspost(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox service validate-address '
             '--location "westus" '
             '--device-type "DataBox" '
             '--shipping-address address-type="Commercial" city="San Francisco" company-name="Microsoft" country="US" '
             'postal-code="94107" state-or-province="CA" street-address1="16 TOWNSEND ST" street-address2="Unit 1" '
             '--validation-type "ValidateAddress"',
             checks=[])


# EXAMPLE: ServiceValidateInputs
@try_manual
def step_servicevalidateinputs(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    # EXAMPLE NOT FOUND!
    pass


# EXAMPLE: AvailableSkusPost
@try_manual
def step_availableskuspost(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox service list-available-sku-by-resource-group '
             '--country "US" '
             '--available-sku-request-location "westus" '
             '--transfer-type "ImportToAzure" '
             '--location "westus" '
             '--resource-group "{rg_8}"',
             checks=[])


# EXAMPLE: JobsDelete
@try_manual
def step_jobsdelete(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    test.cmd('az databox job delete -y '
             '--name "{myJob}" '
             '--resource-group "{rg}"',
             checks=[])


@try_manual
def cleanup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    pass


@try_manual
def call_scenario(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):
    setup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobscreate(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobsget5(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobsget4(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobsget3(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobsget2(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobsget1(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobsget(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobslistbyresourcegroup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobslist(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_operationsget(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_servicevalidateinputsbyresourcegroup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_availableskusbyresourcegroup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_bookshipmentpickuppost(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobslistcredentials(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobscancelpost(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobspatch(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_serviceregionconfiguration(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_validateaddresspost(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_servicevalidateinputs(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_availableskuspost(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    step_jobsdelete(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
    cleanup(test, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)


@try_manual
class DataBoxManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestdatabox_databoxbvt'[:7], key='rg_4', parameter_name='rg_4')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_databoxbvt1'[:7], key='rg_5', parameter_name='rg_5')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_akvenkat'[:7], key='rg_7', parameter_name='rg_7')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_SdkRg5154'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_SdkRg7937'[:7], key='rg_2', parameter_name='rg_2')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_SdkRg8091'[:7], key='rg_3', parameter_name='rg_3')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_SdkRg7478'[:7], key='rg_6', parameter_name='rg_6')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_bvttoolrg6'[:7], key='rg_8', parameter_name='rg_8')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_SdkRg4981'[:7], key='rg_9', parameter_name='rg_9')
    @ResourceGroupPreparer(name_prefix='clitestdatabox_SdkRg6861'[:7], key='rg_10', parameter_name='rg_10')
    @StorageAccountPreparer(name_prefix='clitestdatabox_databoxbvttestaccount'[:7], key='sa',
                            resource_group_parameter_name='rg_4')
    @StorageAccountPreparer(name_prefix='clitestdatabox_databoxbvttestaccount2'[:7], key='sa_2',
                            resource_group_parameter_name='rg_5')
    @StorageAccountPreparer(name_prefix='clitestdatabox_aaaaaa2'[:7], key='sa_3',
                            resource_group_parameter_name='rg_7')
    def test_databox(self, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myJob': 'SdkJob952',
            'myJob2': 'SdkJob1735',
            'myJob3': 'SdkJob6429',
            'myJob4': 'SdkJob9640',
            'myJob5': 'TJ-636646322037905056',
        })

        call_scenario(self, rg_4, rg_5, rg_7, rg, rg_2, rg_3, rg_6, rg_8, rg_9, rg_10)
        calc_coverage(__file__)
        raise_if()
