# CIHatchedScreen

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a hatched screen filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIHatchedScreen
```

## Topics

### Instance Properties
- [var angle: Float](cihatchedscreen/3228481-angle.md)
  The angle of the pattern.
- [var center: CGPoint](cihatchedscreen/3228482-center.md)
  The x and y position to use as the center of the hatched screen pattern.
- [var inputImage: CIImage?](cihatchedscreen/3228483-inputimage.md)
  The image to use as an input image.
- [var sharpness: Float](cihatchedscreen/3228484-sharpness.md)
  The amount of sharpening to apply.
- [var width: Float](cihatchedscreen/3228485-width.md)
  The distance between lines in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func hatchedScreen() -> any CIFilter & CIHatchedScreen](cifilter/3228336-hatchedscreen.md)
  Creates a monochrome image with a series of lines to add detail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cihatchedscreen)*