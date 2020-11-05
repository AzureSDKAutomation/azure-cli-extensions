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


class ApplicationGroupType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Resource Type of ApplicationGroup.
    """

    REMOTE_APP = "RemoteApp"
    DESKTOP = "Desktop"

class ApplicationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Application type of application.
    """

    REMOTE_APP = "RemoteApp"
    DESKTOP = "Desktop"

class CommandLineSetting(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies whether this published application can be launched with command line arguments
    provided by the client, command line arguments specified at publish time, or no command line
    arguments at all.
    """

    DO_NOT_ALLOW = "DoNotAllow"
    ALLOW = "Allow"
    REQUIRE = "Require"

class HostPoolType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """HostPool type for desktop.
    """

    PERSONAL = "Personal"
    POOLED = "Pooled"

class LoadBalancerType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the load balancer.
    """

    BREADTH_FIRST = "BreadthFirst"
    DEPTH_FIRST = "DepthFirst"
    PERSISTENT = "Persistent"

class PersonalDesktopAssignmentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """PersonalDesktopAssignment type for HostPool.
    """

    AUTOMATIC = "Automatic"
    DIRECT = "Direct"

class PreferredAppGroupType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of preferred application group type, default to Desktop Application Group
    """

    NONE = "None"
    DESKTOP = "Desktop"
    RAIL_APPLICATIONS = "RailApplications"

class RegistrationTokenOperation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of resetting the token.
    """

    DELETE = "Delete"
    NONE = "None"
    UPDATE = "Update"

class RemoteApplicationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Resource Type of Application.
    """

    IN_BUILT = "InBuilt"
    MSIX_APPLICATION = "MsixApplication"

class SessionState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of user session.
    """

    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    DISCONNECTED = "Disconnected"
    PENDING = "Pending"
    LOG_OFF = "LogOff"
    USER_PROFILE_DISK_MOUNTED = "UserProfileDiskMounted"

class SsoSecretType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of single sign on Secret Type.
    """

    SHARED_KEY = "SharedKey"
    CERTIFICATE = "Certificate"
    SHARED_KEY_IN_KEY_VAULT = "SharedKeyInKeyVault"
    CERTIFICATE_IN_KEY_VAULT = "CertificateInKeyVault"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status for a SessionHost.
    """

    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"
    SHUTDOWN = "Shutdown"
    DISCONNECTED = "Disconnected"
    UPGRADING = "Upgrading"
    UPGRADE_FAILED = "UpgradeFailed"

class UpdateState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Update state of a SessionHost.
    """

    INITIAL = "Initial"
    PENDING = "Pending"
    STARTED = "Started"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
