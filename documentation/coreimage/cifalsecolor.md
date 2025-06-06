# CIFalseColor

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a false color filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIFalseColor
```

## Topics

### Instance Properties
- [var color0: CIColor](cifalsecolor/3228256-color0.md)
  The first color to use for the color ramp.
- [var color1: CIColor](cifalsecolor/3228257-color1.md)
  The second color to use for the color ramp.
- [var inputImage: CIImage?](cifalsecolor/3228258-inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func falseColor() -> any CIFilter & CIFalseColor](cifilter/3228325-falsecolor.md)
  Replaces an image’s colors with specified colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifalsecolor)*