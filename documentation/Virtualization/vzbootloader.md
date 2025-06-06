# VZBootLoader

**Framework**: Virtualization  
**Kind**: class

The base class that defines the management of the initial process of the guest system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZBootLoader
```

#### Overview

The [`VZBootLoader`](vzbootloader.md) abstract class defines the common behaviors for booting a guest operating system into a VM. Don’t create instances of this class directly. Instead, instantiate the subclass that corresponds to the type of operating system you plan to load. For example, to create a boot loader object for a Linux kernel, create a [`VZLinuxBootLoader`](vzlinuxbootloader.md) object; to create a boot loader object for installation using an ISO image create a [`VZEFIBootLoader`](vzefibootloader.md). For a macOS system create [`VZMacOSBootLoader`](vzmacosbootloader.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZEFIBootLoader](vzefibootloader.md)
- [VZLinuxBootLoader](vzlinuxbootloader.md)
- [VZMacOSBootLoader](vzmacosbootloader.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZEFIBootLoader](vzefibootloader.md)
  The boot loader configuration the system uses to boot guest-operating systems that expect an Extensible Firmware Interface (EFI) ROM.
- [class VZLinuxBootLoader](vzlinuxbootloader.md)
  An object that loads and configures a Linux kernel as the guest system of your VM.
- [class VZLinuxBootLoader](vzlinuxbootloader.md)
  An object that loads and configures a Linux kernel as the guest system of your VM.
- [class VZEFIBootLoader](vzefibootloader.md)
  The boot loader configuration the system uses to boot guest-operating systems that expect an Extensible Firmware Interface (EFI) ROM.
- [class VZEFIVariableStore](vzefivariablestore.md)
  An object that represents the Extensible Firmware Interface (EFI) variable store that contains NVRAM variables the EFI exposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzbootloader)*