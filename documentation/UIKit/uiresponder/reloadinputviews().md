# reloadInputViews()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the custom input and accessory views when the object is the first responder.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func reloadInputViews()
```

```objc
- (void) reloadInputViews;
```

## Discussion

You can use this method to refresh the custom input view or input accessory view associated with the current object when it’s the first responder. The views are replaced immediately, without animating them into place. If the current object isn’t the first responder, this method has no effect.

## See Also

### Managing input views
- [var inputView: UIView?](./inputview.md)
  The custom input view to display when the responder becomes the first responder.
- [var inputViewController: UIInputViewController?](./inputviewcontroller.md)
  The custom input view controller to use when the responder becomes the first responder.
- [var inputAccessoryView: UIView?](./inputaccessoryview.md)
  The custom input accessory view to display when the responder becomes the first responder.
- [var inputAccessoryViewController: UIInputViewController?](./inputaccessoryviewcontroller.md)
  The custom input accessory view controller to display when the responder becomes the first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/reloadinputviews())*