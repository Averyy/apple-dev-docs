# CIMotionBlur

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a motion blur filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIMotionBlur
```

## Topics

### Instance Properties
- [var angle: Float](cimotionblur/3228591-angle.md)
  The angle of the motion, in radians, that determines which direction the blur smears.
- [var inputImage: CIImage?](cimotionblur/3228592-inputimage.md)
  The image to use as an input image.
- [var radius: Float](cimotionblur/3228593-radius.md)
  The radius of the blur, in pixels.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func motionBlur() -> any CIFilter & CIMotionBlur](cifilter/3228369-motionblur.md)
  Creates motion blur on an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimotionblur)*