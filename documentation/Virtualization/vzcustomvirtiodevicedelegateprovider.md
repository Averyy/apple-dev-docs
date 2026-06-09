# VZCustomVirtioDeviceDelegateProvider

**Framework**: Virtualization  
**Kind**: class

A custom Virtio Device provider for devices that implement a custom Virtio device configuration delegate.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZCustomVirtioDeviceDelegateProvider
```

#### Overview

The delegate runs in the same process as the guest’s `VZVirtualMachine` instance.

## Topics

### Initializers
- [init(deviceQueue: dispatch_queue_t, delegate: any VZCustomVirtioDeviceConfigurationDelegate)](vzcustomvirtiodevicedelegateprovider/init(devicequeue:delegate:).md)
  Creates a custom Virtio device delegate provider.
### Instance Properties
- [var delegate: (any VZCustomVirtioDeviceConfigurationDelegate)?](vzcustomvirtiodevicedelegateprovider/delegate.md)
  The delegate object that implements the device.
- [var deviceQueue: dispatch_queue_t](vzcustomvirtiodevicedelegateprovider/devicequeue.md)
  The queue the framework uses to synchronize operations for this device.

## Relationships

### Inherits From
- [VZCustomVirtioDeviceProvider](vzcustomvirtiodeviceprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZCustomVirtioDeviceProvider](vzcustomvirtiodeviceprovider.md)
  A base class that describes the provider of a custom Virtio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegateprovider)*