# willRemoveSubview(_:)

**Framework**: UIKit  
**Kind**: method

Tells the view that a subview is about to be removed.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func willRemoveSubview(_ subview: UIView)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever subviews are removed. This method is called when the subview’s superview changes or when the subview is removed from the view hierarchy completely.

## Parameters

- `subview`: The subview that will be removed.

## See Also

- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [func didAddSubview(UIView)](uiview/didaddsubview(_:).md)
  Tells the view that a subview was added.
- [func willMove(toSuperview: UIView?)](uiview/willmove(tosuperview:).md)
  Tells the view that its superview is about to change to the specified superview.
- [func didMoveToSuperview()](uiview/didmovetosuperview.md)
  Tells the view that its superview changed.
- [func willMove(toWindow: UIWindow?)](uiview/willmove(towindow:).md)
  Tells the view that its window object is about to change.
- [func didMoveToWindow()](uiview/didmovetowindow.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/willremovesubview(_:))*