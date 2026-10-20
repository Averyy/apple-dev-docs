# transform

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies the transform applied to the view, relative to the center of its bounds.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var transform: CGAffineTransform { get set }
```

```objc
@property (nonatomic) CGAffineTransform transform;
```

#### Discussion

Use this property to scale or rotate the view’s frame rectangle within its superview’s coordinate system. (To change the position of the view, modify the [`center`](./center.md) property instead.) The default value of this property is `CGAffineTransformIdentity`.

Transformations occur relative to the view’s anchor point. By default, the anchor point is equal to the center point of the frame rectangle. To change the anchor point, modify the [`anchorPoint`](../../QuartzCore/calayer/anchorpoint.md) property of the view’s underlying [`CALayer`](../../QuartzCore/calayer.md) object.

Changes to this property can be animated.

In iOS 8.0 and later, the `transform` property does not affect Auto Layout. Auto layout calculates a view’s alignment rectangle based on its untransformed frame.

> ⚠️ **Warning**:  When the value of this property is anything other than the identity transform, the value in the [`frame`](./frame.md) property is undefined and should be ignored.

## See Also

### Configuring the bounds and frame rectangles
- [var frame: CGRect](./frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var bounds: CGRect](./bounds.md)
  The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [var center: CGPoint](./center.md)
  The center point of the view’s frame rectangle.
- [var transform3D: CATransform3D](./transform3d.md)
  The three-dimensional transform to apply to the view.
- [var anchorPoint: CGPoint](./anchorpoint.md)
  The anchor point of the view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/transform)*