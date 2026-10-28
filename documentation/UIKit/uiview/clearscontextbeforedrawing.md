# clearsContextBeforeDrawing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var clearsContextBeforeDrawing: Bool { get set }
```

```objc
@property (nonatomic) BOOL clearsContextBeforeDrawing;
```

## Discussion

When set to [`true`](../../Swift/true.md), the drawing buffer is automatically cleared to transparent black before the [`draw(_:)`](./draw%28_%29.md) method is called. This behavior ensures that there are no visual artifacts left over when the view’s contents are redrawn. If the view’s [`isOpaque`](./isopaque.md) property is also set to [`true`](../../Swift/true.md), the [`backgroundColor`](./backgroundcolor.md) property of the view must not be `nil` or drawing errors may occur. The default value of this property is [`true`](../../Swift/true.md).

If you set the value of this property to [`false`](../../Swift/false.md), you are responsible for ensuring the contents of the view are drawn properly in your [`draw(_:)`](./draw%28_%29.md) method. If your drawing code is already heavily optimized, setting this property is [`false`](../../Swift/false.md) can improve performance, especially during scrolling when only a portion of the view might need to be redrawn.

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
- [var mask: UIView?](./mask.md)
  An optional view whose alpha channel is used to mask a view’s content.
- [class var layerClass: AnyClass](./layerclass.md)
  Returns the class used to create the layer for instances of this class.
- [var layer: CALayer](./layer.md)
  The view’s Core Animation layer to use for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/clearscontextbeforedrawing)*