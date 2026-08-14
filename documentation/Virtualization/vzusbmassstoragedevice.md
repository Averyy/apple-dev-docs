# VZUSBMassStorageDevice

**Framework**: Virtualization  
**Kind**: class

A class that represents a hot-pluggable USB mass storage device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class VZUSBMassStorageDevice
```

#### Overview

Create this device either by instantiating it directly and passing [`VZUSBMassStorageDeviceConfiguration`](vzusbmassstoragedeviceconfiguration.md) to its initializer, or instantiating a `VZUSBMassStorageDeviceConfiguration` in a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md). Direct instantiation creates an object that you can pass to [`attach(device:completionHandler:)`](vzusbcontroller/attach(device:completionhandler:).md). Instantiation through `VZUSBMassStorageDeviceConfiguration` makes the device available in the [`usbDevices`](vzusbcontroller/usbdevices.md) property.

## Topics

### Creating a USB mass storage device
- [init(configuration: VZUSBMassStorageDeviceConfiguration)](vzusbmassstoragedevice/init(configuration:).md)
  Creates a USB mass storage device with the provided configuration.

## Relationships

### Inherits From
- [VZStorageDevice](vzstoragedevice.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [VZUSBDevice](vzusbdevice.md)

## See Also

- [class VZUSBController](vzusbcontroller.md)
  A class that represents a USB controller in a VM.
- [class VZUSBPassthroughDevice](vzusbpassthroughdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbmassstoragedevice)*