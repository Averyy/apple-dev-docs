# MPSScaleTransform

**Framework**: Metal Performance Shaders  
**Kind**: struct

A transform matrix for explicit resampling control with a Lanczos kernel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MPSScaleTransform
```

## Topics

### Initializers
- [init()](mpsscaletransform/1618820-init.md)
- [init(scaleX: Double, scaleY: Double, translateX: Double, translateY: Double)](mpsscaletransform/1618862-init.md)
### Instance Properties
- [var scaleX: Double](mpsscaletransform/1618773-scalex.md)
  The horizontal scale factor.
- [var scaleY: Double](mpsscaletransform/1618785-scaley.md)
  The vertical scale factor.
- [var translateX: Double](mpsscaletransform/1618795-translatex.md)
  The horizontal translation factor.
- [var translateY: Double](mpsscaletransform/1618872-translatey.md)
  The vertical translation factor.

## See Also

- [class MPSImageLanczosScale](mpsimagelanczosscale.md)
  A filter that resizes and changes the aspect ratio of an image using Lanczos resampling. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsscaletransform)*