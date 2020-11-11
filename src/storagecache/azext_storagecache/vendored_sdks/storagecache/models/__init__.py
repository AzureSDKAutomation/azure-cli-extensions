# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ASCOperation
    from ._models_py3 import ApiOperation
    from ._models_py3 import ApiOperationDisplay
    from ._models_py3 import ApiOperationListResult
    from ._models_py3 import ApiOperationPropertiesServiceSpecification
    from ._models_py3 import Cache
    from ._models_py3 import CacheActiveDirectorySettingsCredentials
    from ._models_py3 import CacheHealth
    from ._models_py3 import CacheUpgradeStatus
    from ._models_py3 import CacheUsernameDownloadSettingsCredentials
    from ._models_py3 import CachesListResult
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import ErrorResponse
    from ._models_py3 import MetricDimension
    from ._models_py3 import MetricSpecification
    from ._models_py3 import NamespaceJunction
    from ._models_py3 import Nfs3Target
    from ._models_py3 import NfsAccessPolicy
    from ._models_py3 import NfsAccessRule
    from ._models_py3 import ResourceSku
    from ._models_py3 import ResourceSkuCapabilities
    from ._models_py3 import ResourceSkuLocationInfo
    from ._models_py3 import ResourceSkusResult
    from ._models_py3 import Restriction
    from ._models_py3 import StorageTarget
    from ._models_py3 import StorageTargetResource
    from ._models_py3 import StorageTargetsResult
    from ._models_py3 import SystemData
    from ._models_py3 import UsageModel
    from ._models_py3 import UsageModelDisplay
    from ._models_py3 import UsageModelsResult
except (SyntaxError, ImportError):
    from ._models import ASCOperation  # type: ignore
    from ._models import ApiOperation  # type: ignore
    from ._models import ApiOperationDisplay  # type: ignore
    from ._models import ApiOperationListResult  # type: ignore
    from ._models import ApiOperationPropertiesServiceSpecification  # type: ignore
    from ._models import Cache  # type: ignore
    from ._models import CacheActiveDirectorySettingsCredentials  # type: ignore
    from ._models import CacheHealth  # type: ignore
    from ._models import CacheUpgradeStatus  # type: ignore
    from ._models import CacheUsernameDownloadSettingsCredentials  # type: ignore
    from ._models import CachesListResult  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import MetricDimension  # type: ignore
    from ._models import MetricSpecification  # type: ignore
    from ._models import NamespaceJunction  # type: ignore
    from ._models import Nfs3Target  # type: ignore
    from ._models import NfsAccessPolicy  # type: ignore
    from ._models import NfsAccessRule  # type: ignore
    from ._models import ResourceSku  # type: ignore
    from ._models import ResourceSkuCapabilities  # type: ignore
    from ._models import ResourceSkuLocationInfo  # type: ignore
    from ._models import ResourceSkusResult  # type: ignore
    from ._models import Restriction  # type: ignore
    from ._models import StorageTarget  # type: ignore
    from ._models import StorageTargetResource  # type: ignore
    from ._models import StorageTargetsResult  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import UsageModel  # type: ignore
    from ._models import UsageModelDisplay  # type: ignore
    from ._models import UsageModelsResult  # type: ignore

from ._storage_cache_management_client_enums import (
    CacheIdentityType,
    CreatedByType,
    DomainJoinedType,
    FirmwareStatusType,
    HealthStateType,
    MetricAggregationType,
    NfsAccessRuleAccess,
    NfsAccessRuleScope,
    ProvisioningStateType,
    ReasonCode,
    StorageTargetType,
    UsernameDownloadedType,
    UsernameSource,
)

__all__ = [
    'ASCOperation',
    'ApiOperation',
    'ApiOperationDisplay',
    'ApiOperationListResult',
    'ApiOperationPropertiesServiceSpecification',
    'Cache',
    'CacheActiveDirectorySettingsCredentials',
    'CacheHealth',
    'CacheUpgradeStatus',
    'CacheUsernameDownloadSettingsCredentials',
    'CachesListResult',
    'CloudErrorBody',
    'ErrorResponse',
    'MetricDimension',
    'MetricSpecification',
    'NamespaceJunction',
    'Nfs3Target',
    'NfsAccessPolicy',
    'NfsAccessRule',
    'ResourceSku',
    'ResourceSkuCapabilities',
    'ResourceSkuLocationInfo',
    'ResourceSkusResult',
    'Restriction',
    'StorageTarget',
    'StorageTargetResource',
    'StorageTargetsResult',
    'SystemData',
    'UsageModel',
    'UsageModelDisplay',
    'UsageModelsResult',
    'CacheIdentityType',
    'CreatedByType',
    'DomainJoinedType',
    'FirmwareStatusType',
    'HealthStateType',
    'MetricAggregationType',
    'NfsAccessRuleAccess',
    'NfsAccessRuleScope',
    'ProvisioningStateType',
    'ReasonCode',
    'StorageTargetType',
    'UsernameDownloadedType',
    'UsernameSource',
]
