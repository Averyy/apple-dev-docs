# tintColor

**Framework**: UIKit  
**Kind**: property

The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tintColor: UIColor! { get set }
```

#### Discussion

If the system cannot find a nondefault color in the hierarchy, this property’s value is a system-defined color instead.

If the view’s [`tintAdjustmentMode`](uiview/tintadjustmentmode-swift.property.md) property’s value is [`UIView.TintAdjustmentMode.dimmed`](uiview/tintadjustmentmode-swift.enum/dimmed.md), then the [`tintColor`](uiview/tintcolor.md) property value is automatically dimmed.

To refresh subview rendering when this property changes, override the [`tintColorDidChange()`](uiview/tintcolordidchange().md) method.

Colors that are pattern colors (as described in [`UIColor`](uicolor.md)) are not supported.

> ❗ **Important**:  If you attempt to use a pattern color as a tint color, the system raises an exception.

## See Also

- [func tintColorDidChange()](uiview/tintcolordidchange.md)
  Called by the system when the tint color property changes.
- [var backgroundColor: UIColor?](uiview/backgroundcolor.md)
  The view’s background color.
- [var isHidden: Bool](uiview/ishidden.md)
  A Boolean value that determines whether the view is hidden.
- [var alpha: CGFloat](uiview/alpha.md)
  The view’s alpha value.
- [var isOpaque: Bool](uiview/isopaque.md)
  A Boolean value that determines whether the view is opaque.
- [var tintAdjustmentMode: UIView.TintAdjustmentMode](uiview/tintadjustmentmode-swift.property.md)
  The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [var clipsToBounds: Bool](uiview/clipstobounds.md)
  A Boolean value that determines whether subviews are confined to the bounds of the view.
- [var clearsContextBeforeDrawing: Bool](uiview/clearscontextbeforedrawing.md)
  A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [var mask: UIView?](uiview/mask.md)
  An optional view whose alpha channel is used to mask a view’s content.
- [class var layerClass: AnyClass](uiview/layerclass.md)
  Returns the class used to create the layer for instances of this class.
- [var layer: CALayer](uiview/layer.md)
  The view’s Core Animation layer to use for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/tintcolor)*