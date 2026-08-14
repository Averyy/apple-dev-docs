# VZPlatformConfiguration

**Framework**: Virtualization  
**Kind**: class

The base class for a platform configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZPlatformConfiguration
```

#### Overview

Don’t instantiate directly `VZPlatformConfiguration`, use one of its subclasses, such as [`VZGenericPlatformConfiguration`](vzgenericplatformconfiguration.md) or [`VZMacPlatformConfiguration`](vzmacplatformconfiguration.md) instead.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZGenericPlatformConfiguration](vzgenericplatformconfiguration.md)
- [VZMacPlatformConfiguration](vzmacplatformconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZMacPlatformConfiguration](vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
- [class VZVirtualMachineConfiguration](vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZVirtualMachineStartOptions](vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.
- [class VZGenericPlatformConfiguration](vzgenericplatformconfiguration.md)
  The platform configuration for a generic Intel or ARM virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzplatformconfiguration)*