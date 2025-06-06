# insertSubview(_:at:)

**Framework**: UIKit  
**Kind**: method

Inserts a subview at the specified index.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func insertSubview(_ view: UIView, at index: Int)
```

#### Discussion

This method establishes a strong reference to `view` and sets its next responder to the receiver, which is its new superview.

Views can have only one superview. If `view` already has a superview and that view is not the receiver, this method removes the previous superview before making the receiver its new superview.

## Parameters

- `view`: The view to insert. This value cannot be  .
- `index`: The index in the array of the   property at which to insert the view. Subview indices start at   and cannot be greater than the number of subviews.

## See Also

- [var superview: UIView?](uiview/superview.md)
  The receiver’s superview, or `nil` if it has none.
- [var subviews: [UIView]](uiview/subviews.md)
  The receiver’s immediate subviews.
- [var window: UIWindow?](uiview/window.md)
  The receiver’s window object, or `nil` if it has none.
- [func addSubview(UIView)](uiview/addsubview(_:).md)
  Adds a view to the end of the receiver’s list of subviews.
- [func bringSubviewToFront(UIView)](uiview/bringsubviewtofront(_:).md)
  Moves the specified subview so that it appears on top of its siblings.
- [func sendSubviewToBack(UIView)](uiview/sendsubviewtoback(_:).md)
  Moves the specified subview so that it appears behind its siblings.
- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [func insertSubview(UIView, aboveSubview: UIView)](uiview/insertsubview(_:abovesubview:).md)
  Inserts a view above another view in the view hierarchy.
- [func insertSubview(UIView, belowSubview: UIView)](uiview/insertsubview(_:belowsubview:).md)
  Inserts a view below another view in the view hierarchy.
- [func exchangeSubview(at: Int, withSubviewAt: Int)](uiview/exchangesubview(at:withsubviewat:).md)
  Exchanges the subviews at the specified indices.
- [func isDescendant(of: UIView) -> Bool](uiview/isdescendant(of:).md)
  Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/insertsubview(_:at:))*