# VZPlatformConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for a platform configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZPlatformConfiguration
```

```objc
@interface VZPlatformConfiguration : NSObject
```

#### Overview

Don’t instantiate directly `VZPlatformConfiguration`, use one of its subclasses, such as [`VZGenericPlatformConfiguration`](./vzgenericplatformconfiguration.md) or [`VZMacPlatformConfiguration`](./vzmacplatformconfiguration.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZGenericPlatformConfiguration](./vzgenericplatformconfiguration.md)
- [VZMacPlatformConfiguration](./vzmacplatformconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZMacPlatformConfiguration](./vzmacplatformconfiguration.md)
  The platform configuration for booting macOS on Apple silicon.
### Configurations
- [class VZVirtualMachineConfiguration](./vzvirtualmachineconfiguration.md)
  The environment attributes and list of devices to use during the configuration of macOS or Linux VMs.
- [class VZVirtualMachineStartOptions](./vzvirtualmachinestartoptions.md)
  The abstract class for VM start options.
- [class VZGenericPlatformConfiguration](./vzgenericplatformconfiguration.md)
  The platform configuration for a generic Intel or ARM virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzplatformconfiguration)*