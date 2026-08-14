# VZVirtioDeviceSpecificConfiguration

**Framework**: Virtualization  
**Kind**: class

The device-specific configuration for a Virtio device

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZVirtioDeviceSpecificConfiguration
```

#### Overview

This class represents a Virtio device’s device-specific configuration.

For more details about device-specific configuration for different Virtio devices, see the [`Virtio specification`](https://developer.apple.comhttps://docs.oasis-open.org/virtio/virtio/v1.3/csd01/virtio-v1.3-csd01.html).

Serialize any device-specific configuration structure into an [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) object, and instantiate a [`VZVirtioDeviceSpecificConfiguration`](vzvirtiodevicespecificconfiguration.md) object with it, and set this object on the [`deviceSpecificConfiguration`](vzcustomvirtiodeviceconfiguration/devicespecificconfiguration.md) property.

## Topics

### Initializers
- [init(configurationData: Data)](vzvirtiodevicespecificconfiguration/init(configurationdata:).md)
  Initializes a Virtio device specific configuration object with the configuration data you provide
### Instance Properties
- [var configurationData: Data](vzvirtiodevicespecificconfiguration/configurationdata.md)
  The serialized device-specific configuration.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZCustomVirtioDevice](vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
- [class VZCustomVirtioDeviceConfiguration](vzcustomvirtiodeviceconfiguration.md)
  An object that defines a custom Virtio Device configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiodevicespecificconfiguration)*