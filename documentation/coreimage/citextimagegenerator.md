# CITextImageGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a text image generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CITextImageGenerator
```

## Topics

### Instance Properties
- [var fontName: String](citextimagegenerator/3228785-fontname.md)
  The name of the font to use for the generated text.
- [var fontSize: Float](citextimagegenerator/3228786-fontsize.md)
  The size of the font to use for the generated text.
- [var scaleFactor: Float](citextimagegenerator/3228787-scalefactor.md)
  The scale of the font to use for the generated text.
- [var text: String](citextimagegenerator/3228788-text.md)
  The text to render.
- [var padding: Float](citextimagegenerator/4401974-padding.md)

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func textImageGenerator() -> any CIFilter & CITextImageGenerator](cifilter/3228422-textimagegenerator.md)
  Generates a text image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citextimagegenerator)*