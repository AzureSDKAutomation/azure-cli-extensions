# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Application
    from ._models_py3 import ApplicationGroup
    from ._models_py3 import ApplicationGroupList
    from ._models_py3 import ApplicationGroupPatch
    from ._models_py3 import ApplicationList
    from ._models_py3 import ApplicationPatch
    from ._models_py3 import Desktop
    from ._models_py3 import DesktopList
    from ._models_py3 import DesktopPatch
    from ._models_py3 import HostPool
    from ._models_py3 import HostPoolList
    from ._models_py3 import HostPoolPatch
    from ._models_py3 import RegistrationInfo
    from ._models_py3 import RegistrationInfoPatch
    from ._models_py3 import Resource
    from ._models_py3 import ResourceProviderOperation
    from ._models_py3 import ResourceProviderOperationDisplay
    from ._models_py3 import ResourceProviderOperationList
    from ._models_py3 import SendMessage
    from ._models_py3 import SessionHost
    from ._models_py3 import SessionHostList
    from ._models_py3 import SessionHostPatch
    from ._models_py3 import StartMenuItem
    from ._models_py3 import StartMenuItemList
    from ._models_py3 import TrackedResource
    from ._models_py3 import UserSession
    from ._models_py3 import UserSessionList
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceList
    from ._models_py3 import WorkspacePatch
except (SyntaxError, ImportError):
    from ._models import Application  # type: ignore
    from ._models import ApplicationGroup  # type: ignore
    from ._models import ApplicationGroupList  # type: ignore
    from ._models import ApplicationGroupPatch  # type: ignore
    from ._models import ApplicationList  # type: ignore
    from ._models import ApplicationPatch  # type: ignore
    from ._models import Desktop  # type: ignore
    from ._models import DesktopList  # type: ignore
    from ._models import DesktopPatch  # type: ignore
    from ._models import HostPool  # type: ignore
    from ._models import HostPoolList  # type: ignore
    from ._models import HostPoolPatch  # type: ignore
    from ._models import RegistrationInfo  # type: ignore
    from ._models import RegistrationInfoPatch  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import ResourceProviderOperation  # type: ignore
    from ._models import ResourceProviderOperationDisplay  # type: ignore
    from ._models import ResourceProviderOperationList  # type: ignore
    from ._models import SendMessage  # type: ignore
    from ._models import SessionHost  # type: ignore
    from ._models import SessionHostList  # type: ignore
    from ._models import SessionHostPatch  # type: ignore
    from ._models import StartMenuItem  # type: ignore
    from ._models import StartMenuItemList  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import UserSession  # type: ignore
    from ._models import UserSessionList  # type: ignore
    from ._models import Workspace  # type: ignore
    from ._models import WorkspaceList  # type: ignore
    from ._models import WorkspacePatch  # type: ignore

from ._desktop_virtualization_api_client_enums import (
    ApplicationGroupType,
    ApplicationType,
    CommandLineSetting,
    HostPoolType,
    LoadBalancerType,
    PersonalDesktopAssignmentType,
    RegistrationTokenOperation,
    SessionState,
    Status,
    UpdateState,
)

__all__ = [
    'Application',
    'ApplicationGroup',
    'ApplicationGroupList',
    'ApplicationGroupPatch',
    'ApplicationList',
    'ApplicationPatch',
    'Desktop',
    'DesktopList',
    'DesktopPatch',
    'HostPool',
    'HostPoolList',
    'HostPoolPatch',
    'RegistrationInfo',
    'RegistrationInfoPatch',
    'Resource',
    'ResourceProviderOperation',
    'ResourceProviderOperationDisplay',
    'ResourceProviderOperationList',
    'SendMessage',
    'SessionHost',
    'SessionHostList',
    'SessionHostPatch',
    'StartMenuItem',
    'StartMenuItemList',
    'TrackedResource',
    'UserSession',
    'UserSessionList',
    'Workspace',
    'WorkspaceList',
    'WorkspacePatch',
    'ApplicationGroupType',
    'ApplicationType',
    'CommandLineSetting',
    'HostPoolType',
    'LoadBalancerType',
    'PersonalDesktopAssignmentType',
    'RegistrationTokenOperation',
    'SessionState',
    'Status',
    'UpdateState',
]
