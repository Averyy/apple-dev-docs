# VZMacGuestProvisioningOptions

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The configuration for guest setup during macOS virtual machine startup.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZMacGuestProvisioningOptions
```

```objc
@interface VZMacGuestProvisioningOptions : VZGuestProvisioningOptions
```

#### Overview

> **Note**: This configuration requires guest macOS 27 or later to function properly. Earlier versions of macOS don’t support the automated guest configuration protocol and ignore these settings.

This configuration class provides automated setup capabilities for macOS virtual machines that allow hosts to configure a user account and initial setup workflows without manual intervention during the guest boot process.

The configuration enables automated macOS installation and setup workflows by providing user credentials and setup preferences to the guest system during startup.

macOS only evaluates these options on the first boot after restore. The Virtualization framework can’t use them to reconfigure macOS once the framework has already provisioned it.

Changes to the properties after starting the virtual machine have no effect.

## Topics

### Initializers
- [init()](./vzmacguestprovisioningoptions/init%28%29.md)
### Instance Properties
- [var enablesRemoteLogin: Bool](./vzmacguestprovisioningoptions/enablesremotelogin.md)
  A Boolean value that indicates whether to enable Remote Login (using SSH) for the macOS virtual machine.
- [var fullName: String](./vzmacguestprovisioningoptions/fullname.md)
  A person’s full name to configure for the macOS virtual machine.
- [var logsInAutomatically: Bool](./vzmacguestprovisioningoptions/logsinautomatically.md)
  A Boolean value that indicates whether to automatically log in the person at startup.
- [var password: String](./vzmacguestprovisioningoptions/password.md)
  The password to configure for the macOS virtual machine.
- [var username: String](./vzmacguestprovisioningoptions/username.md)
  The username for logging into the macOS virtual machine.

## Relationships

### Inherits From
- [VZGuestProvisioningOptions](./vzguestprovisioningoptions.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [class VZGuestProvisioningOptions](./vzguestprovisioningoptions.md)
  The base class for guest provisioning options.
- [class VZMacOSVirtualMachineStartOptions](./vzmacosvirtualmachinestartoptions.md)
  A class that describes start options for macOS VMs.
### Provisioning options
- [class VZGuestProvisioningOptions](./vzguestprovisioningoptions.md)
  The base class for guest provisioning options.
- [class VZGuestMemoryMapping](./vzguestmemorymapping.md)
  An object that represents a chunk of the guest operating system’s dynamic random access memory (DRAM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacguestprovisioningoptions)*