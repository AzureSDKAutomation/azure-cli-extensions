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
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_datashare.action import (
    AddBlobDataSet,
    AddBlobFolderDataSet,
    AddBlobContainerDataSet,
    AddADLSGen2FileDataSet,
    AddADLSGen2FolderDataSet,
    AddADLSGen2FileSystemDataSet,
    AddADLSGen1FolderDataSet,
    AddADLSGen1FileDataSet,
    AddKustoClusterDataSet,
    AddKustoDatabaseDataSet,
    AddSqlDWTableDataSet,
    AddSqlDBTableDataSet,
    AddBlobDataSetMapping,
    AddBlobFolderDataSetMapping,
    AddBlobContainerDataSetMapping,
    AddADLSGen2FileDataSetMapping,
    AddADLSGen2FolderDataSetMapping,
    AddADLSGen2FileSystemDataSetMapping,
    AddKustoClusterDataSetMapping,
    AddKustoDatabaseDataSetMapping,
    AddSqlDWTableDataSetMapping,
    AddSqlDBTableDataSetMapping,
    AddScheduledSynchronizationSetting,
    AddScheduledTrigger
)


def load_arguments(self, _):

    with self.argument_context('datashare account list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare account show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', options_list=['--name', '-n'], help='The name of the share account.',
                   id_part='name')

    with self.argument_context('datashare account create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', options_list=['--name', '-n'], help='The name of the share account.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)

    with self.argument_context('datashare account update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', options_list=['--name', '-n'], help='The name of the share account.',
                   id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('datashare account delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', options_list=['--name', '-n'], help='The name of the share account.',
                   id_part='name')

    with self.argument_context('datashare account wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', options_list=['--name', '-n'], help='The name of the share account.',
                   id_part='name')

    with self.argument_context('datashare consumer-invitation show') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('invitation_id', help='An invitation id')

    with self.argument_context('datashare consumer-invitation list-invitation') as c:
        c.argument('skip_token', help='The continuation token')

    with self.argument_context('datashare consumer-invitation reject-invitation') as c:
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('invitation_id', help='Unique id of the invitation.')

    with self.argument_context('datashare data-set list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='continuation token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')

    with self.argument_context('datashare data-set show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('data_set_name', options_list=['--name', '-n'], help='The name of the dataSet.', id_part='child_name'
                   '_2')

    with self.argument_context('datashare data-set create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share to add the data set to.')
        c.argument('data_set_name', options_list=['--name', '-n'], help='The name of the dataSet.')
        c.argument('blob_data_set', action=AddBlobDataSet, nargs='+', help='An Azure storage blob data set.',
                   arg_group='DataSet')
        c.argument('blob_folder_data_set', action=AddBlobFolderDataSet, nargs='+', help='An Azure storage blob folder d'
                   'ata set.', arg_group='DataSet')
        c.argument('blob_container_data_set', action=AddBlobContainerDataSet, nargs='+', help='An Azure storage blob co'
                   'ntainer data set.', arg_group='DataSet')
        c.argument('a_d_l_s_gen2_file_data_set', action=AddADLSGen2FileDataSet, nargs='+', help='An ADLS Gen 2 file dat'
                   'a set.', arg_group='DataSet')
        c.argument('a_d_l_s_gen2_folder_data_set', action=AddADLSGen2FolderDataSet, nargs='+', help='An ADLS Gen 2 fold'
                   'er data set.', arg_group='DataSet')
        c.argument('a_d_l_s_gen2_file_system_data_set', action=AddADLSGen2FileSystemDataSet, nargs='+', help='An ADLS G'
                   'en 2 file system data set.', arg_group='DataSet')
        c.argument('a_d_l_s_gen1_folder_data_set', action=AddADLSGen1FolderDataSet, nargs='+', help='An ADLS Gen 1 fold'
                   'er data set.', arg_group='DataSet')
        c.argument('a_d_l_s_gen1_file_data_set', action=AddADLSGen1FileDataSet, nargs='+', help='An ADLS Gen 1 file dat'
                   'a set.', arg_group='DataSet')
        c.argument('kusto_cluster_data_set', action=AddKustoClusterDataSet, nargs='+',
                   help='A kusto cluster data set.', arg_group='DataSet')
        c.argument('kusto_database_data_set', action=AddKustoDatabaseDataSet, nargs='+', help='A kusto database data se'
                   't.', arg_group='DataSet')
        c.argument('sql_d_w_table_data_set', action=AddSqlDWTableDataSet, nargs='+', help='A SQL DW table data set.',
                   arg_group='DataSet')
        c.argument('sql_d_b_table_data_set', action=AddSqlDBTableDataSet, nargs='+', help='A SQL DB table data set.',
                   arg_group='DataSet')

    with self.argument_context('datashare data-set delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('data_set_name', options_list=['--name', '-n'], help='The name of the dataSet.', id_part='child_name'
                   '_2')

    with self.argument_context('datashare data-set wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('data_set_name', options_list=['--name', '-n'], help='The name of the dataSet.', id_part='child_name'
                   '_2')

    with self.argument_context('datashare data-set-mapping list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription.')
        c.argument('skip_token', help='Continuation token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')

    with self.argument_context('datashare data-set-mapping show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', help='The name of the shareSubscription.', id_part='child_name_1')
        c.argument('data_set_mapping_name', options_list=['--name', '-n'], help='The name of the dataSetMapping.',
                   id_part='child_name_2')

    with self.argument_context('datashare data-set-mapping create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription which will hold the data set sin'
                   'k.')
        c.argument('data_set_mapping_name', options_list=['--name', '-n'], help='The name of the data set mapping to be'
                   ' created.')
        c.argument('blob_data_set_mapping', action=AddBlobDataSetMapping, nargs='+', help='A Blob data set mapping.',
                   arg_group='DataSetMapping')
        c.argument('blob_folder_data_set_mapping', action=AddBlobFolderDataSetMapping, nargs='+', help='A Blob folder d'
                   'ata set mapping.', arg_group='DataSetMapping')
        c.argument('blob_container_data_set_mapping', action=AddBlobContainerDataSetMapping, nargs='+', help='A Blob co'
                   'ntainer data set mapping.', arg_group='DataSetMapping')
        c.argument('a_d_l_s_gen2_file_data_set_mapping', action=AddADLSGen2FileDataSetMapping, nargs='+', help='An ADLS'
                   ' Gen2 file data set mapping.', arg_group='DataSetMapping')
        c.argument('a_d_l_s_gen2_folder_data_set_mapping', action=AddADLSGen2FolderDataSetMapping, nargs='+', help='An '
                   'ADLS Gen2 folder data set mapping.', arg_group='DataSetMapping')
        c.argument('a_d_l_s_gen2_file_system_data_set_mapping', action=AddADLSGen2FileSystemDataSetMapping, nargs='+',
                   help='An ADLS Gen2 file system data set mapping.', arg_group='DataSetMapping')
        c.argument('kusto_cluster_data_set_mapping', action=AddKustoClusterDataSetMapping, nargs='+', help='A Kusto clu'
                   'ster data set mapping', arg_group='DataSetMapping')
        c.argument('kusto_database_data_set_mapping', action=AddKustoDatabaseDataSetMapping, nargs='+', help='A Kusto d'
                   'atabase data set mapping', arg_group='DataSetMapping')
        c.argument('sql_d_w_table_data_set_mapping', action=AddSqlDWTableDataSetMapping, nargs='+', help='A SQL DW Tabl'
                   'e data set mapping.', arg_group='DataSetMapping')
        c.argument('sql_d_b_table_data_set_mapping', action=AddSqlDBTableDataSetMapping, nargs='+', help='A SQL DB Tabl'
                   'e data set mapping.', arg_group='DataSetMapping')

    with self.argument_context('datashare data-set-mapping delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', help='The name of the shareSubscription.', id_part='child_name_1')
        c.argument('data_set_mapping_name', options_list=['--name', '-n'], help='The name of the dataSetMapping.',
                   id_part='child_name_2')

    with self.argument_context('datashare invitation list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='The continuation token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')

    with self.argument_context('datashare invitation show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('invitation_name', options_list=['--name', '-n'], help='The name of the invitation.', id_part='child'
                   '_name_2')

    with self.argument_context('datashare invitation create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share to send the invitation for.')
        c.argument('invitation_name', options_list=['--name', '-n'], help='The name of the invitation.')
        c.argument('target_active_directory_id', help='The target Azure AD Id. Can\'t be combined with email.')
        c.argument('target_email', help='The email the invitation is directed to.')
        c.argument('target_object_id', help='The target user or application Id that invitation is being sent to. Must b'
                   'e specified along TargetActiveDirectoryId. This enables sending invitations to specific users or ap'
                   'plications in an AD tenant.')

    with self.argument_context('datashare invitation delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('invitation_name', options_list=['--name', '-n'], help='The name of the invitation.', id_part='child'
                   '_name_2')

    with self.argument_context('datashare share list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('skip_token', help='Continuation Token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')

    with self.argument_context('datashare share show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', options_list=['--name', '-n'], help='The name of the share to retrieve.', id_part='chi'
                   'ld_name_1')

    with self.argument_context('datashare share create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', options_list=['--name', '-n'], help='The name of the share.')
        c.argument('description', help='Share description.')
        c.argument('share_kind', arg_type=get_enum_type(['CopyBased', 'InPlace']), help='Share kind.')
        c.argument('terms', help='Share terms.')

    with self.argument_context('datashare share delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', options_list=['--name', '-n'], help='The name of the share.', id_part='child_name_1')

    with self.argument_context('datashare share list-synchronization') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', options_list=['--name', '-n'], help='The name of the share.')
        c.argument('skip_token', help='Continuation token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')

    with self.argument_context('datashare share list-synchronization-detail') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', options_list=['--name', '-n'], help='The name of the share.')
        c.argument('skip_token', help='Continuation token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')
        c.argument('consumer_email', help='Email of the user who created the synchronization')
        c.argument('consumer_name', help='Name of the user who created the synchronization')
        c.argument('consumer_tenant_name', help='Tenant name of the consumer who created the synchronization')
        c.argument('duration_ms', help='synchronization duration')
        c.argument('end_time', help='End time of synchronization')
        c.argument('message', help='message of synchronization')
        c.argument('start_time', help='start time of synchronization')
        c.argument('status', help='Raw Status')
        c.argument('synchronization_id', help='Synchronization id')

    with self.argument_context('datashare share wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', options_list=['--name', '-n'], help='The name of the share to retrieve.', id_part='chi'
                   'ld_name_1')

    with self.argument_context('datashare provider-share-subscription list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='Continuation Token')

    with self.argument_context('datashare provider-share-subscription get-by-share') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('provider_share_subscription_id', help='To locate shareSubscription', id_part='child_name_2')

    with self.argument_context('datashare provider-share-subscription reinstate') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('provider_share_subscription_id', help='To locate shareSubscription', id_part='child_name_2')

    with self.argument_context('datashare provider-share-subscription revoke') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('provider_share_subscription_id', help='To locate shareSubscription', id_part='child_name_2')

    with self.argument_context('datashare share-subscription list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('skip_token', help='Continuation Token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')

    with self.argument_context('datashare share-subscription show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', options_list=['--name', '-n'], help='The name of the shareSubscription.',
                    id_part='child_name_1')

    with self.argument_context('datashare share-subscription create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', options_list=['--name', '-n'],
                   help='The name of the shareSubscription.')
        c.argument('invitation_id', help='The invitation id.')
        c.argument('source_share_location', help='Source share location.')

    with self.argument_context('datashare share-subscription delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', options_list=['--name', '-n'], help='The name of the shareSubscription.',
                    id_part='child_name_1')

    with self.argument_context('datashare share-subscription cancel-synchronization') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', options_list=['--name', '-n'], help='The name of the shareSubscription.',
                    id_part='child_name_1')
        c.argument('synchronization_id', help='Synchronization id')

    with self.argument_context('datashare share-subscription list-source-share-synchronization-setting') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', options_list=['--name', '-n'],
                   help='The name of the shareSubscription.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare share-subscription list-synchronization') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', options_list=['--name', '-n'],
                   help='The name of the share subscription.')
        c.argument('skip_token', help='Continuation token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')

    with self.argument_context('datashare share-subscription list-synchronization-detail') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', options_list=['--name', '-n'],
                   help='The name of the share subscription.')
        c.argument('skip_token', help='Continuation token')
        c.argument('filter', help='Filters the results using OData syntax.')
        c.argument('orderby', help='Sorts the results using OData syntax.')
        c.argument('synchronization_id', help='Synchronization id')

    with self.argument_context('datashare share-subscription synchronize') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', options_list=['--name', '-n'], help='The name of share subscription',
                   id_part='child_name_1')
        c.argument('synchronization_mode', arg_type=get_enum_type(['Incremental', 'FullSync']), help='Mode of synchroni'
                   'zation used in triggers and snapshot sync. Incremental by default')

    with self.argument_context('datashare share-subscription wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', options_list=['--name', '-n'], help='The name of the shareSubscription.',
                    id_part='child_name_1')

    with self.argument_context('datashare consumer-source-data-set list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the shareSubscription.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare synchronization-setting list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share.')
        c.argument('skip_token', help='continuation token')

    with self.argument_context('datashare synchronization-setting show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('synchronization_setting_name', options_list=['--name', '-n'], help='The name of the synchronization'
                   'Setting.', id_part='child_name_2')

    with self.argument_context('datashare synchronization-setting create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_name', help='The name of the share to add the synchronization setting to.')
        c.argument('synchronization_setting_name', options_list=['--name', '-n'], help='The name of the synchronization'
                   'Setting.')
        c.argument('scheduled_synchronization_setting', action=AddScheduledSynchronizationSetting, nargs='+', help='A t'
                   'ype of synchronization setting based on schedule', arg_group='SynchronizationSetting')

    with self.argument_context('datashare synchronization-setting delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('synchronization_setting_name', options_list=['--name', '-n'], help='The name of the synchronization'
                   'Setting .', id_part='child_name_2')

    with self.argument_context('datashare synchronization-setting wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_name', help='The name of the share.', id_part='child_name_1')
        c.argument('synchronization_setting_name', options_list=['--name', '-n'], help='The name of the synchronization'
                   'Setting.', id_part='child_name_2')

    with self.argument_context('datashare trigger list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription.')
        c.argument('skip_token', help='Continuation token')

    with self.argument_context('datashare trigger show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', help='The name of the shareSubscription.', id_part='child_name_1')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The name of the trigger.', id_part='child_name_'
                   '2')

    with self.argument_context('datashare trigger create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.')
        c.argument('share_subscription_name', help='The name of the share subscription which will hold the data set sin'
                   'k.')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The name of the trigger.')
        c.argument('scheduled_trigger', action=AddScheduledTrigger, nargs='+', help='A type of trigger based on schedul'
                   'e', arg_group='Trigger')

    with self.argument_context('datashare trigger delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', help='The name of the shareSubscription.', id_part='child_name_1')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The name of the trigger.', id_part='child_name_'
                   '2')

    with self.argument_context('datashare trigger wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('account_name', help='The name of the share account.', id_part='name')
        c.argument('share_subscription_name', help='The name of the shareSubscription.', id_part='child_name_1')
        c.argument('trigger_name', options_list=['--name', '-n'], help='The name of the trigger.', id_part='child_name_'
                   '2')
