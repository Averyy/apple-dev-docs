# arrangedSubviews

**Framework**: UIKit  
**Kind**: property

The list of views arranged by the stack view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var arrangedSubviews: [UIView] { get }
```

#### Discussion

The stack view ensures that the [`arrangedSubviews`](uistackview/arrangedsubviews.md) array is always a subset of its [`subviews`](uiview/subviews.md) array. Therefore, whenever the [`addArrangedSubview(_:)`](uistackview/addarrangedsubview(_:).md) method is called, the stack view adds the view as a subview, if it isn’t already. Whenever an arranged view’s [`removeFromSuperview()`](uiview/removefromsuperview().md) method is called, the stack view removes the view from its [`arrangedSubviews`](uistackview/arrangedsubviews.md) array.

## See Also

- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [convenience init(arrangedSubviews: [UIView])](uistackview/init(arrangedsubviews:).md)
  Returns a new stack view object that manages the provided views.
- [func addArrangedSubview(UIView)](uistackview/addarrangedsubview(_:).md)
  Adds a view to the end of the arranged subviews array.
- [func insertArrangedSubview(UIView, at: Int)](uistackview/insertarrangedsubview(_:at:).md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(UIView)](uistackview/removearrangedsubview(_:).md)
  Removes the provided view from the stack’s array of arranged subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/arrangedsubviews)*