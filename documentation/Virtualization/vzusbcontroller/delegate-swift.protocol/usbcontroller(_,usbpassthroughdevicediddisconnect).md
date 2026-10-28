# usbController(_:usbPassthroughDeviceDidDisconnect:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 27.0+

## Declaration

```swift
optional func usbController(_ usbController: VZUSBController, usbPassthroughDeviceDidDisconnect device: VZUSBPassthroughDevice)
```

```objc
- (void) usbController:(VZUSBController *) usbController usbPassthroughDeviceDidDisconnect:(VZUSBPassthroughDevice *) device;
```

## Discussion

Invoked when a USB device’s IOService is terminated.

When invoked, the framework has detached the corresponding VZUSBPassthroughDevice from its VZUSBController and removed the device from the VZUSBController.usbDevices array.

## Parameters

- `usbController`: The VZUSBController invoking the delegate method.
- `device`: The VZUSBPassthroughDevice that disconnected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzusbcontroller/delegate-swift.protocol/usbcontroller(_:usbpassthroughdevicediddisconnect:))*