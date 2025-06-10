# errorCorrectionLevel

**Framework**: Core Image  
**Kind**: property

The QR code error correction level.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel { get }
```

#### Discussion

The possible error correction levels of [`CIQRCodeDescriptor.ErrorCorrectionLevel`](ciqrcodedescriptor/errorcorrectionlevel-swift.enum.md) are enumerated as follows:

- [`CIQRCodeDescriptor.ErrorCorrectionLevel.levelL`](ciqrcodedescriptor/errorcorrectionlevel-swift.enum/levell.md) = ‘L’
- [`CIQRCodeDescriptor.ErrorCorrectionLevel.levelM`](ciqrcodedescriptor/errorcorrectionlevel-swift.enum/levelm.md) = ‘M’
- [`CIQRCodeDescriptor.ErrorCorrectionLevel.levelQ`](ciqrcodedescriptor/errorcorrectionlevel-swift.enum/levelq.md) = ‘Q’
- [`CIQRCodeDescriptor.ErrorCorrectionLevel.levelH`](ciqrcodedescriptor/errorcorrectionlevel-swift.enum/levelh.md) = ‘H’

## See Also

- [var errorCorrectedPayload: Data](ciqrcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the QR code.
- [var symbolVersion: Int](ciqrcodedescriptor/symbolversion-swift.property.md)
  The version of the QR code.
- [var maskPattern: UInt8](ciqrcodedescriptor/maskpattern-swift.property.md)
  The QR code’s mask pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/errorcorrectionlevel-swift.property)*