# init(arrangedSubviews:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Returns a new stack view object that manages the provided views.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(arrangedSubviews views: [UIView])
```

```objc
- (instancetype) initWithArrangedSubviews:(NSArray<__kindof UIView *> *) views;
```

## Return Value

A new stack view object. This stack view contains and lays out the provided views in a single stack. You can modify the orientation or appearance of this stack, using the stack view’s properties.

## Discussion

The stack view adds all the arranged views to its [`arrangedSubviews`](./arrangedsubviews.md) array. It also adds these views as subviews. If any view contained in the `arrangedSubviews` array receives a [`removeFromSuperview()`](../uiview/removefromsuperview%28%29.md) method call, the stack view also removes it from the `arrangedSubviews`.

## Parameters

- `views`: The views to be arranged by the stack view.

## See Also

### Related Documentation
- [func insertArrangedSubview(UIView, at: Int)](./insertarrangedsubview%28_,at%29.md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeFromSuperview()](../uiview/removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [var arrangedSubviews: [UIView]](./arrangedsubviews.md)
  The list of views arranged by the stack view.
- [func addArrangedSubview(UIView)](./addarrangedsubview%28_%29.md)
  Adds a view to the end of the arranged subviews array.
- [func removeArrangedSubview(UIView)](./removearrangedsubview%28_%29.md)
  Removes the provided view from the stack’s array of arranged subviews.
### Initializing a stack view
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates a stack view with the specified frame.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a stack view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/init(arrangedsubviews:))*