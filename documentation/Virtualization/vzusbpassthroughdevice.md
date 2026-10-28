# VZUSBPassthroughDevice

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZUSBPassthroughDevice
```

```objc
@interface VZUSBPassthroughDevice : NSObject
```

## Overview

Class representing a USB passthrough device.

This device is created through either instantiating it directly and passing VZUSBPassthroughDeviceConfiguration to its initializer or instantiating a VZUSBPassthroughDeviceConfiguration in a VZVirtualMachineConfiguration. Direct instantiation will create an object that can be passed to -[VZUSBController attachDevice:completionHandler:] method. Instantiation via VZUSBPassthroughDeviceConfiguration will make the device available in the usbDevices property of VZUSBController.

## Topics

### Initializers
- [init(configuration: VZUSBPassthroughDeviceConfiguration) throws](./vzusbpassthroughdevice/init%28configuration%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [VZUSBDevice](./vzusbdevice.md)

## See Also

### Storage Devices
- [class VZUSBMassStorageDevice](./vzusbmassstoragedevice.md)
  A class that represents a hot-pluggable USB mass storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbpassthroughdevice)*