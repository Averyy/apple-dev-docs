# didMoveToWindow()

**Framework**: UIKit  
**Kind**: method

Tells the view that its window object changed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func didMoveToWindow()
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the window changes.

The [`window`](uiview/window.md) property may be `nil` by the time that this method is called, indicating that the receiver does not currently reside in any window. This occurs when the receiver has just been removed from its superview or when the receiver has just been added to a superview that is not attached to a window. Overrides of this method may choose to ignore such cases if they are not of interest.

## See Also

- [func didAddSubview(UIView)](uiview/didaddsubview(_:).md)
  Tells the view that a subview was added.
- [func willRemoveSubview(UIView)](uiview/willremovesubview(_:).md)
  Tells the view that a subview is about to be removed.
- [func willMove(toSuperview: UIView?)](uiview/willmove(tosuperview:).md)
  Tells the view that its superview is about to change to the specified superview.
- [func didMoveToSuperview()](uiview/didmovetosuperview.md)
  Tells the view that its superview changed.
- [func willMove(toWindow: UIWindow?)](uiview/willmove(towindow:).md)
  Tells the view that its window object is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/didmovetowindow())*