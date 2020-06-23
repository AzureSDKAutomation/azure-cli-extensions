# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._customproviders_enums import *


class Association(msrest.serialization.Model):
    """The resource definition of this association.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The association id.
    :vartype id: str
    :ivar name: The association name.
    :vartype name: str
    :ivar type: The association type.
    :vartype type: str
    :param target_resource_id: The REST resource instance of the target resource for this
     association.
    :type target_resource_id: str
    :ivar provisioning_state: The provisioning state of the association. Possible values include:
     "Accepted", "Deleting", "Running", "Succeeded", "Failed".
    :vartype provisioning_state: str or ~customproviders.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'target_resource_id': {'key': 'properties.targetResourceId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        target_resource_id: Optional[str] = None,
        **kwargs
    ):
        super(Association, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.target_resource_id = target_resource_id
        self.provisioning_state = None


class AssociationsList(msrest.serialization.Model):
    """List of associations.

    :param value: The array of associations.
    :type value: list[~customproviders.models.Association]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Association]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["Association"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(AssociationsList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class CustomRPRouteDefinition(msrest.serialization.Model):
    """A route definition that defines an action or resource that can be interacted with through the custom resource provider.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the route definition. This becomes the name for the ARM
     extension (e.g.
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
    :type name: str
    :param endpoint: Required. The route definition endpoint URI that the custom resource provider
     will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or
     can specify to route via a path (e.g. 'https://testendpoint/{requestPath}').
    :type endpoint: str
    """

    _validation = {
        'name': {'required': True},
        'endpoint': {'required': True, 'pattern': r'^https://.+'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        endpoint: str,
        **kwargs
    ):
        super(CustomRPRouteDefinition, self).__init__(**kwargs)
        self.name = name
        self.endpoint = endpoint


class CustomRPActionRouteDefinition(CustomRPRouteDefinition):
    """The route definition for an action implemented by the custom resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the route definition. This becomes the name for the ARM
     extension (e.g.
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
    :type name: str
    :param endpoint: Required. The route definition endpoint URI that the custom resource provider
     will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or
     can specify to route via a path (e.g. 'https://testendpoint/{requestPath}').
    :type endpoint: str
    :ivar routing_type: The routing types that are supported for action requests. Default value:
     "Proxy".
    :vartype routing_type: str
    """

    _validation = {
        'name': {'required': True},
        'endpoint': {'required': True, 'pattern': r'^https://.+'},
        'routing_type': {'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'routing_type': {'key': 'routingType', 'type': 'str'},
    }

    routing_type = "Proxy"

    def __init__(
        self,
        *,
        name: str,
        endpoint: str,
        **kwargs
    ):
        super(CustomRPActionRouteDefinition, self).__init__(name=name, endpoint=endpoint, **kwargs)


class Resource(msrest.serialization.Model):
    """The resource definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class CustomRPManifest(Resource):
    """A manifest file that defines the custom resource provider resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param actions: A list of actions that the custom resource provider implements.
    :type actions: list[~customproviders.models.CustomRPActionRouteDefinition]
    :param resource_types: A list of resource types that the custom resource provider implements.
    :type resource_types: list[~customproviders.models.CustomRPResourceTypeRouteDefinition]
    :param validations: A list of validations to run on the custom resource provider's requests.
    :type validations: list[~customproviders.models.CustomRPValidations]
    :ivar provisioning_state: The provisioning state of the resource provider. Possible values
     include: "Accepted", "Deleting", "Running", "Succeeded", "Failed".
    :vartype provisioning_state: str or ~customproviders.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'actions': {'key': 'properties.actions', 'type': '[CustomRPActionRouteDefinition]'},
        'resource_types': {'key': 'properties.resourceTypes', 'type': '[CustomRPResourceTypeRouteDefinition]'},
        'validations': {'key': 'properties.validations', 'type': '[CustomRPValidations]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        actions: Optional[List["CustomRPActionRouteDefinition"]] = None,
        resource_types: Optional[List["CustomRPResourceTypeRouteDefinition"]] = None,
        validations: Optional[List["CustomRPValidations"]] = None,
        **kwargs
    ):
        super(CustomRPManifest, self).__init__(location=location, tags=tags, **kwargs)
        self.actions = actions
        self.resource_types = resource_types
        self.validations = validations
        self.provisioning_state = None


class CustomRPResourceTypeRouteDefinition(CustomRPRouteDefinition):
    """The route definition for a resource implemented by the custom resource provider.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the route definition. This becomes the name for the ARM
     extension (e.g.
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
    :type name: str
    :param endpoint: Required. The route definition endpoint URI that the custom resource provider
     will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or
     can specify to route via a path (e.g. 'https://testendpoint/{requestPath}').
    :type endpoint: str
    :param routing_type: The routing types that are supported for resource requests. Possible
     values include: "Proxy", "Proxy,Cache".
    :type routing_type: str or ~customproviders.models.ResourceTypeRouting
    """

    _validation = {
        'name': {'required': True},
        'endpoint': {'required': True, 'pattern': r'^https://.+'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'routing_type': {'key': 'routingType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        endpoint: str,
        routing_type: Optional[Union[str, "ResourceTypeRouting"]] = None,
        **kwargs
    ):
        super(CustomRPResourceTypeRouteDefinition, self).__init__(name=name, endpoint=endpoint, **kwargs)
        self.routing_type = routing_type


class CustomRPValidations(msrest.serialization.Model):
    """A validation to apply on custom resource provider requests.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar validation_type: The type of validation to run against a matching request. Default value:
     "Swagger".
    :vartype validation_type: str
    :param specification: Required. A link to the validation specification. The specification must
     be hosted on raw.githubusercontent.com.
    :type specification: str
    """

    _validation = {
        'validation_type': {'constant': True},
        'specification': {'required': True, 'pattern': r'^https://raw.githubusercontent.com/.+'},
    }

    _attribute_map = {
        'validation_type': {'key': 'validationType', 'type': 'str'},
        'specification': {'key': 'specification', 'type': 'str'},
    }

    validation_type = "Swagger"

    def __init__(
        self,
        *,
        specification: str,
        **kwargs
    ):
        super(CustomRPValidations, self).__init__(**kwargs)
        self.specification = specification


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details: list[~customproviders.models.ErrorDefinition]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :param error: The error details.
    :type error: ~customproviders.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorDefinition"] = None,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = error


class ListByCustomRPManifest(msrest.serialization.Model):
    """List of custom resource providers.

    :param value: The array of custom resource provider manifests.
    :type value: list[~customproviders.models.CustomRPManifest]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CustomRPManifest]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["CustomRPManifest"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ListByCustomRPManifest, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ResourceProviderOperation(msrest.serialization.Model):
    """Supported operations of this resource provider.

    :param name: Operation name, in format of {provider}/{resource}/{operation}.
    :type name: str
    :param display: Display metadata associated with the operation.
    :type display: ~customproviders.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["ResourceProviderOperationDisplay"] = None,
        **kwargs
    ):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :param provider: Resource provider: Microsoft Custom Providers.
    :type provider: str
    :param resource: Resource on which the operation is performed.
    :type resource: str
    :param operation: Type of operation: get, read, delete, etc.
    :type operation: str
    :param description: Description of this operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class ResourceProviderOperationList(msrest.serialization.Model):
    """Results of the request to list operations.

    :param value: List of operations supported by this resource provider.
    :type value: list[~customproviders.models.ResourceProviderOperation]
    :param next_link: The URL to use for getting the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ResourceProviderOperation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ResourceProvidersUpdate(msrest.serialization.Model):
    """custom resource provider update information.

    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(ResourceProvidersUpdate, self).__init__(**kwargs)
        self.tags = tags
