# VZCustomVirtioDeviceProvider

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A base class that describes the provider of a custom Virtio device.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZCustomVirtioDeviceProvider
```

```objc
@interface VZCustomVirtioDeviceProvider : NSObject
```

## Overview

A Custom Virtio device provider describes how the custom Virtio device is implemented. Don’t instantiate `VZCustomVirtioDeviceProvider` directly. use one of its subclasses such as [`VZCustomVirtioDeviceDelegateProvider`](./vzcustomvirtiodevicedelegateprovider.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZCustomVirtioDeviceDelegateProvider](./vzcustomvirtiodevicedelegateprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZCustomVirtioDeviceDelegateProvider](./vzcustomvirtiodevicedelegateprovider.md)
  A custom Virtio Device provider for devices that implement a custom Virtio device configuration delegate.
### Responding to Virtio driver events
- [class VZCustomVirtioDeviceDelegateProvider](./vzcustomvirtiodevicedelegateprovider.md)
  A custom Virtio Device provider for devices that implement a custom Virtio device configuration delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceprovider)*