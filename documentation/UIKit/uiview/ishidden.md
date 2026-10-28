# isHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view is hidden.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (nonatomic, getter=isHidden) BOOL hidden;
```

## Discussion

Setting the value of this property to [`true`](../../Swift/true.md) hides the receiver and setting it to [`false`](../../Swift/false.md) shows the receiver. The default value is [`false`](../../Swift/false.md).

A hidden view disappears from its window and does not receive input events. It remains in its superview’s list of subviews, however, and participates in autoresizing as usual. Hiding a view with subviews has the effect of hiding those subviews and any view descendants they might have. This effect is implicit and does not alter the hidden state of the receiver’s descendants.

Hiding the view that is the window’s current first responder causes the view’s next valid key view to become the new first responder.

The value of this property reflects the state of the receiver only and does not account for the state of the receiver’s ancestors in the view hierarchy. Thus this property can be [`false`](../../Swift/false.md) but the receiver may still be hidden if an ancestor is hidden.

## See Also

### Configuring a view’s visual appearance
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The view’s background color.
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
- [var layer: CALayer](./layer.md)
  The view’s Core Animation layer to use for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/ishidden)*