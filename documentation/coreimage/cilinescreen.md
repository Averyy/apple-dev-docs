# CILineScreen

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a line screen filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CILineScreen
```

## Topics

### Instance Properties
- [var angle: Float](cilinescreen/3228536-angle.md)
  The angle of the pattern.
- [var center: CGPoint](cilinescreen/3228537-center.md)
  The x and y position to use as the center of the line screen pattern.
- [var inputImage: CIImage?](cilinescreen/3228538-inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cilinescreen/3228539-sharpness.md)
  The sharpness of the pattern.
- [var width: Float](cilinescreen/3228540-width.md)
  The distance between lines in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func lineScreen() -> any CIFilter & CILineScreen](cifilter/3228348-linescreen.md)
  Creates a monochrome image with a series of small lines to add detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilinescreen)*