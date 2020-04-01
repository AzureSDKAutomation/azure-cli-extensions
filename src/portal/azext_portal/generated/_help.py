# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['portal dashboard'] = """
    type: group
    short-summary: portal dashboard
"""

helps['portal dashboard list'] = """
    type: command
    short-summary: Gets all the dashboards within a subscription.
    examples:
      - name: List all custom resource providers on the resourceGroup
        text: |-
               az portal dashboard list --resource-group "testRG"
"""

helps['portal dashboard show'] = """
    type: command
    short-summary: Gets the Dashboard.
    examples:
      - name: Get a Dashboard
        text: |-
               az portal dashboard show --dashboard-name "testDashboard" --resource-group "testRG"
"""

helps['portal dashboard create'] = """
    type: command
    short-summary: Creates or updates a Dashboard.
    examples:
      - name: Create or update a Dashboard
        text: |-
               az portal dashboard create --location "eastus" --properties-lenses "{\\"aLens\\":{\\"order\\":
               1,\\"parts\\":{\\"aPart\\":{\\"position\\":{\\"colSpan\\":3,\\"rowSpan\\":4,\\"x\\":1,\\"y\\":2}},\\"bPar
               t\\":{\\"position\\":{\\"colSpan\\":6,\\"rowSpan\\":6,\\"x\\":5,\\"y\\":5}}}},\\"bLens\\":{\\"order\\":2,
               \\"parts\\":{}}}" --properties-metadata metadata=[object Object] --tags
               aKey=aValue anotherKey=anotherValue --dashboard-name "testDashboard" --resource-group
               "testRG"
"""

helps['portal dashboard update'] = """
    type: command
    short-summary: Updates an existing Dashboard.
    examples:
      - name: Update a Dashboard
        text: |-
               az portal dashboard update --tags aKey=bValue anotherKey=anotherValue2 --dashboard-name
               "testDashboard" --resource-group "testRG"
"""

helps['portal dashboard delete'] = """
    type: command
    short-summary: Deletes the Dashboard.
    examples:
      - name: Delete a Dashboard
        text: |-
               az portal dashboard delete --dashboard-name "testDashboard" --resource-group "testRG"
"""
