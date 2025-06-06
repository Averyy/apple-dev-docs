# didAddSubview(_:)

**Framework**: UIKit  
**Kind**: method

Tells the view that a subview was added.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func didAddSubview(_ subview: UIView)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override it to perform additional actions when subviews are added. This method is called in response to adding a subview using any of the relevant view methods.

## Parameters

- `subview`: The view that was added as a subview.

## See Also

- [func insertSubview(UIView, belowSubview: UIView)](uiview/insertsubview(_:belowsubview:).md)
  Inserts a view below another view in the view hierarchy.
- [func insertSubview(UIView, aboveSubview: UIView)](uiview/insertsubview(_:abovesubview:).md)
  Inserts a view above another view in the view hierarchy.
- [func addSubview(UIView)](uiview/addsubview(_:).md)
  Adds a view to the end of the receiver’s list of subviews.
- [func insertSubview(UIView, at: Int)](uiview/insertsubview(_:at:).md)
  Inserts a subview at the specified index.
- [func willRemoveSubview(UIView)](uiview/willremovesubview(_:).md)
  Tells the view that a subview is about to be removed.
- [func willMove(toSuperview: UIView?)](uiview/willmove(tosuperview:).md)
  Tells the view that its superview is about to change to the specified superview.
- [func didMoveToSuperview()](uiview/didmovetosuperview.md)
  Tells the view that its superview changed.
- [func willMove(toWindow: UIWindow?)](uiview/willmove(towindow:).md)
  Tells the view that its window object is about to change.
- [func didMoveToWindow()](uiview/didmovetowindow.md)
  Tells the view that its window object changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/didaddsubview(_:))*