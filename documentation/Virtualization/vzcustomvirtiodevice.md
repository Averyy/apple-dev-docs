# VZCustomVirtioDevice

**Framework**: Virtualization  
**Kind**: class

An interface that represents a custom Virtio device that you provide the implementation for.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZCustomVirtioDevice
```

#### Overview

A Virtio device is a virtual emulated device the framework exposes to the guest OS following the Virtio standard. For more information about the Virtio standard, see the [`Virtio specification`](https://developer.apple.comhttps://docs.oasis-open.org/virtio/virtio/v1.3/csd01/virtio-v1.3-csd01.html).

A `VZCustomVirtioDevice` allows you to define, configure, and provide your own implementation for a device that uses the Virtio protocol.

To define a `VZCustomVirtioDevice` create and configure a `VZCustomVirtioDeviceConfiguration` object.

Once configured, the framework creates a `VZCustomVirtioDevice` object and returns it through the invocation of the delegate’s [`customVirtioConfiguration(_:didCreateDevice:)`](vzcustomvirtiodeviceconfigurationdelegate/customvirtioconfiguration(_:didcreatedevice:).md) method. Implement a class that conforms to the [`VZCustomVirtioDeviceDelegate`](vzcustomvirtiodevicedelegate.md) protocol to provide an implementation for the device.

The Virtualization framework performs all operations on the [`VZCustomVirtioDevice`](vzcustomvirtiodevice.md) and [`VZCustomVirtioDeviceDelegate`](vzcustomvirtiodevicedelegate.md) through a serial queue that you can configure through the [`deviceQueue`](vzcustomvirtiodevice/devicequeue.md) property. If the queue isn’t set, the framework performs all operations on the queue in the VM’s [`VZVirtualMachine`](vzvirtualmachine.md) [`queue`](vzvirtualmachine/queue.md) property by default.

## Topics

### Instance Properties
- [var delegate: (any VZCustomVirtioDeviceDelegate)?](vzcustomvirtiodevice/delegate.md)
  The device’s delegate.
- [var deviceQueue: dispatch_queue_t](vzcustomvirtiodevice/devicequeue.md)
  The dispatch queue this device uses.
- [var negotiatedFeatures: VZNegotiatedVirtioFeatureSet?](vzcustomvirtiodevice/negotiatedfeatures.md)
  The set of features that the driver and the device have successfully negotiated, or `nil` if no feature negotiation has taken place.
- [var sharedMemoryRegions: [VZVirtioSharedMemoryRegion]](vzcustomvirtiodevice/sharedmemoryregions.md)
  An array of shared memory regions that this device exposes to the guest.
### Instance Methods
- [func guestMemoryMapping(atPhysicalAddress: UInt64, length: Int) -> VZGuestMemoryMapping?](vzcustomvirtiodevice/guestmemorymapping(atphysicaladdress:length:).md)
  Returns guest memory mapping referred to by physicalAddress and length.
- [func queue(at: UInt16) -> VZVirtioQueue?](vzcustomvirtiodevice/queue(at:).md)
  Returns Virtio queue at the specified index that belongs to this device.
- [func requestReset()](vzcustomvirtiodevice/requestreset.md)
  A request to reset the device.
- [func update(VZVirtioDeviceSpecificConfiguration, completionHandler: ((any Error)?) -> Void)](vzcustomvirtiodevice/update(_:completionhandler:).md)
  Updates the device’s device-specific configuration.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZCustomVirtioDeviceConfiguration](vzcustomvirtiodeviceconfiguration.md)
  An object that defines a custom Virtio Device configuration.
- [protocol VZCustomVirtioDeviceConfigurationDelegate](vzcustomvirtiodeviceconfigurationdelegate.md)
  A class that conforms to the custom Virtio device configuration delegate protocol that can provide methods for tracking the state of a custom Virtio device configuration object.
- [protocol VZCustomVirtioDeviceDelegate](vzcustomvirtiodevicedelegate.md)
  A delegate protocol that defines the methods you implement to respond to the life cycle events of a custom Virtio device.
- [class VZVirtioQueue](vzvirtioqueue.md)
  A Virtio queue.
- [class VZVirtioSharedMemoryRegion](vzvirtiosharedmemoryregion.md)
  A class that represents a Virtio shared memory region for a custom Virtio device in a virtual machine.
- [class VZCustomVirtioDeviceConfiguration](vzcustomvirtiodeviceconfiguration.md)
  An object that defines a custom Virtio Device configuration.
- [class VZVirtioDeviceSpecificConfiguration](vzvirtiodevicespecificconfiguration.md)
  The device-specific configuration for a Virtio device


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevice)*