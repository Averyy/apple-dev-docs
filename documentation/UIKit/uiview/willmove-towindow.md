# willMove(toWindow:)

**Framework**: UIKit  
**Kind**: method

Tells the view that its window object is about to change.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func willMove(toWindow newWindow: UIWindow?)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions whenever the window changes.

## Parameters

- `newWindow`: The window object that will be at the root of the receiver’s new view hierarchy. This parameter may be  .

## See Also

- [func didAddSubview(UIView)](uiview/didaddsubview(_:).md)
  Tells the view that a subview was added.
- [func willRemoveSubview(UIView)](uiview/willremovesubview(_:).md)
  Tells the view that a subview is about to be removed.
- [func willMove(toSuperview: UIView?)](uiview/willmove(tosuperview:).md)
  Tells the view that its superview is about to change to the specified superview.
- [func didMoveToSuperview()](uiview/didmovetosuperview.md)
  Tells the view that its superview changed.
- [func didMoveToWindow()](uiview/didmovetowindow.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/willmove(towindow:))*