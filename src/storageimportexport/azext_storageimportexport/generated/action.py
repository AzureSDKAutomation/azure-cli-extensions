# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddReturnAddress(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.return_address = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'recipient-name':
                d['recipient_name'] = v[0]
            elif kl == 'street-address1':
                d['street_address1'] = v[0]
            elif kl == 'street-address2':
                d['street_address2'] = v[0]
            elif kl == 'city':
                d['city'] = v[0]
            elif kl == 'state-or-province':
                d['state_or_province'] = v[0]
            elif kl == 'postal-code':
                d['postal_code'] = v[0]
            elif kl == 'country-or-region':
                d['country_or_region'] = v[0]
            elif kl == 'phone':
                d['phone'] = v[0]
            elif kl == 'email':
                d['email'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter return_address. All possible keys are: '
                               'recipient-name, street-address1, street-address2, city, state-or-province, '
                               'postal-code, country-or-region, phone, email'.format(k))
        return d


class AddReturnShipping(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.return_shipping = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'carrier-name':
                d['carrier_name'] = v[0]
            elif kl == 'carrier-account-number':
                d['carrier_account_number'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter return_shipping. All possible keys are: '
                               'carrier-name, carrier-account-number'.format(k))
        return d


class AddShippingInformation(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.shipping_information = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'recipient-name':
                d['recipient_name'] = v[0]
            elif kl == 'street-address1':
                d['street_address1'] = v[0]
            elif kl == 'street-address2':
                d['street_address2'] = v[0]
            elif kl == 'city':
                d['city'] = v[0]
            elif kl == 'state-or-province':
                d['state_or_province'] = v[0]
            elif kl == 'postal-code':
                d['postal_code'] = v[0]
            elif kl == 'country-or-region':
                d['country_or_region'] = v[0]
            elif kl == 'phone':
                d['phone'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter shipping_information. All possible keys '
                               'are: recipient-name, street-address1, street-address2, city, state-or-province, '
                               'postal-code, country-or-region, phone'.format(k))
        return d


class AddDeliveryPackage(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.delivery_package = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'carrier-name':
                d['carrier_name'] = v[0]
            elif kl == 'tracking-number':
                d['tracking_number'] = v[0]
            elif kl == 'drive-count':
                d['drive_count'] = v[0]
            elif kl == 'ship-date':
                d['ship_date'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter delivery_package. All possible keys are: '
                               'carrier-name, tracking-number, drive-count, ship-date'.format(k))
        return d


class AddReturnPackage(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.return_package = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'carrier-name':
                d['carrier_name'] = v[0]
            elif kl == 'tracking-number':
                d['tracking_number'] = v[0]
            elif kl == 'drive-count':
                d['drive_count'] = v[0]
            elif kl == 'ship-date':
                d['ship_date'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter return_package. All possible keys are: '
                               'carrier-name, tracking-number, drive-count, ship-date'.format(k))
        return d


class AddStorageimportexportJobCreateDriveList(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddStorageimportexportJobCreateDriveList, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'drive-id':
                d['drive_id'] = v[0]
            elif kl == 'bit-locker-key':
                d['bit_locker_key'] = v[0]
            elif kl == 'manifest-file':
                d['manifest_file'] = v[0]
            elif kl == 'manifest-hash':
                d['manifest_hash'] = v[0]
            elif kl == 'drive-header-hash':
                d['drive_header_hash'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'copy-status':
                d['copy_status'] = v[0]
            elif kl == 'percent-complete':
                d['percent_complete'] = v[0]
            elif kl == 'verbose-log-uri':
                d['verbose_log_uri'] = v[0]
            elif kl == 'error-log-uri':
                d['error_log_uri'] = v[0]
            elif kl == 'manifest-uri':
                d['manifest_uri'] = v[0]
            elif kl == 'bytes-succeeded':
                d['bytes_succeeded'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter drive_list. All possible keys are: '
                               'drive-id, bit-locker-key, manifest-file, manifest-hash, drive-header-hash, state, '
                               'copy-status, percent-complete, verbose-log-uri, error-log-uri, manifest-uri, '
                               'bytes-succeeded'.format(k))
        return d


class AddExport(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.export = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'blob-list-blob-path':
                d['blob_list_blob_path'] = v[0]
            elif kl == 'blob-path':
                d['blob_path'] = v
            elif kl == 'blob-path-prefix':
                d['blob_path_prefix'] = v
            else:
                raise CLIError('Unsupported Key {} is provided for parameter export. All possible keys are: '
                               'blob-list-blob-path, blob-path, blob-path-prefix'.format(k))
        return d


class AddEncryptionKey(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.encryption_key = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        d['kek_type'] = "MicrosoftManaged"
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'kek-type':
                d['kek_type'] = v[0]
            elif kl == 'kek-url':
                d['kek_url'] = v[0]
            elif kl == 'kek-vault-resource-id':
                d['kek_vault_resource_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter encryption_key. All possible keys are: '
                               'kek-type, kek-url, kek-vault-resource-id'.format(k))
        return d


class AddStorageimportexportJobUpdateDriveList(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddStorageimportexportJobUpdateDriveList, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'drive-id':
                d['drive_id'] = v[0]
            elif kl == 'bit-locker-key':
                d['bit_locker_key'] = v[0]
            elif kl == 'manifest-file':
                d['manifest_file'] = v[0]
            elif kl == 'manifest-hash':
                d['manifest_hash'] = v[0]
            elif kl == 'drive-header-hash':
                d['drive_header_hash'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'copy-status':
                d['copy_status'] = v[0]
            elif kl == 'percent-complete':
                d['percent_complete'] = v[0]
            elif kl == 'verbose-log-uri':
                d['verbose_log_uri'] = v[0]
            elif kl == 'error-log-uri':
                d['error_log_uri'] = v[0]
            elif kl == 'manifest-uri':
                d['manifest_uri'] = v[0]
            elif kl == 'bytes-succeeded':
                d['bytes_succeeded'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter drive_list. All possible keys are: '
                               'drive-id, bit-locker-key, manifest-file, manifest-hash, drive-header-hash, state, '
                               'copy-status, percent-complete, verbose-log-uri, error-log-uri, manifest-uri, '
                               'bytes-succeeded'.format(k))
        return d
