# VZXHCIControllerConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The configuration object for the USB Extensible Host Controller Interface (XHCI) controller.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class VZXHCIControllerConfiguration
```

```objc
@interface VZXHCIControllerConfiguration : VZUSBControllerConfiguration
```

## Overview

Use this configuration to create a USB XHCI controller device for the guest.

## Topics

### Initializers
- [init()](./vzxhcicontrollerconfiguration/init%28%29.md)
  Creates a USB Extensible Host Controller Interface (XHCI) configuration.

## Relationships

### Inherits From
- [VZUSBControllerConfiguration](./vzusbcontrollerconfiguration.md)
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
- [class VZUSBControllerConfiguration](./vzusbcontrollerconfiguration.md)
  The base class for a USB controller configuration.
- [class VZUSBPassthroughDeviceConfiguration](./vzusbpassthroughdeviceconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzxhcicontrollerconfiguration)*