# textField(_:shouldChangeCharactersIn:replacementString:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to change the specified text.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

## Declaration

```swift
optional func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool
```

```objc
- (BOOL) textField:(UITextField *) textField shouldChangeCharactersInRange:(NSRange) range replacementString:(NSString *) string;
```

## Return Value

[`true`](../../Swift/true.md) if the specified text range should be replaced; otherwise, [`false`](../../Swift/false.md) to keep the old text.

## Discussion

The text field calls this method whenever user actions cause its text to change. Use this method to validate text as it is typed by the user. For example, you could use this method to prevent the user from entering anything but numerical values.

## Parameters

- `textField`: The text field containing the text.
- `range`: The range of characters to be replaced.
- `string`: The replacement string for the specified range. During typing, this parameter normally contains only the single new character that was typed, but it may contain more characters if the user is pasting text. When the user deletes one or more characters, the replacement string is empty.

## See Also

### Editing the text field’s text
- [func textFieldShouldClear(UITextField) -> Bool](./textfieldshouldclear%28_%29.md)
  Asks the delegate whether to remove the text field’s current contents.
- [func textFieldShouldReturn(UITextField) -> Bool](./textfieldshouldreturn%28_%29.md)
  Asks the delegate whether to process the pressing of the Return button for the text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:shouldchangecharactersin:replacementstring:))*