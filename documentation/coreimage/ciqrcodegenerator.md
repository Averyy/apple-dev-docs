# CIQRCodeGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a QR code generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIQRCodeGenerator
```

## Topics

### Instance Properties
- [var correctionLevel: String](ciqrcodegenerator/3228682-correctionlevel.md)
  The QR code correction level: L, M, Q, or H.
- [var message: Data](ciqrcodegenerator/3228683-message.md)
  The message to encode in the QR code.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func qrCodeGenerator() -> any CIFilter & CIQRCodeGenerator](cifilter/3228262-qrcodegenerator.md)
  Generates a quick response (QR) code image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodegenerator)*