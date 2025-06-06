# CIQRCodeDescriptor.ErrorCorrectionLevel

**Framework**: Core Image  
**Kind**: enum

Constants that indicate the percentage of the symbol dedicated to error correction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum ErrorCorrectionLevel : Int, @unchecked Sendable
```

## Topics

### Enumeration Cases
- [CIQRCodeDescriptor.ErrorCorrectionLevel.levelL](ciqrcodedescriptor/errorcorrectionlevel/levell.md)
  Low-percentage error correction: 20% of the symbol data is dedicated to error correction.
- [CIQRCodeDescriptor.ErrorCorrectionLevel.levelM](ciqrcodedescriptor/errorcorrectionlevel/levelm.md)
  Medium-percentage error correction: 37% of the symbol data is dedicated to error correction.
- [CIQRCodeDescriptor.ErrorCorrectionLevel.levelQ](ciqrcodedescriptor/errorcorrectionlevel/levelq.md)
  High-percentage error correction: 55% of the symbol data is dedicated to error correction.
- [CIQRCodeDescriptor.ErrorCorrectionLevel.levelH](ciqrcodedescriptor/errorcorrectionlevel/levelh.md)
  Very-high-percentage error correction: 65% of the symbol data is dedicated to error correction.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/errorcorrectionlevel)*