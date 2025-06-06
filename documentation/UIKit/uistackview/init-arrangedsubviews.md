# init(arrangedSubviews:)

**Framework**: UIKit  
**Kind**: init

Returns a new stack view object that manages the provided views.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(arrangedSubviews views: [UIView])
```

#### Return Value

A new stack view object. This stack view contains and lays out the provided views in a single stack. You can modify the orientation or appearance of this stack, using the stack view’s properties.

#### Discussion

The stack view adds all the arranged views to its [`arrangedSubviews`](uistackview/arrangedsubviews.md) array. It also adds these views as subviews. If any view contained in the `arrangedSubviews` array receives a [`removeFromSuperview()`](uiview/removefromsuperview().md) method call, the stack view also removes it from the `arrangedSubviews`.

## Parameters

- `views`: The views to be arranged by the stack view.

## See Also

- [func insertArrangedSubview(UIView, at: Int)](uistackview/insertarrangedsubview(_:at:).md)
  Adds the provided view to the array of arranged subviews at the specified index.
- [func removeFromSuperview()](uiview/removefromsuperview.md)
  Unlinks the view from its superview and its window, and removes it from the responder chain.
- [var arrangedSubviews: [UIView]](uistackview/arrangedsubviews.md)
  The list of views arranged by the stack view.
- [func addArrangedSubview(UIView)](uistackview/addarrangedsubview(_:).md)
  Adds a view to the end of the arranged subviews array.
- [func removeArrangedSubview(UIView)](uistackview/removearrangedsubview(_:).md)
  Removes the provided view from the stack’s array of arranged subviews.
- [init(frame: CGRect)](uistackview/init(frame:).md)
  Creates a stack view with the specified frame.
- [init(coder: NSCoder)](uistackview/init(coder:).md)
  Creates a stack view from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uistackview/init(arrangedsubviews:))*