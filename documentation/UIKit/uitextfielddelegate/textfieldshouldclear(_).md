# textFieldShouldClear(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to remove the text field’s current contents.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func textFieldShouldClear(_ textField: UITextField) -> Bool
```

```objc
- (BOOL) textFieldShouldClear:(UITextField *) textField;
```

#### Return Value

[`true`](../../Swift/true.md) if the text field’s contents should be cleared; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The text field calls this method in response to the user pressing the built-in clear button. (This button is not shown by default but can be enabled by changing the value in the [`clearButtonMode`](../uitextfield/clearbuttonmode.md) property of the text field.) This method is also called when editing begins and the [`clearsOnBeginEditing`](../uitextfield/clearsonbeginediting.md) property of the text field is set to [`true`](../../Swift/true.md).

If you do not implement this method, the text field clears the text as if the method had returned [`true`](../../Swift/true.md).

## Parameters

- `textField`: The text field containing the text.

## See Also

### Editing the text field’s text
- [func textFieldShouldReturn(UITextField) -> Bool](./textfieldshouldreturn%28_%29.md)
  Asks the delegate whether to process the pressing of the Return button for the text field.
- [func textField(UITextField, shouldChangeCharactersIn: NSRange, replacementString: String) -> Bool](./textfield%28_,shouldchangecharactersin,replacementstring%29.md)
  Asks the delegate whether to change the specified text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldclear(_:))*