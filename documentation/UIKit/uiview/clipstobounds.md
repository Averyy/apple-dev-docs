# clipsToBounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether subviews are confined to the bounds of the view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var clipsToBounds: Bool { get set }
```

```objc
@property (nonatomic) BOOL clipsToBounds;
```

## Mentions

- [Using responders and the responder chain to handle events](../using-responders-and-the-responder-chain-to-handle-events.md)

#### Discussion

Setting this value to [`true`](../../Swift/true.md) causes subviews to be clipped to the bounds of the view. If set to [`false`](../../Swift/false.md), subviews whose frames extend beyond the visible bounds of the view aren’t clipped.

The default value is [`false`](../../Swift/false.md). Some subclasses of [`UIView`](../uiview.md), like [`UIScrollView`](../uiscrollview.md), override the default value to [`true`](../../Swift/true.md).

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
- [var clearsContextBeforeDrawing: Bool](./clearscontextbeforedrawing.md)
  A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [var mask: UIView?](./mask.md)
  An optional view whose alpha channel is used to mask a view’s content.
- [class var layerClass: AnyClass](./layerclass.md)
  Returns the class used to create the layer for instances of this class.
- [var layer: CALayer](./layer.md)
  The view’s Core Animation layer to use for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/clipstobounds)*