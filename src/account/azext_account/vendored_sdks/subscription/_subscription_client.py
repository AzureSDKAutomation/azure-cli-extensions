# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import SubscriptionClientConfiguration
from .operations import SubscriptionsOperations
from .operations import TenantsOperations
from .operations import SubscriptionOperations
from .operations import SubscriptionOperationOperations
from .operations import Operations
from .operations import SubscriptionPolicyOperations
from .operations import BillingAccountOperations
from . import models


class SubscriptionClient(object):
    """The subscription client.

    :ivar subscriptions: SubscriptionsOperations operations
    :vartype subscriptions: subscription_client.operations.SubscriptionsOperations
    :ivar tenants: TenantsOperations operations
    :vartype tenants: subscription_client.operations.TenantsOperations
    :ivar subscription: SubscriptionOperations operations
    :vartype subscription: subscription_client.operations.SubscriptionOperations
    :ivar subscription_operation: SubscriptionOperationOperations operations
    :vartype subscription_operation: subscription_client.operations.SubscriptionOperationOperations
    :ivar operations: Operations operations
    :vartype operations: subscription_client.operations.Operations
    :ivar subscription_policy: SubscriptionPolicyOperations operations
    :vartype subscription_policy: subscription_client.operations.SubscriptionPolicyOperations
    :ivar billing_account: BillingAccountOperations operations
    :vartype billing_account: subscription_client.operations.BillingAccountOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SubscriptionClientConfiguration(credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.subscriptions = SubscriptionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tenants = TenantsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription = SubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription_operation = SubscriptionOperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription_policy = SubscriptionPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.billing_account = BillingAccountOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> SubscriptionClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
