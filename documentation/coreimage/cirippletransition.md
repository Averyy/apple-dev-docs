# CIRippleTransition

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a ripple transition filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIRippleTransition
```

## Topics

### Instance Properties
- [var center: CGPoint](cirippletransition/3228692-center.md)
  The x and y position to use as the center of the effect.
- [var extent: CGRect](cirippletransition/3228693-extent.md)
  A rectangle that defines the extent of the effect.
- [var scale: Float](cirippletransition/3228694-scale.md)
  A value that determines whether the ripple starts as a bulge (a higher value) or a dimple (a lower value).
- [var shadingImage: CIImage?](cirippletransition/3228695-shadingimage.md)
  An image that looks like a shaded sphere enclosed in a square.
- [var width: Float](cirippletransition/3228696-width.md)
  The width of the ripple.

## Relationships

### Inherits From
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func rippleTransition() -> any CIFilter & CIRippleTransition](cifilter/3228397-rippletransition.md)
  Simulates a ripple in a pond to transiton from one image to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirippletransition)*