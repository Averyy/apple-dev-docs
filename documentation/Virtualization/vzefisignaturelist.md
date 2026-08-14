# VZEFISignatureList

**Framework**: Virtualization  
**Kind**: class

A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class VZEFISignatureList
```

#### Overview

This class represents a UEFI signature list that can contain X.509 certificates or SHA-256 hashes.

UEFI firmware stores the contents of signature lists in the Key Exchange Key (KEK) signature database, allowed signature database (db), and the forbidden signature database (dbx).

## Topics

### Initializers
- [init(contentsOf: URL) throws](vzefisignaturelist/init(contentsof:).md)
  Creates a signature list from a file.
- [init(contentsOfURL: URL) throws](vzefisignaturelist/init(contentsofurl:).md)
- [convenience init(signatures: [VZEFISignature])](vzefisignaturelist/init(signatures:).md)
### Instance Properties
- [var signatures: [VZEFISignature]](vzefisignaturelist/signatures-3cz50.md)

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

- [class VZEFISignatureDatabaseConfiguration](vzefisignaturedatabaseconfiguration.md)
  A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.
- [class VZEFISignatureDatabaseConfiguration](vzefisignaturedatabaseconfiguration.md)
  A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.
- [enum VZEFISignature](vzefisignature-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturelist)*