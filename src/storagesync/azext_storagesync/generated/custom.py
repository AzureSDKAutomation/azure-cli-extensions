# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from azure.cli.core.util import sdk_no_wait


def storagesync_storage_sync_service_list(client,
                                          resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def storagesync_storage_sync_service_show(client,
                                          resource_group_name,
                                          storage_sync_service_name):
    return client.get(resource_group_name=resource_group_name,
                      storage_sync_service_name=storage_sync_service_name)


def storagesync_storage_sync_service_create(client,
                                            resource_group_name,
                                            storage_sync_service_name,
                                            location,
                                            tags=None,
                                            incoming_traffic_policy=None,
                                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       location=location,
                       tags=tags,
                       incoming_traffic_policy=incoming_traffic_policy)


def storagesync_storage_sync_service_update(client,
                                            resource_group_name,
                                            storage_sync_service_name,
                                            tags=None,
                                            incoming_traffic_policy=None,
                                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       tags=tags,
                       incoming_traffic_policy=incoming_traffic_policy)


def storagesync_storage_sync_service_delete(client,
                                            resource_group_name,
                                            storage_sync_service_name,
                                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name)


def storagesync_private_link_resource_list(client,
                                           resource_group_name,
                                           storage_sync_service_name):
    return client.list_by_storage_sync_service(resource_group_name=resource_group_name,
                                               storage_sync_service_name=storage_sync_service_name)


def storagesync_private_endpoint_connection_list(client,
                                                 resource_group_name,
                                                 storage_sync_service_name):
    return client.list_by_storage_sync_service(resource_group_name=resource_group_name,
                                               storage_sync_service_name=storage_sync_service_name)


def storagesync_private_endpoint_connection_show(client,
                                                 resource_group_name,
                                                 storage_sync_service_name,
                                                 private_endpoint_connection_name):
    return client.get(resource_group_name=resource_group_name,
                      storage_sync_service_name=storage_sync_service_name,
                      private_endpoint_connection_name=private_endpoint_connection_name)


def storagesync_private_endpoint_connection_create(client,
                                                   resource_group_name,
                                                   storage_sync_service_name,
                                                   private_endpoint_connection_name,
                                                   private_link_service_connection_state=None,
                                                   no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       private_endpoint_connection_name=private_endpoint_connection_name,
                       private_endpoint=None,
                       private_link_service_connection_state=private_link_service_connection_state)


def storagesync_private_endpoint_connection_delete(client,
                                                   resource_group_name,
                                                   storage_sync_service_name,
                                                   private_endpoint_connection_name,
                                                   no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       private_endpoint_connection_name=private_endpoint_connection_name)


def storagesync_sync_group_list(client,
                                resource_group_name,
                                storage_sync_service_name):
    return client.list_by_storage_sync_service(resource_group_name=resource_group_name,
                                               storage_sync_service_name=storage_sync_service_name)


def storagesync_sync_group_show(client,
                                resource_group_name,
                                storage_sync_service_name,
                                sync_group_name):
    return client.get(resource_group_name=resource_group_name,
                      storage_sync_service_name=storage_sync_service_name,
                      sync_group_name=sync_group_name)


def storagesync_sync_group_create(client,
                                  resource_group_name,
                                  storage_sync_service_name,
                                  sync_group_name,
                                  properties=None):
    return client.create(resource_group_name=resource_group_name,
                         storage_sync_service_name=storage_sync_service_name,
                         sync_group_name=sync_group_name,
                         properties=properties)


def storagesync_sync_group_delete(client,
                                  resource_group_name,
                                  storage_sync_service_name,
                                  sync_group_name):
    return client.delete(resource_group_name=resource_group_name,
                         storage_sync_service_name=storage_sync_service_name,
                         sync_group_name=sync_group_name)


def storagesync_cloud_endpoint_list(client,
                                    resource_group_name,
                                    storage_sync_service_name,
                                    sync_group_name):
    return client.list_by_sync_group(resource_group_name=resource_group_name,
                                     storage_sync_service_name=storage_sync_service_name,
                                     sync_group_name=sync_group_name)


def storagesync_cloud_endpoint_show(client,
                                    resource_group_name,
                                    storage_sync_service_name,
                                    sync_group_name,
                                    cloud_endpoint_name):
    return client.get(resource_group_name=resource_group_name,
                      storage_sync_service_name=storage_sync_service_name,
                      sync_group_name=sync_group_name,
                      cloud_endpoint_name=cloud_endpoint_name)


def storagesync_cloud_endpoint_create(client,
                                      resource_group_name,
                                      storage_sync_service_name,
                                      sync_group_name,
                                      cloud_endpoint_name,
                                      storage_account_resource_id=None,
                                      azure_file_share_name=None,
                                      storage_account_tenant_id=None,
                                      friendly_name=None,
                                      no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       cloud_endpoint_name=cloud_endpoint_name,
                       storage_account_resource_id=storage_account_resource_id,
                       azure_file_share_name=azure_file_share_name,
                       storage_account_tenant_id=storage_account_tenant_id,
                       friendly_name=friendly_name)


def storagesync_cloud_endpoint_delete(client,
                                      resource_group_name,
                                      storage_sync_service_name,
                                      sync_group_name,
                                      cloud_endpoint_name,
                                      no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       cloud_endpoint_name=cloud_endpoint_name)


def storagesync_cloud_endpoint_post_backup(client,
                                           resource_group_name,
                                           storage_sync_service_name,
                                           sync_group_name,
                                           cloud_endpoint_name,
                                           azure_file_share=None,
                                           no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_post_backup,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       cloud_endpoint_name=cloud_endpoint_name,
                       azure_file_share=azure_file_share)


def storagesync_cloud_endpoint_post_restore(client,
                                            resource_group_name,
                                            storage_sync_service_name,
                                            sync_group_name,
                                            cloud_endpoint_name,
                                            partition=None,
                                            replica_group=None,
                                            request_id=None,
                                            azure_file_share_uri=None,
                                            status=None,
                                            source_azure_file_share_uri=None,
                                            failed_file_list=None,
                                            restore_file_spec=None,
                                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_post_restore,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       cloud_endpoint_name=cloud_endpoint_name,
                       partition=partition,
                       replica_group=replica_group,
                       request_id_parameter=request_id,
                       azure_file_share_uri=azure_file_share_uri,
                       status=status,
                       source_azure_file_share_uri=source_azure_file_share_uri,
                       failed_file_list=failed_file_list,
                       restore_file_spec=restore_file_spec)


def storagesync_cloud_endpoint_pre_backup(client,
                                          resource_group_name,
                                          storage_sync_service_name,
                                          sync_group_name,
                                          cloud_endpoint_name,
                                          azure_file_share=None,
                                          no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_pre_backup,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       cloud_endpoint_name=cloud_endpoint_name,
                       azure_file_share=azure_file_share)


def storagesync_cloud_endpoint_pre_restore(client,
                                           resource_group_name,
                                           storage_sync_service_name,
                                           sync_group_name,
                                           cloud_endpoint_name,
                                           partition=None,
                                           replica_group=None,
                                           request_id=None,
                                           azure_file_share_uri=None,
                                           status=None,
                                           source_azure_file_share_uri=None,
                                           backup_metadata_property_bag=None,
                                           restore_file_spec=None,
                                           pause_wait_for_sync_drain_time_period_in_seconds=None,
                                           no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_pre_restore,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       cloud_endpoint_name=cloud_endpoint_name,
                       partition=partition,
                       replica_group=replica_group,
                       request_id_parameter=request_id,
                       azure_file_share_uri=azure_file_share_uri,
                       status=status,
                       source_azure_file_share_uri=source_azure_file_share_uri,
                       backup_metadata_property_bag=backup_metadata_property_bag,
                       restore_file_spec=restore_file_spec,
                       pause_wait_for_sync_drain_time_period_in_seconds=pause_wait_for_sync_drain_time_period_in_seconds)


def storagesync_cloud_endpoint_restoreheartbeat(client,
                                                resource_group_name,
                                                storage_sync_service_name,
                                                sync_group_name,
                                                cloud_endpoint_name):
    return client.restoreheartbeat(resource_group_name=resource_group_name,
                                   storage_sync_service_name=storage_sync_service_name,
                                   sync_group_name=sync_group_name,
                                   cloud_endpoint_name=cloud_endpoint_name)


def storagesync_cloud_endpoint_trigger_change_detection(client,
                                                        resource_group_name,
                                                        storage_sync_service_name,
                                                        sync_group_name,
                                                        cloud_endpoint_name,
                                                        directory_path=None,
                                                        change_detection_mode=None,
                                                        paths=None,
                                                        no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_trigger_change_detection,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       cloud_endpoint_name=cloud_endpoint_name,
                       directory_path=directory_path,
                       change_detection_mode=change_detection_mode,
                       paths=paths)


def storagesync_server_endpoint_list(client,
                                     resource_group_name,
                                     storage_sync_service_name,
                                     sync_group_name):
    return client.list_by_sync_group(resource_group_name=resource_group_name,
                                     storage_sync_service_name=storage_sync_service_name,
                                     sync_group_name=sync_group_name)


def storagesync_server_endpoint_show(client,
                                     resource_group_name,
                                     storage_sync_service_name,
                                     sync_group_name,
                                     server_endpoint_name):
    return client.get(resource_group_name=resource_group_name,
                      storage_sync_service_name=storage_sync_service_name,
                      sync_group_name=sync_group_name,
                      server_endpoint_name=server_endpoint_name)


def storagesync_server_endpoint_create(client,
                                       resource_group_name,
                                       storage_sync_service_name,
                                       sync_group_name,
                                       server_endpoint_name,
                                       server_local_path=None,
                                       cloud_tiering=None,
                                       volume_free_space_percent=None,
                                       tier_files_older_than_days=None,
                                       friendly_name=None,
                                       server_resource_id=None,
                                       offline_data_transfer=None,
                                       offline_data_transfer_share_name=None,
                                       initial_download_policy=None,
                                       local_cache_mode=None,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       server_endpoint_name=server_endpoint_name,
                       server_local_path=server_local_path,
                       cloud_tiering=cloud_tiering,
                       volume_free_space_percent=volume_free_space_percent,
                       tier_files_older_than_days=tier_files_older_than_days,
                       friendly_name=friendly_name,
                       server_resource_id=server_resource_id,
                       offline_data_transfer=offline_data_transfer,
                       offline_data_transfer_share_name=offline_data_transfer_share_name,
                       initial_download_policy=initial_download_policy,
                       local_cache_mode=local_cache_mode)


def storagesync_server_endpoint_update(client,
                                       resource_group_name,
                                       storage_sync_service_name,
                                       sync_group_name,
                                       server_endpoint_name,
                                       cloud_tiering=None,
                                       volume_free_space_percent=None,
                                       tier_files_older_than_days=None,
                                       offline_data_transfer=None,
                                       offline_data_transfer_share_name=None,
                                       local_cache_mode=None,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_update,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       server_endpoint_name=server_endpoint_name,
                       cloud_tiering=cloud_tiering,
                       volume_free_space_percent=volume_free_space_percent,
                       tier_files_older_than_days=tier_files_older_than_days,
                       offline_data_transfer=offline_data_transfer,
                       offline_data_transfer_share_name=offline_data_transfer_share_name,
                       local_cache_mode=local_cache_mode)


def storagesync_server_endpoint_delete(client,
                                       resource_group_name,
                                       storage_sync_service_name,
                                       sync_group_name,
                                       server_endpoint_name,
                                       no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       server_endpoint_name=server_endpoint_name)


def storagesync_server_endpoint_recall_action(client,
                                              resource_group_name,
                                              storage_sync_service_name,
                                              sync_group_name,
                                              server_endpoint_name,
                                              pattern=None,
                                              recall_path=None,
                                              no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_recall_action,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       sync_group_name=sync_group_name,
                       server_endpoint_name=server_endpoint_name,
                       pattern=pattern,
                       recall_path=recall_path)


def storagesync_registered_server_list(client,
                                       resource_group_name,
                                       storage_sync_service_name):
    return client.list_by_storage_sync_service(resource_group_name=resource_group_name,
                                               storage_sync_service_name=storage_sync_service_name)


def storagesync_registered_server_show(client,
                                       resource_group_name,
                                       storage_sync_service_name,
                                       server_id):
    return client.get(resource_group_name=resource_group_name,
                      storage_sync_service_name=storage_sync_service_name,
                      server_id=server_id)


def storagesync_registered_server_create(client,
                                         resource_group_name,
                                         storage_sync_service_name,
                                         server_id,
                                         server_certificate=None,
                                         agent_version=None,
                                         server_osversion=None,
                                         last_heart_beat=None,
                                         server_role=None,
                                         cluster_id=None,
                                         cluster_name=None,
                                         properties_server_id=None,
                                         friendly_name=None,
                                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       server_id=server_id,
                       server_certificate=server_certificate,
                       agent_version=agent_version,
                       server_os_version=server_osversion,
                       last_heart_beat=last_heart_beat,
                       server_role=server_role,
                       cluster_id=cluster_id,
                       cluster_name=cluster_name,
                       registered_server_create_parameters_properties_server_id=properties_server_id,
                       friendly_name=friendly_name)


def storagesync_registered_server_delete(client,
                                         resource_group_name,
                                         storage_sync_service_name,
                                         server_id,
                                         no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       server_id=server_id)


def storagesync_registered_server_trigger_rollover(client,
                                                   resource_group_name,
                                                   storage_sync_service_name,
                                                   server_id,
                                                   server_certificate=None,
                                                   no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_trigger_rollover,
                       resource_group_name=resource_group_name,
                       storage_sync_service_name=storage_sync_service_name,
                       server_id=server_id,
                       server_certificate=server_certificate)


def storagesync_workflow_list(client,
                              resource_group_name,
                              storage_sync_service_name):
    return client.list_by_storage_sync_service(resource_group_name=resource_group_name,
                                               storage_sync_service_name=storage_sync_service_name)


def storagesync_workflow_show(client,
                              resource_group_name,
                              storage_sync_service_name,
                              workflow_id):
    return client.get(resource_group_name=resource_group_name,
                      storage_sync_service_name=storage_sync_service_name,
                      workflow_id=workflow_id)


def storagesync_workflow_abort(client,
                               resource_group_name,
                               storage_sync_service_name,
                               workflow_id):
    return client.abort(resource_group_name=resource_group_name,
                        storage_sync_service_name=storage_sync_service_name,
                        workflow_id=workflow_id)


def storagesync_operation_status_show(client,
                                      resource_group_name,
                                      location_name,
                                      workflow_id,
                                      operation_id):
    return client.get(resource_group_name=resource_group_name,
                      location_name=location_name,
                      workflow_id=workflow_id,
                      operation_id=operation_id)
