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


def desktopvirtualization_workspace_list(client,
                                         resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def desktopvirtualization_workspace_show(client,
                                         resource_group_name,
                                         workspace_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name)


def desktopvirtualization_workspace_create(client,
                                           resource_group_name,
                                           workspace_name,
                                           location,
                                           tags=None,
                                           description=None,
                                           friendly_name=None,
                                           application_group_references=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   workspace_name=workspace_name,
                                   tags=tags,
                                   location=location,
                                   description=description,
                                   friendly_name=friendly_name,
                                   application_group_references=application_group_references)


def desktopvirtualization_workspace_update(client,
                                           resource_group_name,
                                           workspace_name,
                                           tags=None,
                                           description=None,
                                           friendly_name=None,
                                           application_group_references=None):
    return client.update(resource_group_name=resource_group_name,
                         workspace_name=workspace_name,
                         tags=tags,
                         description=description,
                         friendly_name=friendly_name,
                         application_group_references=application_group_references)


def desktopvirtualization_workspace_delete(client,
                                           resource_group_name,
                                           workspace_name):
    return client.delete(resource_group_name=resource_group_name,
                         workspace_name=workspace_name)


def desktopvirtualization_applicationgroup_list(client,
                                                resource_group_name=None,
                                                filter_=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             filter=filter_)
    return client.list_by_subscription(filter=filter_)


def desktopvirtualization_applicationgroup_show(client,
                                                resource_group_name,
                                                application_group_name):
    return client.get(resource_group_name=resource_group_name,
                      application_group_name=application_group_name)


def desktopvirtualization_applicationgroup_create(client,
                                                  resource_group_name,
                                                  application_group_name,
                                                  location,
                                                  host_pool_arm_path,
                                                  application_group_type,
                                                  tags=None,
                                                  description=None,
                                                  friendly_name=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   application_group_name=application_group_name,
                                   tags=tags,
                                   location=location,
                                   description=description,
                                   friendly_name=friendly_name,
                                   host_pool_arm_path=host_pool_arm_path,
                                   application_group_type=application_group_type)


def desktopvirtualization_applicationgroup_update(client,
                                                  resource_group_name,
                                                  application_group_name,
                                                  tags=None,
                                                  description=None,
                                                  friendly_name=None):
    return client.update(resource_group_name=resource_group_name,
                         application_group_name=application_group_name,
                         tags=tags,
                         description=description,
                         friendly_name=friendly_name)


def desktopvirtualization_applicationgroup_delete(client,
                                                  resource_group_name,
                                                  application_group_name):
    return client.delete(resource_group_name=resource_group_name,
                         application_group_name=application_group_name)


def desktopvirtualization_hostpool_list(client,
                                        resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def desktopvirtualization_hostpool_show(client,
                                        resource_group_name,
                                        host_pool_name):
    return client.get(resource_group_name=resource_group_name,
                      host_pool_name=host_pool_name)


def desktopvirtualization_hostpool_create(client,
                                          resource_group_name,
                                          host_pool_name,
                                          location,
                                          host_pool_type,
                                          load_balancer_type,
                                          preferred_app_group_type,
                                          tags=None,
                                          friendly_name=None,
                                          description=None,
                                          personal_desktop_assignment_type=None,
                                          custom_rdp_property=None,
                                          max_session_limit=None,
                                          ring=None,
                                          validation_environment=None,
                                          registration_info=None,
                                          vm_template=None,
                                          sso_context=None,
                                          ssoadfs_authority=None,
                                          sso_client_id=None,
                                          sso_client_secret_key_vault_path=None,
                                          sso_secret_type=None,
                                          start_vm_on_connect=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   host_pool_name=host_pool_name,
                                   tags=tags,
                                   location=location,
                                   friendly_name=friendly_name,
                                   description=description,
                                   host_pool_type=host_pool_type,
                                   personal_desktop_assignment_type=personal_desktop_assignment_type,
                                   custom_rdp_property=custom_rdp_property,
                                   max_session_limit=max_session_limit,
                                   load_balancer_type=load_balancer_type,
                                   ring=ring,
                                   validation_environment=validation_environment,
                                   registration_info=registration_info,
                                   vm_template=vm_template,
                                   sso_context=sso_context,
                                   ssoadfs_authority=ssoadfs_authority,
                                   sso_client_id=sso_client_id,
                                   sso_client_secret_key_vault_path=sso_client_secret_key_vault_path,
                                   sso_secret_type=sso_secret_type,
                                   preferred_app_group_type=preferred_app_group_type,
                                   start_vm_on_connect=start_vm_on_connect)


def desktopvirtualization_hostpool_update(client,
                                          resource_group_name,
                                          host_pool_name,
                                          tags=None,
                                          friendly_name=None,
                                          description=None,
                                          custom_rdp_property=None,
                                          max_session_limit=None,
                                          personal_desktop_assignment_type=None,
                                          load_balancer_type=None,
                                          ring=None,
                                          validation_environment=None,
                                          registration_info=None,
                                          vm_template=None,
                                          sso_context=None,
                                          ssoadfs_authority=None,
                                          sso_client_id=None,
                                          sso_client_secret_key_vault_path=None,
                                          sso_secret_type=None,
                                          preferred_app_group_type=None,
                                          start_vm_on_connect=None):
    return client.update(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         tags=tags,
                         friendly_name=friendly_name,
                         description=description,
                         custom_rdp_property=custom_rdp_property,
                         max_session_limit=max_session_limit,
                         personal_desktop_assignment_type=personal_desktop_assignment_type,
                         load_balancer_type=load_balancer_type,
                         ring=ring,
                         validation_environment=validation_environment,
                         registration_info=registration_info,
                         vm_template=vm_template,
                         sso_context=sso_context,
                         ssoadfs_authority=ssoadfs_authority,
                         sso_client_id=sso_client_id,
                         sso_client_secret_key_vault_path=sso_client_secret_key_vault_path,
                         sso_secret_type=sso_secret_type,
                         preferred_app_group_type=preferred_app_group_type,
                         start_vm_on_connect=start_vm_on_connect)


def desktopvirtualization_hostpool_delete(client,
                                          resource_group_name,
                                          host_pool_name,
                                          force=None):
    return client.delete(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         force=force)


def desktopvirtualization_msix_package_list(client,
                                            resource_group_name,
                                            host_pool_name):
    return client.list(resource_group_name=resource_group_name,
                       host_pool_name=host_pool_name)


def desktopvirtualization_msix_package_show(client,
                                            resource_group_name,
                                            host_pool_name,
                                            msix_package_full_name):
    return client.get(resource_group_name=resource_group_name,
                      host_pool_name=host_pool_name,
                      msix_package_full_name=msix_package_full_name)


def desktopvirtualization_msix_package_create(client,
                                              resource_group_name,
                                              host_pool_name,
                                              msix_package_full_name,
                                              image_path=None,
                                              package_name=None,
                                              package_family_name=None,
                                              display_name=None,
                                              package_relative_path=None,
                                              is_regular_registration=None,
                                              is_active=None,
                                              package_dependencies=None,
                                              version=None,
                                              last_updated=None,
                                              package_applications=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   host_pool_name=host_pool_name,
                                   msix_package_full_name=msix_package_full_name,
                                   image_path=image_path,
                                   package_name=package_name,
                                   package_family_name=package_family_name,
                                   display_name=display_name,
                                   package_relative_path=package_relative_path,
                                   is_regular_registration=is_regular_registration,
                                   is_active=is_active,
                                   package_dependencies=package_dependencies,
                                   version=version,
                                   last_updated=last_updated,
                                   package_applications=package_applications)


def desktopvirtualization_msix_package_update(client,
                                              resource_group_name,
                                              host_pool_name,
                                              msix_package_full_name,
                                              is_active=None,
                                              is_regular_registration=None,
                                              display_name=None):
    return client.update(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         msix_package_full_name=msix_package_full_name,
                         is_active=is_active,
                         is_regular_registration=is_regular_registration,
                         display_name=display_name)


def desktopvirtualization_msix_package_delete(client,
                                              resource_group_name,
                                              host_pool_name,
                                              msix_package_full_name):
    return client.delete(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         msix_package_full_name=msix_package_full_name)


def desktopvirtualization_msix_image_expand(client,
                                            resource_group_name,
                                            host_pool_name,
                                            uri=None):
    return client.expand(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         uri=uri)
