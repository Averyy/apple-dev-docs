# customVirtioDevice(_:didReceiveNotificationFor:)

**Framework**: Virtualization  
**Kind**: method

The method the framework calls when the device receives a virtqueue (Virtio queue) notification from the guest.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
optional func customVirtioDevice(_ device: VZCustomVirtioDevice, didReceiveNotificationFor queue: VZVirtioQueue)
```

## Parameters

- `device`: The device invoking the delegate method.
- `queue`: The queue that received the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate/customvirtiodevice(_:didreceivenotificationfor:))*