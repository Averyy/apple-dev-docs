# removeArrangedSubview(_:)

**Framework**: UIKit  
**Kind**: method

Removes the provided view from the stack’s array of arranged subviews.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeArrangedSubview(_ view: UIView)
```

#### Discussion

This method removes the provided view from the stack’s [`arrangedSubviews`](uistackview/arrangedsubviews.md) array. The stack view no longer manages the view’s position and size. However, this method doesn’t remove the provided view from the stack’s [`subviews`](uiview/subviews.md) array; therefore, the view is still displayed as part of the view hierarchy.

To prevent the view from appearing on screen after calling the stack’s [`removeArrangedSubview(_:)`](uistackview/removearrangedsubview(_:).md) method, explicitly remove the view from the subviews array by calling the view’s [`removeFromSuperview()`](uiview/removefromsuperview().md) method, or set the view’s [`isHidden`](uiview/ishidden.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `view`: The view to be removed from the array of views arranged by the stack.

## See Also

- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [convenience init(arrangedSubviews: [UIView])](uistackview/init(arrangedsubviews:).md)
  Returns a new stack view object that manages the provided views.
- [func addArrangedSubview(UIView)](uistackview/addarrangedsubview(_:).md)
  Adds a view to the end of the arranged subviews array.
- [var arrangedSubviews: [UIView]](uistackview/arrangedsubviews.md)
  The list of views arranged by the stack view.
- [func insertArrangedSubview(UIView, at: Int)](uistackview/insertarrangedsubview(_:at:).md)
  Adds the provided view to the array of arranged subviews at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/removearrangedsubview(_:))*