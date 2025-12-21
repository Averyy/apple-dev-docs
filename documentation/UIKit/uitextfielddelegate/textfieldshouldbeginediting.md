# textFieldShouldBeginEditing(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to begin editing in the specified text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textFieldShouldBeginEditing(_ textField: UITextField) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if editing should begin or [`false`](https://developer.apple.com/documentation/Swift/false) if it should not.

#### Discussion

The text field calls this method when the user performs an action that would normally initiate the editing of the text field’s text. Implement this method if you want to prevent editing from happening in some situations. For example, you could use this method to prevent the user from editing the text field’s contents more than once. Most of the time, you should return [`true`](https://developer.apple.com/documentation/Swift/true) to allow editing to proceed.

If you do not implement this method, the text field acts as if this method had returned [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `textField`: The text field in which editing is about to begin.

## See Also

- [func textFieldDidBeginEditing(UITextField)](uitextfielddelegate/textfielddidbeginediting(_:).md)
  Tells the delegate when editing begins in the specified text field.
- [func textFieldShouldEndEditing(UITextField) -> Bool](uitextfielddelegate/textfieldshouldendediting(_:).md)
  Asks the delegate whether to stop editing in the specified text field.
- [func textFieldDidEndEditing(UITextField, reason: UITextField.DidEndEditingReason)](uitextfielddelegate/textfielddidendediting(_:reason:).md)
  Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [func textFieldDidEndEditing(UITextField)](uitextfielddelegate/textfielddidendediting(_:).md)
  Tells the delegate when editing stops for the specified text field.
- [UITextField.DidEndEditingReason](uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldbeginediting(_:))*