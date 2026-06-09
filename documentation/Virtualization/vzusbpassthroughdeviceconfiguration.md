# VZUSBPassthroughDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZUSBPassthroughDeviceConfiguration
```

#### Overview

Configuration of a VZUSBPassthroughDevice.

This device configuration creates a VZUSBPassthroughDevice. A VZUSBPassthroughDeviceConfiguration is an abstraction of a USB device that is connected to the system and makes the USB device accessible to a VZVirtualMachine by capturing it.

The USB device is captured when the VZVirtualMachine is started with a VZUSBPassthroughDeviceConfiguration added to a VZUSBControllerConfiguration. The USB device is also captured by a running VZVirtualMachine when -[VZUSBController attachDevice:completionHandler:] is called.

## Topics

### Initializers
- [init(device: AAUSBAccessory)](vzusbpassthroughdeviceconfiguration/init(device:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [VZUSBDeviceConfiguration](vzusbdeviceconfiguration.md)

## See Also

- [class VZUSBControllerConfiguration](vzusbcontrollerconfiguration.md)
  The base class for a USB controller configuration.
- [class VZXHCIControllerConfiguration](vzxhcicontrollerconfiguration.md)
  The configuration object for the USB Extensible Host Controller Interface (XHCI) controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbpassthroughdeviceconfiguration)*