# CIVignetteEffect

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a vignette-effect filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIVignetteEffect
```

## Topics

### Instance Properties
- [var center: CGPoint](civignetteeffect/3228830-center.md)
  The center of the effect as x and y coordinates.
- [var falloff: Float](civignetteeffect/3228831-falloff.md)
  The falloff of the effect.
- [var inputImage: CIImage?](civignetteeffect/3228832-inputimage.md)
  The image to use as an input image.
- [var intensity: Float](civignetteeffect/3228833-intensity.md)
  The intensity of the effect.
- [var radius: Float](civignetteeffect/3228834-radius.md)
  The distance from the center of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func vignetteEffect() -> any CIFilter & CIVignetteEffect](cifilter/3228430-vignetteeffect.md)
  Gradually darkens a specified area of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civignetteeffect)*