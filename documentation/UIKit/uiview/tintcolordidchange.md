# tintColorDidChange()

**Framework**: UIKit  
**Kind**: method

Called by the system when the tint color property changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func tintColorDidChange()
```

#### Discussion

The system calls this method on a view when your code changes the value of the [`tintColor`](uiview/tintcolor.md) property on that view. In addition, the system calls this method on a subview that inherits a changed interaction tint color.

In your implementation, refresh the view rendering as needed.

## See Also

- [var tintColor: UIColor!](uiview/tintcolor.md)
  The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.
- [func setNeedsDisplay()](uiview/setneedsdisplay.md)
  Marks the receiver’s entire bounds rectangle as needing to be redrawn.
- [func setNeedsDisplay(CGRect)](uiview/setneedsdisplay(_:).md)
  Marks the specified rectangle of the receiver as needing to be redrawn.
- [var contentScaleFactor: CGFloat](uiview/contentscalefactor.md)
  The scale factor applied to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/tintcolordidchange())*