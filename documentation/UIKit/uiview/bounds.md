# bounds

**Framework**: UIKit  
**Kind**: property

The bounds rectangle, which describes the view’s location and size in its own coordinate system.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var bounds: CGRect { get set }
```

## Mentions

- [Implementing a Multi-Touch app](implementing-a-multi-touch-app.md)

#### Discussion

The default bounds origin is (0,0) and the size is the same as the size of the rectangle in the [`frame`](uiview/frame.md) property. Changing the size portion of this rectangle grows or shrinks the view relative to its center point. Changing the size also changes the size of the rectangle in the [`frame`](uiview/frame.md) property to match. The coordinates of the bounds rectangle are always specified in points.

Changing the bounds rectangle automatically redisplays the view without calling its [`draw(_:)`](uiview/draw(_:).md) method. If you want UIKit to call the [`draw(_:)`](uiview/draw(_:).md) method, set the [`contentMode`](uiview/contentmode-swift.property.md) property to [`UIView.ContentMode.redraw`](uiview/contentmode-swift.enum/redraw.md).

Changes to this property can be animated.

## See Also

- [var frame: CGRect](uiview/frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var center: CGPoint](uiview/center.md)
  The center point of the view’s frame rectangle.
- [var transform: CGAffineTransform](uiview/transform.md)
  Specifies the transform applied to the view, relative to the center of its bounds.
- [var transform3D: CATransform3D](uiview/transform3d.md)
  The three-dimensional transform to apply to the view.
- [var anchorPoint: CGPoint](uiview/anchorpoint.md)
  The anchor point of the view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/bounds)*