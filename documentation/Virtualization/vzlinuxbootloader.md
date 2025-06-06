# VZLinuxBootLoader

**Framework**: Virtualization  
**Kind**: class

An object that loads and configures a Linux kernel as the guest system of your VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class VZLinuxBootLoader
```

## Mentions

- [Creating and Running a Linux Virtual Machine](creating-and-running-a-linux-virtual-machine.md)

#### Overview

Create and configure a [`VZLinuxBootLoader`](vzlinuxbootloader.md) object during the initial configuration of your VM. Use this object to specify the location of the Linux kernel that serves as the guest operating system. You can also specify additional information to use during the boot process, such as command-line parameters to pass to the kernel. Assign the [`VZLinuxBootLoader`](vzlinuxbootloader.md) object to the [`bootLoader`](vzvirtualmachineconfiguration/bootloader.md) property of your [`VZVirtualMachineConfiguration`](vzvirtualmachineconfiguration.md) object.  A configuration with `VZLinuxBootLoader` is only valid if used with [`VZGenericPlatformConfiguration`](vzgenericplatformconfiguration.md).

## Topics

### Creating the Linux boot loader
- [init(kernelURL: URL)](vzlinuxbootloader/init(kernelurl:).md)
  Creates a boot loader that launches the Linux kernel at the specified URL.
### Configuring the boot parameters
- [var commandLine: String](vzlinuxbootloader/commandline.md)
  The command-line parameters to pass to the Linux kernel at boot time.
- [var initialRamdiskURL: URL?](vzlinuxbootloader/initialramdiskurl.md)
  The location of an optional RAM disk, which the boot loader maps into memory before it boots the Linux kernel.
### Getting the kernel file
- [var kernelURL: URL](vzlinuxbootloader/kernelurl.md)
  The URL of the Linux kernel file.

## Relationships

### Inherits From
- [VZBootLoader](vzbootloader.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZGenericPlatformConfiguration](vzgenericplatformconfiguration.md)
  The platform configuration for a generic Intel or ARM virtual machine.
- [class VZBootLoader](vzbootloader.md)
  The base class that defines the management of the initial process of the guest system.
- [class VZEFIBootLoader](vzefibootloader.md)
  The boot loader configuration the system uses to boot guest-operating systems that expect an Extensible Firmware Interface (EFI) ROM.
- [class VZEFIVariableStore](vzefivariablestore.md)
  An object that represents the Extensible Firmware Interface (EFI) variable store that contains NVRAM variables the EFI exposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxbootloader)*