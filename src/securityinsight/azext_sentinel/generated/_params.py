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
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    get_enum_type,
    resource_group_name_type
)
from azext_sentinel.action import (
    AddFusionAlertRule,
    AddMicrosoftSecurityIncidentCreationAlertRule,
    AddScheduledAlertRule,
    AddIncidentInfo,
    AddAadDataConnector,
    AddAatpDataConnector,
    AddAscDataConnector,
    AddAwsCloudTrailDataConnector,
    AddMcasDataConnector,
    AddMdatpDataConnector,
    AddOfficeDataConnector,
    AddTiDataConnector,
    AddLabels,
    AddOwner
)


def load_arguments(self, _):

    with self.argument_context('sentinel alert-rule list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')

    with self.argument_context('sentinel alert-rule show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('rule_id', type=str, help='Alert rule ID', id_part='child_name_1')

    with self.argument_context('sentinel alert-rule create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')
        c.argument('rule_id', type=str, help='Alert rule ID')
        c.argument('action_id', type=str, help='Action ID')
        c.argument('etag', type=str, help='Etag of the azure resource')
        c.argument('logic_app_resource_id', type=str, help='Logic App Resource Id, /subscriptions/{my-subscription}/res'
                   'ourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.')
        c.argument('trigger_uri', type=str, help='Logic App Callback URL for this specific workflow.')
        c.argument('fusion_alert_rule', action=AddFusionAlertRule, nargs='+', help='Represents Fusion alert rule.',
                   arg_group='AlertRule')
        c.argument('microsoft_security_incident_creation_alert_rule',
                   action=AddMicrosoftSecurityIncidentCreationAlertRule, nargs='+', help='Represents '
                   'MicrosoftSecurityIncidentCreation rule.', arg_group='AlertRule')
        c.argument('scheduled_alert_rule', action=AddScheduledAlertRule, nargs='+', help='Represents scheduled alert '
                   'rule.', arg_group='AlertRule')

    with self.argument_context('sentinel alert-rule update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('rule_id', type=str, help='Alert rule ID', id_part='child_name_1')
        c.argument('fusion_alert_rule', action=AddFusionAlertRule, nargs='+', help='Represents Fusion alert rule.',
                   arg_group='AlertRule')
        c.argument('microsoft_security_incident_creation_alert_rule',
                   action=AddMicrosoftSecurityIncidentCreationAlertRule, nargs='+', help='Represents '
                   'MicrosoftSecurityIncidentCreation rule.', arg_group='AlertRule')
        c.argument('scheduled_alert_rule', action=AddScheduledAlertRule, nargs='+', help='Represents scheduled alert '
                   'rule.', arg_group='AlertRule')

    with self.argument_context('sentinel alert-rule delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('rule_id', type=str, help='Alert rule ID', id_part='child_name_1')
        c.argument('action_id', type=str, help='Action ID', id_part='child_name_2')

    with self.argument_context('sentinel alert-rule show-action') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('rule_id', type=str, help='Alert rule ID', id_part='child_name_1')
        c.argument('action_id', type=str, help='Action ID', id_part='child_name_2')

    with self.argument_context('sentinel action list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')
        c.argument('rule_id', type=str, help='Alert rule ID')

    with self.argument_context('sentinel alert-rule-template list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')

    with self.argument_context('sentinel alert-rule-template show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('alert_rule_template_id', type=str, help='Alert rule template ID', id_part='child_name_1')

    with self.argument_context('sentinel bookmark list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')

    with self.argument_context('sentinel bookmark show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('bookmark_id', type=str, help='Bookmark ID', id_part='child_name_1')

    with self.argument_context('sentinel bookmark create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')
        c.argument('bookmark_id', type=str, help='Bookmark ID')
        c.argument('etag', type=str, help='Etag of the azure resource')
        c.argument('created', help='The time the bookmark was created')
        c.argument('display_name', type=str, help='The display name of the bookmark')
        c.argument('labels', nargs='+', help='List of labels relevant to this bookmark')
        c.argument('notes', type=str, help='The notes of the bookmark')
        c.argument('query', type=str, help='The query of the bookmark.')
        c.argument('query_result', type=str, help='The query result of the bookmark.')
        c.argument('updated', help='The last time the bookmark was updated')
        c.argument('incident_info', action=AddIncidentInfo, nargs='+', help='Describes an incident that relates to '
                   'bookmark')
        c.argument('object_id', help='The object id of the user.', arg_group='Updated By')
        c.argument('user_info_object_id', help='The object id of the user.', arg_group='Created By')

    with self.argument_context('sentinel bookmark update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('bookmark_id', type=str, help='Bookmark ID', id_part='child_name_1')
        c.argument('etag', type=str, help='Etag of the azure resource')
        c.argument('created', help='The time the bookmark was created')
        c.argument('display_name', type=str, help='The display name of the bookmark')
        c.argument('labels', nargs='+', help='List of labels relevant to this bookmark')
        c.argument('notes', type=str, help='The notes of the bookmark')
        c.argument('query', type=str, help='The query of the bookmark.')
        c.argument('query_result', type=str, help='The query result of the bookmark.')
        c.argument('updated', help='The last time the bookmark was updated')
        c.argument('incident_info', action=AddIncidentInfo, nargs='+', help='Describes an incident that relates to '
                   'bookmark')
        c.argument('object_id', help='The object id of the user.', arg_group='Updated By')
        c.argument('user_info_object_id', help='The object id of the user.', arg_group='Created By')
        c.ignore('bookmark')

    with self.argument_context('sentinel bookmark delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('bookmark_id', type=str, help='Bookmark ID', id_part='child_name_1')

    with self.argument_context('sentinel data-connector list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')

    with self.argument_context('sentinel data-connector show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('data_connector_id', type=str, help='Connector ID', id_part='child_name_1')

    with self.argument_context('sentinel data-connector create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')
        c.argument('data_connector_id', type=str, help='Connector ID')
        c.argument('aad_data_connector', action=AddAadDataConnector, nargs='+', help='Represents AAD (Azure Active '
                   'Directory) data connector.', arg_group='DataConnector')
        c.argument('aatp_data_connector', action=AddAatpDataConnector, nargs='+', help='Represents AATP (Azure '
                   'Advanced Threat Protection) data connector.', arg_group='DataConnector')
        c.argument('asc_data_connector', action=AddAscDataConnector, nargs='+', help='Represents ASC (Azure Security '
                   'Center) data connector.', arg_group='DataConnector')
        c.argument('aws_cloud_trail_data_connector', action=AddAwsCloudTrailDataConnector, nargs='+', help='Represents '
                   'Amazon Web Services CloudTrail data connector.', arg_group='DataConnector')
        c.argument('mcas_data_connector', action=AddMcasDataConnector, nargs='+', help='Represents MCAS (Microsoft '
                   'Cloud App Security) data connector.', arg_group='DataConnector')
        c.argument('mdatp_data_connector', action=AddMdatpDataConnector, nargs='+', help='Represents MDATP (Microsoft '
                   'Defender Advanced Threat Protection) data connector.', arg_group='DataConnector')
        c.argument('office_data_connector', action=AddOfficeDataConnector, nargs='+', help='Represents office data '
                   'connector.', arg_group='DataConnector')
        c.argument('ti_data_connector', action=AddTiDataConnector, nargs='+', help='Represents threat intelligence '
                   'data connector.', arg_group='DataConnector')

    with self.argument_context('sentinel data-connector update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('data_connector_id', type=str, help='Connector ID', id_part='child_name_1')
        c.argument('aad_data_connector', action=AddAadDataConnector, nargs='+', help='Represents AAD (Azure Active '
                   'Directory) data connector.', arg_group='DataConnector')
        c.argument('aatp_data_connector', action=AddAatpDataConnector, nargs='+', help='Represents AATP (Azure '
                   'Advanced Threat Protection) data connector.', arg_group='DataConnector')
        c.argument('asc_data_connector', action=AddAscDataConnector, nargs='+', help='Represents ASC (Azure Security '
                   'Center) data connector.', arg_group='DataConnector')
        c.argument('aws_cloud_trail_data_connector', action=AddAwsCloudTrailDataConnector, nargs='+', help='Represents '
                   'Amazon Web Services CloudTrail data connector.', arg_group='DataConnector')
        c.argument('mcas_data_connector', action=AddMcasDataConnector, nargs='+', help='Represents MCAS (Microsoft '
                   'Cloud App Security) data connector.', arg_group='DataConnector')
        c.argument('mdatp_data_connector', action=AddMdatpDataConnector, nargs='+', help='Represents MDATP (Microsoft '
                   'Defender Advanced Threat Protection) data connector.', arg_group='DataConnector')
        c.argument('office_data_connector', action=AddOfficeDataConnector, nargs='+', help='Represents office data '
                   'connector.', arg_group='DataConnector')
        c.argument('ti_data_connector', action=AddTiDataConnector, nargs='+', help='Represents threat intelligence '
                   'data connector.', arg_group='DataConnector')

    with self.argument_context('sentinel data-connector delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('data_connector_id', type=str, help='Connector ID', id_part='child_name_1')

    with self.argument_context('sentinel incident list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')
        c.argument('filter_', options_list=['--filter'], type=str, help='Filters the results, based on a Boolean '
                   'condition. Optional.')
        c.argument('orderby', type=str, help='Sorts the results. Optional.')
        c.argument('top', type=int, help='Returns only the first n results. Optional.')
        c.argument('skip_token', type=str, help='Skiptoken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skiptoken parameter that specifies a starting point to use for subsequent calls. '
                   'Optional.')

    with self.argument_context('sentinel incident show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('incident_id', type=str, help='Incident ID', id_part='child_name_1')

    with self.argument_context('sentinel incident create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')
        c.argument('incident_id', type=str, help='Incident ID')
        c.argument('etag', type=str, help='Etag of the azure resource')
        c.argument('classification', arg_type=get_enum_type(['Undetermined', 'TruePositive', 'BenignPositive',
                                                             'FalsePositive']), help='The reason the incident was '
                   'closed')
        c.argument('classification_comment', type=str, help='Describes the reason the incident was closed')
        c.argument('classification_reason', arg_type=get_enum_type(['SuspiciousActivity', 'SuspiciousButExpected',
                                                                    'IncorrectAlertLogic', 'InaccurateData']),
                   help='The classification reason the incident was closed with')
        c.argument('description', type=str, help='The description of the incident')
        c.argument('first_activity_time_utc', help='The time of the first activity in the incident')
        c.argument('labels', action=AddLabels, nargs='+', help='List of labels relevant to this incident')
        c.argument('last_activity_time_utc', help='The time of the last activity in the incident')
        c.argument('owner', action=AddOwner, nargs='+', help='Describes a user that the incident is assigned to')
        c.argument('severity', arg_type=get_enum_type(['High', 'Medium', 'Low', 'Informational']), help='The severity '
                   'of the incident')
        c.argument('status', arg_type=get_enum_type(['New', 'Active', 'Closed']), help='The status of the incident')
        c.argument('title', type=str, help='The title of the incident')

    with self.argument_context('sentinel incident update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('incident_id', type=str, help='Incident ID', id_part='child_name_1')
        c.argument('etag', type=str, help='Etag of the azure resource')
        c.argument('classification', arg_type=get_enum_type(['Undetermined', 'TruePositive', 'BenignPositive',
                                                             'FalsePositive']), help='The reason the incident was '
                   'closed')
        c.argument('classification_comment', type=str, help='Describes the reason the incident was closed')
        c.argument('classification_reason', arg_type=get_enum_type(['SuspiciousActivity', 'SuspiciousButExpected',
                                                                    'IncorrectAlertLogic', 'InaccurateData']),
                   help='The classification reason the incident was closed with')
        c.argument('description', type=str, help='The description of the incident')
        c.argument('first_activity_time_utc', help='The time of the first activity in the incident')
        c.argument('labels', action=AddLabels, nargs='+', help='List of labels relevant to this incident')
        c.argument('last_activity_time_utc', help='The time of the last activity in the incident')
        c.argument('owner', action=AddOwner, nargs='+', help='Describes a user that the incident is assigned to')
        c.argument('severity', arg_type=get_enum_type(['High', 'Medium', 'Low', 'Informational']), help='The severity '
                   'of the incident')
        c.argument('status', arg_type=get_enum_type(['New', 'Active', 'Closed']), help='The status of the incident')
        c.argument('title', type=str, help='The title of the incident')
        c.ignore('incident')

    with self.argument_context('sentinel incident delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('incident_id', type=str, help='Incident ID', id_part='child_name_1')

    with self.argument_context('sentinel incident-comment list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')
        c.argument('incident_id', type=str, help='Incident ID')
        c.argument('filter_', options_list=['--filter'], type=str, help='Filters the results, based on a Boolean '
                   'condition. Optional.')
        c.argument('orderby', type=str, help='Sorts the results. Optional.')
        c.argument('top', type=int, help='Returns only the first n results. Optional.')
        c.argument('skip_token', type=str, help='Skiptoken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skiptoken parameter that specifies a starting point to use for subsequent calls. '
                   'Optional.')

    with self.argument_context('sentinel incident-comment show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.', id_part='name')
        c.argument('incident_id', type=str, help='Incident ID', id_part='child_name_1')
        c.argument('incident_comment_id', type=str, help='Incident comment ID', id_part='child_name_2')

    with self.argument_context('sentinel incident-comment create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('workspace_name', type=str, help='The name of the workspace.')
        c.argument('incident_id', type=str, help='Incident ID')
        c.argument('incident_comment_id', type=str, help='Incident comment ID')
        c.argument('message', type=str, help='The comment message')
