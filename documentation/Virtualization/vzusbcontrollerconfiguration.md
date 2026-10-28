# VZUSBControllerConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for a USB controller configuration.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class VZUSBControllerConfiguration
```

```objc
@interface VZUSBControllerConfiguration : NSObject
```

## Overview

Don’t create `VZUSBControllerConfiguration` objects directly. Use one of its subclasses, such as [`VZXHCIControllerConfiguration`](./vzxhcicontrollerconfiguration.md), instead.

## Topics

### Instance properties
- [var usbDevices: [any VZUSBDeviceConfiguration]](./vzusbcontrollerconfiguration/usbdevices.md)
  The list of USB devices.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZXHCIControllerConfiguration](./vzxhcicontrollerconfiguration.md)
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
- [class VZXHCIControllerConfiguration](./vzxhcicontrollerconfiguration.md)
  The configuration object for the USB Extensible Host Controller Interface (XHCI) controller.
- [class VZUSBPassthroughDeviceConfiguration](./vzusbpassthroughdeviceconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontrollerconfiguration)*