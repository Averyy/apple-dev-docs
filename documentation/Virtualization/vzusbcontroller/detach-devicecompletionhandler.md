# detach(device:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Detaches a USB device from the controller.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func detach(device: any VZUSBDevice) async throws
```

#### Discussion

If the device successfully detaches from the controller, it disappears from the [`usbDevices`](vzusbcontroller/usbdevices.md) property, the framework sets its [`usbController`](vzusbdevice/usbcontroller.md) property to `nil,` and the completion handler returns `nil`.

If the device doesn’t have an attachment to the controller at the time of calling the detach method, the process fails with [`VZError.Code.deviceNotFound`](vzerror/code/devicenotfound.md).

You need to call this method on the virtual machine’s queue.

## Parameters

- `device`: The USB device to detach.
- `completionHandler`: A block the framework calls after the device detaches, or on an error. The error parameter that passes to the block is   if detaching the device is successful. The framework calls the block on a VM’s queue.

## See Also

- [protocol VZUSBDevice](vzusbdevice.md)
  A protocol that represents a USB device in a VM.
- [func attach(device: any VZUSBDevice, completionHandler: ((any Error)?) -> Void)](vzusbcontroller/attach(device:completionhandler:).md)
  Attaches a USB device to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontroller/detach(device:completionhandler:))*