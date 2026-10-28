# frame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var frame: CGRect { get set }
```

```objc
@property (nonatomic) CGRect frame;
```

## Discussion

This rectangle defines the size and position of the view in its superview’s coordinate system. Use this rectangle during layout operations to set the size and position the view. Setting this property changes the point specified by the [`center`](./center.md) property and changes the size in the [`bounds`](./bounds.md) rectangle accordingly. The coordinates of the frame rectangle are always specified in points.

> ⚠️ **Warning**:  If the [`transform`](./transform.md) property is not the identity transform, the value of this property is undefined and therefore should be ignored.

Changing the frame rectangle automatically redisplays the view without calling its [`draw(_:)`](./draw%28_%29.md) method. If you want UIKit to call the [`draw(_:)`](./draw%28_%29.md) method when the frame rectangle changes, set the [`contentMode`](./contentmode-swift.property.md) property to [`UIView.ContentMode.redraw`](./contentmode-swift.enum/redraw.md).

Changes to this property can be animated. However, if the [`transform`](./transform.md) property contains a non-identity transform, the value of the [`frame`](./frame.md) property is undefined and should not be modified. In that case, reposition the view using the [`center`](./center.md) property and adjust the size using the [`bounds`](./bounds.md) property instead.

## See Also

### Configuring the bounds and frame rectangles
- [var bounds: CGRect](./bounds.md)
  The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [var center: CGPoint](./center.md)
  The center point of the view’s frame rectangle.
- [var transform: CGAffineTransform](./transform.md)
  Specifies the transform applied to the view, relative to the center of its bounds.
- [var transform3D: CATransform3D](./transform3d.md)
  The three-dimensional transform to apply to the view.
- [var anchorPoint: CGPoint](./anchorpoint.md)
  The anchor point of the view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/frame)*