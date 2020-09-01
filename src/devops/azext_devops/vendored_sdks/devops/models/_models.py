# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class CloudErrorBody(msrest.serialization.Model):
    """An error response from the Pipelines Resource Provider.

    :param code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable for display in a user
     interface.
    :type message: str
    :param target: The target of the particular error. For example, the name of the property in
     error or the method where the error occurred.
    :type target: str
    :param details: A list of additional details about the error.
    :type details: list[~azure_dev_ops.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)


class InputDescriptor(msrest.serialization.Model):
    """Representation of a pipeline template input parameter.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Identifier of the input parameter.
    :type id: str
    :param description: Description of the input parameter.
    :type description: str
    :param type: Required. Data type of the value of the input parameter. Possible values include:
     "String", "SecureString", "Int", "Bool", "Authorization".
    :type type: str or ~azure_dev_ops.models.InputDataType
    :param possible_values: List of possible values for the input parameter.
    :type possible_values: list[~azure_dev_ops.models.InputValue]
    """

    _validation = {
        'id': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'possible_values': {'key': 'possibleValues', 'type': '[InputValue]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InputDescriptor, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.description = kwargs.get('description', None)
        self.type = kwargs['type']
        self.possible_values = kwargs.get('possible_values', None)


class InputValue(msrest.serialization.Model):
    """Representation of a pipeline template input parameter value.

    :param value: Value of an input parameter.
    :type value: str
    :param display_value: Description of the input parameter value.
    :type display_value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'display_value': {'key': 'displayValue', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InputValue, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.display_value = kwargs.get('display_value', None)


class Operation(msrest.serialization.Model):
    """Properties of an Operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the operation.
    :vartype name: str
    :param is_data_action: Indicates whether the operation applies to data-plane.
    :type is_data_action: str
    :ivar operation: Friendly name of the operation.
    :vartype operation: str
    :ivar resource: Friendly name of the resource type the operation applies to.
    :vartype resource: str
    :ivar description: Friendly description of the operation.
    :vartype description: str
    :ivar provider: Friendly name of the resource provider.
    :vartype provider: str
    """

    _validation = {
        'name': {'readonly': True},
        'operation': {'readonly': True},
        'resource': {'readonly': True},
        'description': {'readonly': True},
        'provider': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'str'},
        'operation': {'key': 'display.operation', 'type': 'str'},
        'resource': {'key': 'display.resource', 'type': 'str'},
        'description': {'key': 'display.description', 'type': 'str'},
        'provider': {'key': 'display.provider', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.is_data_action = kwargs.get('is_data_action', None)
        self.operation = None
        self.resource = None
        self.description = None
        self.provider = None


class OperationListResult(msrest.serialization.Model):
    """Result of a request to list all operations supported by Microsoft.DevOps resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of operations supported by Microsoft.DevOps resource provider.
    :vartype value: list[~azure_dev_ops.models.Operation]
    :param next_link: The URL to get the next set of operations, if there are any.
    :type next_link: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = kwargs.get('next_link', None)


class Resource(msrest.serialization.Model):
    """An Azure Resource Manager (ARM) resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar type: Resource Type.
    :vartype type: str
    :param tags: A set of tags. Resource Tags.
    :type tags: dict[str, str]
    :param location: Resource Location.
    :type location: str
    :ivar name: Resource Name.
    :vartype name: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.location = kwargs.get('location', None)
        self.name = None


class Pipeline(Resource):
    """Azure DevOps Pipeline used to configure Continuous Integration (CI) & Continuous Delivery (CD) for Azure resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar type: Resource Type.
    :vartype type: str
    :param tags: A set of tags. Resource Tags.
    :type tags: dict[str, str]
    :param location: Resource Location.
    :type location: str
    :ivar name: Resource Name.
    :vartype name: str
    :ivar pipeline_id: Unique identifier of the Azure Pipeline within the Azure DevOps Project.
    :vartype pipeline_id: int
    :param id_properties_bootstrap_configuration_template_id: Required. Unique identifier of the
     pipeline template.
    :type id_properties_bootstrap_configuration_template_id: str
    :param parameters_properties_bootstrap_configuration_template_parameters: Dictionary of input
     parameters used in the pipeline template.
    :type parameters_properties_bootstrap_configuration_template_parameters: dict[str, str]
    :param repository_type: Type of code repository. Possible values include: "gitHub", "vstsGit".
    :type repository_type: str or ~azure_dev_ops.models.CodeRepositoryType
    :param id_properties_bootstrap_configuration_repository_id: Unique immutable identifier of the
     code repository.
    :type id_properties_bootstrap_configuration_repository_id: str
    :param default_branch: Default branch used to configure Continuous Integration (CI) in the
     pipeline.
    :type default_branch: str
    :param properties: Repository-specific properties.
    :type properties: dict[str, str]
    :ivar authorization_type: Type of authorization. Default value: "personalAccessToken".
    :vartype authorization_type: str
    :param parameters_properties_bootstrap_configuration_repository_authorization_parameters:
     Authorization parameters corresponding to the authorization type.
    :type parameters_properties_bootstrap_configuration_repository_authorization_parameters:
     dict[str, str]
    :ivar id_properties_project_id: Unique immutable identifier of the Azure DevOps Project.
    :vartype id_properties_project_id: str
    :param name_properties_project_name: Required. Name of the Azure DevOps Project.
    :type name_properties_project_name: str
    :ivar id_properties_organization_id: Unique immutable identifier for the Azure DevOps
     Organization.
    :vartype id_properties_organization_id: str
    :param name_properties_organization_name: Required. Name of the Azure DevOps Organization.
    :type name_properties_organization_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'pipeline_id': {'readonly': True},
        'id_properties_bootstrap_configuration_template_id': {'required': True},
        'authorization_type': {'constant': True},
        'id_properties_project_id': {'readonly': True},
        'name_properties_project_name': {'required': True},
        'id_properties_organization_id': {'readonly': True},
        'name_properties_organization_name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'pipeline_id': {'key': 'properties.pipelineId', 'type': 'int'},
        'id_properties_bootstrap_configuration_template_id': {'key': 'properties.bootstrapConfiguration.template.id', 'type': 'str'},
        'parameters_properties_bootstrap_configuration_template_parameters': {'key': 'properties.bootstrapConfiguration.template.parameters', 'type': '{str}'},
        'repository_type': {'key': 'properties.bootstrapConfiguration.repository.repositoryType', 'type': 'str'},
        'id_properties_bootstrap_configuration_repository_id': {'key': 'properties.bootstrapConfiguration.repository.id', 'type': 'str'},
        'default_branch': {'key': 'properties.bootstrapConfiguration.repository.defaultBranch', 'type': 'str'},
        'properties': {'key': 'properties.bootstrapConfiguration.repository.properties', 'type': '{str}'},
        'authorization_type': {'key': 'properties.bootstrapConfiguration.repository.authorization.authorizationType', 'type': 'str'},
        'parameters_properties_bootstrap_configuration_repository_authorization_parameters': {'key': 'properties.bootstrapConfiguration.repository.authorization.parameters', 'type': '{str}'},
        'id_properties_project_id': {'key': 'properties.project.id', 'type': 'str'},
        'name_properties_project_name': {'key': 'properties.project.name', 'type': 'str'},
        'id_properties_organization_id': {'key': 'properties.organization.id', 'type': 'str'},
        'name_properties_organization_name': {'key': 'properties.organization.name', 'type': 'str'},
    }

    authorization_type = "personalAccessToken"

    def __init__(
        self,
        **kwargs
    ):
        super(Pipeline, self).__init__(**kwargs)
        self.pipeline_id = None
        self.id_properties_bootstrap_configuration_template_id = kwargs['id_properties_bootstrap_configuration_template_id']
        self.parameters_properties_bootstrap_configuration_template_parameters = kwargs.get('parameters_properties_bootstrap_configuration_template_parameters', None)
        self.repository_type = kwargs.get('repository_type', None)
        self.id_properties_bootstrap_configuration_repository_id = kwargs.get('id_properties_bootstrap_configuration_repository_id', None)
        self.default_branch = kwargs.get('default_branch', None)
        self.properties = kwargs.get('properties', None)
        self.parameters_properties_bootstrap_configuration_repository_authorization_parameters = kwargs.get('parameters_properties_bootstrap_configuration_repository_authorization_parameters', None)
        self.id_properties_project_id = None
        self.name_properties_project_name = kwargs['name_properties_project_name']
        self.id_properties_organization_id = None
        self.name_properties_organization_name = kwargs['name_properties_organization_name']


class PipelineListResult(msrest.serialization.Model):
    """Result of a request to list all Azure Pipelines under a given scope.

    :param value: List of pipelines.
    :type value: list[~azure_dev_ops.models.Pipeline]
    :param next_link: URL to get the next set of Pipelines, if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Pipeline]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PipelineListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class PipelineTemplateDefinition(msrest.serialization.Model):
    """Definition of a pipeline template.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. Unique identifier of the pipeline template.
    :type id: str
    :param description: Description of the pipeline enabled by the template.
    :type description: str
    :param inputs: List of input parameters required by the template to create a pipeline.
    :type inputs: list[~azure_dev_ops.models.InputDescriptor]
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '[InputDescriptor]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PipelineTemplateDefinition, self).__init__(**kwargs)
        self.id = kwargs['id']
        self.description = kwargs.get('description', None)
        self.inputs = kwargs.get('inputs', None)


class PipelineTemplateDefinitionListResult(msrest.serialization.Model):
    """Result of a request to list all pipeline template definitions.

    :param value: List of pipeline template definitions.
    :type value: list[~azure_dev_ops.models.PipelineTemplateDefinition]
    :param next_link: The URL to get the next set of pipeline template definitions, if there are
     any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PipelineTemplateDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PipelineTemplateDefinitionListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class PipelineUpdateParameters(msrest.serialization.Model):
    """Request payload used to update an existing Azure Pipeline.

    :param tags: A set of tags. Dictionary of key-value pairs to be set as tags on the Azure
     Pipeline. This will overwrite any existing tags.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PipelineUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
