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
from azext_databoxedge.action import (
    AddDeviceAdminPassword,
    AddContactInformation,
    AddShippingAddress,
    AddAzureContainerInfo,
    AddUserAccessRights,
    AddClientAccessRights,
    AddRefreshDetails,
    AddFileEventTrigger,
    AddPeriodicTimerEventTrigger
)


def load_arguments(self, _):

    with self.argument_context('databoxedge available-sku list') as c:
        pass

    with self.argument_context('databoxedge device list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('expand', help='Specify $expand=details to populate additional fields related to the resource or Spe'
                   'cify $skipToken=:code:`<token>` to populate the next page in the list.')

    with self.argument_context('databoxedge device show') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device create') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('etag', help='The etag for the devices.')
        c.argument('kind', arg_type=get_enum_type(['AzureDataBoxGateway', 'AzureStackEdge', 'AzureStackHub']), help='Th'
                   'e etag for the devices.')
        c.argument('data_box_edge_device_status', arg_type=get_enum_type(['ReadyToSetup', 'Online', 'Offline', 'NeedsAt'
                   'tention', 'Disconnected', 'PartiallyDisconnected', 'Maintenance']), help='The status of the Data Bo'
                   'x Edge/Gateway device.')
        c.argument('description', help='The Description of the Data Box Edge/Gateway device.')
        c.argument('model_description', help='The description of the Data Box Edge/Gateway device model.')
        c.argument('friendly_name', help='The Data Box Edge/Gateway device name.')
        c.argument('sku_name', arg_type=get_enum_type(['Gateway', 'Edge', 'TEA_1Node', 'TEA_1Node_UPS', 'TEA_1Node_Heat'
                   'er', 'TEA_1Node_UPS_Heater', 'TEA_4Node_Heater', 'TEA_4Node_UPS_Heater', 'TMA', 'TDC', 'TCA_Large',
                    'TCA_Small', 'GPU']), help='SKU name.')

    with self.argument_context('databoxedge device update') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('tags', tags_type)

    with self.argument_context('databoxedge device delete') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device create-or-update-security-setting') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('device_admin_password', action=AddDeviceAdminPassword, nargs='+', help='Device administrator passwo'
                   'rd as an encrypted string (encrypted using RSA PKCS #1) is used to sign into the  local web UI of t'
                   'he device. The Actual password should have at least 8 characters that are a combination of  upperca'
                   'se, lowercase, numeric, and special characters.')

    with self.argument_context('databoxedge device download-update') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device get-extended-information') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device get-network-setting') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device get-update-summary') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device install-update') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device scan-for-update') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge device upload-certificate') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('authentication_type', arg_type=get_enum_type(['Invalid', 'AzureActiveDirectory']), help='The authen'
                   'tication type.')
        c.argument('certificate', help='The base64 encoded certificate raw data.')

    with self.argument_context('databoxedge device wait') as c:
        c.argument('device_name', options_list=['--name', '-n'], help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge sku list') as c:
        c.argument('filter', help='Specify $filter=\'location eq :code:`<location>`\' to filter on location.')

    with self.argument_context('databoxedge alert list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge alert show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The alert name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge bandwidth-schedule list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge bandwidth-schedule show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The bandwidth schedule name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge bandwidth-schedule create') as c:
        c.argument('device_name', help='The device name.')
        c.argument('name', help='The bandwidth schedule name which needs to be added/updated.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('start', help='The start time of the schedule in UTC.')
        c.argument('stop', help='The stop time of the schedule in UTC.')
        c.argument('rate_in_mbps', help='The bandwidth rate in Mbps.')
        c.argument('days', nargs='+', help='The days of the week when this schedule is applicable.')

    with self.argument_context('databoxedge bandwidth-schedule update') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The bandwidth schedule name which needs to be added/updated.',
                   id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('start', help='The start time of the schedule in UTC.')
        c.argument('stop', help='The stop time of the schedule in UTC.')
        c.argument('rate_in_mbps', help='The bandwidth rate in Mbps.')
        c.argument('days', nargs='+', help='The days of the week when this schedule is applicable.')

    with self.argument_context('databoxedge bandwidth-schedule delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The bandwidth schedule name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge bandwidth-schedule wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The bandwidth schedule name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge job show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The job name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order create') as c:
        c.argument('device_name', help='The order details of a device.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('contact_information', action=AddContactInformation, nargs='+', help='The contact details.')
        c.argument('shipping_address', action=AddShippingAddress, nargs='+', help='The shipping address.')
        c.argument('shipment_type', arg_type=get_enum_type(['NotApplicable', 'ShippedToCustomer', 'SelfPickup']),
                   help='ShipmentType of the order')
        c.argument('current_status_status', arg_type=get_enum_type(['Untracked', 'AwaitingFulfilment', 'AwaitingPrepara'
                   'tion', 'AwaitingShipment', 'Shipped', 'Arriving', 'Delivered', 'ReplacementRequested',
                   'LostDevice', 'Declined', 'ReturnInitiated', 'AwaitingReturnShipment', 'ShippedBack', 'CollectedAtMi'
                   'crosoft', 'AwaitingPickup', 'PickupCompleted', 'AwaitingDrop']), help='Status of the order as per t'
                   'he allowed status types.')
        c.argument('current_status_comments', help='Comments related to this status change.')

    with self.argument_context('databoxedge order update') as c:
        c.argument('device_name', help='The order details of a device.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('contact_information', action=AddContactInformation, nargs='+', help='The contact details.')
        c.argument('shipping_address', action=AddShippingAddress, nargs='+', help='The shipping address.')
        c.argument('shipment_type', arg_type=get_enum_type(['NotApplicable', 'ShippedToCustomer', 'SelfPickup']),
                   help='ShipmentType of the order')
        c.argument('current_status_status', arg_type=get_enum_type(['Untracked', 'AwaitingFulfilment', 'AwaitingPrepara'
                   'tion', 'AwaitingShipment', 'Shipped', 'Arriving', 'Delivered', 'ReplacementRequested',
                   'LostDevice', 'Declined', 'ReturnInitiated', 'AwaitingReturnShipment', 'ShippedBack', 'CollectedAtMi'
                   'crosoft', 'AwaitingPickup', 'PickupCompleted', 'AwaitingDrop']), help='Status of the order as per t'
                   'he allowed status types.')
        c.argument('current_status_comments', help='Comments related to this status change.')

    with self.argument_context('databoxedge order delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order list-dc-access-code') as c:
        c.argument('device_name', help='The device name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge order wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge node list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge operation-status show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The job name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge role list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge role show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The role name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge role create') as c:
        c.argument('device_name', help='The device name.')
        c.argument('name', help='The role name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('role', arg_type=CLIArgumentType(options_list=['--role'], help='The role properties. Expected value:'
                   ' json-string/@json-file.'))

    with self.argument_context('databoxedge role update') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The role name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('role', arg_type=CLIArgumentType(options_list=['--role'], help='The role properties. Expected value:'
                   ' json-string/@json-file.'))

    with self.argument_context('databoxedge role delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The role name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge role wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The role name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge share list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge share show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The share name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge share create') as c:
        c.argument('device_name', help='The device name.')
        c.argument('name', help='The share name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('description', help='Description for the share.')
        c.argument('share_status', arg_type=get_enum_type(['Offline', 'Unknown', 'OK', 'Updating', 'NeedsAttention']),
                   help='Current status of the share.')
        c.argument('monitoring_status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Current monitoring statu'
                   's of the share.')
        c.argument('azure_container_info', action=AddAzureContainerInfo, nargs='+', help='Azure container mapping for t'
                   'he share.')
        c.argument('access_protocol', arg_type=get_enum_type(['SMB', 'NFS']), help='Access protocol to be used by the s'
                   'hare.')
        c.argument('user_access_rights', action=AddUserAccessRights, nargs='+', help='Mapping of users and correspondin'
                   'g access rights on the share (required for SMB protocol).')
        c.argument('client_access_rights', action=AddClientAccessRights, nargs='+', help='List of IP addresses and corr'
                   'esponding access rights on the share(required for NFS protocol).')
        c.argument('refresh_details', action=AddRefreshDetails, nargs='+', help='Details of the refresh job on this sha'
                   're.')
        c.argument('data_policy', arg_type=get_enum_type(['Cloud', 'Local']), help='Data policy of the share.')

    with self.argument_context('databoxedge share update') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The share name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('description', help='Description for the share.')
        c.argument('share_status', arg_type=get_enum_type(['Offline', 'Unknown', 'OK', 'Updating', 'NeedsAttention']),
                   help='Current status of the share.')
        c.argument('monitoring_status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Current monitoring statu'
                   's of the share.')
        c.argument('azure_container_info', action=AddAzureContainerInfo, nargs='+', help='Azure container mapping for t'
                   'he share.')
        c.argument('access_protocol', arg_type=get_enum_type(['SMB', 'NFS']), help='Access protocol to be used by the s'
                   'hare.')
        c.argument('user_access_rights', action=AddUserAccessRights, nargs='+', help='Mapping of users and correspondin'
                   'g access rights on the share (required for SMB protocol).')
        c.argument('client_access_rights', action=AddClientAccessRights, nargs='+', help='List of IP addresses and corr'
                   'esponding access rights on the share(required for NFS protocol).')
        c.argument('refresh_details', action=AddRefreshDetails, nargs='+', help='Details of the refresh job on this sha'
                   're.')
        c.argument('data_policy', arg_type=get_enum_type(['Cloud', 'Local']), help='Data policy of the share.')

    with self.argument_context('databoxedge share delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The share name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge share refresh') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The share name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge share wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The share name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge storage-account-credentials list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge storage-account-credentials show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The storage account credential name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge storage-account-credentials create') as c:
        c.argument('device_name', help='The device name.')
        c.argument('name', help='The storage account credential name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('alias', help='Alias for the storage account.')
        c.argument('user_name', help='Username for the storage account.')
        c.argument('account_key', action=AddDeviceAdminPassword, nargs='+', help='Encrypted storage key.')
        c.argument('connection_string', help='Connection string for the storage account. Use this string if username an'
                   'd account key are not specified.')
        c.argument('ssl_status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Signifies whether SSL needs to '
                   'be enabled or not.')
        c.argument('blob_domain_name', help='Blob end point for private clouds.')
        c.argument('account_type', arg_type=get_enum_type(['GeneralPurposeStorage', 'BlobStorage']), help='Type of stor'
                   'age accessed on the storage account.')
        c.argument('storage_account_id', help='Id of the storage account.')

    with self.argument_context('databoxedge storage-account-credentials update') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The storage account credential name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('alias', help='Alias for the storage account.')
        c.argument('user_name', help='Username for the storage account.')
        c.argument('account_key', action=AddDeviceAdminPassword, nargs='+', help='Encrypted storage key.')
        c.argument('connection_string', help='Connection string for the storage account. Use this string if username an'
                   'd account key are not specified.')
        c.argument('ssl_status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Signifies whether SSL needs to '
                   'be enabled or not.')
        c.argument('blob_domain_name', help='Blob end point for private clouds.')
        c.argument('account_type', arg_type=get_enum_type(['GeneralPurposeStorage', 'BlobStorage']), help='Type of stor'
                   'age accessed on the storage account.')
        c.argument('storage_account_id', help='Id of the storage account.')

    with self.argument_context('databoxedge storage-account-credentials delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The storage account credential name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge storage-account-credentials wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The storage account credential name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge storage-account list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge storage-account show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', options_list=['--name', '-n'], help='The storage account name.', id_part='ch'
                   'ild_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge storage-account create') as c:
        c.argument('device_name', help='The device name.')
        c.argument('storage_account_name', options_list=['--name', '-n'], help='The StorageAccount name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('description', help='Description for the storage Account.')
        c.argument('storage_account_status', arg_type=get_enum_type(['OK', 'Offline', 'Unknown', 'Updating', 'NeedsAtte'
                   'ntion']), help='Current status of the storage account')
        c.argument('data_policy', arg_type=get_enum_type(['Cloud', 'Local']), help='Data policy of the storage Account.'
                   '')
        c.argument('storage_account_credential_id', help='Storage Account Credential Id')

    with self.argument_context('databoxedge storage-account update') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', options_list=['--name', '-n'], help='The StorageAccount name.', id_part='chi'
                   'ld_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('description', help='Description for the storage Account.')
        c.argument('storage_account_status', arg_type=get_enum_type(['OK', 'Offline', 'Unknown', 'Updating', 'NeedsAtte'
                   'ntion']), help='Current status of the storage account')
        c.argument('data_policy', arg_type=get_enum_type(['Cloud', 'Local']), help='Data policy of the storage Account.'
                   '')
        c.argument('storage_account_credential_id', help='Storage Account Credential Id')

    with self.argument_context('databoxedge storage-account delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', options_list=['--name', '-n'], help='The StorageAccount name.', id_part='chi'
                   'ld_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge storage-account wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', options_list=['--name', '-n'], help='The storage account name.', id_part='ch'
                   'ild_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge container list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('storage_account_name', help='The storage Account name.')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge container show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', help='The Storage Account Name', id_part='child_name_1')
        c.argument('container_name', options_list=['--name', '-n'], help='The container Name', id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge container create') as c:
        c.argument('device_name', help='The device name.')
        c.argument('storage_account_name', help='The Storage Account Name')
        c.argument('container_name', options_list=['--name', '-n'], help='The container name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('data_format', arg_type=get_enum_type(['BlockBlob', 'PageBlob', 'AzureFile']), help='DataFormat for '
                   'Container')

    with self.argument_context('databoxedge container update') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', help='The Storage Account Name', id_part='child_name_1')
        c.argument('container_name', options_list=['--name', '-n'], help='The container name.',
                   id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('data_format', arg_type=get_enum_type(['BlockBlob', 'PageBlob', 'AzureFile']), help='DataFormat for '
                   'Container')

    with self.argument_context('databoxedge container delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', help='The Storage Account Name', id_part='child_name_1')
        c.argument('container_name', options_list=['--name', '-n'], help='The container name.',
                   id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge container refresh') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', help='The Storage Account Name', id_part='child_name_1')
        c.argument('container_name', options_list=['--name', '-n'], help='The container name.',
                   id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge container wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('storage_account_name', help='The Storage Account Name', id_part='child_name_1')
        c.argument('container_name', options_list=['--name', '-n'], help='The container Name', id_part='child_name_2')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge trigger list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('filter', help='Specify $filter=\'CustomContextTag eq :code:`<tag>`\' to filter on custom context ta'
                   'g property')

    with self.argument_context('databoxedge trigger show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The trigger name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge trigger create') as c:
        c.argument('device_name', help='Creates or updates a trigger')
        c.argument('name', help='The trigger name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('file_event_trigger', action=AddFileEventTrigger, nargs='+', help='Trigger details.', arg_group='Tri'
                   'gger')
        c.argument('periodic_timer_event_trigger', action=AddPeriodicTimerEventTrigger, nargs='+', help='Trigger detail'
                   's.', arg_group='Trigger')

    with self.argument_context('databoxedge trigger update') as c:
        c.argument('device_name', help='Creates or updates a trigger', id_part='name')
        c.argument('name', help='The trigger name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('file_event_trigger', action=AddFileEventTrigger, nargs='+', help='Trigger details.', arg_group='Tri'
                   'gger')
        c.argument('periodic_timer_event_trigger', action=AddPeriodicTimerEventTrigger, nargs='+', help='Trigger detail'
                   's.', arg_group='Trigger')
        c.ignore('FileEventTrigger', 'PeriodicTimerEventTrigger')

    with self.argument_context('databoxedge trigger delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The trigger name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge trigger wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The trigger name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge user list') as c:
        c.argument('device_name', help='The device name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('filter', help='Specify $filter=\'Type eq :code:`<type>`\' to filter on user type property')

    with self.argument_context('databoxedge user show') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The user name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge user create') as c:
        c.argument('device_name', help='The device name.')
        c.argument('name', help='The user name.')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('encrypted_password', action=AddDeviceAdminPassword, nargs='+', help='The password details.')
        c.argument('user_type', arg_type=get_enum_type(['Share', 'LocalManagement', 'ARM']), help='Type of the user.')

    with self.argument_context('databoxedge user update') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The user name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('encrypted_password', action=AddDeviceAdminPassword, nargs='+', help='The password details.')
        c.argument('user_type', arg_type=get_enum_type(['Share', 'LocalManagement', 'ARM']), help='Type of the user.')

    with self.argument_context('databoxedge user delete') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The user name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('databoxedge user wait') as c:
        c.argument('device_name', help='The device name.', id_part='name')
        c.argument('name', help='The user name.', id_part='child_name_1')
        c.argument('resource_group_name', resource_group_name_type)
