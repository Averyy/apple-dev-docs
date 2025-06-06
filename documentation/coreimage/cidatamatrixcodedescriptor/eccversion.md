# CIDataMatrixCodeDescriptor.ECCVersion

**Framework**: Core Image  
**Kind**: enum

Constants concerning Data Matrix code ECC version.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum ECCVersion : Int, @unchecked Sendable
```

#### Overview

ECC 000 - 140 symbols offer five levels of error correction using convolutional code error correction.  Each successive level or error correction offers more protection for the message data but increases the size of the symbol required to carry a given message. See the ISO/IEC 16022:2006 spec for other modes.

ECC 200 symbols utilize Reed-Solomon error correction, with error correction capacity determined by symbol size (in rows and columns).

## Topics

### Enumeration Cases
- [CIDataMatrixCodeDescriptor.ECCVersion.v000](cidatamatrixcodedescriptor/eccversion/v000.md)
  Indicates error correction using convolutional code error correction with zero data protection.
- [CIDataMatrixCodeDescriptor.ECCVersion.v050](cidatamatrixcodedescriptor/eccversion/v050.md)
  Indicates 1/4 (25%) of the symbol dedicated convolutional code error correction.
- [CIDataMatrixCodeDescriptor.ECCVersion.v080](cidatamatrixcodedescriptor/eccversion/v080.md)
  Indicates 1/3 (33%) of the symbol dedicated convolutional code error correction.
- [CIDataMatrixCodeDescriptor.ECCVersion.v100](cidatamatrixcodedescriptor/eccversion/v100.md)
  Indicates 1/2 (50%) of the symbol dedicated convolutional code error correction.
- [CIDataMatrixCodeDescriptor.ECCVersion.v140](cidatamatrixcodedescriptor/eccversion/v140.md)
  Indicates 3/4 (75%) of the symbol dedicated convolutional code error correction.
- [CIDataMatrixCodeDescriptor.ECCVersion.v200](cidatamatrixcodedescriptor/eccversion/v200.md)
  Indicates Reed-Solomon error correction.  Data protection overhead varies based on symbol size.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/eccversion)*