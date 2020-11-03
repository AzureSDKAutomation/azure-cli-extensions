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


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup
@try_manual
def setup(test):
    pass


# EXAMPLE: /BillingAccounts/get/BillingAccounts
@try_manual
def step__billingaccounts_get_billingaccounts(test):
    test.cmd('az billing account show '
             '--name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /BillingAccounts/get/BillingAccountsList
@try_manual
def step__billingaccounts_get_billingaccountslist(test):
    test.cmd('az billing account list',
             checks=[])


# EXAMPLE: /BillingAccounts/get/BillingAccountsListWithExpand
@try_manual
def step__billingaccounts_get(test):
    test.cmd('az billing account list '
             '--expand "soldTo,billingProfiles,billingProfiles/invoiceSections"',
             checks=[])


# EXAMPLE: /BillingAccounts/get/BillingAccountsListWithExpandForEnrollmentDetails
@try_manual
def step__billingaccounts_get2(test):
    test.cmd('az billing account list '
             '--expand "enrollmentDetails,departments,enrollmentAccounts"',
             checks=[])


# EXAMPLE: /BillingAccounts/get/BillingAccountWithExpand
@try_manual
def step__billingaccounts_get_billingaccountwithexpand(test):
    test.cmd('az billing account show '
             '--expand "soldTo,billingProfiles,billingProfiles/invoiceSections" '
             '--name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /BillingAccounts/patch/UpdateBillingAccount
@try_manual
def step__billingaccounts_patch_updatebillingaccount(test):
    test.cmd('az billing account update '
             '--name "{myBillingAccount}" '
             '--display-name "Test Account" '
             '--sold-to address-line1="Test Address 1" city="Redmond" company-name="Contoso" country="US" '
             'first-name="Test" last-name="User" postal-code="12345" region="WA"',
             checks=[
                 test.check("name", "{myBillingAccount}", case_sensitive=False),
                 test.check("displayName", "Test Account", case_sensitive=False),
                 test.check("soldTo.addressLine1", "Test Address 1", case_sensitive=False),
                 test.check("soldTo.city", "Redmond", case_sensitive=False),
                 test.check("soldTo.companyName", "Contoso", case_sensitive=False),
                 test.check("soldTo.country", "US", case_sensitive=False),
                 test.check("soldTo.firstName", "Test", case_sensitive=False),
                 test.check("soldTo.lastName", "User", case_sensitive=False),
                 test.check("soldTo.postalCode", "12345", case_sensitive=False),
                 test.check("soldTo.region", "WA", case_sensitive=False),
             ])


# EXAMPLE: /Agreements/get/AgreementByName
@try_manual
def step__agreements_get_agreementbyname(test):
    test.cmd('az billing agreement show '
             '--name "{myAgreement}" '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /Agreements/get/AgreementsListByBillingAccount
@try_manual
def step__agreements_get(test):
    test.cmd('az billing agreement list '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /BillingProfiles/put/CreateBillingProfile
@try_manual
def step__billingprofiles_put_createbillingprofile(test):
    test.cmd('az billing profile create '
             '--account-name "{myBillingAccount}" '
             '--name "{myBillingProfile}" '
             '--bill-to address-line1="Test Address 1" city="Redmond" country="US" first-name="Test" last-name="User" '
             'postal-code="12345" region="WA" '
             '--display-name "Finance" '
             '--enabled-azure-plans sku-id="0001" '
             '--enabled-azure-plans sku-id="0002" '
             '--invoice-email-opt-in true '
             '--po-number "ABC12345"',
             checks=[
                 test.check("billTo.addressLine1", "Test Address 1", case_sensitive=False),
                 test.check("billTo.city", "Redmond", case_sensitive=False),
                 test.check("billTo.country", "US", case_sensitive=False),
                 test.check("billTo.firstName", "Test", case_sensitive=False),
                 test.check("billTo.lastName", "User", case_sensitive=False),
                 test.check("billTo.postalCode", "12345", case_sensitive=False),
                 test.check("billTo.region", "WA", case_sensitive=False),
                 test.check("displayName", "Finance", case_sensitive=False),
                 test.check("invoiceEmailOptIn", True),
                 test.check("poNumber", "ABC12345", case_sensitive=False),
             ])


# EXAMPLE: /BillingProfiles/get/BillingProfile
@try_manual
def step__billingprofiles_get_billingprofile(test):
    test.cmd('az billing profile show '
             '--account-name "{myBillingAccount}" '
             '--name "{myBillingProfile}"',
             checks=[
                 test.check("name", "{myBillingProfile}", case_sensitive=False),
                 test.check("invoiceEmailOptIn", True),
                 test.check("poNumber", "ABC12345", case_sensitive=False),
             ])


# EXAMPLE: /BillingProfiles/get/BillingProfilesListByBillingAccount
@try_manual
def step__billingprofiles_get(test):
    test.cmd('az billing profile list '
             '--account-name "{myBillingAccount}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /BillingProfiles/get/BillingProfilesListWithExpand
@try_manual
def step__billingprofiles_get2(test):
    test.cmd('az billing profile list '
             '--expand "invoiceSections" '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /BillingProfiles/get/BillingProfileWithExpand
@try_manual
def step__billingprofiles_get_billingprofilewithexpand(test):
    test.cmd('az billing profile show '
             '--expand "invoiceSections" '
             '--account-name "{myBillingAccount}" '
             '--name "{myBillingProfile}"',
             checks=[
                 test.check("name", "{myBillingProfile}", case_sensitive=False),
                 test.check("invoiceEmailOptIn", True),
                 test.check("poNumber", "ABC12345", case_sensitive=False),
             ])


# EXAMPLE: /AvailableBalances/get/AvailableBalanceByBillingProfile
@try_manual
def step__availablebalances_get(test):
    test.cmd('az billing balance show '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}"',
             checks=[])


# EXAMPLE: /BillingRoleAssignments/get/InvoiceSectionRoleAssignmentList
@try_manual
def step__billingroleassignments_get(test):
    test.cmd('az billing role-assignment list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--invoice-section-name "{myInvoiceSection}"',
             checks=[])


# EXAMPLE: /BillingPermissions/get/InvoiceSectionPermissionsList
@try_manual
def step__billingpermissions_get(test):
    test.cmd('az billing permission list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--invoice-section-name "{myInvoiceSection}"',
             checks=[])


# EXAMPLE: /BillingRoleAssignments/get/BillingAccountRoleAssignmentList
@try_manual
def step__billingroleassignments_get2(test):
    test.cmd('az billing role-assignment list '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /BillingRoleAssignments/get/BillingProfileRoleAssignmentList
@try_manual
def step__billingroleassignments_get3(test):
    test.cmd('az billing role-assignment list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}"',
             checks=[])


# EXAMPLE: /BillingRoleAssignments/delete/BillingAccountRoleAssignmentDelete
@try_manual
def step__billingroleassignments_delete(test):
    test.cmd('az billing role-assignment delete -y '
             '--account-name "{myBillingAccount}" '
             '--name "{myBillingRoleAssignment}"',
             checks=[])


# EXAMPLE: /BillingRoleAssignments/delete/BillingProfileRoleAssignmentDelete
@try_manual
def step__billingroleassignments_delete2(test):
    test.cmd('az billing role-assignment delete -y '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--name "{myBillingRoleAssignment}"',
             checks=[])


# EXAMPLE: /BillingProperty/patch/UpdateBillingProperty
@try_manual
def step__billingproperty_patch_updatebillingproperty(test):
    test.cmd('az billing property update '
             '--cost-center "1010"',
             checks=[])


# EXAMPLE: /BillingRoleAssignments/delete/InvoiceSectionRoleAssignmentDelete
@try_manual
def step__billingroleassignments_delete3(test):
    test.cmd('az billing role-assignment delete -y '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--name "{myBillingRoleAssignment}" '
             '--invoice-section-name "{myInvoiceSection}"',
             checks=[])


# EXAMPLE: /BillingRoleDefinitions/get/BillingAccountRoleDefinitionsList
@try_manual
def step__billingroledefinitions_get(test):
    test.cmd('az billing role-definition list '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /Customers/get/CustomersListByBillingAccount
@try_manual
def step__customers_get_customerslistbybillingaccount(test):
    test.cmd('az billing customer list '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /Customers/get/CustomersListByBillingProfile
@try_manual
def step__customers_get_customerslistbybillingprofile(test):
    test.cmd('az billing customer list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}"',
             checks=[])


# EXAMPLE: /Customers/get/CustomerWithExpand
@try_manual
def step__customers_get_customerwithexpand(test):
    test.cmd('az billing customer show '
             '--expand "enabledAzurePlans,resellers" '
             '--account-name "{myBillingAccount}" '
             '--name "{myCustomer}"',
             checks=[])


# EXAMPLE: /BillingPermissions/get/BillingProfilePermissionsList
@try_manual
def step__billingpermissions_get2(test):
    test.cmd('az billing permission list '
             '--account-name "{myBillingAccount}" '
             '--customer-name "{myCustomer}"',
             checks=[])


# EXAMPLE: /BillingRoleDefinitions/get/BillingProfileRoleDefinitionsList
@try_manual
def step__billingroledefinitions_get2(test):
    test.cmd('az billing role-definition list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}"',
             checks=[])


# EXAMPLE: /BillingRoleDefinitions/get/InvoiceSectionRoleDefinitionsList
@try_manual
def step__billingroledefinitions_get3(test):
    test.cmd('az billing role-definition list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--invoice-section-name "{myInvoiceSection}"',
             checks=[])


# EXAMPLE: /BillingSubscriptions/get/BillingSubscription
@try_manual
def step__billingsubscriptions_get_billingsubscription(test):
    test.cmd('az billing subscription show '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /Customers/get/Customer
@try_manual
def step__customers_get_customer(test):
    test.cmd('az billing customer show '
             '--account-name "{myBillingAccount}" '
             '--name "{myCustomer}"',
             checks=[])


# EXAMPLE: /BillingSubscriptions/get/BillingSubscriptionsListByBillingAccount
@try_manual
def step__billingsubscriptions_get(test):
    test.cmd('az billing subscription list '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /BillingSubscriptions/get/BillingSubscriptionsListByBillingProfile
@try_manual
def step__billingsubscriptions_get2(test):
    test.cmd('az billing subscription list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}"',
             checks=[])


# EXAMPLE: /BillingSubscriptions/get/BillingSubscriptionsListByCustomer
@try_manual
def step__billingsubscriptions_get3(test):
    test.cmd('az billing subscription list '
             '--account-name "{myBillingAccount}" '
             '--customer-name "{myCustomer}"',
             checks=[])


# EXAMPLE: /BillingSubscriptions/get/BillingSubscriptionsListByInvoiceSection
@try_manual
def step__billingsubscriptions_get4(test):
    test.cmd('az billing subscription list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--invoice-section-name "{myInvoiceSection}"',
             checks=[])


# EXAMPLE: /BillingProperty/get/BillingProperty
@try_manual
def step__billingproperty_get_billingproperty(test):
    test.cmd('az billing property show',
             checks=[])


# EXAMPLE: /BillingSubscriptions/patch/UpdateBillingProperty
@try_manual
def step__billingsubscriptions_patch(test):
    test.cmd('az billing subscription update '
             '--account-name "{myBillingAccount}" '
             '--cost-center "ABC1234"',
             checks=[])


# EXAMPLE: /BillingSubscriptions/post/MoveBillingSubscription
@try_manual
def step__billingsubscriptions_post(test):
    test.cmd('az billing subscription move '
             '--account-name "{myBillingAccount}" '
             '--destination-invoice-section-id "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billi'
             'ngProfiles/{billingProfileName}/invoiceSections/{newInvoiceSectionName}"',
             checks=[])


# EXAMPLE: /BillingPermissions/get/BillingProfilePermissionsList
@try_manual
def step__billingpermissions_get2(test):
    test.cmd('az billing permission list '
             '--account-name "{myBillingAccount}" '
             '--customer-name "{myCustomer}"',
             checks=[])


# EXAMPLE: /Invoices/get/BillingAccountInvoicesList
@try_manual
def step__invoices_get_billingaccountinvoiceslist(test):
    test.cmd('az billing invoice list '
             '--account-name "{myBillingAccount}" '
             '--period-end-date "2018-06-30" '
             '--period-start-date "2018-01-01"',
             checks=[])


# EXAMPLE: /Instructions/put/PutInstruction
@try_manual
def step__instructions_put_putinstruction(test):
    test.cmd('az billing instruction create '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--name "{myInstruction}" '
             '--amount 5000 '
             '--end-date "2020-12-30T21:26:47.997Z" '
             '--start-date "2019-12-30T21:26:47.997Z"',
             checks=[
                 test.check("name", "{myInstruction}", case_sensitive=False),
                 test.check("amount", 5000),
                 test.check("endDate", "2020-12-30T21:26:47.997Z", case_sensitive=False),
                 test.check("startDate", "2019-12-30T21:26:47.997Z", case_sensitive=False),
             ])


# EXAMPLE: /BillingSubscriptions/post/SubscriptionMoveValidateFailure
@try_manual
def step__billingsubscriptions_post2(test):
    test.cmd('az billing subscription validate-move '
             '--account-name "{myBillingAccount}" '
             '--destination-invoice-section-id "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billi'
             'ngProfiles/{billingProfileName}/invoiceSections/{newInvoiceSectionName}"',
             checks=[])


# EXAMPLE: /Invoices/get/BillingAccountInvoicesListWithRebillDetails
@try_manual
def step__invoices_get(test):
    test.cmd('az billing invoice list '
             '--account-name "{myBillingAccount}" '
             '--period-end-date "2018-06-30" '
             '--period-start-date "2018-01-01"',
             checks=[])


# EXAMPLE: /Invoices/get/BillingSubscriptionsListByBillingAccount
@try_manual
def step__invoices_get2(test):
    test.cmd('az billing invoice list '
             '--period-end-date "2018-06-30" '
             '--period-start-date "2018-01-01"',
             checks=[])


# EXAMPLE: /Instructions/get/InstructionsListByBillingProfile
@try_manual
def step__instructions_get(test):
    test.cmd('az billing instruction list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /Invoices/get/CreditNote
@try_manual
def step__invoices_get_creditnote(test):
    test.cmd('az billing invoice show '
             '--account-name "{myBillingAccount}" '
             '--name "{myInvoice}"',
             checks=[])


# EXAMPLE: /Invoices/get/Invoice
@try_manual
def step__invoices_get_invoice(test):
    test.cmd('az billing invoice show '
             '--account-name "{myBillingAccount}" '
             '--name "{myInvoice}"',
             checks=[])


# EXAMPLE: /Invoices/get/InvoicesListByBillingProfile
@try_manual
def step__invoices_get_invoiceslistbybillingprofile(test):
    test.cmd('az billing invoice list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--period-end-date "2018-06-30" '
             '--period-start-date "2018-01-01"',
             checks=[])


# EXAMPLE: /Invoices/get/InvoicesListByBillingProfileWithRebillDetails
@try_manual
def step__invoices_get3(test):
    test.cmd('az billing invoice list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--period-end-date "2018-06-30" '
             '--period-start-date "2018-01-01"',
             checks=[])


# EXAMPLE: /Invoices/get/InvoiceWithRebillDetails
@try_manual
def step__invoices_get_invoicewithrebilldetails(test):
    test.cmd('az billing invoice show '
             '--account-name "{myBillingAccount}" '
             '--name "{myInvoice}"',
             checks=[])


# EXAMPLE: /Invoices/get/VoidInvoice
@try_manual
def step__invoices_get_voidinvoice(test):
    test.cmd('az billing invoice show '
             '--account-name "{myBillingAccount}" '
             '--name "{myInvoice}"',
             checks=[])


# EXAMPLE: /InvoiceSections/put/PutInvoiceSection
@try_manual
def step__invoicesections_put_putinvoicesection(test):
    test.cmd('az billing invoice section create '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--name "{myInvoiceSection}" '
             '--display-name "invoiceSection1" '
             '--labels costCategory="Support" pcCode="A123456"',
             checks=[
                 test.check("name", "{myInvoiceSection}", case_sensitive=False),
                 test.check("displayName", "invoiceSection1", case_sensitive=False),
                 test.check("labels.costCategory", "Support", case_sensitive=False),
                 test.check("labels.pcCode", "A123456", case_sensitive=False),
             ])


# EXAMPLE: /InvoiceSections/get/InvoiceSectionsListByBillingProfile
@try_manual
def step__invoicesections_get(test):
    test.cmd('az billing invoice section list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}"',
             checks=[
                 test.check('length(@)', 1),
             ])


# EXAMPLE: /BillingPermissions/get/BillingAccountPermissionsList
@try_manual
def step__billingpermissions_get3(test):
    test.cmd('az billing permission list '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /BillingSubscriptions/post/SubscriptionMoveValidateSuccess
@try_manual
def step__billingsubscriptions_post3(test):
    test.cmd('az billing subscription validate-move '
             '--account-name "{myBillingAccount}" '
             '--destination-invoice-section-id "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billi'
             'ngProfiles/{billingProfileName}/invoiceSections/{newInvoiceSectionName}"',
             checks=[])


# EXAMPLE: /Instructions/get/Instruction
@try_manual
def step__instructions_get_instruction(test):
    test.cmd('az billing instruction show '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--name "{myInstruction}"',
             checks=[
                 test.check("name", "{myInstruction}", case_sensitive=False),
                 test.check("amount", 5000),
                 test.check("endDate", "2020-12-30T21:26:47.997Z", case_sensitive=False),
                 test.check("startDate", "2019-12-30T21:26:47.997Z", case_sensitive=False),
             ])


# EXAMPLE: /InvoiceSections/get/InvoiceSection
@try_manual
def step__invoicesections_get_invoicesection(test):
    test.cmd('az billing invoice section show '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--name "{myInvoiceSection}"',
             checks=[
                 test.check("name", "{myInvoiceSection}", case_sensitive=False),
                 test.check("displayName", "invoiceSection1", case_sensitive=False),
                 test.check("labels.costCategory", "Support", case_sensitive=False),
                 test.check("labels.pcCode", "A123456", case_sensitive=False),
             ])


# EXAMPLE: /Policies/put/UpdatePolicy
@try_manual
def step__policies_put_updatepolicy(test):
    test.cmd('az billing policy update '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--marketplace-purchases "OnlyFreeAllowed" '
             '--reservation-purchases "NotAllowed" '
             '--view-charges "Allowed"',
             checks=[])


# EXAMPLE: /Products/get/Product
@try_manual
def step__products_get_product(test):
    test.cmd('az billing product show '
             '--account-name "{myBillingAccount}" '
             '--name "{myProduct}"',
             checks=[])


# EXAMPLE: /Products/get/ProductsListByBillingAccount
@try_manual
def step__products_get_productslistbybillingaccount(test):
    test.cmd('az billing product list '
             '--account-name "{myBillingAccount}"',
             checks=[])


# EXAMPLE: /Products/get/ProductsListByBillingProfile
@try_manual
def step__products_get_productslistbybillingprofile(test):
    test.cmd('az billing product list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}"',
             checks=[])


# EXAMPLE: /Products/get/ProductsListByInvoiceSection
@try_manual
def step__products_get_productslistbyinvoicesection(test):
    test.cmd('az billing product list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--invoice-section-name "{myInvoiceSection}"',
             checks=[])


# EXAMPLE: /Products/get/ProductsListByInvoiceSection
@try_manual
def step__products_get_productslistbyinvoicesection(test):
    test.cmd('az billing product list '
             '--account-name "{myBillingAccount}" '
             '--profile-name "{myBillingProfile}" '
             '--invoice-section-name "{myInvoiceSection}"',
             checks=[])


# EXAMPLE: /Products/patch/UpdateBillingProperty
@try_manual
def step__products_patch_updatebillingproperty(test):
    test.cmd('az billing product update '
             '--account-name "{myBillingAccount}" '
             '--auto-renew "Off" '
             '--name "{myProduct}"',
             checks=[
                 test.check("autoRenew", "Off", case_sensitive=False),
                 test.check("name", "{myProduct}", case_sensitive=False),
             ])


# EXAMPLE: /Products/post/MoveProduct
@try_manual
def step__products_post_moveproduct(test):
    test.cmd('az billing product move '
             '--account-name "{myBillingAccount}" '
             '--destination-invoice-section-id "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billi'
             'ngProfiles/{billingProfileName}/invoiceSections/{newInvoiceSectionName}" '
             '--name "{myProduct}"',
             checks=[])


# EXAMPLE: /Products/post/SubscriptionMoveValidateFailure
@try_manual
def step__products_post(test):
    test.cmd('az billing product validate-move '
             '--account-name "{myBillingAccount}" '
             '--destination-invoice-section-id "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billi'
             'ngProfiles/{billingProfileName}/invoiceSections/{newInvoiceSectionName}" '
             '--name "{myProduct}"',
             checks=[])


# EXAMPLE: /Products/post/SubscriptionMoveValidateSuccess
@try_manual
def step__products_post2(test):
    test.cmd('az billing product validate-move '
             '--account-name "{myBillingAccount}" '
             '--destination-invoice-section-id "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billi'
             'ngProfiles/{billingProfileName}/invoiceSections/{newInvoiceSectionName}" '
             '--name "{myProduct}"',
             checks=[])


# EXAMPLE: /Transactions/get/TransactionsListByInvoice
@try_manual
def step__transactions_get_transactionslistbyinvoice(test):
    test.cmd('az billing transaction list '
             '--account-name "{myBillingAccount}" '
             '--invoice-name "{myInvoice}"',
             checks=[])


# Env cleanup
@try_manual
def cleanup(test):
    pass


# Testcase
@try_manual
def call_scenario(test):
    setup(test)
    step__billingaccounts_get_billingaccounts(test)
    step__billingaccounts_get_billingaccountslist(test)
    step__billingaccounts_get(test)
    step__billingaccounts_get2(test)
    step__billingaccounts_get_billingaccountwithexpand(test)
    step__billingaccounts_patch_updatebillingaccount(test)
    step__agreements_get_agreementbyname(test)
    step__agreements_get(test)
    step__billingprofiles_put_createbillingprofile(test)
    step__billingprofiles_get_billingprofile(test)
    step__billingprofiles_get(test)
    step__billingprofiles_get2(test)
    step__billingprofiles_get_billingprofilewithexpand(test)
    step__availablebalances_get(test)
    step__billingroleassignments_get(test)
    step__billingpermissions_get(test)
    step__billingroleassignments_get2(test)
    step__billingroleassignments_get3(test)
    step__billingroleassignments_delete(test)
    step__billingroleassignments_delete2(test)
    step__billingproperty_patch_updatebillingproperty(test)
    step__billingroleassignments_delete3(test)
    step__billingroledefinitions_get(test)
    step__customers_get_customerslistbybillingaccount(test)
    step__customers_get_customerslistbybillingprofile(test)
    step__customers_get_customerwithexpand(test)
    step__billingpermissions_get2(test)
    step__billingroledefinitions_get2(test)
    step__billingroledefinitions_get3(test)
    step__billingsubscriptions_get_billingsubscription(test)
    step__customers_get_customer(test)
    step__billingsubscriptions_get(test)
    step__billingsubscriptions_get2(test)
    step__billingsubscriptions_get3(test)
    step__billingsubscriptions_get4(test)
    step__billingproperty_get_billingproperty(test)
    step__billingsubscriptions_patch(test)
    step__billingsubscriptions_post(test)
    step__billingpermissions_get2(test)
    step__invoices_get_billingaccountinvoiceslist(test)
    step__instructions_put_putinstruction(test)
    step__billingsubscriptions_post2(test)
    step__invoices_get(test)
    step__invoices_get2(test)
    step__instructions_get(test)
    step__invoices_get_creditnote(test)
    step__invoices_get_invoice(test)
    step__invoices_get_invoiceslistbybillingprofile(test)
    step__invoices_get3(test)
    step__invoices_get_invoicewithrebilldetails(test)
    step__invoices_get_voidinvoice(test)
    step__invoicesections_put_putinvoicesection(test)
    step__invoicesections_get(test)
    step__billingpermissions_get3(test)
    step__billingsubscriptions_post3(test)
    step__instructions_get_instruction(test)
    step__invoicesections_get_invoicesection(test)
    step__policies_put_updatepolicy(test)
    step__products_get_product(test)
    step__products_get_productslistbybillingaccount(test)
    step__products_get_productslistbybillingprofile(test)
    step__products_get_productslistbyinvoicesection(test)
    step__products_get_productslistbyinvoicesection(test)
    step__products_patch_updatebillingproperty(test)
    step__products_post_moveproduct(test)
    step__products_post(test)
    step__products_post2(test)
    step__transactions_get_transactionslistbyinvoice(test)
    cleanup(test)


@try_manual
class BillingManagementClientScenarioTest(ScenarioTest):

    def test_billing(self):

        self.kwargs.update({
            'myBillingAccount': '{billingAccountName}',
            'myBillingProfile': '{billingProfileName}',
            'myCustomer': '{customerName}',
            'myInvoiceSection': '{invoiceSectionName}',
            'myProduct': '{productName}',
            'myInvoice': '{invoiceName}',
            'myBillingRoleAssignment': '{billingRoleAssignmentName}',
            'myAgreement': '{agreementName}',
            'myInstruction': '{instructionName}',
        })

        call_scenario(self)
        calc_coverage(__file__)
        raise_if()
