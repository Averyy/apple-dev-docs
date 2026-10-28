# textFieldDidEndEditing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when editing stops for the specified text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func textFieldDidEndEditing(_ textField: UITextField)
```

```objc
- (void) textFieldDidEndEditing:(UITextField *) textField;
```

## Discussion

This method is called after the text field resigns its first responder status. You can use this method to update your delegate’s state information. For example, you might use this method to hide overlay views that should be visible only while editing.

Implementation of this method by the delegate is optional. If your delegate also implements the [`textFieldDidEndEditing(_:reason:)`](./textfielddidendediting%28_,reason%29.md) method, UIKit calls that method in preference to this one.

## Parameters

- `textField`: The text field for which editing ended.

## See Also

### Managing editing
- [func textFieldShouldBeginEditing(UITextField) -> Bool](./textfieldshouldbeginediting%28_%29.md)
  Asks the delegate whether to begin editing in the specified text field.
- [func textFieldDidBeginEditing(UITextField)](./textfielddidbeginediting%28_%29.md)
  Tells the delegate when editing begins in the specified text field.
- [func textFieldShouldEndEditing(UITextField) -> Bool](./textfieldshouldendediting%28_%29.md)
  Asks the delegate whether to stop editing in the specified text field.
- [func textFieldDidEndEditing(UITextField, reason: UITextField.DidEndEditingReason)](./textfielddidendediting%28_,reason%29.md)
  Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [UITextField.DidEndEditingReason](../uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfielddidendediting(_:))*