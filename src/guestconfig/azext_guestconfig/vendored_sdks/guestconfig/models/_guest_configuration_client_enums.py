# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ActionAfterReboot(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies what happens after a reboot during the application of a configuration. The possible
    values are ContinueConfiguration and StopConfiguration
    """

    CONTINUE_CONFIGURATION = "ContinueConfiguration"
    STOP_CONFIGURATION = "StopConfiguration"

class AllowModuleOverwrite(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """If true - new configurations downloaded from the pull service are allowed to overwrite the old
    ones on the target node. Otherwise, false
    """

    TRUE = "True"
    FALSE = "False"

class ComplianceStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A value indicating compliance status of the machine for the assigned guest configuration.
    """

    COMPLIANT = "Compliant"
    NON_COMPLIANT = "NonCompliant"
    PENDING = "Pending"

class ConfigurationMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies how the LCM(Local Configuration Manager) actually applies the configuration to the
    target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
    """

    APPLY_ONLY = "ApplyOnly"
    APPLY_AND_MONITOR = "ApplyAndMonitor"
    APPLY_AND_AUTO_CORRECT = "ApplyAndAutoCorrect"

class Kind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Kind of the guest configuration. For example:DSC
    """

    DSC = "DSC"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioning state, which only appears in the response.
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    CREATED = "Created"

class RebootIfNeeded(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Set this to true to automatically reboot the node after a configuration that requires reboot is
    applied. Otherwise, you will have to manually reboot the node for any configuration that
    requires it. The default value is false. To use this setting when a reboot condition is enacted
    by something other than DSC (such as Windows Installer), combine this setting with the
    xPendingReboot module.
    """

    TRUE = "True"
    FALSE = "False"

class Type(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of report, Consistency or Initial
    """

    CONSISTENCY = "Consistency"
    INITIAL = "Initial"
