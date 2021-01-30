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


# EXAMPLE: /Accounts/put/Accounts_Create
@try_manual
def step_account_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare account create '
             '--location "West US 2" '
             '--tags tag1="Red" tag2="White" '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=[])
    test.cmd('az datashare account wait --created '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Accounts/get/Accounts_Get
@try_manual
def step_account_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare account show '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Accounts/get/Accounts_ListByResourceGroup
@try_manual
def step_account_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare account list '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Accounts/get/Accounts_ListBySubscription
@try_manual
def step_account_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare account list '
             '-g ""',
             checks=checks)


# EXAMPLE: /Accounts/patch/Accounts_Update
@try_manual
def step_account_update(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare account update '
             '--name "{myAccount}" '
             '--tags tag1="Red" tag2="White" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /DataSetMappings/put/DataSetMappings_SqlDB_Create
@try_manual
def step_data_set_mapping_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set-mapping create '
             '--account-name "{myAccount}" '
             '--sqldb-table-data-set-mapping database-name="Database1" data-set-id="a08f184b-0567-4b11-ba22-a1199336d22'
             '6" schema-name="dbo" sql-server-resource-id="/subscriptions/{subscription_id}/resourceGroups/{rg}/provide'
             'rs/Microsoft.Sql/servers/Server1" table-name="Table1" '
             '--name "{myDataSetMapping}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /DataSetMappings/put/DataSetMappings_SqlDW_Create
@try_manual
def step_data_set_mapping_create2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set-mapping create '
             '--account-name "{myAccount}" '
             '--sqldw-table-data-set-mapping data-set-id="a08f184b-0567-4b11-ba22-a1199336d226" '
             'data-warehouse-name="DataWarehouse1" schema-name="dbo" sql-server-resource-id="/subscriptions/{subscripti'
             'on_id}/resourceGroups/{rg}/providers/Microsoft.Sql/servers/Server1" table-name="Table1" '
             '--name "{myDataSetMapping}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /DataSetMappings/put/DataSetMappings_SqlDWDataSetToAdlsGen2File_Create
@try_manual
def step_data_set_mapping_create3(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set-mapping create '
             '--account-name "{myAccount}" '
             '--adls-gen2-file-data-set-mapping data-set-id="a08f184b-0567-4b11-ba22-a1199336d226" file-path="file21" '
             'file-system="fileSystem" output-type="Csv" resource-group="{rg}" storage-account-name="storage2" '
             'subscription-id="433a8dfd-e5d5-4e77-ad86-90acdc75eb1a" '
             '--name "{myDataSetMapping}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /Shares/put/Shares_Create
@try_manual
def step_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare create '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--description "share description" '
             '--share-kind "CopyBased" '
             '--terms "Confidential" '
             '--name "{myShare}"',
             checks=checks)


# EXAMPLE: /Shares/get/Shares_Get
@try_manual
def step_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare show '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShare}"',
             checks=checks)


# EXAMPLE: /Shares/get/Shares_ListByAccount
@try_manual
def step_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /Shares/post/Shares_ListSynchronizationDetails
@try_manual
def step_list_synchronization_detail(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare list-synchronization-detail '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShare}" '
             '--synchronization-id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb"',
             checks=checks)


# EXAMPLE: /Shares/post/Shares_ListSynchronizations
@try_manual
def step_list_synchronization(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare list-synchronization '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSets/put/DataSets_Create
@try_manual
def step_data_set_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set create '
             '--account-name "{myAccount}" '
             '--blob-data-set container-name="C1" file-path="file21" resource-group="{rg}" '
             'storage-account-name="storage2" subscription-id="433a8dfd-e5d5-4e77-ad86-90acdc75eb1a" '
             '--name "{myDataSet}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSets/put/DataSets_KustoCluster_Create
@try_manual
def step_data_set_create2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set create '
             '--account-name "{myAccount}" '
             '--kusto-cluster-data-set kusto-cluster-resource-id="/subscriptions/{subscription_id}/resourceGroups/{rg}/'
             'providers/Microsoft.Kusto/clusters/Cluster1" '
             '--name "{myDataSet}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSets/put/DataSets_KustoDatabase_Create
@try_manual
def step_data_set_create3(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set create '
             '--account-name "{myAccount}" '
             '--kusto-database-data-set kusto-database-resource-id="/subscriptions/{subscription_id}/resourceGroups/{rg'
             '}/providers/Microsoft.Kusto/clusters/Cluster1/databases/Database1" '
             '--name "{myDataSet}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSets/put/DataSets_SqlDBTable_Create
@try_manual
def step_data_set_create4(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set create '
             '--account-name "{myAccount}" '
             '--sqldb-table-data-set database-name="SqlDB1" schema-name="dbo" sql-server-resource-id="/subscriptions/{s'
             'ubscription_id}/resourceGroups/{rg}/providers/Microsoft.Sql/servers/Server1" table-name="Table1" '
             '--name "{myDataSet}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSets/put/DataSets_SqlDWTable_Create
@try_manual
def step_data_set_create5(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set create '
             '--account-name "{myAccount}" '
             '--sqldw-table-data-set data-warehouse-name="DataWarehouse1" schema-name="dbo" '
             'sql-server-resource-id="/subscriptions/{subscription_id}/resourceGroups/{rg}/providers/Microsoft.Sql/serv'
             'ers/Server1" table-name="Table1" '
             '--name "{myDataSet}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSets/get/DataSets_Get
@try_manual
def step_data_set_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set show '
             '--account-name "{myAccount}" '
             '--name "{myDataSet}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSets/get/DataSets_ListByShare
@try_manual
def step_data_set_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSets/delete/DataSets_Delete
@try_manual
def step_data_set_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set delete -y '
             '--account-name "{myAccount}" '
             '--name "{myDataSet}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /Invitations/put/Invitations_Create
@try_manual
def step_invitation_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare invitation create '
             '--account-name "{myAccount}" '
             '--target-email "receiver@microsoft.com" '
             '--name "{myInvitation}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /Invitations/get/Invitations_Get
@try_manual
def step_invitation_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare invitation show '
             '--account-name "{myAccount}" '
             '--name "{myInvitation}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /Invitations/get/Invitations_ListByShare
@try_manual
def step_invitation_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare invitation list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /Invitations/delete/Invitations_Delete
@try_manual
def step_invitation_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare invitation delete -y '
             '--account-name "{myAccount}" '
             '--name "{myInvitation}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /ProviderShareSubscriptions/get/ProviderShareSubscriptions_GetByShare
@try_manual
def step_provider_share_subscription_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare provider-share-subscription show '
             '--account-name "{myAccount}" '
             '--provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /ProviderShareSubscriptions/get/ProviderShareSubscriptions_ListByShare
@try_manual
def step_provider_share_subscription_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare provider-share-subscription list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /ProviderShareSubscriptions/post/ProviderShareSubscriptions_Reinstate
@try_manual
def step_provider_share_subscription_reinstate(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare provider-share-subscription reinstate '
             '--account-name "{myAccount}" '
             '--provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /ProviderShareSubscriptions/post/ProviderShareSubscriptions_Revoke
@try_manual
def step_provider_share_subscription_revoke(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare provider-share-subscription revoke '
             '--account-name "{myAccount}" '
             '--provider-share-subscription-id "4256e2cf-0f82-4865-961b-12f83333f487" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /Shares/delete/Shares_Delete
@try_manual
def step_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare delete -y '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShare}"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/put/ShareSubscriptions_Create
@try_manual
def step_share_subscription_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription create '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--invitation-id "12345678-1234-1234-12345678abd" '
             '--source-share-location "eastus2" '
             '--name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/get/ShareSubscriptions_Get
@try_manual
def step_share_subscription_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription show '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/get/ShareSubscriptions_ListByAccount
@try_manual
def step_share_subscription_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/post/ShareSubscriptions_CancelSynchronization
@try_manual
def step_share_subscription_cancel_synchronization(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription cancel-synchronization '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShareSubscription}" '
             '--synchronization-id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/post/ShareSubscriptions_ListSourceShareSynchronizationSettings
@try_manual
def step_share_subscription_list2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription list-source-share-synchronization-setting '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShareSubscription2}"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/post/ShareSubscriptions_ListSynchronizationDetails
@try_manual
def step_share_subscription_list3(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription list-synchronization-detail '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShareSubscription2}" '
             '--synchronization-id "7d0536a6-3fa5-43de-b152-3d07c4f6b2bb"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/post/ShareSubscriptions_ListSynchronizations
@try_manual
def step_share_subscription_list_synchronization(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription list-synchronization '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShareSubscription2}"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/post/ShareSubscriptions_Synchronize
@try_manual
def step_share_subscription_synchronize(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription synchronize '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShareSubscription}" '
             '--synchronization-mode "Incremental"',
             checks=checks)


# EXAMPLE: /ShareSubscriptions/delete/ShareSubscriptions_Delete
@try_manual
def step_share_subscription_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare share-subscription delete -y '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /SynchronizationSettings/put/SynchronizationSettings_Create
@try_manual
def step_synchronization_setting_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare synchronization-setting create '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}" '
             '--scheduled-synchronization-setting recurrence-interval="Day" synchronization-time="2018-11-14T04:47:52.9'
             '614956Z" '
             '--name "{myDataSet}"',
             checks=checks)


# EXAMPLE: /SynchronizationSettings/get/SynchronizationSettings_Get
@try_manual
def step_synchronization_setting_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare synchronization-setting show '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}" '
             '--name "{mySynchronizationSetting}"',
             checks=checks)


# EXAMPLE: /SynchronizationSettings/get/SynchronizationSettings_ListByShare
@try_manual
def step_synchronization_setting_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare synchronization-setting list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}"',
             checks=checks)


# EXAMPLE: /SynchronizationSettings/delete/SynchronizationSettings_Delete
@try_manual
def step_synchronization_setting_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare synchronization-setting delete -y '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-name "{myShare}" '
             '--name "{mySynchronizationSetting}"',
             checks=checks)


# EXAMPLE: /Triggers/put/Triggers_Create
@try_manual
def step_trigger_create(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare trigger create '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}" '
             '--scheduled-trigger recurrence-interval="Day" synchronization-mode="Incremental" '
             'synchronization-time="2018-11-14T04:47:52.9614956Z" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/get/Triggers_Get
@try_manual
def step_trigger_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare trigger show '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Triggers/get/Triggers_ListByShareSubscription
@try_manual
def step_trigger_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare trigger list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /Triggers/delete/Triggers_Delete
@try_manual
def step_trigger_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare trigger delete -y '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}" '
             '--name "{myTrigger}"',
             checks=checks)


# EXAMPLE: /Accounts/delete/Accounts_Delete
@try_manual
def step_account_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare account delete -y '
             '--name "{myAccount}" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /ConsumerInvitations/get/ConsumerInvitations_Get
@try_manual
def step_consumer_invitation_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare consumer-invitation show '
             '--invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" '
             '--location "East US 2"',
             checks=checks)


# EXAMPLE: /ConsumerInvitations/get/ConsumerInvitations_ListInvitations
@try_manual
def step_consumer_invitation_list_invitation(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare consumer-invitation list-invitation',
             checks=checks)


# EXAMPLE: /ConsumerInvitations/post/ConsumerInvitations_RejectInvitation
@try_manual
def step_consumer_invitation_reject_invitation(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare consumer-invitation reject-invitation '
             '--invitation-id "dfbbc788-19eb-4607-a5a1-c74181bfff03" '
             '--location "East US 2"',
             checks=checks)


# EXAMPLE: /ConsumerSourceDataSets/get/ConsumerSourceDataSets_ListByShareSubscription
@try_manual
def step_consumer_source_data_set_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare consumer-source-data-set list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShare}"',
             checks=checks)


# EXAMPLE: /DataSetMappings/put/DataSetMappings_Create
@try_manual
def step_data_set_mapping_create4(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set-mapping create '
             '--account-name "{myAccount}" '
             '--blob-data-set-mapping container-name="C1" data-set-id="a08f184b-0567-4b11-ba22-a1199336d226" '
             'file-path="file21" resource-group="{rg}" storage-account-name="storage2" subscription-id="433a8dfd-e5d5-4'
             'e77-ad86-90acdc75eb1a" '
             '--name "{myDataSetMapping}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /DataSetMappings/get/DataSetMappings_Get
@try_manual
def step_data_set_mapping_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set-mapping show '
             '--account-name "{myAccount}" '
             '--name "{myDataSetMapping}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /DataSetMappings/get/DataSetMappings_ListByShareSubscription
@try_manual
def step_data_set_mapping_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set-mapping list '
             '--account-name "{myAccount}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}"',
             checks=checks)


# EXAMPLE: /DataSetMappings/delete/DataSetMappings_Delete
@try_manual
def step_data_set_mapping_delete(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az datashare data-set-mapping delete -y '
             '--account-name "{myAccount}" '
             '--name "{myDataSetMapping}" '
             '--resource-group "{rg}" '
             '--share-subscription-name "{myShareSubscription}"',
             checks=checks)

