# exchangeSubview(at:withSubviewAt:)

**Framework**: UIKit  
**Kind**: method

Exchanges the subviews at the specified indices.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func exchangeSubview(at index1: Int, withSubviewAt index2: Int)
```

#### Discussion

Each index represents the position of the corresponding view in the array in the [`subviews`](uiview/subviews.md) property. Subview indices start at `0` and cannot be greater than the number of subviews. This method does not change the superview of either view but simply swaps their positions in the [`subviews`](uiview/subviews.md) array.

## Parameters

- `index1`: The index of the first subview in the receiver.
- `index2`: The index of the second subview in the receiver.

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
- [func isDescendant(of: UIView) -> Bool](uiview/isdescendant(of:).md)
  Returns a Boolean value indicating whether the receiver is a subview of a given view or identical to that view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/exchangesubview(at:withsubviewat:))*