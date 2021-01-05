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

from knack.help_files import helps


helps['guestconfig guest-configuration-assignment'] = """
    type: group
    short-summary: Manage guest configuration assignment with guestconfig
"""

helps['guestconfig guest-configuration-assignment list'] = """
    type: command
    short-summary: "List all guest configuration assignments for a virtual machine."
    examples:
      - name: List all guest configuration assignments for a virtual machine
        text: |-
               az guestconfig guest-configuration-assignment list --resource-group "myResourceGroupName" --vm-name \
"myVMName"
"""

helps['guestconfig guest-configuration-assignment show'] = """
    type: command
    short-summary: "Get information about a guest configuration assignment."
    examples:
      - name: Get a guest configuration assignment
        text: |-
               az guestconfig guest-configuration-assignment show --name "SecureProtocol" --resource-group \
"myResourceGroupName" --vm-name "myVMName"
"""

helps['guestconfig guest-configuration-assignment-report'] = """
    type: group
    short-summary: Manage guest configuration assignment report with guestconfig
"""

helps['guestconfig guest-configuration-assignment-report list'] = """
    type: command
    short-summary: "List all reports for the guest configuration assignment, latest report first."
    examples:
      - name: List all guest configuration assignments for a virtual machine
        text: |-
               az guestconfig guest-configuration-assignment-report list --guest-configuration-assignment-name \
"AuditSecureProtocol" --resource-group "myResourceGroupName" --vm-name "myVMName"
"""

helps['guestconfig guest-configuration-assignment-report show'] = """
    type: command
    short-summary: "Get a report for the guest configuration assignment, by reportId."
    examples:
      - name: Get a guest configuration assignment report by Id for a virtual machine
        text: |-
               az guestconfig guest-configuration-assignment-report show --guest-configuration-assignment-name \
"AuditSecureProtocol" --report-id "7367cbb8-ae99-47d0-a33b-a283564d2cb1" --resource-group "myResourceGroupName" \
--vm-name "myvm"
"""

helps['guestconfig guest-configuration-hcrp-assignment'] = """
    type: group
    short-summary: Manage guest configuration hcrp assignment with guestconfig
"""

helps['guestconfig guest-configuration-hcrp-assignment list'] = """
    type: command
    short-summary: "List all guest configuration assignments for an ARC machine."
    examples:
      - name: List all guest configuration assignments for a virtual machine
        text: |-
               az guestconfig guest-configuration-hcrp-assignment list --machine-name "myMachineName" --resource-group \
"myResourceGroupName"
"""

helps['guestconfig guest-configuration-hcrp-assignment show'] = """
    type: command
    short-summary: "Get information about a guest configuration assignment."
    examples:
      - name: Get a guest configuration assignment
        text: |-
               az guestconfig guest-configuration-hcrp-assignment show --guest-configuration-assignment-name \
"SecureProtocol" --machine-name "myMachineName" --resource-group "myResourceGroupName"
"""

helps['guestconfig guest-configuration-hcrp-assignment-report'] = """
    type: group
    short-summary: Manage guest configuration hcrp assignment report with guestconfig
"""

helps['guestconfig guest-configuration-hcrp-assignment-report list'] = """
    type: command
    short-summary: "List all reports for the guest configuration assignment, latest report first."
    examples:
      - name: List all guest configuration assignments for a virtual machine
        text: |-
               az guestconfig guest-configuration-hcrp-assignment-report list --guest-configuration-assignment-name \
"AuditSecureProtocol" --machine-name "myMachineName" --resource-group "myResourceGroupName"
"""

helps['guestconfig guest-configuration-hcrp-assignment-report show'] = """
    type: command
    short-summary: "Get a report for the guest configuration assignment, by reportId."
    examples:
      - name: Get a guest configuration assignment report by Id for a virtual machine
        text: |-
               az guestconfig guest-configuration-hcrp-assignment-report show --guest-configuration-assignment-name \
"AuditSecureProtocol" --machine-name "myMachineName" --report-id "7367cbb8-ae99-47d0-a33b-a283564d2cb1" \
--resource-group "myResourceGroupName"
"""
