# init(payload:symbolVersion:maskPattern:errorCorrectionLevel:)

**Framework**: Core Image  
**Kind**: init

Initializes a QR code descriptor for the given payload and parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(payload errorCorrectedPayload: Data, symbolVersion: Int, maskPattern: UInt8, errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel)
```

#### Return Value

 An initialized [`CIAztecCodeDescriptor`](ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

## Parameters

- `errorCorrectedPayload`: The data to encode in the QR code symbol.
- `symbolVersion`: The symbol version, from 1 through 40.
- `maskPattern`: The mask pattern to use in the QR code, from 0 to 7.
- `errorCorrectionLevel`: The QR code’s error correction level: L, M, Q, or H.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/init(payload:symbolversion:maskpattern:errorcorrectionlevel:))*