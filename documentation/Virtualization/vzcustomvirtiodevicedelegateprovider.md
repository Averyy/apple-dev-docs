# VZCustomVirtioDeviceDelegateProvider

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A custom Virtio Device provider for devices that implement a custom Virtio device configuration delegate.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZCustomVirtioDeviceDelegateProvider
```

```objc
@interface VZCustomVirtioDeviceDelegateProvider : VZCustomVirtioDeviceProvider
```

#### Overview

The delegate runs in the same process as the guest’s `VZVirtualMachine` instance.

## Topics

### Initializers
- [init(deviceQueue: dispatch_queue_t, delegate: any VZCustomVirtioDeviceConfigurationDelegate)](./vzcustomvirtiodevicedelegateprovider/init%28devicequeue,delegate%29.md)
  Creates a custom Virtio device delegate provider.
### Instance Properties
- [var delegate: (any VZCustomVirtioDeviceConfigurationDelegate)?](./vzcustomvirtiodevicedelegateprovider/delegate.md)
  The delegate object that implements the device.
- [var deviceQueue: dispatch_queue_t](./vzcustomvirtiodevicedelegateprovider/devicequeue.md)
  The queue the framework uses to synchronize operations for this device.

## Relationships

### Inherits From
- [VZCustomVirtioDeviceProvider](./vzcustomvirtiodeviceprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to Virtio driver events
- [class VZCustomVirtioDeviceProvider](./vzcustomvirtiodeviceprovider.md)
  A base class that describes the provider of a custom Virtio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodevicedelegateprovider)*