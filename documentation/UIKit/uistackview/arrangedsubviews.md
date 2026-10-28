# arrangedSubviews

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The list of views arranged by the stack view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var arrangedSubviews: [UIView] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<__kindof UIView *> * arrangedSubviews;
```

## Discussion

The stack view ensures that the [`arrangedSubviews`](./arrangedsubviews.md) array is always a subset of its [`subviews`](../uiview/subviews.md) array. Therefore, whenever the [`addArrangedSubview(_:)`](./addarrangedsubview%28_%29.md) method is called, the stack view adds the view as a subview, if it isn’t already. Whenever an arranged view’s [`removeFromSuperview()`](../uiview/removefromsuperview%28%29.md) method is called, the stack view removes the view from its [`arrangedSubviews`](./arrangedsubviews.md) array.

## See Also

### Related Documentation
- [func removeFromSuperview()](../uiview/removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [convenience init(arrangedSubviews: [UIView])](./init%28arrangedsubviews%29.md)
  Returns a new stack view object that manages the provided views.
### Managing arranged subviews
- [func addArrangedSubview(UIView)](./addarrangedsubview%28_%29.md)
  Adds a view to the end of the arranged subviews array.
- [func insertArrangedSubview(UIView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeArrangedSubview(UIView)](./removearrangedsubview%28_%29.md)
  Removes the provided view from the stack’s array of arranged subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/arrangedsubviews)*