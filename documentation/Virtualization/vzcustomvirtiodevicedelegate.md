# VZCustomVirtioDeviceDelegate

**Framework**: Virtualization  
**Kind**: protocol  
**Role**: Protocol

A delegate protocol that defines the methods you implement to respond to the life cycle events of a custom Virtio device.

**Availability**:
- macOS 27.0+

## Declaration

```swift
protocol VZCustomVirtioDeviceDelegate : NSObjectProtocol
```

```objc
@protocol VZCustomVirtioDeviceDelegate <NSObject>
```

#### Overview

When you define these methods and set the delegate on your [`VZCustomVirtioDevice`](./vzcustomvirtiodevice.md) instance, the Virtualization framework notifies you when the Virtio device stops, pauses, resumes, or resets by the invocation of the respective methods defined here, and you can provide code to handle each of these situations.

The framework considers the device to be ready when the guest driver sets `DRIVER_OK`, indicated by the invocation of [`customVirtioDeviceDidAcceptDriverOk(_:)`](./vzcustomvirtiodevicedelegate/customvirtiodevicedidacceptdriverok%28_%29.md), this means that the guest driver is set up and ready to drive the device, and the device is ready to process any device operations.

Virtqueue (Virtio queue) notifications trigger device operations, then the framework invokes the [`customVirtioDevice(_:didReceiveNotificationFor:)`](./vzcustomvirtiodevicedelegate/customvirtiodevice%28_,didreceivenotificationfor%29.md) method when the guest driver sends the device a virtqueue notification, and you can provide code to handle the notification.

## Topics

### Instance Methods
- [func customVirtioDevice(VZCustomVirtioDevice, didReceiveNotificationFor: VZVirtioQueue)](./vzcustomvirtiodevicedelegate/customvirtiodevice%28_,didreceivenotificationfor%29.md)
  The method the framework calls when the device receives a virtqueue (Virtio queue) notification from the guest.
- [func customVirtioDeviceDidAcceptDriverOk(VZCustomVirtioDevice)](./vzcustomvirtiodevicedelegate/customvirtiodevicedidacceptdriverok%28_%29.md)
  The method the framework calls when the device and driver successfully complete Virtio negotiation.
- [func customVirtioDeviceSaveState(forRestore: VZCustomVirtioDevice) -> Data?](./vzcustomvirtiodevicedelegate/customvirtiodevicesavestate%28forrestore%29.md)
  The method the framework calls when a device needs to save its state.
- [func customVirtioDeviceShouldRestore(VZCustomVirtioDevice, saveState: Data) -> Bool](./vzcustomvirtiodevicedelegate/customvirtiodeviceshouldrestore%28_,savestate%29.md)
  The method the framework calls when a device restores its state.
- [func customVirtioDeviceWillPause(VZCustomVirtioDevice)](./vzcustomvirtiodevicedelegate/customvirtiodevicewillpause%28_%29.md)
  The method the framework calls when a device pauses.
- [func customVirtioDeviceWillReset(VZCustomVirtioDevice)](./vzcustomvirtiodevicedelegate/customvirtiodevicewillreset%28_%29.md)
  The method the framework calls when a device resets.
- [func customVirtioDeviceWillResume(VZCustomVirtioDevice)](./vzcustomvirtiodevicedelegate/customvirtiodevicewillresume%28_%29.md)
  The method the framework calls when a device resumes.
- [func customVirtioDeviceWillStop(VZCustomVirtioDevice)](./vzcustomvirtiodevicedelegate/customvirtiodevicewillstop%28_%29.md)
  The method the framework calls when a device will be stopped.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZCustomVirtioDevice](./vzcustomvirtiodevice.md)
  An interface that represents a custom Virtio device that you provide the implementation for.
### Responding to Virtio events
- [protocol VZCustomVirtioDeviceConfigurationDelegate](./vzcustomvirtiodeviceconfigurationdelegate.md)
  A class that conforms to the custom Virtio device configuration delegate protocol that can provide methods for tracking the state of a custom Virtio device configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegate)*