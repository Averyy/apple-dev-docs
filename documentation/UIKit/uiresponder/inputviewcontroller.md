# inputViewController

**Framework**: UIKit  
**Kind**: property

The custom input view controller to use when the responder becomes the first responder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var inputViewController: UIInputViewController? { get }
```

#### Discussion

This property is typically used to provide a view controller to replace the system-supplied keyboard that’s presented for [`UITextField`](uitextfield.md) and [`UITextView`](uitextview.md) objects.

The value of this read-only property is `nil`. If you want to provide a custom input view controller to replace the system keyboard in your app, redeclare this property as read-write in a [`UIResponder`](uiresponder.md) subclass. You can then use this property to manage a custom input view controller. When the responder becomes the first responder, the responder infrastructure presents the specified input view controller automatically. Similarly, when the responder resigns its first responder status, the responder infrastructure automatically dismisses the specified input view controller.

## See Also

- [var inputView: UIView?](uiresponder/inputview.md)
  The custom input view to display when the responder becomes the first responder.
- [var inputAccessoryView: UIView?](uiresponder/inputaccessoryview.md)
  The custom input accessory view to display when the responder becomes the first responder.
- [var inputAccessoryViewController: UIInputViewController?](uiresponder/inputaccessoryviewcontroller.md)
  The custom input accessory view controller to display when the responder becomes the first responder.
- [func reloadInputViews()](uiresponder/reloadinputviews.md)
  Updates the custom input and accessory views when the object is the first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/inputviewcontroller)*