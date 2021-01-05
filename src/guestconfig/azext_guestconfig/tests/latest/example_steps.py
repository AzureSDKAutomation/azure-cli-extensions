# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long


from .. import try_manual


# EXAMPLE: /GuestConfigurationAssignments/get/Get a guest configuration assignment
@try_manual
def step_guest_configuration_assignment_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az guestconfig guest-configuration-assignment show '
             '--name "{myGuestConfigurationAssignment}" '
             '--resource-group "{rg}" '
             '--vm-name "myVMName"',
             checks=checks)


# EXAMPLE: /GuestConfigurationAssignments/get/List all guest configuration assignments for a virtual machine
@try_manual
def step_guest_configuration_assignment_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az guestconfig guest-configuration-assignment list '
             '--resource-group "{rg}" '
             '--vm-name "myVMName"',
             checks=checks)


# EXAMPLE: /GuestConfigurationAssignmentReports/get/Get a guest configuration assignment report by Id for a virtual machine
@try_manual
def step_guest_configuration_assignment_report_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az guestconfig guest-configuration-assignment-report show '
             '--guest-configuration-assignment-name "{myGuestConfigurationAssignment2}" '
             '--report-id "7367cbb8-ae99-47d0-a33b-a283564d2cb1" '
             '--resource-group "{rg}" '
             '--vm-name "myvm"',
             checks=checks)


# EXAMPLE: /GuestConfigurationAssignmentReports/get/List all guest configuration assignments for a virtual machine
@try_manual
def step_guest_configuration_assignment_report_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az guestconfig guest-configuration-assignment-report list '
             '--guest-configuration-assignment-name "{myGuestConfigurationAssignment2}" '
             '--resource-group "{rg}" '
             '--vm-name "myVMName"',
             checks=checks)


# EXAMPLE: /GuestConfigurationHCRPAssignmentReports/get/Get a guest configuration assignment report by Id for a virtual machine
@try_manual
def step_guest_configuration_hcrp(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az guestconfig guest-configuration-hcrp-assignment-report show '
             '--guest-configuration-assignment-name "{myGuestConfigurationAssignment2}" '
             '--machine-name "myMachineName" '
             '--report-id "7367cbb8-ae99-47d0-a33b-a283564d2cb1" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /GuestConfigurationHCRPAssignmentReports/get/List all guest configuration assignments for a virtual machine
@try_manual
def step_guest_configuration_hcrp2(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az guestconfig guest-configuration-hcrp-assignment-report list '
             '--guest-configuration-assignment-name "{myGuestConfigurationAssignment2}" '
             '--machine-name "myMachineName" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /GuestConfigurationHCRPAssignments/get/Get a guest configuration assignment
@try_manual
def step_guest_configuration_hcrp_assignment_show(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az guestconfig guest-configuration-hcrp-assignment show '
             '--guest-configuration-assignment-name "{myGuestConfigurationAssignment}" '
             '--machine-name "myMachineName" '
             '--resource-group "{rg}"',
             checks=checks)


# EXAMPLE: /GuestConfigurationHCRPAssignments/get/List all guest configuration assignments for a virtual machine
@try_manual
def step_guest_configuration_hcrp_assignment_list(test, rg, checks=None):
    if checks is None:
        checks = []
    test.cmd('az guestconfig guest-configuration-hcrp-assignment list '
             '--machine-name "myMachineName" '
             '--resource-group "{rg}"',
             checks=checks)

