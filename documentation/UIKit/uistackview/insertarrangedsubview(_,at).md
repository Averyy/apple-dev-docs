# insertArrangedSubview(_:at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds the provided view to the array of arranged subviews at the specified index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func insertArrangedSubview(_ view: UIView, at stackIndex: Int)
```

```objc
- (void) insertArrangedSubview:(UIView *) view atIndex:(NSUInteger) stackIndex;
```

#### Discussion

If index is already occupied, the stack view increases the size of the [`arrangedSubviews`](./arrangedsubviews.md) array and shifts all of its contents at the index and above to the next higher space in the array. Then the stack view stores the provided view at the index.

The stack view also ensures that the [`arrangedSubviews`](./arrangedsubviews.md) array is always a subset of its [`subviews`](../uiview/subviews.md) array. This method automatically adds the provided view as a subview of the stack view, if it isn’t already. When adding subviews, the stack view appends the view to the end of its [`subviews`](../uiview/subviews.md) array. The index only affects the order of views in the [`arrangedSubviews`](./arrangedsubviews.md) array. It doesn’t affect the ordering of views in the [`subviews`](../uiview/subviews.md) array.

## Parameters

- `view`: The view to add to the array of views arranged by the stack.
- `stackIndex`: The index where the stack inserts the new view in its [`arrangedSubviews`](./arrangedsubviews.md) array. This value must not be greater than the number of views currently in this array. If the index is out of bounds, this method throws an [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md) exception.

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
- [func removeArrangedSubview(UIView)](./removearrangedsubview%28_%29.md)
  Removes the provided view from the stack’s array of arranged subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/insertarrangedsubview(_:at:))*