# addArrangedSubview(_:)

**Framework**: UIKit  
**Kind**: method

Adds a view to the end of the arranged subviews array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addArrangedSubview(_ view: UIView)
```

#### Discussion

The stack view ensures that the [`arrangedSubviews`](uistackview/arrangedsubviews.md) array is always a subset of its [`subviews`](uiview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it isn’t already. If the view is already a subview, this operation doesn’t alter the subview ordering.

## Parameters

- `view`: The view to add to the array of views arranged by the stack.

## See Also

- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [convenience init(arrangedSubviews: [UIView])](uistackview/init(arrangedsubviews:).md)
  Returns a new stack view object that manages the provided views.
- [var arrangedSubviews: [UIView]](uistackview/arrangedsubviews.md)
  The list of views arranged by the stack view.
- [func insertArrangedSubview(UIView, at: Int)](uistackview/insertarrangedsubview(_:at:).md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(UIView)](uistackview/removearrangedsubview(_:).md)
  Removes the provided view from the stack’s array of arranged subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/addarrangedsubview(_:))*