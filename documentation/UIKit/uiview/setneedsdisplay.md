# setNeedsDisplay(_:)

**Framework**: Uikit  
**Kind**: method

Marks the specified rectangle of the receiver as needing to be redrawn.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func setNeedsDisplay(_ rect: CGRect)
```

#### Discussion

You can use this method or the [`setNeedsDisplay()`](uiview/setneedsdisplay().md) to notify the system that your view’s contents need to be redrawn. This method adds the specified rectangle into the view’s current list of invalid rectangles and returns immediately. The view is not actually redrawn until the next drawing cycle, at which point all invalidated views are updated.

> **Note**:  If your view is backed by a [`CAEAGLLayer`](https://developer.apple.com/documentation/QuartzCore/CAEAGLLayer) object, this method has no effect. It is intended for use only with views that use native drawing technologies (such as UIKit and Core Graphics) to render their content.

You should use this method to request that a view be redrawn only when the content or appearance of the view change. If you simply change the geometry of the view, the view is typically not redrawn. Instead, its existing content is adjusted based on the value in the view’s [`contentMode`](uiview/contentmode-swift.property.md) property. Redisplaying the existing content improves performance by avoiding the need to redraw content that has not changed.

## Parameters

- `rect`: The rectangular region of the receiver to mark as invalid; it should be specified in the coordinate system of the receiver.

## See Also

- [var contentMode: UIView.ContentMode](uiview/contentmode-swift.property.md)
  A flag used to determine how a view lays out its content when its bounds change.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.
- [func setNeedsDisplay()](uiview/setneedsdisplay.md)
  Marks the receiver’s entire bounds rectangle as needing to be redrawn.
- [var contentScaleFactor: CGFloat](uiview/contentscalefactor.md)
  The scale factor applied to the view.
- [func tintColorDidChange()](uiview/tintcolordidchange.md)
  Called by the system when the tint color property changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/setneedsdisplay(_:))*