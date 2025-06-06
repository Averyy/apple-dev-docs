# CICode128BarcodeGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a Code 128 barcode generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CICode128BarcodeGenerator
```

## Topics

### Instance Properties
- [var barcodeHeight: Float](cicode128barcodegenerator/3228116-barcodeheight.md)
  The height, in pixels, of the generated barcode.
- [var message: Data](cicode128barcodegenerator/3228117-message.md)
  The message to encode in the Code 128 barcode.
- [var quietSpace: Float](cicode128barcodegenerator/3228118-quietspace.md)
  The number of empty white pixels that should surround the barcode.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func code128BarcodeGenerator() -> any CIFilter & CICode128BarcodeGenerator](cifilter/3228281-code128barcodegenerator.md)
  Generates a high-density, linear barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicode128barcodegenerator)*