# VZEFISignatureList

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class VZEFISignatureList
```

```objc
@interface VZEFISignatureList : NSObject
```

#### Overview

This class represents a UEFI signature list that can contain X.509 certificates or SHA-256 hashes.

UEFI firmware stores the contents of signature lists in the Key Exchange Key (KEK) signature database, allowed signature database (db), and the forbidden signature database (dbx).

## Topics

### Initializers
- [init(contentsOf: URL) throws](./vzefisignaturelist/init%28contentsof%29.md)
  Creates a signature list from a file.
- [init(contentsOfURL: URL) throws](./vzefisignaturelist/init%28contentsofurl%29.md)
- [convenience init(signatures: [VZEFISignature])](./vzefisignaturelist/init%28signatures%29.md)
### Instance Properties
- [var signatures: [VZEFISignature]](./vzefisignaturelist/signatures-3cz50.md)
- [signatures](./vzefisignaturelist/signatures-78pcm.md)
  An array of EFI signatures this signature list contains.
### Instance Methods
- [- initWithSignatures:](./vzefisignaturelist/initwithsignatures_.md)
  Creates a signature list from the provided signatures.

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
- [class VZEFISignatureDatabaseConfiguration](./vzefisignaturedatabaseconfiguration.md)
  A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.
### Working with secure boot configurations
- [class VZEFISignatureDatabaseConfiguration](./vzefisignaturedatabaseconfiguration.md)
  A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.
- [enum VZEFISignature](./vzefisignature-swift.enum.md)
- [VZEFISignature](./vzefisignature-c.class.md)
  A base class that represents a Unified Extensible Firmware Interface (UEFI) signature.
- [VZEFISignatureX509Certificate](./vzefisignaturex509certificate.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on an X.509 certificate.
- [VZEFISignatureSHA256Hash](./vzefisignaturesha256hash.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on a SHA-256 cryptographic hash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturelist)*