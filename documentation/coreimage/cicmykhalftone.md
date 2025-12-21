# CICMYKHalftone

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a CMYK halftone filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CICMYKHalftone : CIFilterProtocol
```

## Topics

### Instance Properties
- [var angle: Float](cicmykhalftone/angle.md)
  The angle of the pattern.
- [var center: CGPoint](cicmykhalftone/center.md)
  The x and y position to use as the center of the halftone pattern.
- [var grayComponentReplacement: Float](cicmykhalftone/graycomponentreplacement.md)
  The gray component replacement value.
- [var inputImage: CIImage?](cicmykhalftone/inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cicmykhalftone/sharpness.md)
  The sharpness of the pattern.
- [var underColorRemoval: Float](cicmykhalftone/undercolorremoval.md)
  The under color removal value.
- [var width: Float](cicmykhalftone/width.md)
  The distance between dots in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func cmykHalftone() -> any CIFilter & CICMYKHalftone](cifilter-swift.class/cmykhalftone.md)
  Adds a series of colorful dots to an image.
- [protocol CICircularScreen](cicircularscreen.md)
  The properties you use to configure a circular screen filter.
- [protocol CIDotScreen](cidotscreen.md)
  The properties you use to configure a dot screen filter.
- [protocol CIHatchedScreen](cihatchedscreen.md)
  The properties you use to configure a hatched screen filter.
- [protocol CILineScreen](cilinescreen.md)
  The properties you use to configure a line screen filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicmykhalftone)*