# textFieldShouldReturn(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to process the pressing of the Return button for the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func textFieldShouldReturn(_ textField: UITextField) -> Bool
```

```objc
- (BOOL) textFieldShouldReturn:(UITextField *) textField;
```

## Return Value

[`true`](../../Swift/true.md) if the text field should implement its default behavior for the return button; otherwise, [`false`](../../Swift/false.md).

## Discussion

The text field calls this method whenever the user taps the return button. You can use this method to implement any custom behavior when the button is tapped. For example, if you want to dismiss the keyboard when the user taps the return button, your implementation can call the [`resignFirstResponder()`](../uiresponder/resignfirstresponder%28%29.md) method.

## Parameters

- `textField`: The text field whose return button was pressed.

## See Also

### Editing the text field’s text
- [func textFieldShouldClear(UITextField) -> Bool](./textfieldshouldclear%28_%29.md)
  Asks the delegate whether to remove the text field’s current contents.
- [func textField(UITextField, shouldChangeCharactersIn: NSRange, replacementString: String) -> Bool](./textfield%28_,shouldchangecharactersin,replacementstring%29.md)
  Asks the delegate whether to change the specified text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldreturn(_:))*