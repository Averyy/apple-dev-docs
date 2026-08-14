# VZEFISignatureDatabaseConfiguration

**Framework**: Virtualization  
**Kind**: class

A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZEFISignatureDatabaseConfiguration
```

#### Overview

This class represents the signature lists used in UEFI Secure Boot configuration. It contains three separate arrays, one for each UEFI signature database, which are:

- **Key Exchange Key (KEK)**: This list contains keys authorized to update the db and dbx databases. The array acts as a bridge between the platform owner (who controls the Platform Key) and operating system vendors.
- **Allowed Signature Database (db)**: An “allow list” of trusted UEFI applications, bootloaders, and drivers. The EFI boot loader allows code signed by these signatures to execute during boot.
- **Forbidden Signature Database (dbx)**: A “deny list” of revoked or malicious signatures. The EFI boot loader blocks code matching these signatures from running, even if it matches a signature in the db database.

## Topics

### Initializers
- [init(keyExchangeKeys: [VZEFISignatureList], dbSignatures: [VZEFISignatureList], dbxSignatures: [VZEFISignatureList])](vzefisignaturedatabaseconfiguration/init(keyexchangekeys:dbsignatures:dbxsignatures:).md)
  Creates a signature lists container from signature list objects.
### Instance Properties
- [var dbSignatures: [VZEFISignatureList]](vzefisignaturedatabaseconfiguration/dbsignatures.md)
  Allowed signature database (db) entries.
- [var dbxSignatures: [VZEFISignatureList]](vzefisignaturedatabaseconfiguration/dbxsignatures.md)
  Forbidden signature database (dbx) entries.
- [var keyExchangeKeys: [VZEFISignatureList]](vzefisignaturedatabaseconfiguration/keyexchangekeys.md)
  Key Exchange Key (KEK) database entries.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class VZEFISignatureList](vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
- [class VZEFIVariableStore](vzefivariablestore.md)
  An object that represents the Extensible Firmware Interface (EFI) variable store that contains NVRAM variables the EFI exposes.
- [class VZEFISignatureList](vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
- [enum VZEFISignature](vzefisignature-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturedatabaseconfiguration)*