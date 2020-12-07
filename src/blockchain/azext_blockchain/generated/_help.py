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


helps['blockchain blockchain-member'] = """
    type: group
    short-summary: blockchain blockchain-member
"""

helps['blockchain blockchain-member list'] = """
    type: command
    short-summary: "Lists the blockchain members for a resource group."
    examples:
      - name: BlockchainMembers_List
        text: |-
               az blockchain blockchain-member list --resource-group "mygroup"
"""

helps['blockchain blockchain-member show'] = """
    type: command
    short-summary: "Get details about a blockchain member."
    examples:
      - name: BlockchainMembers_Get
        text: |-
               az blockchain blockchain-member show --name "contosemember1" --resource-group "mygroup"
"""

helps['blockchain blockchain-member create'] = """
    type: command
    short-summary: "Create a blockchain member."
    parameters:
      - name: --sku
        short-summary: "Gets or sets the blockchain member Sku."
        long-summary: |
            Usage: --sku name=XX tier=XX

            name: Gets or sets Sku name
            tier: Gets or sets Sku tier
      - name: --firewall-rules
        short-summary: "Gets or sets firewall rules"
        long-summary: |
            Usage: --firewall-rules rule-name=XX start-ip-address=XX end-ip-address=XX

            rule-name: Gets or sets the name of the firewall rules.
            start-ip-address: Gets or sets the start IP address of the firewall rule range.
            end-ip-address: Gets or sets the end IP address of the firewall rule range.

            Multiple actions can be specified by using more than one --firewall-rules argument.
    examples:
      - name: BlockchainMembers_Create
        text: |-
               az blockchain blockchain-member create --location "southeastasia" --consortium "ContoseConsortium" \
--consortium-management-account-password "<consortiumManagementAccountPassword>" --password "<password>" --protocol \
"Quorum" --name "contosemember1" --resource-group "mygroup"
"""

helps['blockchain blockchain-member update'] = """
    type: command
    short-summary: "Update a blockchain member."
    parameters:
      - name: --firewall-rules
        short-summary: "Gets or sets the firewall rules."
        long-summary: |
            Usage: --firewall-rules rule-name=XX start-ip-address=XX end-ip-address=XX

            rule-name: Gets or sets the name of the firewall rules.
            start-ip-address: Gets or sets the start IP address of the firewall rule range.
            end-ip-address: Gets or sets the end IP address of the firewall rule range.

            Multiple actions can be specified by using more than one --firewall-rules argument.
    examples:
      - name: BlockchainMembers_Update
        text: |-
               az blockchain blockchain-member update --consortium-management-account-password \
"<consortiumManagementAccountPassword>" --password "<password>" --name "ContoseMember1" --resource-group "mygroup"
"""

helps['blockchain blockchain-member delete'] = """
    type: command
    short-summary: "Delete a blockchain member."
    examples:
      - name: BlockchainMembers_Delete
        text: |-
               az blockchain blockchain-member delete --name "contosemember1" --resource-group "mygroup"
"""

helps['blockchain blockchain-member list-all'] = """
    type: command
    short-summary: "Lists the blockchain members for a subscription."
    examples:
      - name: BlockchainMembers_ListAll
        text: |-
               az blockchain blockchain-member list-all
"""

helps['blockchain blockchain-member list-api-key'] = """
    type: command
    short-summary: "Lists the API keys for a blockchain member."
    examples:
      - name: BlockchainMembers_ListApiKeys
        text: |-
               az blockchain blockchain-member list-api-key --name "contosemember1" --resource-group "mygroup"
"""

helps['blockchain blockchain-member list-consortium-member'] = """
    type: command
    short-summary: "Lists the consortium members for a blockchain member."
    examples:
      - name: BlockchainMembers_ListConsortiumMembers
        text: |-
               az blockchain blockchain-member list-consortium-member --name "contosemember1" --resource-group \
"mygroup"
"""

helps['blockchain blockchain-member regenerate-api-key'] = """
    type: command
    short-summary: "Regenerate the API keys for a blockchain member."
    examples:
      - name: BlockchainMembers_ListRegenerateApiKeys
        text: |-
               az blockchain blockchain-member regenerate-api-key --key-name "key1" --name "contosemember1" \
--resource-group "mygroup"
"""

helps['blockchain blockchain-member wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the blockchain blockchain-member is met.
    examples:
      - name: Pause executing next line of CLI script until the blockchain blockchain-member is successfully created.
        text: |-
               az blockchain blockchain-member wait --name "contosemember1" --resource-group "mygroup" --created
      - name: Pause executing next line of CLI script until the blockchain blockchain-member is successfully deleted.
        text: |-
               az blockchain blockchain-member wait --name "contosemember1" --resource-group "mygroup" --deleted
"""

helps['blockchain blockchain-member-operation-result'] = """
    type: group
    short-summary: blockchain blockchain-member-operation-result
"""

helps['blockchain blockchain-member-operation-result show'] = """
    type: command
    short-summary: "Get Async operation result."
    examples:
      - name: BlockchainMemberOperationResults_Get
        text: |-
               az blockchain blockchain-member-operation-result show --operation-id "12f4b309-01e3-4fcf-bc0b-1cc034ca03\
f8" --location-name "southeastasia"
"""

helps['blockchain consortium'] = """
    type: group
    short-summary: blockchain consortium
"""

helps['blockchain consortium list'] = """
    type: command
    short-summary: "Lists the available consortiums for a subscription."
    examples:
      - name: Locations_ListConsortiums
        text: |-
               az blockchain consortium list --name "southeastasia"
"""

helps['blockchain sku'] = """
    type: group
    short-summary: blockchain sku
"""

helps['blockchain sku list'] = """
    type: command
    short-summary: "Lists the Skus of the resource type."
    examples:
      - name: Skus_List
        text: |-
               az blockchain sku list
"""

helps['blockchain transaction-node'] = """
    type: group
    short-summary: blockchain transaction-node
"""

helps['blockchain transaction-node list'] = """
    type: command
    short-summary: "Lists the transaction nodes for a blockchain member."
    examples:
      - name: TransactionNodes_List
        text: |-
               az blockchain transaction-node list --blockchain-member-name "contosemember1" --resource-group \
"mygroup"
"""

helps['blockchain transaction-node show'] = """
    type: command
    short-summary: "Get the details of the transaction node."
    examples:
      - name: TransactionNodes_Get
        text: |-
               az blockchain transaction-node show --blockchain-member-name "contosemember1" --resource-group \
"mygroup" --name "txnode2"
"""

helps['blockchain transaction-node create'] = """
    type: command
    short-summary: "Create or update the transaction node."
    parameters:
      - name: --firewall-rules
        short-summary: "Gets or sets the firewall rules."
        long-summary: |
            Usage: --firewall-rules rule-name=XX start-ip-address=XX end-ip-address=XX

            rule-name: Gets or sets the name of the firewall rules.
            start-ip-address: Gets or sets the start IP address of the firewall rule range.
            end-ip-address: Gets or sets the end IP address of the firewall rule range.

            Multiple actions can be specified by using more than one --firewall-rules argument.
    examples:
      - name: TransactionNodes_Create
        text: |-
               az blockchain transaction-node create --blockchain-member-name "contosemember1" --resource-group \
"mygroup" --location "southeastasia" --password "<password>" --name "txnode2"
"""

helps['blockchain transaction-node update'] = """
    type: command
    short-summary: "Update the transaction node."
    parameters:
      - name: --firewall-rules
        short-summary: "Gets or sets the firewall rules."
        long-summary: |
            Usage: --firewall-rules rule-name=XX start-ip-address=XX end-ip-address=XX

            rule-name: Gets or sets the name of the firewall rules.
            start-ip-address: Gets or sets the start IP address of the firewall rule range.
            end-ip-address: Gets or sets the end IP address of the firewall rule range.

            Multiple actions can be specified by using more than one --firewall-rules argument.
    examples:
      - name: TransactionNodes_Update
        text: |-
               az blockchain transaction-node update --blockchain-member-name "contosemember1" --resource-group \
"mygroup" --password "<password>" --name "txnode2"
"""

helps['blockchain transaction-node delete'] = """
    type: command
    short-summary: "Delete the transaction node."
    examples:
      - name: TransactionNodes_Delete
        text: |-
               az blockchain transaction-node delete --blockchain-member-name "contosemember1" --resource-group \
"mygroup" --name "txNode2"
"""

helps['blockchain transaction-node list-api-key'] = """
    type: command
    short-summary: "List the API keys for the transaction node."
    examples:
      - name: TransactionNodes_ListApiKeys
        text: |-
               az blockchain transaction-node list-api-key --blockchain-member-name "contosemember1" --resource-group \
"mygroup" --name "txnode2"
"""

helps['blockchain transaction-node regenerate-api-key'] = """
    type: command
    short-summary: "Regenerate the API keys for the blockchain member."
    examples:
      - name: TransactionNodes_ListRegenerateApiKeys
        text: |-
               az blockchain transaction-node regenerate-api-key --key-name "key1" --blockchain-member-name \
"contosemember1" --resource-group "mygroup" --name "txnode2"
"""

helps['blockchain transaction-node wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the blockchain transaction-node is met.
    examples:
      - name: Pause executing next line of CLI script until the blockchain transaction-node is successfully created.
        text: |-
               az blockchain transaction-node wait --blockchain-member-name "contosemember1" --resource-group \
"mygroup" --name "txnode2" --created
      - name: Pause executing next line of CLI script until the blockchain transaction-node is successfully deleted.
        text: |-
               az blockchain transaction-node wait --blockchain-member-name "contosemember1" --resource-group \
"mygroup" --name "txnode2" --deleted
"""
