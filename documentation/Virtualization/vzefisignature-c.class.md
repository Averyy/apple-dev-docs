# VZEFISignature

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

A base class that represents a Unified Extensible Firmware Interface (UEFI) signature.

**Availability**:
- macOS 27.0+

## Declaration

```objc
@interface VZEFISignature : NSObject
```

## Overview

Don’t instantiate `VZEFISignature` objects directly; instead, create an instance of one of its subclasses, such as [`VZEFISignatureX509Certificate`](./vzefisignaturex509certificate.md) or [`VZEFISignatureSHA256Hash`](./vzefisignaturesha256hash.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZEFISignatureSHA256Hash](./vzefisignaturesha256hash.md)
- [VZEFISignatureX509Certificate](./vzefisignaturex509certificate.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Related Documentation
- [VZEFISignatureX509Certificate](./vzefisignaturex509certificate.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on an X.509 certificate.
- [VZEFISignatureSHA256Hash](./vzefisignaturesha256hash.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on a SHA-256 cryptographic hash.
- [class VZEFISignatureList](./vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
### Working with secure boot configurations
- [class VZEFISignatureDatabaseConfiguration](./vzefisignaturedatabaseconfiguration.md)
  A container for Unified Extensible Firmware Interface (UEFI) Secure Boot signature lists.
- [class VZEFISignatureList](./vzefisignaturelist.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature list.
- [VZEFISignatureX509Certificate](./vzefisignaturex509certificate.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on an X.509 certificate.
- [VZEFISignatureSHA256Hash](./vzefisignaturesha256hash.md)
  A class that represents a Unified Extensible Firmware Interface (UEFI) signature based on a SHA-256 cryptographic hash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignature-c.class)*