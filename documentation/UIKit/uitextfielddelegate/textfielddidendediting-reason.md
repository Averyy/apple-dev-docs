# textFieldDidEndEditing(_:reason:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate when editing stops for the specified text field, and the reason it stopped.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textFieldDidEndEditing(_ textField: UITextField, reason: UITextField.DidEndEditingReason)
```

#### Discussion

This method is called after the text field resigns its first responder status. You can use this method to update your delegate’s state information. For example, you might use this method to hide overlay views that should be visible only while editing.

Implementation of this method by the delegate is optional. UIKit calls this method in preference to the [`textFieldDidEndEditing(_:)`](uitextfielddelegate/textfielddidendediting(_:).md) method.

## Parameters

- `textField`: The text field for which editing ended.
- `reason`: The reason why editing ended. Use this field to determine whether to incorporate the text editing changes or abandon them.

## See Also

- [func textFieldShouldBeginEditing(UITextField) -> Bool](uitextfielddelegate/textfieldshouldbeginediting(_:).md)
  Asks the delegate whether to begin editing in the specified text field.
- [func textFieldDidBeginEditing(UITextField)](uitextfielddelegate/textfielddidbeginediting(_:).md)
  Tells the delegate when editing begins in the specified text field.
- [func textFieldShouldEndEditing(UITextField) -> Bool](uitextfielddelegate/textfieldshouldendediting(_:).md)
  Asks the delegate whether to stop editing in the specified text field.
- [func textFieldDidEndEditing(UITextField)](uitextfielddelegate/textfielddidendediting(_:).md)
  Tells the delegate when editing stops for the specified text field.
- [UITextField.DidEndEditingReason](uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfielddidendediting(_:reason:))*