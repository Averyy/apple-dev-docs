# textFieldShouldEndEditing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether to stop editing in the specified text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func textFieldShouldEndEditing(_ textField: UITextField) -> Bool
```

```objc
- (BOOL) textFieldShouldEndEditing:(UITextField *) textField;
```

#### Return Value

[`true`](../../Swift/true.md) if editing should stop or [`false`](../../Swift/false.md) if it should continue.

#### Discussion

The text field calls this method when it is asked to resign the first responder status. This can happen when the user selects another control or when you call the text field’s [`resignFirstResponder()`](../uiresponder/resignfirstresponder%28%29.md) method. Before the focus change occurs, however, the text field calls this method and gives you a chance to prevent the change from happening.

Normally, you would return [`true`](../../Swift/true.md) from this method to allow the text field to resign the first responder status. You might return [`false`](../../Swift/false.md), however, in cases where your delegate detects invalid contents in the text field. Returning [`false`](../../Swift/false.md) prevents the user from switching to another control until the text field contains a valid value.

> **Note**:  If you use this method to validate the contents of the text field, you might also want to use an overlay view to provide feedback to that effect. For example, you might display a small icon indicating the text is invalid. For more information about adding overlays to text fields, see the methods of [`UITextField`](../uitextfield.md).

Be aware that this method provides only a recommendation about whether editing should end. Even if you return [`false`](../../Swift/false.md), UIKit might still force an end to editing. For example, text fields always resign the first responder status when they are removed from their parent view or window.

Implementation of this method by the delegate is optional. If you do not implement this method, the text field resigns the first responder status as if this method had returned [`true`](../../Swift/true.md).

## Parameters

- `textField`: The text field in which editing is about to end.

## See Also

### Managing editing
- [func textFieldShouldBeginEditing(UITextField) -> Bool](./textfieldshouldbeginediting%28_%29.md)
  Asks the delegate whether to begin editing in the specified text field.
- [func textFieldDidBeginEditing(UITextField)](./textfielddidbeginediting%28_%29.md)
  Tells the delegate when editing begins in the specified text field.
- [func textFieldDidEndEditing(UITextField, reason: UITextField.DidEndEditingReason)](./textfielddidendediting%28_,reason%29.md)
  Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [func textFieldDidEndEditing(UITextField)](./textfielddidendediting%28_%29.md)
  Tells the delegate when editing stops for the specified text field.
- [UITextField.DidEndEditingReason](../uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfieldshouldendediting(_:))*