# insertArrangedSubview(_:at:)

**Framework**: UIKit  
**Kind**: method

Adds the provided view to the array of arranged subviews at the specified index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func insertArrangedSubview(_ view: UIView, at stackIndex: Int)
```

#### Discussion

If index is already occupied, the stack view increases the size of the [`arrangedSubviews`](uistackview/arrangedsubviews.md) array and shifts all of its contents at the index and above to the next higher space in the array. Then the stack view stores the provided view at the index.

The stack view also ensures that the [`arrangedSubviews`](uistackview/arrangedsubviews.md) array is always a subset of its [`subviews`](uiview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it isn’t already. When adding subviews, the stack view appends the view to the end of its [`subviews`](uiview/subviews.md) array. The index only affects the order of views in the [`arrangedSubviews`](uistackview/arrangedsubviews.md) array. It doesn’t affect the ordering of views in the [`subviews`](uiview/subviews.md) array.

## Parameters

- `view`: The view to add to the array of views arranged by the stack.
- `stackIndex`: The index where the stack inserts the new view in its   array. This value must not be greater than the number of views currently in this array. If the index is out of bounds, this method throws an   exception.

## See Also

- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [convenience init(arrangedSubviews: [UIView])](uistackview/init(arrangedsubviews:).md)
  Returns a new stack view object that manages the provided views.
- [func addArrangedSubview(UIView)](uistackview/addarrangedsubview(_:).md)
  Adds a view to the end of the arranged subviews array.
- [var arrangedSubviews: [UIView]](uistackview/arrangedsubviews.md)
  The list of views arranged by the stack view.
- [func removeArrangedSubview(UIView)](uistackview/removearrangedsubview(_:).md)
  Removes the provided view from the stack’s array of arranged subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/insertarrangedsubview(_:at:))*