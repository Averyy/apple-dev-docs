# CICircularScreen

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a circular screen filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CICircularScreen : CIFilterProtocol
```

## Topics

### Instance Properties
- [var center: CGPoint](cicircularscreen/center.md)
  The x and y position to use as the center of the circular screen pattern.
- [var inputImage: CIImage?](cicircularscreen/inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cicircularscreen/sharpness.md)
  The sharpness of the circles.
- [var width: Float](cicircularscreen/width.md)
  The distance between each circle in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func circularScreen() -> any CIFilter & CICircularScreen](cifilter-swift.class/circularscreen.md)
  Adds a circular overlay to an image.
- [protocol CICMYKHalftone](cicmykhalftone.md)
  The properties you use to configure a CMYK halftone filter.
- [protocol CIDotScreen](cidotscreen.md)
  The properties you use to configure a dot screen filter.
- [protocol CIHatchedScreen](cihatchedscreen.md)
  The properties you use to configure a hatched screen filter.
- [protocol CILineScreen](cilinescreen.md)
  The properties you use to configure a line screen filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicircularscreen)*