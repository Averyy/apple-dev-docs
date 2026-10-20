# VZVirtioEntropyDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A source of entropy for the guest’s random number generator.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZVirtioEntropyDeviceConfiguration
```

```objc
@interface VZVirtioEntropyDeviceConfiguration : VZEntropyDeviceConfiguration
```

## Mentions

- [Creating and Running a Linux Virtual Machine](./creating-and-running-a-linux-virtual-machine.md)

#### Overview

Use a [`VZVirtioEntropyDeviceConfiguration`](./vzvirtioentropydeviceconfiguration.md) object to expose a source of entropy for the guest operating system’s random-number generator. When you create this object and add it to your virtual machine’s configuration, the virtual machine configures a Virtio-compliant entropy device. The guest operating system uses this device as a seed to generate random numbers.

Create a [`VZVirtioEntropyDeviceConfiguration`](./vzvirtioentropydeviceconfiguration.md) object and add it to the [`entropyDevices`](./vzvirtualmachineconfiguration/entropydevices.md) property of your virtual machine’s configuration.

## Topics

### Creating the configuration object
- [init()](./vzvirtioentropydeviceconfiguration/init%28%29.md)
  Creates an entropy device configuration object.

## Relationships

### Inherits From
- [VZEntropyDeviceConfiguration](./vzentropydeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configurations
- [class VZEntropyDeviceConfiguration](./vzentropydeviceconfiguration.md)
  The common configuration traits for entropy devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioentropydeviceconfiguration)*