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


helps['storagecache sku'] = """
    type: group
    short-summary: storagecache sku
"""

helps['storagecache sku list'] = """
    type: command
    short-summary: Get the list of StorageCache.Cache SKUs available to this subscription.
    examples:
      - name: Skus_List
        text: |-
               az storagecache sku list
"""

helps['storagecache usage-model'] = """
    type: group
    short-summary: storagecache usage-model
"""

helps['storagecache usage-model list'] = """
    type: command
    short-summary: Get the list of Cache Usage Models available to this subscription.
    examples:
      - name: UsageModels_List
        text: |-
               az storagecache usage-model list
"""

helps['storagecache asc-operation'] = """
    type: group
    short-summary: storagecache asc-operation
"""

helps['storagecache asc-operation show'] = """
    type: command
    short-summary: Gets the status of an asynchronous operation for the Azure HPC cache
    examples:
      - name: AscOperations_Get
        text: |-
               az storagecache asc-operation show --operation-id "testoperationid" --location "West US"
"""

helps['storagecache cache'] = """
    type: group
    short-summary: storagecache cache
"""

helps['storagecache cache list'] = """
    type: command
    short-summary: Returns all Caches the user has access to under a subscription.
    examples:
      - name: Caches_ListByResourceGroup
        text: |-
               az storagecache cache list --resource-group "scgroup"
"""

helps['storagecache cache show'] = """
    type: command
    short-summary: Returns a Cache.
    examples:
      - name: Caches_Get
        text: |-
               az storagecache cache show --cache-name "sc1" --resource-group "scgroup"
"""

helps['storagecache cache create'] = """
    type: command
    short-summary: Create or update a Cache.
    parameters:
      - name: --network-settings
        short-summary: Specifies network settings of the cache.
        long-summary: |
            Usage: --network-settings mtu=XX

            mtu: The IPv4 maximum transmission unit configured for the subnet.
      - name: --security-settings
        short-summary: Specifies security settings of the cache.
        long-summary: |
            Usage: --security-settings root-squash=XX

            root-squash: root squash of cache property.
    examples:
      - name: Caches_CreateOrUpdate
        text: |-
               az storagecache cache create --location "westus" --cache-size-gb 3072 --subnet "/subscriptions/00000000-\
0000-0000-0000-000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1" --s\
ku-name "Standard_2G" --tags "{\\"Dept\\":\\"ContosoAds\\"}" --cache-name "sc1" --resource-group "scgroup"
"""

helps['storagecache cache update'] = """
    type: command
    short-summary: Update a Cache instance.
    parameters:
      - name: --network-settings
        short-summary: Specifies network settings of the cache.
        long-summary: |
            Usage: --network-settings mtu=XX

            mtu: The IPv4 maximum transmission unit configured for the subnet.
      - name: --security-settings
        short-summary: Specifies security settings of the cache.
        long-summary: |
            Usage: --security-settings root-squash=XX

            root-squash: root squash of cache property.
    examples:
      - name: Caches_Update
        text: |-
               az storagecache cache update --location "westus" --cache-size-gb 3072 --subnet "/subscriptions/00000000-\
0000-0000-0000-000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtualNetworks/scvnet/subnets/sub1" --s\
ku-name "Standard_2G" --tags "{\\"Dept\\":\\"ContosoAds\\"}" --cache-name "sc1" --resource-group "scgroup"
"""

helps['storagecache cache delete'] = """
    type: command
    short-summary: Schedules a Cache for deletion.
    examples:
      - name: Caches_Delete
        text: |-
               az storagecache cache delete --cache-name "sc" --resource-group "scgroup"
"""

helps['storagecache cache flush'] = """
    type: command
    short-summary: Tells a Cache to write all dirty data to the Storage Target(s). During the flush, clients will see e\
rrors returned until the flush is complete.
    examples:
      - name: Caches_Flush
        text: |-
               az storagecache cache flush --cache-name "sc" --resource-group "scgroup"
"""

helps['storagecache cache start'] = """
    type: command
    short-summary: Tells a Stopped state Cache to transition to Active state.
    examples:
      - name: Caches_Start
        text: |-
               az storagecache cache start --cache-name "sc" --resource-group "scgroup"
"""

helps['storagecache cache stop'] = """
    type: command
    short-summary: Tells an Active Cache to transition to Stopped state.
    examples:
      - name: Caches_Stop
        text: |-
               az storagecache cache stop --cache-name "sc" --resource-group "scgroup"
"""

helps['storagecache cache upgrade-firmware'] = """
    type: command
    short-summary: Upgrade a Cache's firmware if a new version is available. Otherwise, this operation has no effect.
    examples:
      - name: Caches_UpgradeFirmware
        text: |-
               az storagecache cache upgrade-firmware --cache-name "sc1" --resource-group "scgroup"
"""

helps['storagecache cache wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the storagecache cache is met.
    examples:
      - name: Pause executing next line of CLI script until the storagecache cache is successfully created.
        text: |-
               az storagecache cache wait --cache-name "sc1" --resource-group "scgroup" --created
      - name: Pause executing next line of CLI script until the storagecache cache is successfully deleted.
        text: |-
               az storagecache cache wait --cache-name "sc1" --resource-group "scgroup" --deleted
"""

helps['storagecache storage-target'] = """
    type: group
    short-summary: storagecache storage-target
"""

helps['storagecache storage-target list'] = """
    type: command
    short-summary: Returns a list of Storage Targets for the specified Cache.
    examples:
      - name: StorageTargets_List
        text: |-
               az storagecache storage-target list --cache-name "sc1" --resource-group "scgroup"
"""

helps['storagecache storage-target show'] = """
    type: command
    short-summary: Returns a Storage Target from a Cache.
    examples:
      - name: StorageTargets_Get
        text: |-
               az storagecache storage-target show --cache-name "sc1" --resource-group "scgroup" --name "st1"
"""

helps['storagecache storage-target create'] = """
    type: command
    short-summary: Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down o\
r unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again.
    parameters:
      - name: --junctions
        short-summary: List of Cache namespace junctions to target for namespace associations.
        long-summary: |
            Usage: --junctions namespace-path=XX target-path=XX nfs-export=XX

            namespace-path: Namespace path on a Cache for a Storage Target.
            target-path: Path in Storage Target to which namespacePath points.
            nfs-export: NFS export where targetPath exists.

            Multiple actions can be specified by using more than one --junctions argument.
      - name: --nfs3
        short-summary: Properties when targetType is nfs3.
        long-summary: |
            Usage: --nfs3 target=XX usage-model=XX

            target: IP address or host name of an NFSv3 host (e.g., 10.0.44.44).
            usage-model: Identifies the primary usage model to be used for this Storage Target. Get choices from .../us\
ageModels
      - name: --clfs
        short-summary: Properties when targetType is clfs.
        long-summary: |
            Usage: --clfs target=XX

            target: Resource ID of storage container.
    examples:
      - name: StorageTargets_CreateOrUpdate
        text: |-
               az storagecache storage-target create --cache-name "sc1" --resource-group "scgroup" --name "st1" --junct\
ions namespace-path="/path/on/cache" nfs-export="exp1" target-path="/path/on/exp1" --junctions namespace-path="/path2/o\
n/cache" nfs-export="exp2" target-path="/path2/on/exp2" --nfs3 target="10.0.44.44" usage-model="READ_HEAVY_INFREQ" --ta\
rget-type "nfs3"
"""

helps['storagecache storage-target update'] = """
    type: command
    short-summary: Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down o\
r unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again.
    parameters:
      - name: --junctions
        short-summary: List of Cache namespace junctions to target for namespace associations.
        long-summary: |
            Usage: --junctions namespace-path=XX target-path=XX nfs-export=XX

            namespace-path: Namespace path on a Cache for a Storage Target.
            target-path: Path in Storage Target to which namespacePath points.
            nfs-export: NFS export where targetPath exists.

            Multiple actions can be specified by using more than one --junctions argument.
      - name: --nfs3
        short-summary: Properties when targetType is nfs3.
        long-summary: |
            Usage: --nfs3 target=XX usage-model=XX

            target: IP address or host name of an NFSv3 host (e.g., 10.0.44.44).
            usage-model: Identifies the primary usage model to be used for this Storage Target. Get choices from .../us\
ageModels
      - name: --clfs
        short-summary: Properties when targetType is clfs.
        long-summary: |
            Usage: --clfs target=XX

            target: Resource ID of storage container.
    examples:
      - name: StorageTargets_CreateOrUpdate
        text: |-
               az storagecache storage-target update --cache-name "sc1" --resource-group "scgroup" --name "st1" --junct\
ions namespace-path="/path/on/cache" nfs-export="exp1" target-path="/path/on/exp1" --junctions namespace-path="/path2/o\
n/cache" nfs-export="exp2" target-path="/path2/on/exp2" --nfs3 target="10.0.44.44" usage-model="READ_HEAVY_INFREQ" --ta\
rget-type "nfs3"
"""

helps['storagecache storage-target delete'] = """
    type: command
    short-summary: Removes a Storage Target from a Cache. This operation is allowed at any time, but if the Cache is do\
wn or unhealthy, the actual removal of the Storage Target may be delayed until the Cache is healthy again. Note that if\
 the Cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted.
    examples:
      - name: StorageTargets_Delete
        text: |-
               az storagecache storage-target delete --cache-name "sc1" --resource-group "scgroup" --name "st1"
"""

helps['storagecache storage-target wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the storagecache storage-target is met.
    examples:
      - name: Pause executing next line of CLI script until the storagecache storage-target is successfully created.
        text: |-
               az storagecache storage-target wait --cache-name "sc1" --resource-group "scgroup" --name "st1" --created
      - name: Pause executing next line of CLI script until the storagecache storage-target is successfully deleted.
        text: |-
               az storagecache storage-target wait --cache-name "sc1" --resource-group "scgroup" --name "st1" --deleted
"""
