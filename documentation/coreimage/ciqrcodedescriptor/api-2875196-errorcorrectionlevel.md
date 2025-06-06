# errorCorrectionLevel

**Framework**: Core Image  
**Kind**: instp

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

The possible error correction levels of [`CIQRCodeDescriptor.ErrorCorrectionLevel`](ciqrcodedescriptor/errorcorrectionlevel.md) are enumerated as follows:

- [`CIQRCodeDescriptor.ErrorCorrectionLevel.levelL`](ciqrcodedescriptor/errorcorrectionlevel/levell.md) = 'L'
- [`CIQRCodeDescriptor.ErrorCorrectionLevel.levelM`](ciqrcodedescriptor/errorcorrectionlevel/levelm.md) = 'M'
- [`CIQRCodeDescriptor.ErrorCorrectionLevel.levelQ`](ciqrcodedescriptor/errorcorrectionlevel/levelq.md) = 'Q'
- [`CIQRCodeDescriptor.ErrorCorrectionLevel.levelH`](ciqrcodedescriptor/errorcorrectionlevel/levelh.md) = 'H'

## See Also

- [var errorCorrectedPayload: Data](ciqrcodedescriptor/2875167-errorcorrectedpayload.md)
  The error-corrected payload containing the data encoded in the QR code.
- [var symbolVersion: Int](ciqrcodedescriptor/2875193-symbolversion.md)
  The version of the QR code.
- [var maskPattern: UInt8](ciqrcodedescriptor/2875191-maskpattern.md)
  The QR code's mask pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/2875196-errorcorrectionlevel)*