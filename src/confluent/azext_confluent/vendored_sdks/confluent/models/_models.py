# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ConfluentAgreementProperties(msrest.serialization.Model):
    """Terms properties for Marketplace and Confluent.

    :param publisher: Publisher identifier string.
    :type publisher: str
    :param product: Product identifier string.
    :type product: str
    :param plan: Plan identifier string.
    :type plan: str
    :param license_text_link: Link to HTML with Microsoft and Publisher terms.
    :type license_text_link: str
    :param privacy_policy_link: Link to the privacy policy of the publisher.
    :type privacy_policy_link: str
    :param retrieve_datetime: Date and time in UTC of when the terms were accepted. This is empty
     if Accepted is false.
    :type retrieve_datetime: ~datetime.datetime
    :param signature: Terms signature.
    :type signature: str
    :param accepted: If any version of the terms have been accepted, otherwise false.
    :type accepted: bool
    """

    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'plan': {'key': 'plan', 'type': 'str'},
        'license_text_link': {'key': 'licenseTextLink', 'type': 'str'},
        'privacy_policy_link': {'key': 'privacyPolicyLink', 'type': 'str'},
        'retrieve_datetime': {'key': 'retrieveDatetime', 'type': 'iso-8601'},
        'signature': {'key': 'signature', 'type': 'str'},
        'accepted': {'key': 'accepted', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfluentAgreementProperties, self).__init__(**kwargs)
        self.publisher = kwargs.get('publisher', None)
        self.product = kwargs.get('product', None)
        self.plan = kwargs.get('plan', None)
        self.license_text_link = kwargs.get('license_text_link', None)
        self.privacy_policy_link = kwargs.get('privacy_policy_link', None)
        self.retrieve_datetime = kwargs.get('retrieve_datetime', None)
        self.signature = kwargs.get('signature', None)
        self.accepted = kwargs.get('accepted', None)


class ConfluentAgreementResource(msrest.serialization.Model):
    """Agreement Terms definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ARM id of the resource.
    :vartype id: str
    :ivar name: The name of the agreement.
    :vartype name: str
    :ivar type: The type of the agreement.
    :vartype type: str
    :param properties: Represents the properties of the resource.
    :type properties: ~azure.mgmt.confluent.models.ConfluentAgreementProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ConfluentAgreementProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfluentAgreementResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = kwargs.get('properties', None)


class ConfluentAgreementResourceListResponse(msrest.serialization.Model):
    """Response of a agreements operation.

    :param value: Results of a list operation.
    :type value: list[~azure.mgmt.confluent.models.ConfluentAgreementResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConfluentAgreementResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfluentAgreementResourceListResponse, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class ErrorResponseBody(msrest.serialization.Model):
    """Response body of Error.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message.
    :vartype message: str
    :ivar target: Error target.
    :vartype target: str
    :ivar details: Error detail.
    :vartype details: list[~azure.mgmt.confluent.models.ErrorResponseBody]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'target': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponseBody]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponseBody, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None


class OfferDetail(msrest.serialization.Model):
    """Confluent Offer detail.

    :param publisher_id: Publisher Id.
    :type publisher_id: str
    :param id: Offer Id.
    :type id: str
    :param plan_id: Offer Plan Id.
    :type plan_id: str
    :param plan_name: Offer Plan Name.
    :type plan_name: str
    :param term_unit: Offer Plan Term unit.
    :type term_unit: str
    :param status: SaaS Offer Status. Possible values include: "Started",
     "PendingFulfillmentStart", "InProgress", "Subscribed", "Suspended", "Reinstated", "Succeeded",
     "Failed", "Unsubscribed", "Updating".
    :type status: str or ~azure.mgmt.confluent.models.SaaSOfferStatus
    """

    _validation = {
        'publisher_id': {'max_length': 50, 'min_length': 0},
        'id': {'max_length': 50, 'min_length': 0},
        'plan_id': {'max_length': 50, 'min_length': 0},
        'plan_name': {'max_length': 50, 'min_length': 0},
        'term_unit': {'max_length': 25, 'min_length': 0},
    }

    _attribute_map = {
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_name': {'key': 'planName', 'type': 'str'},
        'term_unit': {'key': 'termUnit', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OfferDetail, self).__init__(**kwargs)
        self.publisher_id = kwargs.get('publisher_id', None)
        self.id = kwargs.get('id', None)
        self.plan_id = kwargs.get('plan_id', None)
        self.plan_name = kwargs.get('plan_name', None)
        self.term_unit = kwargs.get('term_unit', None)
        self.status = kwargs.get('status', None)


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider: Microsoft.Confluent.
    :type provider: str
    :param resource: Type on which the operation is performed, e.g., 'clusters'.
    :type resource: str
    :param operation: Operation type, e.g., read, write, delete, etc.
    :type operation: str
    :param description: Description of the operation, e.g., 'Write confluent'.
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
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationListResult(msrest.serialization.Model):
    """Result of GET request to list Confluent operations.

    :param value: List of Confluent operations supported by the Microsoft.Confluent provider.
    :type value: list[~azure.mgmt.confluent.models.OperationResult]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationResult]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class OperationResult(msrest.serialization.Model):
    """An Confluent REST API operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~azure.mgmt.confluent.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationResult, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OrganizationResource(msrest.serialization.Model):
    """Organization resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ARM id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: A set of tags. Organization resource tags.
    :type tags: dict[str, str]
    :param location: Location of Organization resource.
    :type location: str
    :ivar created_time: The creation time of the resource.
    :vartype created_time: ~datetime.datetime
    :param provisioning_state: Provision states for confluent RP. Possible values include:
     "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted",
     "NotSpecified".
    :type provisioning_state: str or ~azure.mgmt.confluent.models.ProvisionState
    :ivar organization_id: Id of the Confluent organization.
    :vartype organization_id: str
    :ivar sso_url: SSO url for the Confluent organization.
    :vartype sso_url: str
    :param offer_detail: Confluent offer detail.
    :type offer_detail: ~azure.mgmt.confluent.models.OfferDetail
    :param user_detail: Subscriber detail.
    :type user_detail: ~azure.mgmt.confluent.models.UserDetail
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'created_time': {'readonly': True},
        'organization_id': {'readonly': True},
        'sso_url': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'created_time': {'key': 'properties.createdTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'organization_id': {'key': 'properties.organizationId', 'type': 'str'},
        'sso_url': {'key': 'properties.ssoUrl', 'type': 'str'},
        'offer_detail': {'key': 'properties.offerDetail', 'type': 'OfferDetail'},
        'user_detail': {'key': 'properties.userDetail', 'type': 'UserDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrganizationResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)
        self.created_time = None
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.organization_id = None
        self.sso_url = None
        self.offer_detail = kwargs.get('offer_detail', None)
        self.user_detail = kwargs.get('user_detail', None)


class OrganizationResourceListResult(msrest.serialization.Model):
    """The response of a list operation.

    :param value: Result of a list operation.
    :type value: list[~azure.mgmt.confluent.models.OrganizationResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OrganizationResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrganizationResourceListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class OrganizationResourceProperties(msrest.serialization.Model):
    """Organization resource property.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar created_time: The creation time of the resource.
    :vartype created_time: ~datetime.datetime
    :param provisioning_state: Provision states for confluent RP. Possible values include:
     "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted",
     "NotSpecified".
    :type provisioning_state: str or ~azure.mgmt.confluent.models.ProvisionState
    :ivar organization_id: Id of the Confluent organization.
    :vartype organization_id: str
    :ivar sso_url: SSO url for the Confluent organization.
    :vartype sso_url: str
    :param offer_detail: Confluent offer detail.
    :type offer_detail: ~azure.mgmt.confluent.models.OfferDetail
    :param user_detail: Subscriber detail.
    :type user_detail: ~azure.mgmt.confluent.models.UserDetail
    """

    _validation = {
        'created_time': {'readonly': True},
        'organization_id': {'readonly': True},
        'sso_url': {'readonly': True},
    }

    _attribute_map = {
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'organization_id': {'key': 'organizationId', 'type': 'str'},
        'sso_url': {'key': 'ssoUrl', 'type': 'str'},
        'offer_detail': {'key': 'offerDetail', 'type': 'OfferDetail'},
        'user_detail': {'key': 'userDetail', 'type': 'UserDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrganizationResourceProperties, self).__init__(**kwargs)
        self.created_time = None
        self.provisioning_state = kwargs.get('provisioning_state', None)
        self.organization_id = None
        self.sso_url = None
        self.offer_detail = kwargs.get('offer_detail', None)
        self.user_detail = kwargs.get('user_detail', None)


class OrganizationResourcePropertiesautogenerated(OrganizationResourceProperties):
    """Organization resource properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar created_time: The creation time of the resource.
    :vartype created_time: ~datetime.datetime
    :param provisioning_state: Provision states for confluent RP. Possible values include:
     "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted",
     "NotSpecified".
    :type provisioning_state: str or ~azure.mgmt.confluent.models.ProvisionState
    :ivar organization_id: Id of the Confluent organization.
    :vartype organization_id: str
    :ivar sso_url: SSO url for the Confluent organization.
    :vartype sso_url: str
    :param offer_detail: Confluent offer detail.
    :type offer_detail: ~azure.mgmt.confluent.models.OfferDetail
    :param user_detail: Subscriber detail.
    :type user_detail: ~azure.mgmt.confluent.models.UserDetail
    """

    _validation = {
        'created_time': {'readonly': True},
        'organization_id': {'readonly': True},
        'sso_url': {'readonly': True},
    }

    _attribute_map = {
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'organization_id': {'key': 'organizationId', 'type': 'str'},
        'sso_url': {'key': 'ssoUrl', 'type': 'str'},
        'offer_detail': {'key': 'offerDetail', 'type': 'OfferDetail'},
        'user_detail': {'key': 'userDetail', 'type': 'UserDetail'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrganizationResourcePropertiesautogenerated, self).__init__(**kwargs)


class OrganizationResourcePropertiesOfferDetail(OfferDetail):
    """Confluent offer detail.

    :param publisher_id: Publisher Id.
    :type publisher_id: str
    :param id: Offer Id.
    :type id: str
    :param plan_id: Offer Plan Id.
    :type plan_id: str
    :param plan_name: Offer Plan Name.
    :type plan_name: str
    :param term_unit: Offer Plan Term unit.
    :type term_unit: str
    :param status: SaaS Offer Status. Possible values include: "Started",
     "PendingFulfillmentStart", "InProgress", "Subscribed", "Suspended", "Reinstated", "Succeeded",
     "Failed", "Unsubscribed", "Updating".
    :type status: str or ~azure.mgmt.confluent.models.SaaSOfferStatus
    """

    _validation = {
        'publisher_id': {'max_length': 50, 'min_length': 0},
        'id': {'max_length': 50, 'min_length': 0},
        'plan_id': {'max_length': 50, 'min_length': 0},
        'plan_name': {'max_length': 50, 'min_length': 0},
        'term_unit': {'max_length': 25, 'min_length': 0},
    }

    _attribute_map = {
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'plan_name': {'key': 'planName', 'type': 'str'},
        'term_unit': {'key': 'termUnit', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrganizationResourcePropertiesOfferDetail, self).__init__(**kwargs)


class UserDetail(msrest.serialization.Model):
    """Subscriber detail.

    :param first_name: First name.
    :type first_name: str
    :param last_name: Last name.
    :type last_name: str
    :param email_address: Email address.
    :type email_address: str
    """

    _validation = {
        'first_name': {'max_length': 50, 'min_length': 0},
        'last_name': {'max_length': 50, 'min_length': 0},
        'email_address': {'pattern': r'^\S+@\S+\.\S+$'},
    }

    _attribute_map = {
        'first_name': {'key': 'firstName', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UserDetail, self).__init__(**kwargs)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.email_address = kwargs.get('email_address', None)


class OrganizationResourcePropertiesUserDetail(UserDetail):
    """Subscriber detail.

    :param first_name: First name.
    :type first_name: str
    :param last_name: Last name.
    :type last_name: str
    :param email_address: Email address.
    :type email_address: str
    """

    _validation = {
        'first_name': {'max_length': 50, 'min_length': 0},
        'last_name': {'max_length': 50, 'min_length': 0},
        'email_address': {'pattern': r'^\S+@\S+\.\S+$'},
    }

    _attribute_map = {
        'first_name': {'key': 'firstName', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrganizationResourcePropertiesUserDetail, self).__init__(**kwargs)


class OrganizationResourceUpdate(msrest.serialization.Model):
    """Organization Resource update.

    :param tags: A set of tags. ARM resource tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OrganizationResourceUpdate, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class ResourceProviderDefaultErrorResponse(msrest.serialization.Model):
    """Default error response for resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar error: Response body of Error.
    :vartype error: ~azure.mgmt.confluent.models.ErrorResponseBody
    """

    _validation = {
        'error': {'readonly': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseBody'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceProviderDefaultErrorResponse, self).__init__(**kwargs)
        self.error = None
