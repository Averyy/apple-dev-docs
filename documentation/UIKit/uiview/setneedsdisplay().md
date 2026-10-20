# setNeedsDisplay()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Marks the receiver’s entire bounds rectangle as needing to be redrawn.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func setNeedsDisplay()
```

```objc
- (void) setNeedsDisplay;
```

## Mentions

- [Updating views automatically with observation tracking in UIKit](../updating-views-automatically-with-observation-tracking-in-uikit.md)

#### Discussion

You can use this method or the [`setNeedsDisplay(_:)`](./setneedsdisplay%28_%29.md) to notify the system that your view’s contents need to be redrawn. This method makes a note of the request and returns immediately. The view is not actually redrawn until the next drawing cycle, at which point all invalidated views are updated.

> **Note**:  If your view is backed by a [`CAEAGLLayer`](../../QuartzCore/caeagllayer.md) object, this method has no effect. It is intended for use only with views that use native drawing technologies (such as UIKit and Core Graphics) to render their content.

You should use this method to request that a view be redrawn only when the content or appearance of the view change. If you simply change the geometry of the view, the view is typically not redrawn. Instead, its existing content is adjusted based on the value in the view’s [`contentMode`](./contentmode-swift.property.md) property. Redisplaying the existing content improves performance by avoiding the need to redraw content that has not changed.

## See Also

### Related Documentation
- [var contentMode: UIView.ContentMode](./contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
### Drawing and updating the view
- [func draw(CGRect)](./draw%28_%29.md)
  Draws the view’s image within the passed-in rectangle.
- [func setNeedsDisplay(CGRect)](./setneedsdisplay%28_%29.md)
  Marks the specified rectangle of the receiver as needing to be redrawn.
- [var contentScaleFactor: CGFloat](./contentscalefactor.md)
  The scale factor applied to the view.
- [func tintColorDidChange()](./tintcolordidchange%28%29.md)
  Called by the system when the tint color property changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setneedsdisplay())*