# usbDevices

**Framework**: Virtualization  
**Kind**: property

The list of attached USB devices for the controller.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var usbDevices: [any VZUSBDevice] { get }
```

#### Discussion

If a [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) contains a USB controller configuration that contains USB devices, those devices appear in the list when you start the virtual machine.

## See Also

- [protocol VZUSBDevice](vzusbdevice.md)
  A protocol that represents a USB device in a VM.
- [protocol VZUSBDeviceConfiguration](vzusbdeviceconfiguration.md)
  The protocol for configuring USB devices.
- [class VZUSBControllerConfiguration](vzusbcontrollerconfiguration.md)
  The base class for a USB controller configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontroller/usbdevices)*