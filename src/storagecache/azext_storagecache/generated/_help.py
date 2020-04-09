# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
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
    examples:
      - name: Caches_CreateOrUpdate
        text: |-
               az storagecache cache create --location "westus" --properties-subnet "/subscriptions/00000
               000-0000-0000-0000-000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtual
               Networks/scvnet/subnets/sub1" --sku name=Standard_2G --tags Dept=Initech --cache-name
               "sc1" --resource-group "scgroup"
"""

helps['storagecache cache update'] = """
    type: command
    short-summary: Update a Cache instance.
    examples:
      - name: Caches_Update
        text: |-
               az storagecache cache update --location "westus" --properties-subnet "/subscriptions/00000
               000-0000-0000-0000-000000000000/resourceGroups/scgroup/providers/Microsoft.Network/virtual
               Networks/scvnet/subnets/sub1" --sku name=Standard_2G --tags Dept=Initech --cache-name
               "sc1" --resource-group "scgroup"
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
    short-summary: Tells a Cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete.
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
               az storagecache storage-target show --cache-name "sc1" --resource-group "scgroup"
               --storage-target-name "st1"
"""

helps['storagecache storage-target create'] = """
    type: command
    short-summary: Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again.
    examples:
      - name: StorageTargets_CreateOrUpdate
        text: |-
               az storagecache storage-target create --cache-name "sc1" --resource-group "scgroup"
               --storage-target-name "st1" --properties-junctions
               namespace-path=/path/on/cache nfs-export=exp1 target-path=/path/on/exp1
               --properties-junctions
               namespace-path=/path2/on/cache nfs-export=exp2 target-path=/path2/on/exp2
               --properties-nfs3 target=10.0.44.44 usage-model=READ_HEAVY_INFREQ
               --properties-target-type "nfs3"
"""

helps['storagecache storage-target update'] = """
    type: command
    short-summary: Create or update a Storage Target. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the Cache is healthy again.
    examples:
      - name: StorageTargets_CreateOrUpdate
        text: |-
               az storagecache storage-target create --cache-name "sc1" --resource-group "scgroup"
               --storage-target-name "st1" --properties-junctions
               namespace-path=/path/on/cache nfs-export=exp1 target-path=/path/on/exp1
               --properties-junctions
               namespace-path=/path2/on/cache nfs-export=exp2 target-path=/path2/on/exp2
               --properties-nfs3 target=10.0.44.44 usage-model=READ_HEAVY_INFREQ
               --properties-target-type "nfs3"
"""

helps['storagecache storage-target delete'] = """
    type: command
    short-summary: Removes a Storage Target from a Cache. This operation is allowed at any time, but if the Cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the Cache is healthy again. Note that if the Cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted.
    examples:
      - name: StorageTargets_Delete
        text: |-
               az storagecache storage-target delete --cache-name "sc1" --resource-group "scgroup"
               --storage-target-name "st1"
"""
