# transform3D

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The three-dimensional transform to apply to the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var transform3D: CATransform3D { get set }
```

```objc
@property (nonatomic) CATransform3D transform3D;
```

#### Discussion

The default value of this property is [`CATransform3DIdentity`](../../QuartzCore/catransform3didentity.md).

## See Also

### Configuring the bounds and frame rectangles
- [var frame: CGRect](./frame.md)
  The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [var bounds: CGRect](./bounds.md)
  The bounds rectangle, which describes the view’s location and size in its own coordinate system.
- [var center: CGPoint](./center.md)
  The center point of the view’s frame rectangle.
- [var transform: CGAffineTransform](./transform.md)
  Specifies the transform applied to the view, relative to the center of its bounds.
- [var anchorPoint: CGPoint](./anchorpoint.md)
  The anchor point of the view’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/transform3d)*