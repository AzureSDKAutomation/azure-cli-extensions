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

from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_databox.action import (
    AddSku,
    AddDataBoxScheduleAvailabilityRequest,
    AddDiskScheduleAvailabilityRequest,
    AddHeavyScheduleAvailabilityRequest,
    AddShippingAddress,
    AddCreateJobValidations
)


def load_arguments(self, _):

    with self.argument_context('databox job list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('skip_token', help='$skipToken is supported on Get list of jobs, which provides the next page in the'
                   ' list of jobs.')

    with self.argument_context('databox job show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n'], help='The name of the job Resource within the specified r'
                   'esource group. job names must be between 3 and 24 characters in length and use any alphanumeric and'
                   ' underscore only', id_part='name')
        c.argument('expand', help='$expand is supported on details parameter for job, which provides details on the job'
                   ' stages.')

    with self.argument_context('databox job create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n'], help='The name of the job Resource within the specified r'
                   'esource group. job names must be between 3 and 24 characters in length and use any alphanumeric and'
                   ' underscore only')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('sku', action=AddSku, nargs='+', help='The sku type.')
        c.argument('identity_type', help='Identity type')
        c.argument('transfer_type', arg_type=get_enum_type(['ImportToAzure', 'ExportFromAzure']), help='Type of the dat'
                   'a transfer.')
        c.argument('details', arg_type=CLIArgumentType(options_list=['--details'], help='Details of a job run. This fie'
                   'ld will only be sent for expand details filter. Expected value: json-string/@json-file.'))
        c.argument('delivery_type', arg_type=get_enum_type(['NonScheduled', 'Scheduled']),
                   help='Delivery type of Job.')
        c.argument('delivery_info_scheduled_date_time', help='Scheduled date time.')

    with self.argument_context('databox job update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n'], help='The name of the job Resource within the specified r'
                   'esource group. job names must be between 3 and 24 characters in length and use any alphanumeric and'
                   ' underscore only', id_part='name')
        c.argument('if_match', help='Defines the If-Match condition. The patch will be performed only if the ETag of th'
                   'e job on the server matches this value.')
        c.argument('tags', tags_type)
        c.argument('identity_type', help='Identity type')
        c.argument('details', arg_type=CLIArgumentType(options_list=['--details'], help='Details of a job to be updated'
                   '. Expected value: json-string/@json-file.'))

    with self.argument_context('databox job delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n'], help='The name of the job Resource within the specified r'
                   'esource group. job names must be between 3 and 24 characters in length and use any alphanumeric and'
                   ' underscore only', id_part='name')

    with self.argument_context('databox job book-shipment-pick-up') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n'], help='The name of the job Resource within the specified r'
                   'esource group. job names must be between 3 and 24 characters in length and use any alphanumeric and'
                   ' underscore only', id_part='name')
        c.argument('start_time', help='Minimum date after which the pick up should commence, this must be in local time'
                   ' of pick up area.')
        c.argument('end_time', help='Maximum date before which the pick up should commence, this must be in local time '
                   'of pick up area.')
        c.argument('shipment_location', help='Shipment Location in the pickup place. Eg.front desk')

    with self.argument_context('databox job cancel') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n'], help='The name of the job Resource within the specified r'
                   'esource group. job names must be between 3 and 24 characters in length and use any alphanumeric and'
                   ' underscore only', id_part='name')
        c.argument('reason', help='Reason for cancellation.')

    with self.argument_context('databox job list-credentials') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n'], help='The name of the job Resource within the specified r'
                   'esource group. job names must be between 3 and 24 characters in length and use any alphanumeric and'
                   ' underscore only')

    with self.argument_context('databox job wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('job_name', options_list=['--name', '-n'], help='The name of the job Resource within the specified r'
                   'esource group. job names must be between 3 and 24 characters in length and use any alphanumeric and'
                   ' underscore only', id_part='name')
        c.argument('expand', help='$expand is supported on details parameter for job, which provides details on the job'
                   ' stages.')

    with self.argument_context('databox service list-available-sku-by-resource-group') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('transfer_type', arg_type=get_enum_type(['ImportToAzure', 'ExportFromAzure']), help='Type of the tra'
                   'nsfer.')
        c.argument('country', help='ISO country code. Country for hardware shipment. For codes check: https://en.wikipe'
                   'dia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements')
        c.argument('sku_names', nargs='+', help='Sku Names to filter for available skus')

    with self.argument_context('databox service region-configuration') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group, id_part='name')
        c.argument('data_box_schedule_availability_request', action=AddDataBoxScheduleAvailabilityRequest, nargs='+',
                   help='Request body to get the availability for scheduling data box orders orders.', arg_group='Sched'
                   'uleAvailabilityRequest')
        c.argument('disk_schedule_availability_request', action=AddDiskScheduleAvailabilityRequest, nargs='+', help='Re'
                   'quest body to get the availability for scheduling disk orders.', arg_group='ScheduleAvailabilityReq'
                   'uest')
        c.argument('heavy_schedule_availability_request', action=AddHeavyScheduleAvailabilityRequest, nargs='+', help=
                   'Request body to get the availability for scheduling heavy orders.', arg_group='ScheduleAvailability'
                   'Request')
        c.argument('transport_availability_request_sku_name', arg_type=get_enum_type(['DataBox', 'DataBoxDisk', 'DataBo'
                   'xHeavy']), help='Type of the device.')

    with self.argument_context('databox service region-configuration-by-resource-group') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group, id_part='name')
        c.argument('data_box_schedule_availability_request', action=AddDataBoxScheduleAvailabilityRequest, nargs='+',
                   help='Request body to get the availability for scheduling data box orders orders.', arg_group='Sched'
                   'uleAvailabilityRequest')
        c.argument('disk_schedule_availability_request', action=AddDiskScheduleAvailabilityRequest, nargs='+', help='Re'
                   'quest body to get the availability for scheduling disk orders.', arg_group='ScheduleAvailabilityReq'
                   'uest')
        c.argument('heavy_schedule_availability_request', action=AddHeavyScheduleAvailabilityRequest, nargs='+', help=
                   'Request body to get the availability for scheduling heavy orders.', arg_group='ScheduleAvailability'
                   'Request')
        c.argument('transport_availability_request_sku_name', arg_type=get_enum_type(['DataBox', 'DataBoxDisk', 'DataBo'
                   'xHeavy']), help='Type of the device.')

    with self.argument_context('databox service validate-address') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group, id_part='name')
        c.argument('validation_type', arg_type=get_enum_type(['ValidateAddress', 'ValidateSubscriptionIsAllowedToCreate'
                   'Job', 'ValidatePreferences', 'ValidateCreateOrderLimit', 'ValidateSkuAvailability', 'ValidateDataTr'
                   'ansferDetails']), help='Identifies the type of validation request.')
        c.argument('shipping_address', action=AddShippingAddress, nargs='+', help='Shipping address of the customer.')
        c.argument('device_type', arg_type=get_enum_type(['DataBox', 'DataBoxDisk', 'DataBoxHeavy']), help='Device type'
                   ' to be used for the job.')
        c.argument('transport_preferences_preferred_shipment_type', arg_type=get_enum_type(['CustomerManaged', 'Microso'
                   'ftManaged']), help='Indicates Shipment Logistics type that the customer preferred.')

    with self.argument_context('databox service validate-input') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group, id_part='name')
        c.argument('create_job_validations', action=AddCreateJobValidations, nargs='+', help='It does all pre-job creat'
                   'ion validations.', arg_group='ValidationRequest')

    with self.argument_context('databox service validate-input-by-resource-group') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group, id_part='name')
        c.argument('create_job_validations', action=AddCreateJobValidations, nargs='+', help='It does all pre-job creat'
                   'ion validations.', arg_group='ValidationRequest')
