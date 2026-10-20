# VZUSBPassthroughDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZUSBPassthroughDeviceConfiguration
```

```objc
@interface VZUSBPassthroughDeviceConfiguration : NSObject
```

#### Overview

Configuration of a VZUSBPassthroughDevice.

This device configuration creates a VZUSBPassthroughDevice. A VZUSBPassthroughDeviceConfiguration is an abstraction of a USB device that is connected to the system and makes the USB device accessible to a VZVirtualMachine by capturing it.

The USB device is captured when the VZVirtualMachine is started with a VZUSBPassthroughDeviceConfiguration added to a VZUSBControllerConfiguration. The USB device is also captured by a running VZVirtualMachine when -[VZUSBController attachDevice:completionHandler:] is called.

## Topics

### Initializers
- [init(device: AAUSBAccessory)](./vzusbpassthroughdeviceconfiguration/init%28device%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [VZUSBDeviceConfiguration](./vzusbdeviceconfiguration.md)

## See Also

### Configurations
- [class VZUSBControllerConfiguration](./vzusbcontrollerconfiguration.md)
  The base class for a USB controller configuration.
- [class VZXHCIControllerConfiguration](./vzxhcicontrollerconfiguration.md)
  The configuration object for the USB Extensible Host Controller Interface (XHCI) controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbpassthroughdeviceconfiguration)*