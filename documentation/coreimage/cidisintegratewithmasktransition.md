# CIDisintegrateWithMaskTransition

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a disintegrate-with-mask transition filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIDisintegrateWithMaskTransition
```

## Topics

### Instance Properties
- [var maskImage: CIImage?](cidisintegratewithmasktransition/3228217-maskimage.md)
  An image that defines the shape to use when disintegrating from the source to the target image.
- [var shadowDensity: Float](cidisintegratewithmasktransition/3228218-shadowdensity.md)
  The density of the shadow the mask creates.
- [var shadowOffset: CGPoint](cidisintegratewithmasktransition/3228219-shadowoffset.md)
  The offset of the shadow the mask creates.
- [var shadowRadius: Float](cidisintegratewithmasktransition/3228220-shadowradius.md)
  The radius of the shadow the mask creates.

## Relationships

### Inherits From
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func disintegrateWithMaskTransition() -> any CIFilter & CIDisintegrateWithMaskTransition](cifilter/3228312-disintegratewithmasktransition.md)
  Transitions between two images using a mask image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidisintegratewithmasktransition)*