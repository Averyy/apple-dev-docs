# tintAdjustmentMode

**Framework**: UIKit  
**Kind**: property

The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tintAdjustmentMode: UIView.TintAdjustmentMode { get set }
```

#### Discussion

When this property’s value is [`UIView.TintAdjustmentMode.dimmed`](uiview/tintadjustmentmode-swift.enum/dimmed.md), the value of the [`tintColor`](uiview/tintcolor.md) property is modified to provide a dimmed appearance.

If the system cannot find a non-default value in the subview hierarchy when you query this property, the value is [`UIView.TintAdjustmentMode.normal`](uiview/tintadjustmentmode-swift.enum/normal.md).

When this property’s value changes (either by the view’s value changing or by one of its superview’s values changing), the system calls the [`tintColorDidChange()`](uiview/tintcolordidchange().md) method to allow the view to refresh its rendering.

## See Also

- [var backgroundColor: UIColor?](uiview/backgroundcolor.md)
  The view’s background color.
- [var isHidden: Bool](uiview/ishidden.md)
  A Boolean value that determines whether the view is hidden.
- [var alpha: CGFloat](uiview/alpha.md)
  The view’s alpha value.
- [var isOpaque: Bool](uiview/isopaque.md)
  A Boolean value that determines whether the view is opaque.
- [var tintColor: UIColor!](uiview/tintcolor.md)
  The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/tintadjustmentmode-swift.property)*