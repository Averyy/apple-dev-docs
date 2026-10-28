# removeArrangedSubview(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Removes the provided view from the stack’s array of arranged subviews.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeArrangedSubview(_ view: UIView)
```

```objc
- (void) removeArrangedSubview:(UIView *) view;
```

## Discussion

This method removes the provided view from the stack’s [`arrangedSubviews`](./arrangedsubviews.md) array. The stack view no longer manages the view’s position and size. However, this method doesn’t remove the provided view from the stack’s [`subviews`](../uiview/subviews.md) array; therefore, the view is still displayed as part of the view hierarchy.

To prevent the view from appearing on screen after calling the stack’s [`removeArrangedSubview(_:)`](./removearrangedsubview%28_%29.md) method, explicitly remove the view from the subviews array by calling the view’s [`removeFromSuperview()`](../uiview/removefromsuperview%28%29.md) method, or set the view’s [`isHidden`](../uiview/ishidden.md) property to [`true`](../../Swift/true.md).

## Parameters

- `view`: The view to be removed from the array of views arranged by the stack.

## See Also

### Related Documentation
- [func removeFromSuperview()](../uiview/removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [convenience init(arrangedSubviews: [UIView])](./init%28arrangedsubviews%29.md)
  Returns a new stack view object that manages the provided views.
### Managing arranged subviews
- [func addArrangedSubview(UIView)](./addarrangedsubview%28_%29.md)
  Adds a view to the end of the arranged subviews array.
- [var arrangedSubviews: [UIView]](./arrangedsubviews.md)
  The list of views arranged by the stack view.
- [func insertArrangedSubview(UIView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds the provided view to the array of arranged subviews at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/removearrangedsubview(_:))*