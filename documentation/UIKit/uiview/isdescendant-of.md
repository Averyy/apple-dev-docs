# isDescendant(of:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func isDescendant(of view: UIView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver is an immediate or distant subview of `view` or if `view` is the receiver itself; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `view`: The view to test against the receiver’s view hierarchy.

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
- [func insertSubview(UIView, at: Int)](uiview/insertsubview(_:at:).md)
  Inserts a subview at the specified index.
- [func insertSubview(UIView, aboveSubview: UIView)](uiview/insertsubview(_:abovesubview:).md)
  Inserts a view above another view in the view hierarchy.
- [func insertSubview(UIView, belowSubview: UIView)](uiview/insertsubview(_:belowsubview:).md)
  Inserts a view below another view in the view hierarchy.
- [func exchangeSubview(at: Int, withSubviewAt: Int)](uiview/exchangesubview(at:withsubviewat:).md)
  Exchanges the subviews at the specified indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/isdescendant(of:))*