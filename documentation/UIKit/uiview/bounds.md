# bounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bounds rectangle, which describes the view’s location and size in its own coordinate system.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var bounds: CGRect { get set }
```

```objc
@property (nonatomic) CGRect bounds;
```

## Mentions

- [Implementing a Multi-Touch app](../implementing-a-multi-touch-app.md)

## Discussion

The default bounds origin is (0,0) and the size is the same as the size of the rectangle in the [`frame`](./frame.md) property. Changing the size portion of this rectangle grows or shrinks the view relative to its center point. Changing the size also changes the size of the rectangle in the [`frame`](./frame.md) property to match. The coordinates of the bounds rectangle are always specified in points.

Changing the bounds rectangle automatically redisplays the view without calling its [`draw(_:)`](./draw%28_%29.md) method. If you want UIKit to call the [`draw(_:)`](./draw%28_%29.md) method, set the [`contentMode`](./contentmode-swift.property.md) property to [`UIView.ContentMode.redraw`](./contentmode-swift.enum/redraw.md).

Changes to this property can be animated.

## See Also

### Configuring the bounds and frame rectangles
- [var frame: CGRect](./frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var center: CGPoint](./center.md)
  The center point of the view’s frame rectangle.
- [var transform: CGAffineTransform](./transform.md)
  Specifies the transform applied to the view, relative to the center of its bounds.
- [var transform3D: CATransform3D](./transform3d.md)
  The three-dimensional transform to apply to the view.
- [var anchorPoint: CGPoint](./anchorpoint.md)
  The anchor point of the view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/bounds)*