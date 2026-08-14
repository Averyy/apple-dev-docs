# VZCustomVirtioDeviceProvider

**Framework**: Virtualization  
**Kind**: class

A base class that describes the provider of a custom Virtio device.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZCustomVirtioDeviceProvider
```

#### Overview

A Custom Virtio device provider describes how the custom Virtio device is implemented. Don’t instantiate `VZCustomVirtioDeviceProvider` directly. use one of its subclasses such as [`VZCustomVirtioDeviceDelegateProvider`](vzcustomvirtiodevicedelegateprovider.md) instead.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZCustomVirtioDeviceDelegateProvider](vzcustomvirtiodevicedelegateprovider.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZCustomVirtioDeviceDelegateProvider](vzcustomvirtiodevicedelegateprovider.md)
  A custom Virtio Device provider for devices that implement a custom Virtio device configuration delegate.
- [class VZCustomVirtioDeviceDelegateProvider](vzcustomvirtiodevicedelegateprovider.md)
  A custom Virtio Device provider for devices that implement a custom Virtio device configuration delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceprovider)*