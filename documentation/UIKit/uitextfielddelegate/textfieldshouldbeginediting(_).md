# textFieldShouldBeginEditing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to begin editing in the specified text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func textFieldShouldBeginEditing(_ textField: UITextField) -> Bool
```

```objc
- (BOOL) textFieldShouldBeginEditing:(UITextField *) textField;
```

#### Return Value

[`true`](../../Swift/true.md) if editing should begin or [`false`](../../Swift/false.md) if it should not.

#### Discussion

The text field calls this method when the user performs an action that would normally initiate the editing of the text field’s text. Implement this method if you want to prevent editing from happening in some situations. For example, you could use this method to prevent the user from editing the text field’s contents more than once. Most of the time, you should return [`true`](../../Swift/true.md) to allow editing to proceed.

If you do not implement this method, the text field acts as if this method had returned [`true`](../../Swift/true.md).

## Parameters

- `textField`: The text field in which editing is about to begin.

## See Also

### Managing editing
- [func textFieldDidBeginEditing(UITextField)](./textfielddidbeginediting%28_%29.md)
  Tells the delegate when editing begins in the specified text field.
- [func textFieldShouldEndEditing(UITextField) -> Bool](./textfieldshouldendediting%28_%29.md)
  Asks the delegate whether to stop editing in the specified text field.
- [func textFieldDidEndEditing(UITextField, reason: UITextField.DidEndEditingReason)](./textfielddidendediting%28_,reason%29.md)
  Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [func textFieldDidEndEditing(UITextField)](./textfielddidendediting%28_%29.md)
  Tells the delegate when editing stops for the specified text field.
- [UITextField.DidEndEditingReason](../uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldbeginediting(_:))*