# symbolVersion

**Framework**: Core Image  
**Kind**: property

The version of the QR code which corresponds to the size of the QR code symbol.

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

ISO/IEC 18004 defines versions from 1 to 40, where a higher symbol version indicates a larger data-carrying capacity. This field is required in order to properly interpret the error corrected payload.

## See Also

- [var errorCorrectedPayload: Data](ciqrcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected codeword payload that comprises the QR code symbol.
- [var maskPattern: UInt8](ciqrcodedescriptor/maskpattern-swift.property.md)
  The data mask pattern for the QR code symbol.
- [var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel](ciqrcodedescriptor/errorcorrectionlevel-swift.property.md)
  The error correction level of the QR code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/symbolversion-swift.property)*