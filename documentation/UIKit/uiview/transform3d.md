# transform3D

**Framework**: UIKit  
**Kind**: property

The three-dimensional transform to apply to the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var transform3D: CATransform3D { get set }
```

#### Discussion

The default value of this property is [`CATransform3DIdentity`](https://developer.apple.com/documentation/QuartzCore/CATransform3DIdentity).

## See Also

- [var frame: CGRect](uiview/frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var bounds: CGRect](uiview/bounds.md)
  The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [var center: CGPoint](uiview/center.md)
  The center point of the view’s frame rectangle.
- [var transform: CGAffineTransform](uiview/transform.md)
  Specifies the transform applied to the view, relative to the center of its bounds.
- [var anchorPoint: CGPoint](uiview/anchorpoint.md)
  The anchor point of the view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/transform3d)*