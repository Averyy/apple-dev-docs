# VZDirectorySharingDevice

**Framework**: Virtualization  
**Kind**: class

The base class that represents a directory sharing device in a VM.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZDirectorySharingDevice
```

#### Overview

Don’t instantiate `VZDirectorySharingDevice` directly; configure a directory sharing device first by using [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) through a subclass of [`VZDirectorySharingDeviceConfiguration`](vzdirectorysharingdeviceconfiguration.md).

When you create a [`VZVirtualMachine`](vzvirtualmachine.md) from the configuration, the directory sharing devices are available through the `VZVirtualMachine.directorySharingDevices` property.

The real type of `VZDirectorySharingDevice` corresponds to the type used by the configuration. For example, a [`VZVirtioFileSystemDeviceConfiguration`](vzvirtiofilesystemdeviceconfiguration.md) leads to a device of type [`VZVirtioFileSystemDevice`](vzvirtiofilesystemdevice.md).

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZVirtioFileSystemDevice](vzvirtiofilesystemdevice.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZVirtioFileSystemDevice](vzvirtiofilesystemdevice.md)
  An object the defines a VIRTIO file system device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdirectorysharingdevice)*