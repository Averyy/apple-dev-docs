# VZConsolePortConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for a console port configuration.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZConsolePortConfiguration
```

```objc
@interface VZConsolePortConfiguration : NSObject
```

## Overview

Don’t instantiate `VZConsolePortConfiguration` directly, instead use one of its subclasses like [`VZVirtioConsolePortConfiguration`](./vzvirtioconsoleportconfiguration.md).

## Topics

### Configuring the attachment
- [var attachment: VZSerialPortAttachment?](./vzconsoleportconfiguration/attachment.md)
  The serial port attachment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZVirtioConsolePortConfiguration](./vzvirtioconsoleportconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configurations
- [class VZConsoleDeviceConfiguration](./vzconsoledeviceconfiguration.md)
  The base class for a console device configuration.
- [class VZVirtioConsoleDeviceConfiguration](./vzvirtioconsoledeviceconfiguration.md)
  A console device that enables communication between the host and the guest using console ports through a Virtio interface.
- [class VZVirtioConsolePortConfiguration](./vzvirtioconsoleportconfiguration.md)
  A class that represents the configuration options you can set on a Virtio console port.
- [class VZVirtioConsolePortConfigurationArray](./vzvirtioconsoleportconfigurationarray.md)
  A class that represents a collection of Virtio console port configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzconsoleportconfiguration)*