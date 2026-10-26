# VZEFISignatureX509Certificate

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on an X.509 certificate.

**Availability**:
- macOS 27.0+

## Declaration

```objc
@interface VZEFISignatureX509Certificate : VZEFISignature
```

#### Overview

This class represents a signature entry containing a DER-encoded X.509 certificate. The Platform Key (PK), the Key Exchange Key (KEK) database, and the allowed signature database (db) commonly use X.509 certificates.

## Topics

### Instance Properties
- [certificate](./vzefisignaturex509certificate/certificate.md)
  The X.509 certificate contained in this signature.
### Instance Methods
- [- initWithCertificate:](./vzefisignaturex509certificate/initwithcertificate_.md)
  Creates a signature from an X.509 certificate.

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
- [VZEFISignatureSHA256Hash](./vzefisignaturesha256hash.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on a SHA-256 cryptographic hash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturex509certificate)*