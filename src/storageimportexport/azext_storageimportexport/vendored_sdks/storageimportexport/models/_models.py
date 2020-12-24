# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class DriveBitLockerKey(msrest.serialization.Model):
    """BitLocker recovery key or password to the specified drive.

    :param bit_locker_key: BitLocker recovery key or password.
    :type bit_locker_key: str
    :param drive_id: Drive ID.
    :type drive_id: str
    """

    _attribute_map = {
        'bit_locker_key': {'key': 'bitLockerKey', 'type': 'str'},
        'drive_id': {'key': 'driveId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DriveBitLockerKey, self).__init__(**kwargs)
        self.bit_locker_key = kwargs.get('bit_locker_key', None)
        self.drive_id = kwargs.get('drive_id', None)


class DriveStatus(msrest.serialization.Model):
    """Provides information about the drive's status.

    :param drive_id: The drive's hardware serial number, without spaces.
    :type drive_id: str
    :param bit_locker_key: The BitLocker key used to encrypt the drive.
    :type bit_locker_key: str
    :param manifest_file: The relative path of the manifest file on the drive.
    :type manifest_file: str
    :param manifest_hash: The Base16-encoded MD5 hash of the manifest file on the drive.
    :type manifest_hash: str
    :param drive_header_hash: The drive header hash value.
    :type drive_header_hash: str
    :param state: The drive's current state. Possible values include: "Specified", "Received",
     "NeverReceived", "Transferring", "Completed", "CompletedMoreInfo", "ShippedBack".
    :type state: str or ~storage_import_export.models.DriveState
    :param copy_status: Detailed status about the data transfer process. This field is not returned
     in the response until the drive is in the Transferring state.
    :type copy_status: str
    :param percent_complete: Percentage completed for the drive.
    :type percent_complete: int
    :param verbose_log_uri: A URI that points to the blob containing the verbose log for the data
     transfer operation.
    :type verbose_log_uri: str
    :param error_log_uri: A URI that points to the blob containing the error log for the data
     transfer operation.
    :type error_log_uri: str
    :param manifest_uri: A URI that points to the blob containing the drive manifest file.
    :type manifest_uri: str
    :param bytes_succeeded: Bytes successfully transferred for the drive.
    :type bytes_succeeded: long
    """

    _attribute_map = {
        'drive_id': {'key': 'driveId', 'type': 'str'},
        'bit_locker_key': {'key': 'bitLockerKey', 'type': 'str'},
        'manifest_file': {'key': 'manifestFile', 'type': 'str'},
        'manifest_hash': {'key': 'manifestHash', 'type': 'str'},
        'drive_header_hash': {'key': 'driveHeaderHash', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'copy_status': {'key': 'copyStatus', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'verbose_log_uri': {'key': 'verboseLogUri', 'type': 'str'},
        'error_log_uri': {'key': 'errorLogUri', 'type': 'str'},
        'manifest_uri': {'key': 'manifestUri', 'type': 'str'},
        'bytes_succeeded': {'key': 'bytesSucceeded', 'type': 'long'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DriveStatus, self).__init__(**kwargs)
        self.drive_id = kwargs.get('drive_id', None)
        self.bit_locker_key = kwargs.get('bit_locker_key', None)
        self.manifest_file = kwargs.get('manifest_file', None)
        self.manifest_hash = kwargs.get('manifest_hash', None)
        self.drive_header_hash = kwargs.get('drive_header_hash', None)
        self.state = kwargs.get('state', None)
        self.copy_status = kwargs.get('copy_status', None)
        self.percent_complete = kwargs.get('percent_complete', None)
        self.verbose_log_uri = kwargs.get('verbose_log_uri', None)
        self.error_log_uri = kwargs.get('error_log_uri', None)
        self.manifest_uri = kwargs.get('manifest_uri', None)
        self.bytes_succeeded = kwargs.get('bytes_succeeded', None)


class ErrorResponse(msrest.serialization.Model):
    """Response when errors occurred.

    :param code: Provides information about the error code.
    :type code: str
    :param message: Provides information about the error message.
    :type message: str
    :param target: Provides information about the error target.
    :type target: str
    :param details: Describes the error details if present.
    :type details: list[~storage_import_export.models.ErrorResponseErrorDetailsItem]
    :param innererror: Inner error object if present.
    :type innererror: object
    """

    _attribute_map = {
        'code': {'key': 'error.code', 'type': 'str'},
        'message': {'key': 'error.message', 'type': 'str'},
        'target': {'key': 'error.target', 'type': 'str'},
        'details': {'key': 'error.details', 'type': '[ErrorResponseErrorDetailsItem]'},
        'innererror': {'key': 'error.innererror', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)


class ErrorResponseErrorDetailsItem(msrest.serialization.Model):
    """ErrorResponseErrorDetailsItem.

    :param code: Provides information about the error code.
    :type code: str
    :param target: Provides information about the error target.
    :type target: str
    :param message: Provides information about the error message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponseErrorDetailsItem, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.target = kwargs.get('target', None)
        self.message = kwargs.get('message', None)


class Export(msrest.serialization.Model):
    """A property containing information about the blobs to be exported for an export job. This property is required for export jobs, but must not be specified for import jobs.

    :param blob_listblob_path: The relative URI to the block blob that contains the list of blob
     paths or blob path prefixes as defined above, beginning with the container name. If the blob is
     in root container, the URI must begin with $root.
    :type blob_listblob_path: str
    :param blob_path: A collection of blob-path strings.
    :type blob_path: list[str]
    :param blob_path_prefix: A collection of blob-prefix strings.
    :type blob_path_prefix: list[str]
    """

    _attribute_map = {
        'blob_listblob_path': {'key': 'blobListblobPath', 'type': 'str'},
        'blob_path': {'key': 'blobList.blobPath', 'type': '[str]'},
        'blob_path_prefix': {'key': 'blobList.blobPathPrefix', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Export, self).__init__(**kwargs)
        self.blob_listblob_path = kwargs.get('blob_listblob_path', None)
        self.blob_path = kwargs.get('blob_path', None)
        self.blob_path_prefix = kwargs.get('blob_path_prefix', None)


class GetBitLockerKeysResponse(msrest.serialization.Model):
    """GetBitLockerKeys response.

    :param value: drive status.
    :type value: list[~storage_import_export.models.DriveBitLockerKey]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DriveBitLockerKey]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GetBitLockerKeysResponse, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class JobDetails(msrest.serialization.Model):
    """Specifies the job properties.

    :param storage_account_id: The resource identifier of the storage account where data will be
     imported to or exported from.
    :type storage_account_id: str
    :param job_type: The type of job.
    :type job_type: str
    :param return_address: Specifies the return address information for the job.
    :type return_address: ~storage_import_export.models.ReturnAddress
    :param return_shipping: Specifies the return carrier and customer's account with the carrier.
    :type return_shipping: ~storage_import_export.models.ReturnShipping
    :param shipping_information: Contains information about the Microsoft datacenter to which the
     drives should be shipped.
    :type shipping_information: ~storage_import_export.models.ShippingInformation
    :param delivery_package: Contains information about the package being shipped by the customer
     to the Microsoft data center.
    :type delivery_package: ~storage_import_export.models.PackageInfomation
    :param return_package: Contains information about the package being shipped from the Microsoft
     data center to the customer to return the drives. The format is the same as the deliveryPackage
     property above. This property is not included if the drives have not yet been returned.
    :type return_package: ~storage_import_export.models.PackageInfomation
    :param diagnostics_path: The virtual blob directory to which the copy logs and backups of drive
     manifest files (if enabled) will be stored.
    :type diagnostics_path: str
    :param log_level: Default value is Error. Indicates whether error logging or verbose logging
     will be enabled.
    :type log_level: str
    :param backup_drive_manifest: Default value is false. Indicates whether the manifest files on
     the drives should be copied to block blobs.
    :type backup_drive_manifest: bool
    :param state: Current state of the job.
    :type state: str
    :param cancel_requested: Indicates whether a request has been submitted to cancel the job.
    :type cancel_requested: bool
    :param percent_complete: Overall percentage completed for the job.
    :type percent_complete: int
    :param incomplete_blob_list_uri: A blob path that points to a block blob containing a list of
     blob names that were not exported due to insufficient drive space. If all blobs were exported
     successfully, then this element is not included in the response.
    :type incomplete_blob_list_uri: str
    :param drive_list: List of up to ten drives that comprise the job. The drive list is a required
     element for an import job; it is not specified for export jobs.
    :type drive_list: list[~storage_import_export.models.DriveStatus]
    :param export: A property containing information about the blobs to be exported for an export
     job. This property is included for export jobs only.
    :type export: ~storage_import_export.models.Export
    :param provisioning_state: Specifies the provisioning state of the job.
    :type provisioning_state: str
    """

    _attribute_map = {
        'storage_account_id': {'key': 'storageAccountId', 'type': 'str'},
        'job_type': {'key': 'jobType', 'type': 'str'},
        'return_address': {'key': 'returnAddress', 'type': 'ReturnAddress'},
        'return_shipping': {'key': 'returnShipping', 'type': 'ReturnShipping'},
        'shipping_information': {'key': 'shippingInformation', 'type': 'ShippingInformation'},
        'delivery_package': {'key': 'deliveryPackage', 'type': 'PackageInfomation'},
        'return_package': {'key': 'returnPackage', 'type': 'PackageInfomation'},
        'diagnostics_path': {'key': 'diagnosticsPath', 'type': 'str'},
        'log_level': {'key': 'logLevel', 'type': 'str'},
        'backup_drive_manifest': {'key': 'backupDriveManifest', 'type': 'bool'},
        'state': {'key': 'state', 'type': 'str'},
        'cancel_requested': {'key': 'cancelRequested', 'type': 'bool'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'incomplete_blob_list_uri': {'key': 'incompleteBlobListUri', 'type': 'str'},
        'drive_list': {'key': 'driveList', 'type': '[DriveStatus]'},
        'export': {'key': 'export', 'type': 'Export'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(JobDetails, self).__init__(**kwargs)
        self.storage_account_id = kwargs.get('storage_account_id', None)
        self.job_type = kwargs.get('job_type', None)
        self.return_address = kwargs.get('return_address', None)
        self.return_shipping = kwargs.get('return_shipping', None)
        self.shipping_information = kwargs.get('shipping_information', None)
        self.delivery_package = kwargs.get('delivery_package', None)
        self.return_package = kwargs.get('return_package', None)
        self.diagnostics_path = kwargs.get('diagnostics_path', None)
        self.log_level = kwargs.get('log_level', None)
        self.backup_drive_manifest = kwargs.get('backup_drive_manifest', None)
        self.state = kwargs.get('state', None)
        self.cancel_requested = kwargs.get('cancel_requested', None)
        self.percent_complete = kwargs.get('percent_complete', None)
        self.incomplete_blob_list_uri = kwargs.get('incomplete_blob_list_uri', None)
        self.drive_list = kwargs.get('drive_list', None)
        self.export = kwargs.get('export', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)


class JobResponse(msrest.serialization.Model):
    """Contains the job information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Specifies the resource identifier of the job.
    :vartype id: str
    :ivar name: Specifies the name of the job.
    :vartype name: str
    :ivar type: Specifies the type of the job resource.
    :vartype type: str
    :param location: Specifies the Azure location where the job is created.
    :type location: str
    :param tags: A set of tags. Specifies the tags that are assigned to the job.
    :type tags: object
    :param properties: Specifies the job properties.
    :type properties: ~storage_import_export.models.JobDetails
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'properties': {'key': 'properties', 'type': 'JobDetails'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(JobResponse, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.properties = kwargs.get('properties', None)


class ListJobsResponse(msrest.serialization.Model):
    """List jobs response.

    :param next_link: link to next batch of jobs.
    :type next_link: str
    :param value: Job list.
    :type value: list[~storage_import_export.models.JobResponse]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'value': {'key': 'value', 'type': '[JobResponse]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListJobsResponse, self).__init__(**kwargs)
        self.next_link = kwargs.get('next_link', None)
        self.value = kwargs.get('value', None)


class ListOperationsResponse(msrest.serialization.Model):
    """List operations response.

    :param value: operations.
    :type value: list[~storage_import_export.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListOperationsResponse, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class Location(msrest.serialization.Model):
    """Provides information about an Azure data center location.

    :param id: Specifies the resource identifier of the location.
    :type id: str
    :param name: Specifies the name of the location. Use List Locations to get all supported
     locations.
    :type name: str
    :param type: Specifies the type of the location.
    :type type: str
    :param recipient_name: The recipient name to use when shipping the drives to the Azure data
     center.
    :type recipient_name: str
    :param street_address1: The first line of the street address to use when shipping the drives to
     the Azure data center.
    :type street_address1: str
    :param street_address2: The second line of the street address to use when shipping the drives
     to the Azure data center.
    :type street_address2: str
    :param city: The city name to use when shipping the drives to the Azure data center.
    :type city: str
    :param state_or_province: The state or province to use when shipping the drives to the Azure
     data center.
    :type state_or_province: str
    :param postal_code: The postal code to use when shipping the drives to the Azure data center.
    :type postal_code: str
    :param country_or_region: The country or region to use when shipping the drives to the Azure
     data center.
    :type country_or_region: str
    :param phone: The phone number for the Azure data center.
    :type phone: str
    :param supported_carriers: A list of carriers that are supported at this location.
    :type supported_carriers: list[str]
    :param alternate_locations: A list of location IDs that should be used to ship shipping drives
     to for jobs created against the current location. If the current location is active, it will be
     part of the list. If it is temporarily closed due to maintenance, this list may contain other
     locations.
    :type alternate_locations: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'recipient_name': {'key': 'properties.recipientName', 'type': 'str'},
        'street_address1': {'key': 'properties.streetAddress1', 'type': 'str'},
        'street_address2': {'key': 'properties.streetAddress2', 'type': 'str'},
        'city': {'key': 'properties.city', 'type': 'str'},
        'state_or_province': {'key': 'properties.stateOrProvince', 'type': 'str'},
        'postal_code': {'key': 'properties.postalCode', 'type': 'str'},
        'country_or_region': {'key': 'properties.countryOrRegion', 'type': 'str'},
        'phone': {'key': 'properties.phone', 'type': 'str'},
        'supported_carriers': {'key': 'properties.supportedCarriers', 'type': '[str]'},
        'alternate_locations': {'key': 'properties.alternateLocations', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Location, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.recipient_name = kwargs.get('recipient_name', None)
        self.street_address1 = kwargs.get('street_address1', None)
        self.street_address2 = kwargs.get('street_address2', None)
        self.city = kwargs.get('city', None)
        self.state_or_province = kwargs.get('state_or_province', None)
        self.postal_code = kwargs.get('postal_code', None)
        self.country_or_region = kwargs.get('country_or_region', None)
        self.phone = kwargs.get('phone', None)
        self.supported_carriers = kwargs.get('supported_carriers', None)
        self.alternate_locations = kwargs.get('alternate_locations', None)


class LocationsResponse(msrest.serialization.Model):
    """Locations response.

    :param value: locations.
    :type value: list[~storage_import_export.models.Location]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Location]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(LocationsResponse, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class Operation(msrest.serialization.Model):
    """Describes a supported operation by the Storage Import/Export job API.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the operation.
    :type name: str
    :param provider: The resource provider name to which the operation belongs.
    :type provider: str
    :param resource: The name of the resource to which the operation belongs.
    :type resource: str
    :param operation: The display name of the operation.
    :type operation: str
    :param description: Short description of the operation.
    :type description: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'provider': {'key': 'display.provider', 'type': 'str'},
        'resource': {'key': 'display.resource', 'type': 'str'},
        'operation': {'key': 'display.operation', 'type': 'str'},
        'description': {'key': 'display.description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class PackageInfomation(msrest.serialization.Model):
    """Contains information about the package being shipped by the customer to the Microsoft data center.

    All required parameters must be populated in order to send to Azure.

    :param carrier_name: Required. The name of the carrier that is used to ship the import or
     export drives.
    :type carrier_name: str
    :param tracking_number: Required. The tracking number of the package.
    :type tracking_number: str
    :param drive_count: Required. The number of drives included in the package.
    :type drive_count: int
    :param ship_date: Required. The date when the package is shipped.
    :type ship_date: str
    """

    _validation = {
        'carrier_name': {'required': True},
        'tracking_number': {'required': True},
        'drive_count': {'required': True},
        'ship_date': {'required': True},
    }

    _attribute_map = {
        'carrier_name': {'key': 'carrierName', 'type': 'str'},
        'tracking_number': {'key': 'trackingNumber', 'type': 'str'},
        'drive_count': {'key': 'driveCount', 'type': 'int'},
        'ship_date': {'key': 'shipDate', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PackageInfomation, self).__init__(**kwargs)
        self.carrier_name = kwargs['carrier_name']
        self.tracking_number = kwargs['tracking_number']
        self.drive_count = kwargs['drive_count']
        self.ship_date = kwargs['ship_date']


class PutJobParameters(msrest.serialization.Model):
    """Put Job parameters.

    :param location: Specifies the supported Azure location where the job should be created.
    :type location: str
    :param tags: A set of tags. Specifies the tags that will be assigned to the job.
    :type tags: object
    :param storage_account_id: The resource identifier of the storage account where data will be
     imported to or exported from.
    :type storage_account_id: str
    :param job_type: The type of job.
    :type job_type: str
    :param return_address: Specifies the return address information for the job.
    :type return_address: ~storage_import_export.models.ReturnAddress
    :param return_shipping: Specifies the return carrier and customer's account with the carrier.
    :type return_shipping: ~storage_import_export.models.ReturnShipping
    :param shipping_information: Contains information about the Microsoft datacenter to which the
     drives should be shipped.
    :type shipping_information: ~storage_import_export.models.ShippingInformation
    :param delivery_package: Contains information about the package being shipped by the customer
     to the Microsoft data center.
    :type delivery_package: ~storage_import_export.models.PackageInfomation
    :param return_package: Contains information about the package being shipped from the Microsoft
     data center to the customer to return the drives. The format is the same as the deliveryPackage
     property above. This property is not included if the drives have not yet been returned.
    :type return_package: ~storage_import_export.models.PackageInfomation
    :param diagnostics_path: The virtual blob directory to which the copy logs and backups of drive
     manifest files (if enabled) will be stored.
    :type diagnostics_path: str
    :param log_level: Default value is Error. Indicates whether error logging or verbose logging
     will be enabled.
    :type log_level: str
    :param backup_drive_manifest: Default value is false. Indicates whether the manifest files on
     the drives should be copied to block blobs.
    :type backup_drive_manifest: bool
    :param state: Current state of the job.
    :type state: str
    :param cancel_requested: Indicates whether a request has been submitted to cancel the job.
    :type cancel_requested: bool
    :param percent_complete: Overall percentage completed for the job.
    :type percent_complete: int
    :param incomplete_blob_list_uri: A blob path that points to a block blob containing a list of
     blob names that were not exported due to insufficient drive space. If all blobs were exported
     successfully, then this element is not included in the response.
    :type incomplete_blob_list_uri: str
    :param drive_list: List of up to ten drives that comprise the job. The drive list is a required
     element for an import job; it is not specified for export jobs.
    :type drive_list: list[~storage_import_export.models.DriveStatus]
    :param export: A property containing information about the blobs to be exported for an export
     job. This property is included for export jobs only.
    :type export: ~storage_import_export.models.Export
    :param provisioning_state: Specifies the provisioning state of the job.
    :type provisioning_state: str
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'job_type': {'key': 'properties.jobType', 'type': 'str'},
        'return_address': {'key': 'properties.returnAddress', 'type': 'ReturnAddress'},
        'return_shipping': {'key': 'properties.returnShipping', 'type': 'ReturnShipping'},
        'shipping_information': {'key': 'properties.shippingInformation', 'type': 'ShippingInformation'},
        'delivery_package': {'key': 'properties.deliveryPackage', 'type': 'PackageInfomation'},
        'return_package': {'key': 'properties.returnPackage', 'type': 'PackageInfomation'},
        'diagnostics_path': {'key': 'properties.diagnosticsPath', 'type': 'str'},
        'log_level': {'key': 'properties.logLevel', 'type': 'str'},
        'backup_drive_manifest': {'key': 'properties.backupDriveManifest', 'type': 'bool'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'cancel_requested': {'key': 'properties.cancelRequested', 'type': 'bool'},
        'percent_complete': {'key': 'properties.percentComplete', 'type': 'int'},
        'incomplete_blob_list_uri': {'key': 'properties.incompleteBlobListUri', 'type': 'str'},
        'drive_list': {'key': 'properties.driveList', 'type': '[DriveStatus]'},
        'export': {'key': 'properties.export', 'type': 'Export'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PutJobParameters, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.storage_account_id = kwargs.get('storage_account_id', None)
        self.job_type = kwargs.get('job_type', None)
        self.return_address = kwargs.get('return_address', None)
        self.return_shipping = kwargs.get('return_shipping', None)
        self.shipping_information = kwargs.get('shipping_information', None)
        self.delivery_package = kwargs.get('delivery_package', None)
        self.return_package = kwargs.get('return_package', None)
        self.diagnostics_path = kwargs.get('diagnostics_path', None)
        self.log_level = kwargs.get('log_level', None)
        self.backup_drive_manifest = kwargs.get('backup_drive_manifest', None)
        self.state = kwargs.get('state', None)
        self.cancel_requested = kwargs.get('cancel_requested', None)
        self.percent_complete = kwargs.get('percent_complete', None)
        self.incomplete_blob_list_uri = kwargs.get('incomplete_blob_list_uri', None)
        self.drive_list = kwargs.get('drive_list', None)
        self.export = kwargs.get('export', None)
        self.provisioning_state = kwargs.get('provisioning_state', None)


class ReturnAddress(msrest.serialization.Model):
    """Specifies the return address information for the job.

    All required parameters must be populated in order to send to Azure.

    :param recipient_name: Required. The name of the recipient who will receive the hard drives
     when they are returned.
    :type recipient_name: str
    :param street_address1: Required. The first line of the street address to use when returning
     the drives.
    :type street_address1: str
    :param street_address2: The second line of the street address to use when returning the drives.
    :type street_address2: str
    :param city: Required. The city name to use when returning the drives.
    :type city: str
    :param state_or_province: The state or province to use when returning the drives.
    :type state_or_province: str
    :param postal_code: Required. The postal code to use when returning the drives.
    :type postal_code: str
    :param country_or_region: Required. The country or region to use when returning the drives.
    :type country_or_region: str
    :param phone: Required. Phone number of the recipient of the returned drives.
    :type phone: str
    :param email: Required. Email address of the recipient of the returned drives.
    :type email: str
    """

    _validation = {
        'recipient_name': {'required': True},
        'street_address1': {'required': True},
        'city': {'required': True},
        'postal_code': {'required': True},
        'country_or_region': {'required': True},
        'phone': {'required': True},
        'email': {'required': True},
    }

    _attribute_map = {
        'recipient_name': {'key': 'recipientName', 'type': 'str'},
        'street_address1': {'key': 'streetAddress1', 'type': 'str'},
        'street_address2': {'key': 'streetAddress2', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state_or_province': {'key': 'stateOrProvince', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
        'country_or_region': {'key': 'countryOrRegion', 'type': 'str'},
        'phone': {'key': 'phone', 'type': 'str'},
        'email': {'key': 'email', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ReturnAddress, self).__init__(**kwargs)
        self.recipient_name = kwargs['recipient_name']
        self.street_address1 = kwargs['street_address1']
        self.street_address2 = kwargs.get('street_address2', None)
        self.city = kwargs['city']
        self.state_or_province = kwargs.get('state_or_province', None)
        self.postal_code = kwargs['postal_code']
        self.country_or_region = kwargs['country_or_region']
        self.phone = kwargs['phone']
        self.email = kwargs['email']


class ReturnShipping(msrest.serialization.Model):
    """Specifies the return carrier and customer's account with the carrier.

    All required parameters must be populated in order to send to Azure.

    :param carrier_name: Required. The carrier's name.
    :type carrier_name: str
    :param carrier_account_number: Required. The customer's account number with the carrier.
    :type carrier_account_number: str
    """

    _validation = {
        'carrier_name': {'required': True},
        'carrier_account_number': {'required': True},
    }

    _attribute_map = {
        'carrier_name': {'key': 'carrierName', 'type': 'str'},
        'carrier_account_number': {'key': 'carrierAccountNumber', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ReturnShipping, self).__init__(**kwargs)
        self.carrier_name = kwargs['carrier_name']
        self.carrier_account_number = kwargs['carrier_account_number']


class ShippingInformation(msrest.serialization.Model):
    """Contains information about the Microsoft datacenter to which the drives should be shipped.

    All required parameters must be populated in order to send to Azure.

    :param recipient_name: Required. The name of the recipient who will receive the hard drives
     when they are returned.
    :type recipient_name: str
    :param street_address1: Required. The first line of the street address to use when returning
     the drives.
    :type street_address1: str
    :param street_address2: The second line of the street address to use when returning the drives.
    :type street_address2: str
    :param city: Required. The city name to use when returning the drives.
    :type city: str
    :param state_or_province: Required. The state or province to use when returning the drives.
    :type state_or_province: str
    :param postal_code: Required. The postal code to use when returning the drives.
    :type postal_code: str
    :param country_or_region: Required. The country or region to use when returning the drives.
    :type country_or_region: str
    :param phone: Phone number of the recipient of the returned drives.
    :type phone: str
    """

    _validation = {
        'recipient_name': {'required': True},
        'street_address1': {'required': True},
        'city': {'required': True},
        'state_or_province': {'required': True},
        'postal_code': {'required': True},
        'country_or_region': {'required': True},
    }

    _attribute_map = {
        'recipient_name': {'key': 'recipientName', 'type': 'str'},
        'street_address1': {'key': 'streetAddress1', 'type': 'str'},
        'street_address2': {'key': 'streetAddress2', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state_or_province': {'key': 'stateOrProvince', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
        'country_or_region': {'key': 'countryOrRegion', 'type': 'str'},
        'phone': {'key': 'phone', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ShippingInformation, self).__init__(**kwargs)
        self.recipient_name = kwargs['recipient_name']
        self.street_address1 = kwargs['street_address1']
        self.street_address2 = kwargs.get('street_address2', None)
        self.city = kwargs['city']
        self.state_or_province = kwargs['state_or_province']
        self.postal_code = kwargs['postal_code']
        self.country_or_region = kwargs['country_or_region']
        self.phone = kwargs.get('phone', None)


class UpdateJobParameters(msrest.serialization.Model):
    """Update Job parameters.

    :param tags: A set of tags. Specifies the tags that will be assigned to the job.
    :type tags: object
    :param cancel_requested: If specified, the value must be true. The service will attempt to
     cancel the job.
    :type cancel_requested: bool
    :param state: If specified, the value must be Shipping, which tells the Import/Export service
     that the package for the job has been shipped. The ReturnAddress and DeliveryPackage properties
     must have been set either in this request or in a previous request, otherwise the request will
     fail.
    :type state: str
    :param return_address: Specifies the return address information for the job.
    :type return_address: ~storage_import_export.models.ReturnAddress
    :param return_shipping: Specifies the return carrier and customer's account with the carrier.
    :type return_shipping: ~storage_import_export.models.ReturnShipping
    :param delivery_package: Contains information about the package being shipped by the customer
     to the Microsoft data center.
    :type delivery_package: ~storage_import_export.models.PackageInfomation
    :param log_level: Indicates whether error logging or verbose logging is enabled.
    :type log_level: str
    :param backup_drive_manifest: Indicates whether the manifest files on the drives should be
     copied to block blobs.
    :type backup_drive_manifest: bool
    :param drive_list: List of drives that comprise the job.
    :type drive_list: list[~storage_import_export.models.DriveStatus]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': 'object'},
        'cancel_requested': {'key': 'properties.cancelRequested', 'type': 'bool'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'return_address': {'key': 'properties.returnAddress', 'type': 'ReturnAddress'},
        'return_shipping': {'key': 'properties.returnShipping', 'type': 'ReturnShipping'},
        'delivery_package': {'key': 'properties.deliveryPackage', 'type': 'PackageInfomation'},
        'log_level': {'key': 'properties.logLevel', 'type': 'str'},
        'backup_drive_manifest': {'key': 'properties.backupDriveManifest', 'type': 'bool'},
        'drive_list': {'key': 'properties.driveList', 'type': '[DriveStatus]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UpdateJobParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.cancel_requested = kwargs.get('cancel_requested', None)
        self.state = kwargs.get('state', None)
        self.return_address = kwargs.get('return_address', None)
        self.return_shipping = kwargs.get('return_shipping', None)
        self.delivery_package = kwargs.get('delivery_package', None)
        self.log_level = kwargs.get('log_level', None)
        self.backup_drive_manifest = kwargs.get('backup_drive_manifest', None)
        self.drive_list = kwargs.get('drive_list', None)
