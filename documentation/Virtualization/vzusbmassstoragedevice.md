# VZUSBMassStorageDevice

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A class that represents a hot-pluggable USB mass storage device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class VZUSBMassStorageDevice
```

```objc
@interface VZUSBMassStorageDevice : VZStorageDevice
```

## Overview

Create this device either by instantiating it directly and passing [`VZUSBMassStorageDeviceConfiguration`](./vzusbmassstoragedeviceconfiguration.md) to its initializer, or instantiating a `VZUSBMassStorageDeviceConfiguration` in a [`VZVirtualMachineConfiguration`](./vzvirtualmachineconfiguration.md). Direct instantiation creates an object that you can pass to [`attach(device:completionHandler:)`](./vzusbcontroller/attach%28device,completionhandler%29.md). Instantiation through `VZUSBMassStorageDeviceConfiguration` makes the device available in the [`usbDevices`](./vzusbcontroller/usbdevices.md) property.

## Topics

### Creating a USB mass storage device
- [init(configuration: VZUSBMassStorageDeviceConfiguration)](./vzusbmassstoragedevice/init%28configuration%29.md)
  Creates a USB mass storage device with the provided configuration.

## Relationships

### Inherits From
- [VZStorageDevice](./vzstoragedevice.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [VZUSBDevice](./vzusbdevice.md)

## See Also

### Related Documentation
- [class VZUSBController](./vzusbcontroller.md)
  A class that represents a USB controller in a VM.
### Storage Devices
- [class VZUSBPassthroughDevice](./vzusbpassthroughdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbmassstoragedevice)*