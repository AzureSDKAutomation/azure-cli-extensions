# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type
)
from azure.cli.core.commands.validators import validate_file_or_dict
from azext_billing.action import (
    AddSoldTo,
    AddEnabledAzurePlans,
    AddLabels
)


def load_arguments(self, _):

    with self.argument_context('billing account list') as c:
        c.argument('expand', type=str,
                   help='May be used to expand the soldTo, invoice sections and billing profiles.')

    with self.argument_context('billing account show') as c:
        c.argument('account_name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies a '
                   'billing account.')
        c.argument('expand', type=str,
                   help='May be used to expand the soldTo, invoice sections and billing profiles.')

    with self.argument_context('billing account update') as c:
        c.argument('account_name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies a '
                   'billing account.')
        c.argument('display_name', type=str, help='The billing account name.')
        c.argument('sold_to', action=AddSoldTo, nargs='*', help='The address of the individual or organization that is '
                   'responsible for the billing account.')
        c.argument('departments', type=validate_file_or_dict, help='The departments associated to the enrollment. '
                   'Expected value: json-string/@json-file.')
        c.argument('enrollment_accounts', type=validate_file_or_dict, help='The accounts associated to the enrollment. '
                   'Expected value: json-string/@json-file.')
        c.argument('billing_profiles_value', type=validate_file_or_dict, help='The billing profiles associated with '
                   'the billing account. Expected value: json-string/@json-file.')

    with self.argument_context('billing account wait') as c:
        c.argument('account_name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies a '
                   'billing account.')
        c.argument('expand', type=str,
                   help='May be used to expand the soldTo, invoice sections and billing profiles.')

    with self.argument_context('billing balance show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')

    with self.argument_context('billing instruction list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')

    with self.argument_context('billing instruction show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('name', options_list=['--name', '-n'], type=str, help='Instruction Name.')

    with self.argument_context('billing instruction create') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('name', options_list=['--name', '-n'], type=str, help='Instruction Name.')
        c.argument('amount', type=float, help='The amount budgeted for this billing instruction.')
        c.argument('start_date', help='The date this billing instruction goes into effect.')
        c.argument('end_date', help='The date this billing instruction is no longer in effect.')
        c.argument('creation_date', help='The date this billing instruction was created.')

    with self.argument_context('billing profile list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('expand', type=str, help='May be used to expand the invoice sections.')

    with self.argument_context('billing profile show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies a '
                   'billing profile.')
        c.argument('expand', type=str, help='May be used to expand the invoice sections.')

    with self.argument_context('billing profile create') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies a '
                   'billing profile.')
        c.argument('display_name', type=str, help='The name of the billing profile.')
        c.argument('po_number', type=str, help='The purchase order name that will appear on the invoices generated for '
                   'the billing profile.')
        c.argument('bill_to', action=AddSoldTo, nargs='*', help='Billing address.')
        c.argument('invoice_email_opt_in', arg_type=get_three_state_flag(), help='Flag controlling whether the '
                   'invoices for the billing profile are sent through email.')
        c.argument('enabled_azure_plans', action=AddEnabledAzurePlans, nargs='*', help='Information about the enabled '
                   'azure plans.')
        c.argument('invoice_sections_value', type=validate_file_or_dict, help='The invoice sections associated to the '
                   'billing profile. Expected value: json-string/@json-file.')

    with self.argument_context('billing profile update') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies a '
                   'billing profile.')
        c.argument('display_name', type=str, help='The name of the billing profile.')
        c.argument('po_number', type=str, help='The purchase order name that will appear on the invoices generated for '
                   'the billing profile.')
        c.argument('bill_to', action=AddSoldTo, nargs='*', help='Billing address.')
        c.argument('invoice_email_opt_in', arg_type=get_three_state_flag(), help='Flag controlling whether the '
                   'invoices for the billing profile are sent through email.')
        c.argument('enabled_azure_plans', action=AddEnabledAzurePlans, nargs='*', help='Information about the enabled '
                   'azure plans.')
        c.argument('invoice_sections_value', type=validate_file_or_dict, help='The invoice sections associated to the '
                   'billing profile. Expected value: json-string/@json-file.')

    with self.argument_context('billing profile wait') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies a '
                   'billing profile.')
        c.argument('expand', type=str, help='May be used to expand the invoice sections.')

    with self.argument_context('billing customer list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('search', type=str, help='Used for searching customers by their name. Any customer with name '
                   'containing the search text will be included in the response')
        c.argument('filter_', options_list=['--filter'], type=str,
                   help='May be used to filter the list of customers.')

    with self.argument_context('billing customer show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('customer_name', options_list=['--name', '-n', '--customer-name'], type=str, help='The ID that '
                   'uniquely identifies a customer.')
        c.argument('expand', type=str, help='May be used to expand enabledAzurePlans and resellers')

    with self.argument_context('billing invoice section list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')

    with self.argument_context('billing invoice section show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', options_list=['--name', '-n', '--invoice-section-name'], type=str, help=''
                   'The ID that uniquely identifies an invoice section.')

    with self.argument_context('billing invoice section create') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', options_list=['--name', '-n', '--invoice-section-name'], type=str, help=''
                   'The ID that uniquely identifies an invoice section.')
        c.argument('display_name', type=str, help='The name of the invoice section.')
        c.argument('labels', action=AddLabels, nargs='*', help='Dictionary of metadata associated with the invoice '
                   'section. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')

    with self.argument_context('billing invoice section update') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', options_list=['--name', '-n', '--invoice-section-name'], type=str, help=''
                   'The ID that uniquely identifies an invoice section.')
        c.argument('display_name', type=str, help='The name of the invoice section.')
        c.argument('labels', action=AddLabels, nargs='*', help='Dictionary of metadata associated with the invoice '
                   'section. Expect value: KEY1=VALUE1 KEY2=VALUE2 ...')

    with self.argument_context('billing invoice section wait') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', options_list=['--name', '-n', '--invoice-section-name'], type=str, help=''
                   'The ID that uniquely identifies an invoice section.')

    with self.argument_context('billing permission list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', type=str, help='The ID that uniquely identifies an invoice section.')
        c.argument('customer_name', type=str, help='The ID that uniquely identifies a customer.')

    with self.argument_context('billing subscription list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', type=str, help='The ID that uniquely identifies an invoice section.')
        c.argument('customer_name', type=str, help='The ID that uniquely identifies a customer.')

    with self.argument_context('billing subscription show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')

    with self.argument_context('billing subscription update') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('subscription_billing_status', arg_type=get_enum_type(['Active', 'Inactive', 'Abandoned', 'Deleted',
                                                                          'Warning']), help='The current billing '
                   'status of the subscription.')
        c.argument('cost_center', type=str, help='The cost center applied to the subscription.')
        c.argument('sku_id', type=str, help='The sku ID of the Azure plan for the subscription.')

    with self.argument_context('billing subscription move') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('destination_invoice_section_id', type=str, help='The destination invoice section id.')

    with self.argument_context('billing subscription validate-move') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('destination_invoice_section_id', type=str, help='The destination invoice section id.')

    with self.argument_context('billing subscription wait') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')

    with self.argument_context('billing product list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', type=str, help='The ID that uniquely identifies an invoice section.')
        c.argument('filter_', options_list=['--filter'], type=str, help='May be used to filter by product type. The '
                   'filter supports \'eq\', \'lt\', \'gt\', \'le\', \'ge\', and \'and\'. It does not currently support '
                   '\'ne\', \'or\', or \'not\'. Tag filter is a key value pair string where key and value are '
                   'separated by a colon (:).')
        c.argument('customer_name', type=str, help='The ID that uniquely identifies a customer.')

    with self.argument_context('billing product show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('product_name', options_list=['--name', '-n', '--product-name'], type=str, help='The ID that '
                   'uniquely identifies a product.')

    with self.argument_context('billing product update') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('product_name', options_list=['--name', '-n', '--product-name'], type=str, help='The ID that '
                   'uniquely identifies a product.')
        c.argument('auto_renew', arg_type=get_enum_type(['Off', 'On']), help='Indicates whether auto renewal is turned '
                   'on or off for a product.')
        c.argument('status', arg_type=get_enum_type(['Active', 'Inactive', 'PastDue', 'Expiring', 'Expired',
                                                     'Disabled', 'Cancelled', 'AutoRenew']), help='The current status '
                   'of the product.')
        c.argument('billing_frequency', arg_type=get_enum_type(['OneTime', 'Monthly', 'UsageBased']), help='The '
                   'frequency at which the product will be billed.')

    with self.argument_context('billing product move') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('product_name', options_list=['--name', '-n', '--product-name'], type=str, help='The ID that '
                   'uniquely identifies a product.')
        c.argument('destination_invoice_section_id', type=str, help='The destination invoice section id.')

    with self.argument_context('billing product validate-move') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('product_name', options_list=['--name', '-n', '--product-name'], type=str, help='The ID that '
                   'uniquely identifies a product.')
        c.argument('destination_invoice_section_id', type=str, help='The destination invoice section id.')

    with self.argument_context('billing invoice list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('period_start_date', type=str, help='The start date to fetch the invoices. The date should be '
                   'specified in MM-DD-YYYY format.')
        c.argument('period_end_date', type=str, help='The end date to fetch the invoices. The date should be specified '
                   'in MM-DD-YYYY format.')

    with self.argument_context('billing invoice show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('name', options_list=['--name', '-n'], type=str,
                   help='The ID that uniquely identifies an invoice.')

    with self.argument_context('billing transaction list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('invoice_name', type=str, help='The ID that uniquely identifies an invoice.')

    with self.argument_context('billing policy update') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('marketplace_purchases', arg_type=get_enum_type(['AllAllowed', 'OnlyFreeAllowed', 'NotAllowed']),
                   help='The policy that controls whether Azure marketplace purchases are allowed for a billing '
                   'profile.')
        c.argument('reservation_purchases', arg_type=get_enum_type(['Allowed', 'NotAllowed']), help='The policy that '
                   'controls whether Azure reservation purchases are allowed for a billing profile.')
        c.argument('view_charges', arg_type=get_enum_type(['Allowed', 'NotAllowed']), help='The policy that controls '
                   'whether users with Azure RBAC access to a subscription can view its charges.')

    with self.argument_context('billing property update') as c:
        c.argument('cost_center', type=str, help='The cost center applied to the subscription.')

    with self.argument_context('billing role-definition list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', type=str, help='The ID that uniquely identifies an invoice section.')

    with self.argument_context('billing role-assignment list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', type=str, help='The ID that uniquely identifies an invoice section.')

    with self.argument_context('billing role-assignment delete') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('profile_name', type=str, help='The ID that uniquely identifies a billing profile.')
        c.argument('invoice_section_name', type=str, help='The ID that uniquely identifies an invoice section.')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies a role '
                   'assignment.')

    with self.argument_context('billing agreement list') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('expand', type=str, help='May be used to expand the participants.')

    with self.argument_context('billing agreement show') as c:
        c.argument('account_name', type=str, help='The ID that uniquely identifies a billing account.')
        c.argument('name', options_list=['--name', '-n'], type=str, help='The ID that uniquely identifies an '
                   'agreement.')
        c.argument('expand', type=str, help='May be used to expand the participants.')
