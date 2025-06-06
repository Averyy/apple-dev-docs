# CIAztecCodeGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure an Aztec code generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIAztecCodeGenerator
```

## Topics

### Instance Properties
- [var compactStyle: Float](ciazteccodegenerator/3228063-compactstyle.md)
  A Boolean that specifies whether to force a compact style Aztec code.
- [var correctionLevel: Float](ciazteccodegenerator/3228064-correctionlevel.md)
  The Aztec error correction, a value from 5 to 95.
- [var layers: Float](ciazteccodegenerator/3228065-layers.md)
  The number of Aztec layers, a value from 1 to 32.
- [var message: Data](ciazteccodegenerator/3228066-message.md)
  The message to encode in the Aztec barcode.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](cifilter/3228268-azteccodegenerator.md)
  Generates a low-density barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodegenerator)*