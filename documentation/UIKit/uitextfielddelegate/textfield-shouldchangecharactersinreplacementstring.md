# textField(_:shouldChangeCharactersIn:replacementString:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to change the specified text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified text range should be replaced; otherwise, [`false`](https://developer.apple.com/documentation/swift/false) to keep the old text.

#### Discussion

The text field calls this method whenever user actions cause its text to change. Use this method to validate text as it is typed by the user. For example, you could use this method to prevent the user from entering anything but numerical values.

## Parameters

- `textField`: The text field containing the text.
- `range`: The range of characters to be replaced.
- `string`: The replacement string for the specified range. During typing, this parameter normally contains only the single new character that was typed, but it may contain more characters if the user is pasting text. When the user deletes one or more characters, the replacement string is empty.

## See Also

- [func textFieldShouldClear(UITextField) -> Bool](uitextfielddelegate/textfieldshouldclear(_:).md)
  Asks the delegate whether to remove the text field’s current contents.
- [func textFieldShouldReturn(UITextField) -> Bool](uitextfielddelegate/textfieldshouldreturn(_:).md)
  Asks the delegate whether to process the pressing of the Return button for the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:shouldchangecharactersin:replacementstring:))*