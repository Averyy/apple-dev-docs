# removeFromSuperview()

**Framework**: UIKit  
**Kind**: method

Unlinks the view from its superview and its window, and removes it from the responder chain.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func removeFromSuperview()
```

## Mentions

- [Creating a custom container view controller](creating-a-custom-container-view-controller.md)

#### Discussion

If the view’s superview is not `nil`, the superview releases the view.

Calling this method removes any constraints that refer to the view you are removing, or that refer to any view in the subtree of the view you are removing.

> ❗ **Important**:  Never call this method from inside your view’s [`draw(_:)`](uiview/draw(_:).md) method.

 Never call this method from inside your view’s [`draw(_:)`](uiview/draw(_:).md) method.

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
- [func insertSubview(UIView, at: Int)](uiview/insertsubview(_:at:).md)
  Inserts a subview at the specified index.
- [func insertSubview(UIView, aboveSubview: UIView)](uiview/insertsubview(_:abovesubview:).md)
  Inserts a view above another view in the view hierarchy.
- [func insertSubview(UIView, belowSubview: UIView)](uiview/insertsubview(_:belowsubview:).md)
  Inserts a view below another view in the view hierarchy.
- [func exchangeSubview(at: Int, withSubviewAt: Int)](uiview/exchangesubview(at:withsubviewat:).md)
  Exchanges the subviews at the specified indices.
- [func isDescendant(of: UIView) -> Bool](uiview/isdescendant(of:).md)
  Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/removefromsuperview())*