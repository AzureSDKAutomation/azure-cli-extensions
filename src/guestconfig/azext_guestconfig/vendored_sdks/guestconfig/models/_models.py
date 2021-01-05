# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AssignmentInfo(msrest.serialization.Model):
    """Information about the guest configuration assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the guest configuration assignment.
    :vartype name: str
    :param configuration: Information about the configuration.
    :type configuration: ~guest_configuration_client.models.ConfigurationInfo
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'ConfigurationInfo'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AssignmentInfo, self).__init__(**kwargs)
        self.name = None
        self.configuration = kwargs.get('configuration', None)


class AssignmentReport(msrest.serialization.Model):
    """AssignmentReport.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the report for the guest configuration assignment.
    :vartype id: str
    :ivar report_id: GUID that identifies the guest configuration assignment report under a
     subscription, resource group.
    :vartype report_id: str
    :param assignment: Configuration details of the guest configuration assignment.
    :type assignment: ~guest_configuration_client.models.AssignmentInfo
    :param vm: Information about the VM.
    :type vm: ~guest_configuration_client.models.VmInfo
    :ivar start_time: Start date and time of the guest configuration assignment compliance status
     check.
    :vartype start_time: ~datetime.datetime
    :ivar end_time: End date and time of the guest configuration assignment compliance status
     check.
    :vartype end_time: ~datetime.datetime
    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~guest_configuration_client.models.ComplianceStatus
    :ivar operation_type: Type of report, Consistency or Initial. Possible values include:
     "Consistency", "Initial".
    :vartype operation_type: str or ~guest_configuration_client.models.Type
    :param resources: The list of resources for which guest configuration assignment compliance is
     checked.
    :type resources: list[~guest_configuration_client.models.AssignmentReportResource]
    """

    _validation = {
        'id': {'readonly': True},
        'report_id': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'compliance_status': {'readonly': True},
        'operation_type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'report_id': {'key': 'reportId', 'type': 'str'},
        'assignment': {'key': 'assignment', 'type': 'AssignmentInfo'},
        'vm': {'key': 'vm', 'type': 'VmInfo'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[AssignmentReportResource]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AssignmentReport, self).__init__(**kwargs)
        self.id = None
        self.report_id = None
        self.assignment = kwargs.get('assignment', None)
        self.vm = kwargs.get('vm', None)
        self.start_time = None
        self.end_time = None
        self.compliance_status = None
        self.operation_type = None
        self.resources = kwargs.get('resources', None)


class AssignmentReportDetails(msrest.serialization.Model):
    """Details of the guest configuration assignment report.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~guest_configuration_client.models.ComplianceStatus
    :ivar start_time: Start date and time of the guest configuration assignment compliance status
     check.
    :vartype start_time: ~datetime.datetime
    :ivar end_time: End date and time of the guest configuration assignment compliance status
     check.
    :vartype end_time: ~datetime.datetime
    :ivar job_id: GUID of the report.
    :vartype job_id: str
    :ivar operation_type: Type of report, Consistency or Initial. Possible values include:
     "Consistency", "Initial".
    :vartype operation_type: str or ~guest_configuration_client.models.Type
    :param resources: The list of resources for which guest configuration assignment compliance is
     checked.
    :type resources: list[~guest_configuration_client.models.AssignmentReportResource]
    """

    _validation = {
        'compliance_status': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'job_id': {'readonly': True},
        'operation_type': {'readonly': True},
    }

    _attribute_map = {
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[AssignmentReportResource]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AssignmentReportDetails, self).__init__(**kwargs)
        self.compliance_status = None
        self.start_time = None
        self.end_time = None
        self.job_id = None
        self.operation_type = None
        self.resources = kwargs.get('resources', None)


class AssignmentReportResource(msrest.serialization.Model):
    """The guest configuration assignment resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~guest_configuration_client.models.ComplianceStatus
    :ivar resource_id: Name of the guest configuration assignment resource setting.
    :vartype resource_id: str
    :param reasons: Compliance reason and reason code for a resource.
    :type reasons:
     list[~guest_configuration_client.models.AssignmentReportResourceComplianceReason]
    :ivar properties: Properties of a guest configuration assignment resource.
    :vartype properties: object
    """

    _validation = {
        'compliance_status': {'readonly': True},
        'resource_id': {'readonly': True},
        'properties': {'readonly': True},
    }

    _attribute_map = {
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'reasons': {'key': 'reasons', 'type': '[AssignmentReportResourceComplianceReason]'},
        'properties': {'key': 'properties', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AssignmentReportResource, self).__init__(**kwargs)
        self.compliance_status = None
        self.resource_id = None
        self.reasons = kwargs.get('reasons', None)
        self.properties = None


class AssignmentReportResourceComplianceReason(msrest.serialization.Model):
    """Reason and code for the compliance of the guest configuration assignment resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar phrase: Reason for the compliance of the guest configuration assignment resource.
    :vartype phrase: str
    :ivar code: Code for the compliance of the guest configuration assignment resource.
    :vartype code: str
    """

    _validation = {
        'phrase': {'readonly': True},
        'code': {'readonly': True},
    }

    _attribute_map = {
        'phrase': {'key': 'phrase', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AssignmentReportResourceComplianceReason, self).__init__(**kwargs)
        self.phrase = None
        self.code = None


class ConfigurationInfo(msrest.serialization.Model):
    """Information about the configuration.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the configuration.
    :vartype name: str
    :ivar version: Version of the configuration.
    :vartype version: str
    """

    _validation = {
        'name': {'readonly': True},
        'version': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationInfo, self).__init__(**kwargs)
        self.name = None
        self.version = None


class ConfigurationParameter(msrest.serialization.Model):
    """Represents a configuration parameter.

    :param name: Name of the configuration parameter.
    :type name: str
    :param value: Value of the configuration parameter.
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationParameter, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)


class ConfigurationSetting(msrest.serialization.Model):
    """Configuration setting of LCM (Local Configuration Manager).

    :param configuration_mode: Specifies how the LCM(Local Configuration Manager) actually applies
     the configuration to the target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and
     ApplyAndAutoCorrect. Possible values include: "ApplyOnly", "ApplyAndMonitor",
     "ApplyAndAutoCorrect".
    :type configuration_mode: str or ~guest_configuration_client.models.ConfigurationMode
    :param allow_module_overwrite: If true - new configurations downloaded from the pull service
     are allowed to overwrite the old ones on the target node. Otherwise, false. Possible values
     include: "True", "False".
    :type allow_module_overwrite: str or ~guest_configuration_client.models.AllowModuleOverwrite
    :param action_after_reboot: Specifies what happens after a reboot during the application of a
     configuration. The possible values are ContinueConfiguration and StopConfiguration. Possible
     values include: "ContinueConfiguration", "StopConfiguration".
    :type action_after_reboot: str or ~guest_configuration_client.models.ActionAfterReboot
    :param refresh_frequency_mins: The time interval, in minutes, at which the LCM checks a pull
     service to get updated configurations. This value is ignored if the LCM is not configured in
     pull mode. The default value is 30.
    :type refresh_frequency_mins: float
    :param reboot_if_needed: Set this to true to automatically reboot the node after a
     configuration that requires reboot is applied. Otherwise, you will have to manually reboot the
     node for any configuration that requires it. The default value is false. To use this setting
     when a reboot condition is enacted by something other than DSC (such as Windows Installer),
     combine this setting with the xPendingReboot module. Possible values include: "True", "False".
     Default value: "False".
    :type reboot_if_needed: str or ~guest_configuration_client.models.RebootIfNeeded
    :param configuration_mode_frequency_mins: How often, in minutes, the current configuration is
     checked and applied. This property is ignored if the ConfigurationMode property is set to
     ApplyOnly. The default value is 15.
    :type configuration_mode_frequency_mins: float
    """

    _attribute_map = {
        'configuration_mode': {'key': 'configurationMode', 'type': 'str'},
        'allow_module_overwrite': {'key': 'allowModuleOverwrite', 'type': 'str'},
        'action_after_reboot': {'key': 'actionAfterReboot', 'type': 'str'},
        'refresh_frequency_mins': {'key': 'refreshFrequencyMins', 'type': 'float'},
        'reboot_if_needed': {'key': 'rebootIfNeeded', 'type': 'str'},
        'configuration_mode_frequency_mins': {'key': 'configurationModeFrequencyMins', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationSetting, self).__init__(**kwargs)
        self.configuration_mode = kwargs.get('configuration_mode', None)
        self.allow_module_overwrite = kwargs.get('allow_module_overwrite', None)
        self.action_after_reboot = kwargs.get('action_after_reboot', None)
        self.refresh_frequency_mins = kwargs.get('refresh_frequency_mins', 30)
        self.reboot_if_needed = kwargs.get('reboot_if_needed', "False")
        self.configuration_mode_frequency_mins = kwargs.get('configuration_mode_frequency_mins', 15)


class ErrorResponse(msrest.serialization.Model):
    """Error response of an operation failure.

    :param error:
    :type error: ~guest_configuration_client.models.ErrorResponseError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ErrorResponseError(msrest.serialization.Model):
    """ErrorResponseError.

    :param code: Error code.
    :type code: str
    :param message: Detail error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponseError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class Resource(msrest.serialization.Model):
    """The core properties of ARM resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the guest configuration assignment.
    :vartype id: str
    :param name: Name of the guest configuration assignment.
    :type name: str
    :param location: Region where the VM is located.
    :type location: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = kwargs.get('name', None)
        self.location = kwargs.get('location', None)
        self.type = None


class GuestConfigurationAssignment(Resource):
    """Guest configuration assignment is an association between a machine and guest configuration.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the guest configuration assignment.
    :vartype id: str
    :param name: Name of the guest configuration assignment.
    :type name: str
    :param location: Region where the VM is located.
    :type location: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param properties: Properties of the Guest configuration assignment.
    :type properties: ~guest_configuration_client.models.GuestConfigurationAssignmentProperties
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'GuestConfigurationAssignmentProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GuestConfigurationAssignment, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)


class GuestConfigurationAssignmentList(msrest.serialization.Model):
    """The response of the list guest configuration assignment operation.

    :param value: Result of the list guest configuration assignment operation.
    :type value: list[~guest_configuration_client.models.GuestConfigurationAssignment]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[GuestConfigurationAssignment]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GuestConfigurationAssignmentList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class GuestConfigurationAssignmentProperties(msrest.serialization.Model):
    """Guest configuration assignment properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar target_resource_id: VM resource Id.
    :vartype target_resource_id: str
    :param guest_configuration: The guest configuration to assign.
    :type guest_configuration: ~guest_configuration_client.models.GuestConfigurationNavigation
    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~guest_configuration_client.models.ComplianceStatus
    :ivar last_compliance_status_checked: Date and time when last compliance status was checked.
    :vartype last_compliance_status_checked: ~datetime.datetime
    :ivar latest_report_id: Id of the latest report for the guest configuration assignment.
    :vartype latest_report_id: str
    :param latest_assignment_report: Last reported guest configuration assignment report.
    :type latest_assignment_report: ~guest_configuration_client.models.AssignmentReport
    :param context: The source which initiated the guest configuration assignment. Ex: Azure
     Policy.
    :type context: str
    :ivar assignment_hash: Combined hash of the configuration package and parameters.
    :vartype assignment_hash: str
    :ivar provisioning_state: The provisioning state, which only appears in the response. Possible
     values include: "Succeeded", "Failed", "Canceled", "Created".
    :vartype provisioning_state: str or ~guest_configuration_client.models.ProvisioningState
    """

    _validation = {
        'target_resource_id': {'readonly': True},
        'compliance_status': {'readonly': True},
        'last_compliance_status_checked': {'readonly': True},
        'latest_report_id': {'readonly': True},
        'assignment_hash': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'guest_configuration': {'key': 'guestConfiguration', 'type': 'GuestConfigurationNavigation'},
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'last_compliance_status_checked': {'key': 'lastComplianceStatusChecked', 'type': 'iso-8601'},
        'latest_report_id': {'key': 'latestReportId', 'type': 'str'},
        'latest_assignment_report': {'key': 'latestAssignmentReport', 'type': 'AssignmentReport'},
        'context': {'key': 'context', 'type': 'str'},
        'assignment_hash': {'key': 'assignmentHash', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GuestConfigurationAssignmentProperties, self).__init__(**kwargs)
        self.target_resource_id = None
        self.guest_configuration = kwargs.get('guest_configuration', None)
        self.compliance_status = None
        self.last_compliance_status_checked = None
        self.latest_report_id = None
        self.latest_assignment_report = kwargs.get('latest_assignment_report', None)
        self.context = kwargs.get('context', None)
        self.assignment_hash = None
        self.provisioning_state = None


class GuestConfigurationAssignmentReport(msrest.serialization.Model):
    """Report for the guest configuration assignment. Report contains information such as compliance status, reason, and more.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the report for the guest configuration assignment.
    :vartype id: str
    :ivar name: GUID that identifies the guest configuration assignment report under a
     subscription, resource group.
    :vartype name: str
    :param properties: Properties of the guest configuration report.
    :type properties:
     ~guest_configuration_client.models.GuestConfigurationAssignmentReportProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'GuestConfigurationAssignmentReportProperties'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GuestConfigurationAssignmentReport, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.properties = kwargs.get('properties', None)


class GuestConfigurationAssignmentReportList(msrest.serialization.Model):
    """List of guest configuration assignment reports.

    :param value: List of reports for the guest configuration. Report contains information such as
     compliance status, reason and more.
    :type value: list[~guest_configuration_client.models.GuestConfigurationAssignmentReport]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[GuestConfigurationAssignmentReport]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GuestConfigurationAssignmentReportList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class GuestConfigurationAssignmentReportProperties(msrest.serialization.Model):
    """Report for the guest configuration assignment. Report contains information such as compliance status, reason, and more.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar compliance_status: A value indicating compliance status of the machine for the assigned
     guest configuration. Possible values include: "Compliant", "NonCompliant", "Pending".
    :vartype compliance_status: str or ~guest_configuration_client.models.ComplianceStatus
    :ivar report_id: GUID that identifies the guest configuration assignment report under a
     subscription, resource group.
    :vartype report_id: str
    :param assignment: Configuration details of the guest configuration assignment.
    :type assignment: ~guest_configuration_client.models.AssignmentInfo
    :param vm: Information about the VM.
    :type vm: ~guest_configuration_client.models.VmInfo
    :ivar start_time: Start date and time of the guest configuration assignment compliance status
     check.
    :vartype start_time: ~datetime.datetime
    :ivar end_time: End date and time of the guest configuration assignment compliance status
     check.
    :vartype end_time: ~datetime.datetime
    :param details: Details of the assignment report.
    :type details: ~guest_configuration_client.models.AssignmentReportDetails
    """

    _validation = {
        'compliance_status': {'readonly': True},
        'report_id': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
    }

    _attribute_map = {
        'compliance_status': {'key': 'complianceStatus', 'type': 'str'},
        'report_id': {'key': 'reportId', 'type': 'str'},
        'assignment': {'key': 'assignment', 'type': 'AssignmentInfo'},
        'vm': {'key': 'vm', 'type': 'VmInfo'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'details': {'key': 'details', 'type': 'AssignmentReportDetails'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GuestConfigurationAssignmentReportProperties, self).__init__(**kwargs)
        self.compliance_status = None
        self.report_id = None
        self.assignment = kwargs.get('assignment', None)
        self.vm = kwargs.get('vm', None)
        self.start_time = None
        self.end_time = None
        self.details = kwargs.get('details', None)


class GuestConfigurationNavigation(msrest.serialization.Model):
    """Guest configuration is an artifact that encapsulates DSC configuration and its dependencies. The artifact is a zip file containing DSC configuration (as MOF) and dependent resources and other dependencies like modules.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param kind: Kind of the guest configuration. For example:DSC. Possible values include: "DSC".
    :type kind: str or ~guest_configuration_client.models.Kind
    :param name: Name of the guest configuration.
    :type name: str
    :param version: Version of the guest configuration.
    :type version: str
    :ivar content_uri: Uri of the storage where guest configuration package is uploaded.
    :vartype content_uri: str
    :ivar content_hash: Combined hash of the guest configuration package and configuration
     parameters.
    :vartype content_hash: str
    :param configuration_parameter: The configuration parameters for the guest configuration.
    :type configuration_parameter: list[~guest_configuration_client.models.ConfigurationParameter]
    :param configuration_setting: The configuration setting for the guest configuration.
    :type configuration_setting: ~guest_configuration_client.models.ConfigurationSetting
    """

    _validation = {
        'content_uri': {'readonly': True},
        'content_hash': {'readonly': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'content_hash': {'key': 'contentHash', 'type': 'str'},
        'configuration_parameter': {'key': 'configurationParameter', 'type': '[ConfigurationParameter]'},
        'configuration_setting': {'key': 'configurationSetting', 'type': 'ConfigurationSetting'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GuestConfigurationNavigation, self).__init__(**kwargs)
        self.kind = kwargs.get('kind', None)
        self.name = kwargs.get('name', None)
        self.version = kwargs.get('version', None)
        self.content_uri = None
        self.content_hash = None
        self.configuration_parameter = kwargs.get('configuration_parameter', None)
        self.configuration_setting = kwargs.get('configuration_setting', None)


class Operation(msrest.serialization.Model):
    """GuestConfiguration REST API operation.

    :param name: Operation name: For ex.
     providers/Microsoft.GuestConfiguration/guestConfigurationAssignments/write or read.
    :type name: str
    :param display: Provider, Resource, Operation and description values.
    :type display: ~guest_configuration_client.models.OperationDisplay
    :param status_code: Service provider: Microsoft.GuestConfiguration.
    :type status_code: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'status_code': {'key': 'properties.statusCode', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.status_code = kwargs.get('status_code', None)


class OperationDisplay(msrest.serialization.Model):
    """Provider, Resource, Operation and description values.

    :param provider: Service provider: Microsoft.GuestConfiguration.
    :type provider: str
    :param resource: Resource on which the operation is performed:  For ex.
    :type resource: str
    :param operation: Operation type: Read, write, delete, etc.
    :type operation: str
    :param description: Description about operation.
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


class OperationList(msrest.serialization.Model):
    """The response model for the list of Automation operations.

    :param value: List of Automation operations supported by the Automation resource provider.
    :type value: list[~guest_configuration_client.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ProxyResource(Resource):
    """ARM proxy resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM resource id of the guest configuration assignment.
    :vartype id: str
    :param name: Name of the guest configuration assignment.
    :type name: str
    :param location: Region where the VM is located.
    :type location: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProxyResource, self).__init__(**kwargs)


class VmInfo(msrest.serialization.Model):
    """Information about the VM.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Azure resource Id of the VM.
    :vartype id: str
    :ivar uuid: UUID(Universally Unique Identifier) of the VM.
    :vartype uuid: str
    """

    _validation = {
        'id': {'readonly': True},
        'uuid': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'uuid': {'key': 'uuid', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(VmInfo, self).__init__(**kwargs)
        self.id = None
        self.uuid = None
