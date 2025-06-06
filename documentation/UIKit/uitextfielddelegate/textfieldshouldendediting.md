# textFieldShouldEndEditing(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to stop editing in the specified text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textFieldShouldEndEditing(_ textField: UITextField) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if editing should stop or [`false`](https://developer.apple.com/documentation/swift/false) if it should continue.

#### Discussion

The text field calls this method when it is asked to resign the first responder status. This can happen when the user selects another control or when you call the text field’s [`resignFirstResponder()`](uiresponder/resignfirstresponder().md) method. Before the focus change occurs, however, the text field calls this method and gives you a chance to prevent the change from happening.

Normally, you would return [`true`](https://developer.apple.com/documentation/swift/true) from this method to allow the text field to resign the first responder status. You might return [`false`](https://developer.apple.com/documentation/swift/false), however, in cases where your delegate detects invalid contents in the text field. Returning [`false`](https://developer.apple.com/documentation/swift/false) prevents the user from switching to another control until the text field contains a valid value.

> **Note**:  If you use this method to validate the contents of the text field, you might also want to use an overlay view to provide feedback to that effect. For example, you might display a small icon indicating the text is invalid. For more information about adding overlays to text fields, see the methods of [`UITextField`](uitextfield.md).

 If you use this method to validate the contents of the text field, you might also want to use an overlay view to provide feedback to that effect. For example, you might display a small icon indicating the text is invalid. For more information about adding overlays to text fields, see the methods of [`UITextField`](uitextfield.md).

Be aware that this method provides only a recommendation about whether editing should end. Even if you return [`false`](https://developer.apple.com/documentation/swift/false), UIKit might still force an end to editing. For example, text fields always resign the first responder status when they are removed from their parent view or window.

Implementation of this method by the delegate is optional. If you do not implement this method, the text field resigns the first responder status as if this method had returned [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `textField`: The text field in which editing is about to end.

## See Also

- [func textFieldShouldBeginEditing(UITextField) -> Bool](uitextfielddelegate/textfieldshouldbeginediting(_:).md)
  Asks the delegate whether to begin editing in the specified text field.
- [func textFieldDidBeginEditing(UITextField)](uitextfielddelegate/textfielddidbeginediting(_:).md)
  Tells the delegate when editing begins in the specified text field.
- [func textFieldDidEndEditing(UITextField, reason: UITextField.DidEndEditingReason)](uitextfielddelegate/textfielddidendediting(_:reason:).md)
  Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [func textFieldDidEndEditing(UITextField)](uitextfielddelegate/textfielddidendediting(_:).md)
  Tells the delegate when editing stops for the specified text field.
- [UITextField.DidEndEditingReason](uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldendediting(_:))*