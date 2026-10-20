# center

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The center point of the view’s frame rectangle.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var center: CGPoint { get set }
```

```objc
@property (nonatomic) CGPoint center;
```

#### Discussion

The center point is specified in points in the coordinate system of its superview. Setting this property updates the origin of the rectangle in the [`frame`](./frame.md) property appropriately.

Use this property, instead of the [`frame`](./frame.md) property, when you want to change the position of a view. The center point is always valid, even when scaling or rotation factors are applied to the view’s transform.   Changes to this property can be animated.

## See Also

### Configuring the bounds and frame rectangles
- [var frame: CGRect](./frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var bounds: CGRect](./bounds.md)
  The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [var transform: CGAffineTransform](./transform.md)
  Specifies the transform applied to the view, relative to the center of its bounds.
- [var transform3D: CATransform3D](./transform3d.md)
  The three-dimensional transform to apply to the view.
- [var anchorPoint: CGPoint](./anchorpoint.md)
  The anchor point of the view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/center)*