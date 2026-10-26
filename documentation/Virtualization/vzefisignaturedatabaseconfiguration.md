# VZEFISignatureDatabaseConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZEFISignatureDatabaseConfiguration
```

```objc
@interface VZEFISignatureDatabaseConfiguration : NSObject
```

#### Overview

This class represents the signature lists used in UEFI Secure Boot configuration. It contains three separate arrays, one for each UEFI signature database, which are:

- **Key Exchange Key (KEK)**: This list contains keys authorized to update the db and dbx databases. The array acts as a bridge between the platform owner (who controls the Platform Key) and operating system vendors.
- **Allowed Signature Database (db)**: An “allow list” of trusted UEFI applications, bootloaders, and drivers. The EFI boot loader allows code signed by these signatures to execute during boot.
- **Forbidden Signature Database (dbx)**: A “deny list” of revoked or malicious signatures. The EFI boot loader blocks code matching these signatures from running, even if it matches a signature in the db database.

## Topics

### Initializers
- [init(keyExchangeKeys: [VZEFISignatureList], dbSignatures: [VZEFISignatureList], dbxSignatures: [VZEFISignatureList])](./vzefisignaturedatabaseconfiguration/init%28keyexchangekeys,dbsignatures,dbxsignatures%29.md)
  Creates a signature lists container from signature list objects.
### Instance Properties
- [var dbSignatures: [VZEFISignatureList]](./vzefisignaturedatabaseconfiguration/dbsignatures.md)
  Allowed signature database (db) entries.
- [var dbxSignatures: [VZEFISignatureList]](./vzefisignaturedatabaseconfiguration/dbxsignatures.md)
  Forbidden signature database (dbx) entries.
- [var keyExchangeKeys: [VZEFISignatureList]](./vzefisignaturedatabaseconfiguration/keyexchangekeys.md)
  Key Exchange Key (KEK) database entries.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [class VZEFISignatureList](./vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
- [class VZEFIVariableStore](./vzefivariablestore.md)
  An object that represents the Extensible Firmware Interface (EFI) variable store that contains NVRAM variables the EFI exposes.
### Working with secure boot configurations
- [class VZEFISignatureList](./vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
- [enum VZEFISignature](./vzefisignature-swift.enum.md)
- [VZEFISignature](./vzefisignature-c.class.md)
  A base class that represents a Unified Extensible Firmware Interface (UEFI) signature.
- [VZEFISignatureX509Certificate](./vzefisignaturex509certificate.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on an X.509 certificate.
- [VZEFISignatureSHA256Hash](./vzefisignaturesha256hash.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on a SHA-256 cryptographic hash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturedatabaseconfiguration)*