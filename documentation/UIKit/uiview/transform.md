# transform

**Framework**: UIKit  
**Kind**: property

Specifies the transform applied to the view, relative to the center of its bounds.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var transform: CGAffineTransform { get set }
```

#### Discussion

Use this property to scale or rotate the view’s frame rectangle within its superview’s coordinate system. (To change the position of the view, modify the [`center`](uiview/center.md) property instead.) The default value of this property is `CGAffineTransformIdentity`.

Transformations occur relative to the view’s anchor point. By default, the anchor point is equal to the center point of the frame rectangle. To change the anchor point, modify the [`anchorPoint`](https://developer.apple.com/documentation/QuartzCore/CALayer/anchorPoint) property of the view’s underlying [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) object.

Changes to this property can be animated.

In iOS 8.0 and later, the `transform` property does not affect Auto Layout. Auto layout calculates a view’s alignment rectangle based on its untransformed frame.

> ⚠️ **Warning**:  When the value of this property is anything other than the identity transform, the value in the [`frame`](uiview/frame.md) property is undefined and should be ignored.

## See Also

- [var frame: CGRect](uiview/frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var bounds: CGRect](uiview/bounds.md)
  The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [var center: CGPoint](uiview/center.md)
  The center point of the view’s frame rectangle.
- [var transform3D: CATransform3D](uiview/transform3d.md)
  The three-dimensional transform to apply to the view.
- [var anchorPoint: CGPoint](uiview/anchorpoint.md)
  The anchor point of the view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/transform)*