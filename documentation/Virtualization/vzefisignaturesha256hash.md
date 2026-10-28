# VZEFISignatureSHA256Hash

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on a SHA-256 cryptographic hash.

**Availability**:
- macOS 27.0+

## Declaration

```objc
@interface VZEFISignatureSHA256Hash : VZEFISignature
```

## Overview

This class represents a signature entry containing a SHA-256 hash value. The forbidden signature database (dbx) uses hash-based signatures to block specific UEFI binaries that OS vendors have revoked or found to be vulnerable.

## Topics

### Instance Properties
- [data](./vzefisignaturesha256hash/data.md)
  The SHA-256 hash data this signature contains.
### Instance Methods
- [- initWithData:](./vzefisignaturesha256hash/initwithdata_.md)
  Creates a signature from SHA-256 hash data.

## Relationships

### Inherits From
- [VZEFISignature](./vzefisignature-c.class.md)

## See Also

### Related Documentation
- [class VZEFISignatureList](./vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
### Working with secure boot configurations
- [class VZEFISignatureDatabaseConfiguration](./vzefisignaturedatabaseconfiguration.md)
  A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.
- [class VZEFISignatureList](./vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
- [VZEFISignature](./vzefisignature-c.class.md)
  A base class that represents a Unified Extensible Firmware Interface (UEFI) signature.
- [VZEFISignatureX509Certificate](./vzefisignaturex509certificate.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on an X.509 certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturesha256hash)*