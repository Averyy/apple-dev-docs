# VZSocketDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The common configuration traits for socket device requests.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZSocketDeviceConfiguration
```

```objc
@interface VZSocketDeviceConfiguration : NSObject
```

## Overview

Don’t create a [`VZSocketDeviceConfiguration`](./vzsocketdeviceconfiguration.md) object directly. Instead, create a [`VZVirtioSocketDeviceConfiguration`](./vzvirtiosocketdeviceconfiguration.md) object and add it to your virtual machine’s configuration.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZVirtioSocketDeviceConfiguration](./vzvirtiosocketdeviceconfiguration.md)
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
- [class VZVirtioSocketDeviceConfiguration](./vzvirtiosocketdeviceconfiguration.md)
  A configuration object that requests the creation of a socket device to communicate with the guest system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzsocketdeviceconfiguration)*