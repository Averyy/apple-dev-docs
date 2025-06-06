# uuid

**Framework**: Virtualization  
**Kind**: property  
**Required**: Yes

The device’s unique identifier.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var uuid: UUID { get }
```

#### Discussion

This is the identifier the system creates from device configuration objects that conform to [`VZUSBDeviceConfiguration`](vzusbdeviceconfiguration.md).

## See Also

- [var usbController: VZUSBController?](vzusbdevice/usbcontroller.md)
  The USB controller that has an attachment to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbdevice/uuid)*