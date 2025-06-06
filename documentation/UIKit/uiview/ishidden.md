# isHidden

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the view is hidden.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isHidden: Bool { get set }
```

#### Discussion

Setting the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) hides the receiver and setting it to [`false`](https://developer.apple.com/documentation/swift/false) shows the receiver. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

A hidden view disappears from its window and does not receive input events. It remains in its superview’s list of subviews, however, and participates in autoresizing as usual. Hiding a view with subviews has the effect of hiding those subviews and any view descendants they might have. This effect is implicit and does not alter the hidden state of the receiver’s descendants.

Hiding the view that is the window’s current first responder causes the view’s next valid key view to become the new first responder.

The value of this property reflects the state of the receiver only and does not account for the state of the receiver’s ancestors in the view hierarchy. Thus this property can be [`false`](https://developer.apple.com/documentation/swift/false) but the receiver may still be hidden if an ancestor is hidden.

## See Also

- [var backgroundColor: UIColor?](uiview/backgroundcolor.md)
  The view’s background color.
- [var alpha: CGFloat](uiview/alpha.md)
  The view’s alpha value.
- [var isOpaque: Bool](uiview/isopaque.md)
  A Boolean value that determines whether the view is opaque.
- [var tintColor: UIColor!](uiview/tintcolor.md)
  The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/ishidden)*