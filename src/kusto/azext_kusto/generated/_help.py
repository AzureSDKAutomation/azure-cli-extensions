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


helps['kusto demo-cluster'] = """
    type: group
    short-summary: kusto demo-cluster
"""

helps['kusto demo-cluster create'] = """
    type: command
    short-summary: Create or update a Kusto demo cluster.
    examples:
      - name: KustoClustersCreateOrUpdate
        text: |-
               az kusto demo-cluster create --cluster-name "KustoClusterRPTest4" --identity-type "SystemAssigned" --loc\
ation "westus" --enable-purge true --enable-streaming-ingest true --key-vault-properties key-name="keyName" key-vault-u\
ri="https://dummy.keyvault.com" key-version="keyVersion" --sku name="Standard_L8s" capacity=2 tier="Standard" --resourc\
e-group "kustorptest"
"""

helps['kusto demo-cluster update'] = """
    type: command
    short-summary: Create or update a Kusto demo cluster.
    examples:
      - name: KustoClustersCreateOrUpdate
        text: |-
               az kusto demo-cluster update --cluster-name "KustoClusterRPTest4" --identity-type "SystemAssigned" --loc\
ation "westus" --enable-purge true --enable-streaming-ingest true --key-vault-properties key-name="keyName" key-vault-u\
ri="https://dummy.keyvault.com" key-version="keyVersion" --sku name="Standard_L8s" capacity=2 tier="Standard" --resourc\
e-group "kustorptest"
"""

helps['kusto cluster'] = """
    type: group
    short-summary: kusto cluster
"""

helps['kusto cluster list'] = """
    type: command
    short-summary: Lists all Kusto clusters within a subscription.
    examples:
      - name: KustoClustersListByResourceGroup
        text: |-
               az kusto cluster list --resource-group "kustorptest"
"""

helps['kusto cluster show'] = """
    type: command
    short-summary: Gets a Kusto cluster.
    examples:
      - name: KustoClustersGet
        text: |-
               az kusto cluster show --cluster-name "KustoClusterRPTest4" --resource-group "kustorptest"
"""

helps['kusto cluster create'] = """
    type: command
    short-summary: Create or update a Kusto cluster.
    examples:
      - name: KustoClustersCreateOrUpdate
        text: |-
               az kusto cluster create --cluster-name "KustoClusterRPTest4" --identity-type "SystemAssigned" --location\
 "westus" --enable-purge true --enable-streaming-ingest true --key-vault-properties key-name="keyName" key-vault-uri="h\
ttps://dummy.keyvault.com" key-version="keyVersion" --sku name="Standard_L8s" capacity=2 tier="Standard" --resource-gro\
up "kustorptest"
"""

helps['kusto cluster update'] = """
    type: command
    short-summary: Update a Kusto cluster.
    examples:
      - name: KustoClustersUpdate
        text: |-
               az kusto cluster update --cluster-name "KustoClusterRPTest4" --identity-type "SystemAssigned" --location\
 "westus" --enable-purge true --enable-streaming-ingest true --key-vault-properties key-name="keyName" key-vault-uri="h\
ttps://dummy.keyvault.com" key-version="keyVersion" --resource-group "kustorptest"
"""

helps['kusto cluster delete'] = """
    type: command
    short-summary: Deletes a Kusto cluster.
    examples:
      - name: KustoClustersDelete
        text: |-
               az kusto cluster delete --cluster-name "KustoClusterRPTest4" --resource-group "kustorptest"
"""

helps['kusto cluster add-language-extension'] = """
    type: command
    short-summary: Add a list of language extensions that can run within KQL queries.
    examples:
      - name: KustoClusterAddLanguageExtensions
        text: |-
               az kusto cluster add-language-extension --cluster-name "KustoClusterRPTest4" --value language-extension-\
name="PYTHON" --value language-extension-name="R" --resource-group "kustorptest"
"""

helps['kusto cluster detach-follower-database'] = """
    type: command
    short-summary: Detaches all followers of a database owned by this cluster.
    examples:
      - name: KustoClusterDetachFollowerDatabases
        text: |-
               az kusto cluster detach-follower-database --cluster-name "KustoClusterRPTest4" --attached-database-confi\
guration-name "myAttachedDatabaseConfiguration" --cluster-resource-id "/subscriptions/12345678-1234-1234-1234-123456789\
098/resourceGroups/kustorptest/providers/Microsoft.Kusto/clusters/leader4" --resource-group "kustorptest"
"""

helps['kusto cluster diagnose-virtual-network'] = """
    type: command
    short-summary: Diagnoses network connectivity status for external resources on which the service is dependent on.
    examples:
      - name: KustoClusterDiagnoseVirtualNetwork
        text: |-
               az kusto cluster diagnose-virtual-network --cluster-name "KustoClusterRPTest4" --resource-group "kustorp\
test"
"""

helps['kusto cluster list-follower-database'] = """
    type: command
    short-summary: Returns a list of databases that are owned by this cluster and were followed by another cluster.
    examples:
      - name: KustoClusterListFollowerDatabases
        text: |-
               az kusto cluster list-follower-database --cluster-name "KustoClusterRPTest4" --resource-group "kustorpte\
st"
"""

helps['kusto cluster list-language-extension'] = """
    type: command
    short-summary: Returns a list of language extensions that can run within KQL queries.
    examples:
      - name: KustoClusterListLanguageExtensions
        text: |-
               az kusto cluster list-language-extension --cluster-name "KustoClusterRPTest4" --resource-group "kustorpt\
est"
"""

helps['kusto cluster list-sku'] = """
    type: command
    short-summary: Lists eligible SKUs for Kusto resource provider.
    examples:
      - name: KustoClustersListResourceSkus
        text: |-
               az kusto cluster list-sku --cluster-name "KustoClusterRPTest4" --resource-group "kustorptest"
"""

helps['kusto cluster remove-language-extension'] = """
    type: command
    short-summary: Remove a list of language extensions that can run within KQL queries.
    examples:
      - name: KustoClusterRemoveLanguageExtensions
        text: |-
               az kusto cluster remove-language-extension --cluster-name "KustoClusterRPTest4" --value language-extensi\
on-name="PYTHON" --value language-extension-name="R" --resource-group "kustorptest"
"""

helps['kusto cluster start'] = """
    type: command
    short-summary: Starts a Kusto cluster.
    examples:
      - name: KustoClustersStart
        text: |-
               az kusto cluster start --cluster-name "KustoClusterRPTest4" --resource-group "kustorptest"
"""

helps['kusto cluster stop'] = """
    type: command
    short-summary: Stops a Kusto cluster.
    examples:
      - name: KustoClustersStop
        text: |-
               az kusto cluster stop --cluster-name "KustoClusterRPTest4" --resource-group "kustorptest"
"""

helps['kusto cluster-principal-assignment'] = """
    type: group
    short-summary: kusto cluster-principal-assignment
"""

helps['kusto cluster-principal-assignment list'] = """
    type: command
    short-summary: Lists all Kusto cluster principalAssignments.
    examples:
      - name: KustoPrincipalAssignmentsList
        text: |-
               az kusto cluster-principal-assignment list --cluster-name "kustoclusterrptest4" --resource-group "kustor\
ptest"
"""

helps['kusto cluster-principal-assignment show'] = """
    type: command
    short-summary: Gets a Kusto cluster principalAssignment.
    examples:
      - name: KustoClusterPrincipalAssignmentsGet
        text: |-
               az kusto cluster-principal-assignment show --cluster-name "kustoclusterrptest4" --principal-assignment-n\
ame "kustoprincipal1" --resource-group "kustorptest"
"""

helps['kusto cluster-principal-assignment create'] = """
    type: command
    short-summary: Create a Kusto cluster principalAssignment.
    examples:
      - name: KustoClusterPrincipalAssignmentsCreateOrUpdate
        text: |-
               az kusto cluster-principal-assignment create --cluster-name "kustoclusterrptest4" --principal-id "876543\
21-1234-1234-1234-123456789123" --principal-type "App" --role "Admin" --tenant-id "12345678-1234-1234-1234-123456789123\
" --principal-assignment-name "kustoprincipal1" --resource-group "kustorptest"
"""

helps['kusto cluster-principal-assignment update'] = """
    type: command
    short-summary: Create a Kusto cluster principalAssignment.
    examples:
      - name: KustoClusterPrincipalAssignmentsCreateOrUpdate
        text: |-
               az kusto cluster-principal-assignment update --cluster-name "kustoclusterrptest4" --principal-id "876543\
21-1234-1234-1234-123456789123" --principal-type "App" --role "Admin" --tenant-id "12345678-1234-1234-1234-123456789123\
" --principal-assignment-name "kustoprincipal1" --resource-group "kustorptest"
"""

helps['kusto cluster-principal-assignment delete'] = """
    type: command
    short-summary: Deletes a Kusto cluster principalAssignment.
    examples:
      - name: KustoClusterPrincipalAssignmentsDelete
        text: |-
               az kusto cluster-principal-assignment delete --cluster-name "kustoclusterrptest4" --principal-assignment\
-name "kustoprincipal1" --resource-group "kustorptest"
"""

helps['kusto database'] = """
    type: group
    short-summary: kusto database
"""

helps['kusto database list'] = """
    type: command
    short-summary: Returns the list of databases of the given Kusto cluster.
    examples:
      - name: KustoDatabasesListByCluster
        text: |-
               az kusto database list --cluster-name "KustoClusterRPTest4" --resource-group "kustorptest"
"""

helps['kusto database show'] = """
    type: command
    short-summary: Returns a database.
    examples:
      - name: KustoDatabasesGet
        text: |-
               az kusto database show --cluster-name "KustoClusterRPTest4" --database-name "KustoDatabase8" --resource-\
group "kustorptest"
"""

helps['kusto database create'] = """
    type: command
    short-summary: Creates or updates a database.
    examples:
      - name: KustoDatabasesCreateOrUpdate
        text: |-
               az kusto database create --cluster-name "KustoClusterRPTest4" --database-name "KustoDatabase8" --read-wr\
ite-database location="westus" soft-delete-period="P1D" --resource-group "kustorptest"
"""

helps['kusto database update'] = """
    type: command
    short-summary: Updates a database.
    examples:
      - name: KustoDatabasesUpdate
        text: |-
               az kusto database update --cluster-name "KustoClusterRPTest4" --database-name "KustoDatabase8" --read-wr\
ite-database soft-delete-period="P1D" --resource-group "kustorptest"
"""

helps['kusto database delete'] = """
    type: command
    short-summary: Deletes the database with the given name.
    examples:
      - name: KustoDatabasesDelete
        text: |-
               az kusto database delete --cluster-name "KustoClusterRPTest4" --database-name "KustoDatabase8" --resourc\
e-group "kustorptest"
"""

helps['kusto database add-principal'] = """
    type: command
    short-summary: Add Database principals permissions.
    examples:
      - name: KustoDatabaseAddPrincipals
        text: |-
               az kusto database add-principal --cluster-name "KustoClusterRPTest4" --database-name "databaseName1" --v\
alue name="Some User" type="User" app-id="" email="user@microsoft.com" fqn="aaduser=some_guid" role="Admin" --value nam\
e="Kusto" type="Group" app-id="" email="kusto@microsoft.com" fqn="aadgroup=some_guid" role="Viewer" --value name="SomeA\
pp" type="App" app-id="some_guid_app_id" email="" fqn="aadapp=some_guid_app_id" role="Admin" --resource-group "kustorpt\
est"
"""

helps['kusto database list-principal'] = """
    type: command
    short-summary: Returns a list of database principals of the given Kusto cluster and database.
    examples:
      - name: KustoDatabaseListPrincipals
        text: |-
               az kusto database list-principal --cluster-name "KustoClusterRPTest4" --database-name "databaseName1" --\
resource-group "kustorptest"
"""

helps['kusto database remove-principal'] = """
    type: command
    short-summary: Remove Database principals permissions.
    examples:
      - name: KustoDatabaseRemovePrincipals
        text: |-
               az kusto database remove-principal --cluster-name "KustoClusterRPTest4" --database-name "databaseName1" \
--value name="Some User" type="User" app-id="" email="user@microsoft.com" fqn="aaduser=some_guid" role="Admin" --value \
name="Kusto" type="Group" app-id="" email="kusto@microsoft.com" fqn="aadgroup=some_guid" role="Viewer" --value name="So\
meApp" type="App" app-id="some_guid_app_id" email="" fqn="aadapp=some_guid_app_id" role="Admin" --resource-group "kusto\
rptest"
"""

helps['kusto database-principal-assignment'] = """
    type: group
    short-summary: kusto database-principal-assignment
"""

helps['kusto database-principal-assignment list'] = """
    type: command
    short-summary: Lists all Kusto cluster database principalAssignments.
    examples:
      - name: KustoPrincipalAssignmentsList
        text: |-
               az kusto database-principal-assignment list --cluster-name "kustoclusterrptest4" --database-name "Kustod\
atabase8" --resource-group "kustorptest"
"""

helps['kusto database-principal-assignment show'] = """
    type: command
    short-summary: Gets a Kusto cluster database principalAssignment.
    examples:
      - name: KustoDatabasePrincipalAssignmentsGet
        text: |-
               az kusto database-principal-assignment show --cluster-name "kustoclusterrptest4" --database-name "Kustod\
atabase8" --principal-assignment-name "kustoprincipal1" --resource-group "kustorptest"
"""

helps['kusto database-principal-assignment create'] = """
    type: command
    short-summary: Creates a Kusto cluster database principalAssignment.
    examples:
      - name: KustoDatabasePrincipalAssignmentsCreateOrUpdate
        text: |-
               az kusto database-principal-assignment create --cluster-name "kustoclusterrptest4" --database-name "Kust\
odatabase8" --principal-id "87654321-1234-1234-1234-123456789123" --principal-type "App" --role "Admin" --tenant-id "12\
345678-1234-1234-1234-123456789123" --principal-assignment-name "kustoprincipal1" --resource-group "kustorptest"
"""

helps['kusto database-principal-assignment update'] = """
    type: command
    short-summary: Creates a Kusto cluster database principalAssignment.
    examples:
      - name: KustoDatabasePrincipalAssignmentsCreateOrUpdate
        text: |-
               az kusto database-principal-assignment update --cluster-name "kustoclusterrptest4" --database-name "Kust\
odatabase8" --principal-id "87654321-1234-1234-1234-123456789123" --principal-type "App" --role "Admin" --tenant-id "12\
345678-1234-1234-1234-123456789123" --principal-assignment-name "kustoprincipal1" --resource-group "kustorptest"
"""

helps['kusto database-principal-assignment delete'] = """
    type: command
    short-summary: Deletes a Kusto principalAssignment.
    examples:
      - name: KustoDatabasePrincipalAssignmentsDelete
        text: |-
               az kusto database-principal-assignment delete --cluster-name "kustoclusterrptest4" --database-name "Kust\
odatabase8" --principal-assignment-name "kustoprincipal1" --resource-group "kustorptest"
"""

helps['kusto attached-database-configuration'] = """
    type: group
    short-summary: kusto attached-database-configuration
"""

helps['kusto attached-database-configuration list'] = """
    type: command
    short-summary: Returns the list of attached database configurations of the given Kusto cluster.
    examples:
      - name: KustoAttachedDatabaseConfigurationsListByCluster
        text: |-
               az kusto attached-database-configuration list --cluster-name "KustoClusterRPTest4" --resource-group "kus\
torptest"
"""

helps['kusto attached-database-configuration show'] = """
    type: command
    short-summary: Returns an attached database configuration.
    examples:
      - name: AttachedDatabaseConfigurationsGet
        text: |-
               az kusto attached-database-configuration show --attached-database-configuration-name "attachedDatabaseCo\
nfigurations1" --cluster-name "KustoClusterRPTest4" --resource-group "kustorptest"
"""

helps['kusto attached-database-configuration create'] = """
    type: command
    short-summary: Creates or updates an attached database configuration.
    examples:
      - name: AttachedDatabaseConfigurationsCreateOrUpdate
        text: |-
               az kusto attached-database-configuration create --attached-database-configuration-name "attachedDatabase\
Configurations1" --cluster-name "KustoClusterRPTest4" --location "westus" --cluster-resource-id "/subscriptions/1234567\
8-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.Kusto/Clusters/KustoClusterLeader" --datab\
ase-name "db1" --default-principals-modification-kind "Union" --resource-group "kustorptest"
"""

helps['kusto attached-database-configuration update'] = """
    type: command
    short-summary: Creates or updates an attached database configuration.
    examples:
      - name: AttachedDatabaseConfigurationsCreateOrUpdate
        text: |-
               az kusto attached-database-configuration update --attached-database-configuration-name "attachedDatabase\
Configurations1" --cluster-name "KustoClusterRPTest4" --location "westus" --cluster-resource-id "/subscriptions/1234567\
8-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.Kusto/Clusters/KustoClusterLeader" --datab\
ase-name "db1" --default-principals-modification-kind "Union" --resource-group "kustorptest"
"""

helps['kusto attached-database-configuration delete'] = """
    type: command
    short-summary: Deletes the attached database configuration with the given name.
    examples:
      - name: AttachedDatabaseConfigurationsDelete
        text: |-
               az kusto attached-database-configuration delete --attached-database-configuration-name "attachedDatabase\
Configurations1" --cluster-name "KustoClusterRPTest4" --resource-group "kustorptest"
"""

helps['kusto data-connection'] = """
    type: group
    short-summary: kusto data-connection
"""

helps['kusto data-connection list'] = """
    type: command
    short-summary: Returns the list of data connections of the given Kusto database.
    examples:
      - name: KustoDatabasesListByCluster
        text: |-
               az kusto data-connection list --cluster-name "KustoClusterRPTest4" --database-name "KustoDatabase8" --re\
source-group "kustorptest"
"""

helps['kusto data-connection show'] = """
    type: command
    short-summary: Returns a data connection.
    examples:
      - name: KustoDataConnectionsGet
        text: |-
               az kusto data-connection show --cluster-name "KustoClusterRPTest4" --data-connection-name "DataConnectio\
ns8" --database-name "KustoDatabase8" --resource-group "kustorptest"
"""

helps['kusto data-connection event-grid'] = """
    type: group
    short-summary: kusto data-connection sub group event-grid
"""

helps['kusto data-connection event-grid create'] = """
    type: command
    short-summary: Creates or updates a data connection.
"""

helps['kusto data-connection event-hub'] = """
    type: group
    short-summary: kusto data-connection sub group event-hub
"""

helps['kusto data-connection event-hub create'] = """
    type: command
    short-summary: Creates or updates a data connection.
    examples:
      - name: KustoDataConnectionsCreateOrUpdate
        text: |-
               az kusto data-connection event-hub create --cluster-name "KustoClusterRPTest4" --data-connection-name "D\
ataConnections8" --database-name "KustoDatabase8" --location "westus" --consumer-group "testConsumerGroup1" --event-hub\
-resource-id "/subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventH\
ub/namespaces/eventhubTestns1/eventhubs/eventhubTest1" --resource-group "kustorptest"
"""

helps['kusto data-connection iot-hub'] = """
    type: group
    short-summary: kusto data-connection sub group iot-hub
"""

helps['kusto data-connection iot-hub create'] = """
    type: command
    short-summary: Creates or updates a data connection.
"""

helps['kusto data-connection event-grid update'] = """
    type: command
    short-summary: Updates a data connection.
"""

helps['kusto data-connection event-hub update'] = """
    type: command
    short-summary: Updates a data connection.
    examples:
      - name: KustoDataConnectionsUpdate
        text: |-
               az kusto data-connection event-hub update --cluster-name "KustoClusterRPTest4" --data-connection-name "D\
ataConnections8" --database-name "KustoDatabase8" --location "westus" --consumer-group "testConsumerGroup1" --event-hub\
-resource-id "/subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventH\
ub/namespaces/eventhubTestns1/eventhubs/eventhubTest1" --resource-group "kustorptest"
"""

helps['kusto data-connection iot-hub update'] = """
    type: command
    short-summary: Updates a data connection.
"""

helps['kusto data-connection delete'] = """
    type: command
    short-summary: Deletes the data connection with the given name.
    examples:
      - name: KustoDataConnectionsDelete
        text: |-
               az kusto data-connection delete --cluster-name "KustoClusterRPTest4" --data-connection-name "kustoeventh\
ubconnection1" --database-name "KustoDatabase8" --resource-group "kustorptest"
"""

helps['kusto data-connection event-grid data-connection-validation'] = """
    type: command
    short-summary: Checks that the data connection parameters are valid.
"""

helps['kusto data-connection event-hub data-connection-validation'] = """
    type: command
    short-summary: Checks that the data connection parameters are valid.
    examples:
      - name: KustoDataConnectionValidation
        text: |-
               az kusto data-connection event-hub data-connection-validation --cluster-name "KustoClusterRPTest4" --dat\
abase-name "KustoDatabase8" --data-connection-name "DataConnections8" --consumer-group "testConsumerGroup1" --event-hub\
-resource-id "/subscriptions/12345678-1234-1234-1234-123456789098/resourceGroups/kustorptest/providers/Microsoft.EventH\
ub/namespaces/eventhubTestns1/eventhubs/eventhubTest1" --resource-group "kustorptest"
"""

helps['kusto data-connection iot-hub data-connection-validation'] = """
    type: command
    short-summary: Checks that the data connection parameters are valid.
"""
