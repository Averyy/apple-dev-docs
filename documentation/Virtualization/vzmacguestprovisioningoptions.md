# VZMacGuestProvisioningOptions

**Framework**: Virtualization  
**Kind**: class

The configuration for guest setup during macOS virtual machine startup.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZMacGuestProvisioningOptions
```

#### Overview

> **Note**: This configuration requires guest macOS 27 or later to function properly. Earlier versions of macOS don’t support the automated guest configuration protocol and ignore these settings.

This configuration class provides automated setup capabilities for macOS virtual machines that allow hosts to configure a user account and initial setup workflows without manual intervention during the guest boot process.

The configuration enables automated macOS installation and setup workflows by providing user credentials and setup preferences to the guest system during startup.

macOS only evaluates these options on the first boot after restore. The Virtualization framework can’t use them to reconfigure macOS once the framework has already provisioned it.

Changes to the properties after starting the virtual machine have no effect.

## Topics

### Initializers
- [init()](vzmacguestprovisioningoptions/init.md)
### Instance Properties
- [var enablesRemoteLogin: Bool](vzmacguestprovisioningoptions/enablesremotelogin.md)
  A Boolean value that indicates whether to enable Remote Login (using SSH) for the macOS virtual machine.
- [var fullName: String](vzmacguestprovisioningoptions/fullname.md)
  A person’s full name to configure for the macOS virtual machine.
- [var logsInAutomatically: Bool](vzmacguestprovisioningoptions/logsinautomatically.md)
  A Boolean value that indicates whether to automatically log in the person at startup.
- [var password: String](vzmacguestprovisioningoptions/password.md)
  The password to configure for the macOS virtual machine.
- [var username: String](vzmacguestprovisioningoptions/username.md)
  The username for logging into the macOS virtual machine.

## Relationships

### Inherits From
- [VZGuestProvisioningOptions](vzguestprovisioningoptions.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class VZGuestProvisioningOptions](vzguestprovisioningoptions.md)
  The base class for guest provisioning options.
- [class VZMacOSVirtualMachineStartOptions](vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
- [class VZGuestProvisioningOptions](vzguestprovisioningoptions.md)
  The base class for guest provisioning options.
- [class VZGuestMemoryMapping](vzguestmemorymapping.md)
  An object that represents a chunk of the guest operating system’s dynamic random access memory (DRAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacguestprovisioningoptions)*