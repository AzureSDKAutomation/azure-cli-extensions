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


helps['storageimportexport location'] = """
    type: group
    short-summary: Manage location with storageimportexport
"""

helps['storageimportexport location list'] = """
    type: command
    short-summary: "Returns a list of locations to which you can ship the disks associated with an import or export \
job. A location is a Microsoft data center region."
    examples:
      - name: List locations
        text: |-
               az storageimportexport location list
"""

helps['storageimportexport location show'] = """
    type: command
    short-summary: "Returns the details about a location to which you can ship the disks associated with an import or \
export job. A location is an Azure region."
    examples:
      - name: Get locations
        text: |-
               az storageimportexport location show --name "West US"
"""

helps['storageimportexport job'] = """
    type: group
    short-summary: Manage job with storageimportexport
"""

helps['storageimportexport job list'] = """
    type: command
    short-summary: "Returns all active and completed jobs in a resource group. And Returns all active and completed \
jobs in a subscription."
    examples:
      - name: List jobs in a resource group
        text: |-
               az storageimportexport job list --resource-group "myResourceGroup"
      - name: List jobs in a subscription
        text: |-
               az storageimportexport job list
"""

helps['storageimportexport job show'] = """
    type: command
    short-summary: "Gets information about an existing job."
    examples:
      - name: Get job
        text: |-
               az storageimportexport job show --name "myJob" --resource-group "myResourceGroup"
"""

helps['storageimportexport job create'] = """
    type: command
    short-summary: "Creates a new job or updates an existing job in the specified subscription."
    parameters:
      - name: --return-address
        short-summary: "Specifies the return address information for the job."
        long-summary: |
            Usage: --return-address recipient-name=XX street-address1=XX street-address2=XX city=XX \
state-or-province=XX postal-code=XX country-or-region=XX phone=XX email=XX

            recipient-name: Required. The name of the recipient who will receive the hard drives when they are \
returned.
            street-address1: Required. The first line of the street address to use when returning the drives.
            street-address2: The second line of the street address to use when returning the drives.
            city: Required. The city name to use when returning the drives.
            state-or-province: The state or province to use when returning the drives.
            postal-code: Required. The postal code to use when returning the drives.
            country-or-region: Required. The country or region to use when returning the drives.
            phone: Required. Phone number of the recipient of the returned drives.
            email: Required. Email address of the recipient of the returned drives.
      - name: --return-shipping
        short-summary: "Specifies the return carrier and customer's account with the carrier."
        long-summary: |
            Usage: --return-shipping carrier-name=XX carrier-account-number=XX

            carrier-name: Required. The carrier's name.
            carrier-account-number: Required. The customer's account number with the carrier.
      - name: --shipping-information
        short-summary: "Contains information about the Microsoft datacenter to which the drives should be shipped."
        long-summary: |
            Usage: --shipping-information recipient-name=XX street-address1=XX street-address2=XX city=XX \
state-or-province=XX postal-code=XX country-or-region=XX phone=XX

            recipient-name: Required. The name of the recipient who will receive the hard drives when they are \
returned.
            street-address1: Required. The first line of the street address to use when returning the drives.
            street-address2: The second line of the street address to use when returning the drives.
            city: Required. The city name to use when returning the drives.
            state-or-province: Required. The state or province to use when returning the drives.
            postal-code: Required. The postal code to use when returning the drives.
            country-or-region: Required. The country or region to use when returning the drives.
            phone: Phone number of the recipient of the returned drives.
      - name: --delivery-package
        short-summary: "Contains information about the package being shipped by the customer to the Microsoft data \
center."
        long-summary: |
            Usage: --delivery-package carrier-name=XX tracking-number=XX drive-count=XX ship-date=XX

            carrier-name: Required. The name of the carrier that is used to ship the import or export drives.
            tracking-number: Required. The tracking number of the package.
            drive-count: Required. The number of drives included in the package.
            ship-date: Required. The date when the package is shipped.
      - name: --return-package
        short-summary: "Contains information about the package being shipped from the Microsoft data center to the \
customer to return the drives. The format is the same as the deliveryPackage property above. This property is not \
included if the drives have not yet been returned."
        long-summary: |
            Usage: --return-package carrier-name=XX tracking-number=XX drive-count=XX ship-date=XX

            carrier-name: Required. The name of the carrier that is used to ship the import or export drives.
            tracking-number: Required. The tracking number of the package.
            drive-count: Required. The number of drives included in the package.
            ship-date: Required. The date when the package is shipped.
      - name: --drive-list
        short-summary: "List of up to ten drives that comprise the job. The drive list is a required element for an \
import job; it is not specified for export jobs."
        long-summary: |
            Usage: --drive-list drive-id=XX bit-locker-key=XX manifest-file=XX manifest-hash=XX drive-header-hash=XX \
state=XX copy-status=XX percent-complete=XX verbose-log-uri=XX error-log-uri=XX manifest-uri=XX bytes-succeeded=XX

            drive-id: The drive's hardware serial number, without spaces.
            bit-locker-key: The BitLocker key used to encrypt the drive.
            manifest-file: The relative path of the manifest file on the drive.
            manifest-hash: The Base16-encoded MD5 hash of the manifest file on the drive.
            drive-header-hash: The drive header hash value.
            state: The drive's current state.
            copy-status: Detailed status about the data transfer process. This field is not returned in the response \
until the drive is in the Transferring state.
            percent-complete: Percentage completed for the drive.
            verbose-log-uri: A URI that points to the blob containing the verbose log for the data transfer operation.
            error-log-uri: A URI that points to the blob containing the error log for the data transfer operation.
            manifest-uri: A URI that points to the blob containing the drive manifest file.
            bytes-succeeded: Bytes successfully transferred for the drive.

            Multiple actions can be specified by using more than one --drive-list argument.
      - name: --export
        short-summary: "A property containing information about the blobs to be exported for an export job. This \
property is included for export jobs only."
        long-summary: |
            Usage: --export blob-listblob-path=XX blob-path=XX blob-path-prefix=XX

            blob-listblob-path: The relative URI to the block blob that contains the list of blob paths or blob path \
prefixes as defined above, beginning with the container name. If the blob is in root container, the URI must begin \
with $root.
            blob-path: A collection of blob-path strings.
            blob-path-prefix: A collection of blob-prefix strings.
    examples:
      - name: Create job
        text: |-
               az storageimportexport job create --location "West US" --backup-drive-manifest true --diagnostics-path \
"waimportexport" --drive-list bit-locker-key="238810-662376-448998-450120-652806-203390-606320-483076" \
drive-header-hash="" drive-id="9CA995BB" manifest-file="\\\\DriveManifest.xml" manifest-hash="109B21108597EF36D5785F083\
03F3638" --job-type "Import" --log-level "Verbose" --return-address city="Redmond" country-or-region="USA" \
email="Test@contoso.com" phone="4250000000" postal-code="98007" recipient-name="Tets" state-or-province="wa" \
street-address1="Street1" street-address2="street2" --storage-account-id "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxx\
xxxxxx/resourceGroups/myResourceGroup/providers/Microsoft.ClassicStorage/storageAccounts/test" --name "myJob" \
--resource-group "myResourceGroup"
"""

helps['storageimportexport job update'] = """
    type: command
    short-summary: "Updates specific properties of a job. You can call this operation to notify the Import/Export \
service that the hard drives comprising the import or export job have been shipped to the Microsoft data center. It \
can also be used to cancel an existing job."
    parameters:
      - name: --return-address
        short-summary: "Specifies the return address information for the job."
        long-summary: |
            Usage: --return-address recipient-name=XX street-address1=XX street-address2=XX city=XX \
state-or-province=XX postal-code=XX country-or-region=XX phone=XX email=XX

            recipient-name: Required. The name of the recipient who will receive the hard drives when they are \
returned.
            street-address1: Required. The first line of the street address to use when returning the drives.
            street-address2: The second line of the street address to use when returning the drives.
            city: Required. The city name to use when returning the drives.
            state-or-province: The state or province to use when returning the drives.
            postal-code: Required. The postal code to use when returning the drives.
            country-or-region: Required. The country or region to use when returning the drives.
            phone: Required. Phone number of the recipient of the returned drives.
            email: Required. Email address of the recipient of the returned drives.
      - name: --return-shipping
        short-summary: "Specifies the return carrier and customer's account with the carrier."
        long-summary: |
            Usage: --return-shipping carrier-name=XX carrier-account-number=XX

            carrier-name: Required. The carrier's name.
            carrier-account-number: Required. The customer's account number with the carrier.
      - name: --delivery-package
        short-summary: "Contains information about the package being shipped by the customer to the Microsoft data \
center."
        long-summary: |
            Usage: --delivery-package carrier-name=XX tracking-number=XX drive-count=XX ship-date=XX

            carrier-name: Required. The name of the carrier that is used to ship the import or export drives.
            tracking-number: Required. The tracking number of the package.
            drive-count: Required. The number of drives included in the package.
            ship-date: Required. The date when the package is shipped.
      - name: --drive-list
        short-summary: "List of drives that comprise the job."
        long-summary: |
            Usage: --drive-list drive-id=XX bit-locker-key=XX manifest-file=XX manifest-hash=XX drive-header-hash=XX \
state=XX copy-status=XX percent-complete=XX verbose-log-uri=XX error-log-uri=XX manifest-uri=XX bytes-succeeded=XX

            drive-id: The drive's hardware serial number, without spaces.
            bit-locker-key: The BitLocker key used to encrypt the drive.
            manifest-file: The relative path of the manifest file on the drive.
            manifest-hash: The Base16-encoded MD5 hash of the manifest file on the drive.
            drive-header-hash: The drive header hash value.
            state: The drive's current state.
            copy-status: Detailed status about the data transfer process. This field is not returned in the response \
until the drive is in the Transferring state.
            percent-complete: Percentage completed for the drive.
            verbose-log-uri: A URI that points to the blob containing the verbose log for the data transfer operation.
            error-log-uri: A URI that points to the blob containing the error log for the data transfer operation.
            manifest-uri: A URI that points to the blob containing the drive manifest file.
            bytes-succeeded: Bytes successfully transferred for the drive.

            Multiple actions can be specified by using more than one --drive-list argument.
    examples:
      - name: Update job
        text: |-
               az storageimportexport job update --backup-drive-manifest true --log-level "Verbose" --state "" --name \
"myJob" --resource-group "myResourceGroup"
"""

helps['storageimportexport job delete'] = """
    type: command
    short-summary: "Deletes an existing job. Only jobs in the Creating or Completed states can be deleted."
    examples:
      - name: Delete job
        text: |-
               az storageimportexport job delete --name "myJob" --resource-group "myResourceGroup"
"""

helps['storageimportexport bit-locker-key'] = """
    type: group
    short-summary: Manage bit locker key with storageimportexport
"""

helps['storageimportexport bit-locker-key list'] = """
    type: command
    short-summary: "Returns the BitLocker Keys for all drives in the specified job."
    examples:
      - name: List BitLocker Keys for drives in a job
        text: |-
               az storageimportexport bit-locker-key list --job-name "myJob" --resource-group "myResourceGroup"
"""
