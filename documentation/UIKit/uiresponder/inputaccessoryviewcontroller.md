# inputAccessoryViewController

**Framework**: UIKit  
**Kind**: property

The custom input accessory view controller to display when the responder becomes the first responder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var inputAccessoryViewController: UIInputViewController? { get }
```

#### Discussion

This property is typically used to attach an accessory view controller to the system-supplied keyboard that’s presented for [`UITextField`](uitextfield.md) and [`UITextView`](uitextview.md) objects.

The value of this read-only property is `nil`. If you want to attach custom controls to a system-supplied input view controller (such as the system keyboard) or to a custom input view (one you provide in the [`inputViewController`](uiresponder/inputviewcontroller.md) property), redeclare this property as read-write in a [`UIResponder`](uiresponder.md) subclass. You can then use this property to manage a custom accessory view. When the responder becomes the first responder, the responder infrastructure attaches the accessory view to the appropriate input view before displaying it.

## See Also

- [var inputView: UIView?](uiresponder/inputview.md)
  The custom input view to display when the responder becomes the first responder.
- [var inputViewController: UIInputViewController?](uiresponder/inputviewcontroller.md)
  The custom input view controller to use when the responder becomes the first responder.
- [var inputAccessoryView: UIView?](uiresponder/inputaccessoryview.md)
  The custom input accessory view to display when the responder becomes the first responder.
- [func reloadInputViews()](uiresponder/reloadinputviews.md)
  Updates the custom input and accessory views when the object is the first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/inputaccessoryviewcontroller)*