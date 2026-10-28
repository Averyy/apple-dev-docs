# layerClass

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

Returns the class used to create the layer for instances of this class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class var layerClass: AnyClass { get }
```

```objc
@property (class, nonatomic, readonly) Class layerClass;
```

## Return Value

The class used to create the view’s Core Animation layer.

## Discussion

This method returns the [`CALayer`](../../QuartzCore/calayer.md) class object by default. Subclasses can override this method and return a different layer class as needed. For example, if your view uses tiling to display a large scrollable area, you might want to override this property and return the [`CATiledLayer`](../../QuartzCore/catiledlayer.md) class, as shown in the following code.

```swift
override class var layerClass : AnyClass {
   return CATiledLayer.self
}
```

This method is called only once early in the creation of the view in order to create the corresponding layer object.

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
- [var layer: CALayer](./layer.md)
  The view’s Core Animation layer to use for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/layerclass)*