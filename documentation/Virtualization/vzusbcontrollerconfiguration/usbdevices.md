# usbDevices

**Framework**: Virtualization  
**Kind**: property

The list of USB devices.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var usbDevices: [any VZUSBDeviceConfiguration] { get set }
```

#### Discussion

This list represents a set of USB devices that a VM starts with. For each entry in the list, the system creates a corresponding runtime object in the [`usbDevices`](vzusbcontroller/usbdevices.md) property.

The list is empty by default.

## See Also

- [class VZUSBController](vzusbcontroller.md)
  A class that represents a USB controller in a VM.
- [protocol VZUSBDeviceConfiguration](vzusbdeviceconfiguration.md)
  The protocol for configuring USB devices.
- [class VZUSBMassStorageDeviceConfiguration](vzusbmassstoragedeviceconfiguration.md)
  The configuration object that represents a USB Mass storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontrollerconfiguration/usbdevices)*