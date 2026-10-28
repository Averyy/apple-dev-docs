# layer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view’s Core Animation layer to use for rendering.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var layer: CALayer { get }
```

```objc
@property (nonatomic, strong, readonly) CALayer * layer;
```

## Discussion

This property is never `nil`. The value of the [`layerClass`](./layerclass.md) property determines the actual class of the layer object. The view is the layer’s delegate.

> ⚠️ **Warning**:  Because the view is the layer’s delegate, never make the view the delegate of another [`CALayer`](../../QuartzCore/calayer.md) object. Additionally, never change the delegate of this layer object.

## See Also

### Configuring a view’s visual appearance
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The view’s background color.
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that determines whether the view is hidden.
- [var alpha: CGFloat](./alpha.md)
  The view’s alpha value.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value that determines whether the view is opaque.
- [var tintColor: UIColor!](./tintcolor.md)
  The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [var tintAdjustmentMode: UIView.TintAdjustmentMode](./tintadjustmentmode-swift.property.md)
  The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [var clipsToBounds: Bool](./clipstobounds.md)
  A Boolean value that determines whether subviews are confined to the bounds of the view.
- [var clearsContextBeforeDrawing: Bool](./clearscontextbeforedrawing.md)
  A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [var mask: UIView?](./mask.md)
  An optional view whose alpha channel is used to mask a view’s content.
- [class var layerClass: AnyClass](./layerclass.md)
  Returns the class used to create the layer for instances of this class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layer)*