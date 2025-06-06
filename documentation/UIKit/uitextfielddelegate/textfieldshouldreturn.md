# textFieldShouldReturn(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to process the pressing of the Return button for the text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func textFieldShouldReturn(_ textField: UITextField) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the text field should implement its default behavior for the return button; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The text field calls this method whenever the user taps the return button. You can use this method to implement any custom behavior when the button is tapped. For example, if you want to dismiss the keyboard when the user taps the return button, your implementation can call the [`resignFirstResponder()`](uiresponder/resignfirstresponder().md) method.

## Parameters

- `textField`: The text field whose return button was pressed.

## See Also

- [func textField(UITextField, shouldChangeCharactersIn: NSRange, replacementString: String) -> Bool](uitextfielddelegate/textfield(_:shouldchangecharactersin:replacementstring:).md)
  Asks the delegate whether to change the specified text.
- [func textFieldShouldClear(UITextField) -> Bool](uitextfielddelegate/textfieldshouldclear(_:).md)
  Asks the delegate whether to remove the text field’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldreturn(_:))*