# VZUSBControllerConfiguration

**Framework**: Virtualization  
**Kind**: class

The base class for a USB controller configuration.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class VZUSBControllerConfiguration
```

#### Overview

Don’t create `VZUSBControllerConfiguration` objects directly. Use one of its subclasses, such as [`VZXHCIControllerConfiguration`](vzxhcicontrollerconfiguration.md), instead.

## Topics

### Instance properties
- [var usbDevices: [any VZUSBDeviceConfiguration]](vzusbcontrollerconfiguration/usbdevices.md)
  The list of USB devices.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZXHCIControllerConfiguration](vzxhcicontrollerconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZXHCIControllerConfiguration](vzxhcicontrollerconfiguration.md)
  The configuration object for the USB Extensible Host Controller Interface (XHCI) controller.
- [class VZUSBPassthroughDeviceConfiguration](vzusbpassthroughdeviceconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontrollerconfiguration)*