# textFieldDidBeginEditing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when editing begins in the specified text field.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func textFieldDidBeginEditing(_ textField: UITextField)
```

```objc
- (void) textFieldDidBeginEditing:(UITextField *) textField;
```

#### Discussion

This method notifies the delegate that the specified text field just became the first responder. Use this method to update state information or perform other tasks. For example, you might use this method to show overlay views that are visible only while editing.

Implementation of this method by the delegate is optional.

## Parameters

- `textField`: The text field in which an editing session began.

## See Also

### Managing editing
- [func textFieldShouldBeginEditing(UITextField) -> Bool](./textfieldshouldbeginediting%28_%29.md)
  Asks the delegate whether to begin editing in the specified text field.
- [func textFieldShouldEndEditing(UITextField) -> Bool](./textfieldshouldendediting%28_%29.md)
  Asks the delegate whether to stop editing in the specified text field.
- [func textFieldDidEndEditing(UITextField, reason: UITextField.DidEndEditingReason)](./textfielddidendediting%28_,reason%29.md)
  Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [func textFieldDidEndEditing(UITextField)](./textfielddidendediting%28_%29.md)
  Tells the delegate when editing stops for the specified text field.
- [UITextField.DidEndEditingReason](../uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfielddidbeginediting(_:))*