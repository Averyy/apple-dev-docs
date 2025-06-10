# symbolVersion

**Framework**: Core Image  
**Kind**: property

The version of the QR code.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var symbolVersion: Int { get }
```

#### Discussion

ISO/IEC 18004 defines versions from 1 to 40, where a higher symbol version indicates a larger data-carrying capacity

## See Also

- [var errorCorrectedPayload: Data](ciqrcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the QR code.
- [var maskPattern: UInt8](ciqrcodedescriptor/maskpattern-swift.property.md)
  The QR code’s mask pattern.
- [var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel](ciqrcodedescriptor/errorcorrectionlevel-swift.property.md)
  The QR code error correction level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/symbolversion-swift.property)*