# uuid

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The device’s unique identifier.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (copy, readonly) NSUUID * uuid;
```

#### Discussion

This is the identifier the system creates from device configuration objects that conform to [`VZUSBDeviceConfiguration`](../vzusbdeviceconfiguration.md).

## See Also

### Properties
- [var usbController: VZUSBController?](./usbcontroller.md)
  The USB controller that has an attachment to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbdevice/uuid)*