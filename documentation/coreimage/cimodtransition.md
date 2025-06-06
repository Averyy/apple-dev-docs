# CIModTransition

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a mod transition filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIModTransition
```

## Topics

### Instance Properties
- [var angle: Float](cimodtransition/3228569-angle.md)
  The angle of the mod hole pattern.
- [var center: CGPoint](cimodtransition/3228570-center.md)
  The x and y position to use as the center of the effect.
- [var compression: Float](cimodtransition/3228571-compression.md)
  The amount of stretching applied to the mod hole pattern.
- [var radius: Float](cimodtransition/3228572-radius.md)
  The radius of the undistorted mod holes in the pattern.

## Relationships

### Inherits From
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func modTransition() -> any CIFilter & CIModTransition](cifilter/3228363-modtransition.md)
  Transitions between two images by applying irregularly shaped holes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cimodtransition)*