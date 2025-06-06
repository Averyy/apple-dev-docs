# CIDepthOfField

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a depth-of-field filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIDepthOfField
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cidepthoffield/3228204-inputimage.md)
  The image to use as an input image.
- [var point0: CGPoint](cidepthoffield/3228205-point0.md)
  The first point in the focused region of the output image.
- [var point1: CGPoint](cidepthoffield/3228206-point1.md)
  The second point in the focused region of the output image.
- [var radius: Float](cidepthoffield/3228207-radius.md)
  The distance from the center of the effect.
- [var saturation: Float](cidepthoffield/3228208-saturation.md)
  The amount to adjust the saturation by.
- [var unsharpMaskIntensity: Float](cidepthoffield/3228209-unsharpmaskintensity.md)
  The intensity of the unsharp mask effect applied to the in-focus area.
- [var unsharpMaskRadius: Float](cidepthoffield/3228210-unsharpmaskradius.md)
  The radius of the unsharp mask effect applied to the in-focus area.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func depthOfField() -> any CIFilter & CIDepthOfField](cifilter/3228308-depthoffield.md)
  Simulates a depth of field effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidepthoffield)*