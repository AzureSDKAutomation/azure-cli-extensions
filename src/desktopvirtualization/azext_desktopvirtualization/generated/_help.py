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


helps['desktopvirtualization workspace'] = """
    type: group
    short-summary: desktopvirtualization workspace
"""

helps['desktopvirtualization workspace list'] = """
    type: command
    short-summary: List workspaces in subscription.
    examples:
      - name: Workspace_ListByResourceGroup
        text: |-
               az desktopvirtualization workspace list --resource-group "resourceGroup1"
"""

helps['desktopvirtualization workspace show'] = """
    type: command
    short-summary: Get a workspace.
    examples:
      - name: Workspace_Get
        text: |-
               az desktopvirtualization workspace show --resource-group "resourceGroup1" --name "workspace1"
"""

helps['desktopvirtualization workspace create'] = """
    type: command
    short-summary: Create or update a workspace.
    examples:
      - name: Workspace_Create
        text: |-
               az desktopvirtualization workspace create --resource-group "resourceGroup1" --location "centralus" --des\
cription "des1" --friendly-name "friendly" --tags tag1="value1" tag2="value2" --name "workspace1"
"""

helps['desktopvirtualization workspace update'] = """
    type: command
    short-summary: Update a workspace.
    examples:
      - name: Workspace_Update
        text: |-
               az desktopvirtualization workspace update --resource-group "resourceGroup1" --description "des1" --frien\
dly-name "friendly" --tags tag1="value1" tag2="value2" --name "workspace1"
"""

helps['desktopvirtualization workspace delete'] = """
    type: command
    short-summary: Remove a workspace.
    examples:
      - name: Workspace_Delete
        text: |-
               az desktopvirtualization workspace delete --resource-group "resourceGroup1" --name "workspace1"
"""

helps['desktopvirtualization applicationgroup'] = """
    type: group
    short-summary: desktopvirtualization applicationgroup
"""

helps['desktopvirtualization applicationgroup list'] = """
    type: command
    short-summary: List applicationGroups in subscription.
    examples:
      - name: ApplicationGroup_ListByResourceGroup
        text: |-
               az desktopvirtualization applicationgroup list --filter "applicationGroupType eq \'RailApplication\'" --\
resource-group "resourceGroup1"
"""

helps['desktopvirtualization applicationgroup show'] = """
    type: command
    short-summary: Get an application group.
    examples:
      - name: ApplicationGroup_Get
        text: |-
               az desktopvirtualization applicationgroup show --name "applicationGroup1" --resource-group "resourceGrou\
p1"
"""

helps['desktopvirtualization applicationgroup create'] = """
    type: command
    short-summary: Create or update an applicationGroup.
    examples:
      - name: ApplicationGroup_Create
        text: |-
               az desktopvirtualization applicationgroup create --location "centralus" --description "des1" --applicati\
on-group-type "RemoteApp" --friendly-name "friendly" --host-pool-arm-path "/subscriptions/daefabc0-95b4-48b3-b645-8a753\
a63c4fa/resourceGroups/resourceGroup1/providers/Microsoft.DesktopVirtualization/hostPools/hostPool1" --tags tag1="value\
1" tag2="value2" --name "applicationGroup1" --resource-group "resourceGroup1"
"""

helps['desktopvirtualization applicationgroup update'] = """
    type: command
    short-summary: Update an applicationGroup.
    examples:
      - name: ApplicationGroups_Update
        text: |-
               az desktopvirtualization applicationgroup update --description "des1" --friendly-name "friendly" --tags \
tag1="value1" tag2="value2" --name "applicationGroup1" --resource-group "resourceGroup1"
"""

helps['desktopvirtualization applicationgroup delete'] = """
    type: command
    short-summary: Remove an applicationGroup.
    examples:
      - name: ApplicationGroup_Delete
        text: |-
               az desktopvirtualization applicationgroup delete --name "applicationGroup1" --resource-group "resourceGr\
oup1"
"""

helps['desktopvirtualization hostpool'] = """
    type: group
    short-summary: desktopvirtualization hostpool
"""

helps['desktopvirtualization hostpool list'] = """
    type: command
    short-summary: List hostPools in subscription.
    examples:
      - name: HostPool_ListByResourceGroup
        text: |-
               az desktopvirtualization hostpool list --resource-group "resourceGroup1"
"""

helps['desktopvirtualization hostpool show'] = """
    type: command
    short-summary: Get a host pool.
    examples:
      - name: HostPool_Get
        text: |-
               az desktopvirtualization hostpool show --name "hostPool1" --resource-group "resourceGroup1"
"""

helps['desktopvirtualization hostpool create'] = """
    type: command
    short-summary: Create or update a host pool.
    parameters:
      - name: --registration-info
        short-summary: The registration info of HostPool.
        long-summary: |
            Usage: --registration-info expiration-time=XX token=XX registration-token-operation=XX

            expiration-time: Expiration time of registration token.
            token: The registration token base64 encoded string.
            registration-token-operation: The type of resetting the token.
    examples:
      - name: HostPool_Create
        text: |-
               az desktopvirtualization hostpool create --location "centralus" --description "des1" --friendly-name "fr\
iendly" --host-pool-type "Pooled" --load-balancer-type "BreadthFirst" --max-session-limit 999999 --personal-desktop-ass\
ignment-type "Automatic" --preferred-app-group-type "Desktop" --registration-info expiration-time="2020-10-01T14:01:54.\
9571247Z" registration-token-operation="Update" --sso-context "KeyVaultPath" --tags tag1="value1" tag2="value2" --name \
"hostPool1" --resource-group "resourceGroup1"
"""

helps['desktopvirtualization hostpool update'] = """
    type: command
    short-summary: Update a host pool.
    parameters:
      - name: --registration-info
        short-summary: The registration info of HostPool.
        long-summary: |
            Usage: --registration-info expiration-time=XX registration-token-operation=XX

            expiration-time: Expiration time of registration token.
            registration-token-operation: The type of resetting the token.
    examples:
      - name: HostPool_Update
        text: |-
               az desktopvirtualization hostpool update --description "des1" --friendly-name "friendly" --load-balancer\
-type "BreadthFirst" --max-session-limit 999999 --personal-desktop-assignment-type "Automatic" --registration-info expi\
ration-time="2020-10-01T15:01:54.9571247Z" registration-token-operation="Update" --sso-context "KeyVaultPath" --tags ta\
g1="value1" tag2="value2" --name "hostPool1" --resource-group "resourceGroup1"
"""

helps['desktopvirtualization hostpool delete'] = """
    type: command
    short-summary: Remove a host pool.
    examples:
      - name: HostPool_Delete
        text: |-
               az desktopvirtualization hostpool delete --force true --name "hostPool1" --resource-group "resourceGroup\
1"
"""
