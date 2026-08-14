# VZEFIBootLoader

**Framework**: Virtualization  
**Kind**: class

The boot loader configuration the system uses to boot guest-operating systems that expect an Extensible Firmware Interface (EFI) ROM.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class VZEFIBootLoader
```

## Topics

### Creating an EFI boot loader
- [init()](vzefibootloader/init.md)
  Creates a new EFI boot loader.
### Working with secure boot configurations
- [class VZEFISignatureDatabaseConfiguration](vzefisignaturedatabaseconfiguration.md)
  A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.
- [class VZEFISignatureList](vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
- [enum VZEFISignature](vzefisignature-swift.enum.md)
### Accessing the boot loader’s EFI variables
- [var variableStore: VZEFIVariableStore?](vzefibootloader/variablestore.md)
  The boot loader’s EFI variable store.

## Relationships

### Inherits From
- [VZBootLoader](vzbootloader.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZMacOSBootLoader](vzmacosbootloader.md)
  An object that loads and configures a boot loader for running macOS on Apple silicon as a guest system of your VM.
- [class VZBootLoader](vzbootloader.md)
  The base class that defines the management of the initial process of the guest system.
- [class VZLinuxBootLoader](vzlinuxbootloader.md)
  An object that loads and configures a Linux kernel as the guest system of your VM.
- [class VZEFIVariableStore](vzefivariablestore.md)
  An object that represents the Extensible Firmware Interface (EFI) variable store that contains NVRAM variables the EFI exposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefibootloader)*