# didMoveToSuperview()

**Framework**: UIKit  
**Kind**: method

Tells the view that its superview changed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func didMoveToSuperview()
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the superview changes.

## See Also

- [func didAddSubview(UIView)](uiview/didaddsubview(_:).md)
  Tells the view that a subview was added.
- [func willRemoveSubview(UIView)](uiview/willremovesubview(_:).md)
  Tells the view that a subview is about to be removed.
- [func willMove(toSuperview: UIView?)](uiview/willmove(tosuperview:).md)
  Tells the view that its superview is about to change to the specified superview.
- [func willMove(toWindow: UIWindow?)](uiview/willmove(towindow:).md)
  Tells the view that its window object is about to change.
- [func didMoveToWindow()](uiview/didmovetowindow.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/didmovetosuperview())*