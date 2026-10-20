# addArrangedSubview(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds a view to the end of the arranged subviews array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func addArrangedSubview(_ view: UIView)
```

```objc
- (void) addArrangedSubview:(UIView *) view;
```

#### Discussion

The stack view ensures that the [`arrangedSubviews`](./arrangedsubviews.md) array is always a subset of its [`subviews`](../uiview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it isn’t already. If the view is already a subview, this operation doesn’t alter the subview ordering.

## Parameters

- `view`: The view to add to the array of views arranged by the stack.

## See Also

### Related Documentation
- [func removeFromSuperview()](../uiview/removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [convenience init(arrangedSubviews: [UIView])](./init%28arrangedsubviews%29.md)
  Returns a new stack view object that manages the provided views.
### Managing arranged subviews
- [var arrangedSubviews: [UIView]](./arrangedsubviews.md)
  The list of views arranged by the stack view.
- [func insertArrangedSubview(UIView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(UIView)](./removearrangedsubview%28_%29.md)
  Removes the provided view from the stack’s array of arranged subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/addarrangedsubview(_:))*