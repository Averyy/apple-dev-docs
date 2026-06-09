# VZUSBPassthroughDevice

**Framework**: Virtualization  
**Kind**: class

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZUSBPassthroughDevice
```

#### Overview

Class representing a USB passthrough device.

This device is created through either instantiating it directly and passing VZUSBPassthroughDeviceConfiguration to its initializer or instantiating a VZUSBPassthroughDeviceConfiguration in a VZVirtualMachineConfiguration. Direct instantiation will create an object that can be passed to -[VZUSBController attachDevice:completionHandler:] method. Instantiation via VZUSBPassthroughDeviceConfiguration will make the device available in the usbDevices property of VZUSBController.

## Topics

### Initializers
- [init(configuration: VZUSBPassthroughDeviceConfiguration) throws](vzusbpassthroughdevice/init(configuration:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [VZUSBDevice](vzusbdevice.md)

## See Also

- [class VZUSBMassStorageDevice](vzusbmassstoragedevice.md)
  A class that represents a hot-pluggable USB mass storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbpassthroughdevice)*