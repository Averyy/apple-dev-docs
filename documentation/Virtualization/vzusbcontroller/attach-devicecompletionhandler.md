# attach(device:completionHandler:)

**Framework**: Virtualization  
**Kind**: method

Attaches a USB device to the controller.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func attach(device: any VZUSBDevice) async throws
```

#### Discussion

If the device successfully attaches to the controller, it appears in the [`usbDevices`](vzusbcontroller/usbdevices.md) property, the framework sets its [`usbController`](vzusbdevice/usbcontroller.md) property to point to the attached USB controller, and the completion handler returns `nil`.

If the device has a previous attachment to the current USB controller, or to another USB controller, the attach function fails with [`VZError.Code.deviceAlreadyAttached`](vzerror/code/devicealreadyattached.md). If the controller can’t initialize the device correctly, the attach function fails with [`VZError.Code.deviceInitializationFailure`](vzerror/code/deviceinitializationfailure.md).

You need to call this method on the virtual machine’s queue.

## Parameters

- `device`: The USB device to attach.
- `completionHandler`: A block the framework calls after the device attaches, or on an error. The error parameter that passes to the block is   if attaching is successful. The framework calls the block on a VM’s queue.

## See Also

- [protocol VZUSBDevice](vzusbdevice.md)
  A protocol that represents a USB device in a VM.
- [func detach(device: any VZUSBDevice, completionHandler: ((any Error)?) -> Void)](vzusbcontroller/detach(device:completionhandler:).md)
  Detaches a USB device from the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontroller/attach(device:completionhandler:))*