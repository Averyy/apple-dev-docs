# usbController

**Framework**: Virtualization  
**Kind**: property  
**Required**: Yes

The USB controller that has an attachment to the device.

**Availability**:
- macOS 15.0+

## Declaration

```swift
weak var usbController: VZUSBController? { get }
```

#### Discussion

If a USB device object that conforms to this protocol has a current attachment to a USB controller, this property includes a pointer to the device’s USB controller object. Otherwise, it’s `nil`.

## See Also

- [var uuid: UUID](vzusbdevice/uuid.md)
  The device’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbdevice/usbcontroller)*