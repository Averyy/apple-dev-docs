# UITextFieldDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of optional methods to manage editing and validating text in a text field object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITextFieldDelegate : NSObjectProtocol
```

#### Overview

A text field calls the methods of its delegate in response to important changes. You use these methods to validate text that was typed by the user, to respond to specific interactions with the keyboard, and to control the overall editing process. Editing begins shortly before the text field becomes the first responder and displays the keyboard (or its assigned input view). The flow of the editing process is as follows:

1. Before becoming the first responder, the text field calls its delegate’s [`textFieldShouldBeginEditing(_:)`](uitextfielddelegate/textfieldshouldbeginediting(_:).md) method. Use that method to allow or prevent the editing of the text field’s contents.
2. The text field becomes the first responder.

In response, the system displays the keyboard (or the text field’s input view) and posts the [`keyboardWillShowNotification`](uiresponder/keyboardwillshownotification.md) and [`keyboardDidShowNotification`](uiresponder/keyboarddidshownotification.md) notifications as needed. If the keyboard or another input view was already visible, the system posts the [`keyboardWillChangeFrameNotification`](uiresponder/keyboardwillchangeframenotification.md) and [`keyboardDidChangeFrameNotification`](uiresponder/keyboarddidchangeframenotification.md) notifications instead. 3. The text field calls its delegate’s [`textFieldDidBeginEditing(_:)`](uitextfielddelegate/textfielddidbeginediting(_:).md) method and posts a [`textDidBeginEditingNotification`](uitextfield/textdidbegineditingnotification.md) notification. 4. The text field calls various delegate methods during editing:

- Whenever the current text changes, it calls the [`textField(_:shouldChangeCharactersIn:replacementString:)`](uitextfielddelegate/textfield(_:shouldchangecharactersin:replacementstring:).md) method and posts the [`textDidChangeNotification`](uitextfield/textdidchangenotification.md) notification.
- It calls the [`textFieldShouldClear(_:)`](uitextfielddelegate/textfieldshouldclear(_:).md) method when the user taps the built-in button to clear the text.
- It calls the [`textFieldShouldReturn(_:)`](uitextfielddelegate/textfieldshouldreturn(_:).md) method when the user taps the keyboard’s return button.

1. Before resigning as first responder, the text field calls its delegate’s [`textFieldShouldEndEditing(_:)`](uitextfielddelegate/textfieldshouldendediting(_:).md) method. Use that method to validate the current text.
2. The text field resigns as first responder.

In response, the system hides or adjusts the keyboard as needed. When hiding the keyboard, the system posts the [`keyboardWillHideNotification`](uiresponder/keyboardwillhidenotification.md) and [`keyboardDidHideNotification`](uiresponder/keyboarddidhidenotification.md) notifications. 7. The text field calls its delegate’s [`textFieldDidEndEditing(_:)`](uitextfielddelegate/textfielddidendediting(_:).md) method and posts a [`textDidEndEditingNotification`](uitextfield/textdidendeditingnotification.md) notification.

For more information about the features of a text field, see [`UITextField`](uitextfield.md).

## Topics

### Managing editing
- [func textFieldShouldBeginEditing(UITextField) -> Bool](uitextfielddelegate/textfieldshouldbeginediting(_:).md)
  Asks the delegate whether to begin editing in the specified text field.
- [func textFieldDidBeginEditing(UITextField)](uitextfielddelegate/textfielddidbeginediting(_:).md)
  Tells the delegate when editing begins in the specified text field.
- [func textFieldShouldEndEditing(UITextField) -> Bool](uitextfielddelegate/textfieldshouldendediting(_:).md)
  Asks the delegate whether to stop editing in the specified text field.
- [func textFieldDidEndEditing(UITextField, reason: UITextField.DidEndEditingReason)](uitextfielddelegate/textfielddidendediting(_:reason:).md)
  Tells the delegate when editing stops for the specified text field, and the reason it stopped.
- [func textFieldDidEndEditing(UITextField)](uitextfielddelegate/textfielddidendediting(_:).md)
  Tells the delegate when editing stops for the specified text field.
- [UITextField.DidEndEditingReason](uitextfield/didendeditingreason.md)
  Constants that indicate the reason for ending editing in a text field.
### Editing the text field’s text
- [func textField(UITextField, shouldChangeCharactersIn: NSRange, replacementString: String) -> Bool](uitextfielddelegate/textfield(_:shouldchangecharactersin:replacementstring:).md)
  Asks the delegate whether to change the specified text.
- [func textFieldShouldClear(UITextField) -> Bool](uitextfielddelegate/textfieldshouldclear(_:).md)
  Asks the delegate whether to remove the text field’s current contents.
- [func textFieldShouldReturn(UITextField) -> Bool](uitextfielddelegate/textfieldshouldreturn(_:).md)
  Asks the delegate whether to process the pressing of the Return button for the text field.
### Managing text selection
- [func textFieldDidChangeSelection(UITextField)](uitextfielddelegate/textfielddidchangeselection(_:).md)
  Tells the delegate when the text selection changes in the specified text field.
### Providing a context menu
- [func textField(UITextField, editMenuForCharactersIn: NSRange, suggestedActions: [UIMenuElement]) -> UIMenu?](uitextfielddelegate/textfield(_:editmenuforcharactersin:suggestedactions:).md)
  Asks the delegate for the menu to display in the text field, based on the text range and actions the system provides.
### Customizing an edit menu
- [func textField(UITextField, willPresentEditMenuWith: any UIEditMenuInteractionAnimating)](uitextfielddelegate/textfield(_:willpresenteditmenuwith:).md)
  Tells the delegate that the system is about to present an edit menu with an animator.
- [func textField(UITextField, willDismissEditMenuWith: any UIEditMenuInteractionAnimating)](uitextfielddelegate/textfield(_:willdismisseditmenuwith:).md)
  Tells the delegate that the system is about to dismiss an edit menu with an animator.
### Inserting a Smart Reply suggestion
- [func textField(UITextField, insertInputSuggestion: UIInputSuggestion)](uitextfielddelegate/textfield(_:insertinputsuggestion:).md)
  Tells the delegate when the keyboard delivers an input suggestion.
### Instance Methods
- [func textField(UITextField, editMenuForCharactersInRanges: [NSValue], suggestedActions: [UIMenuElement]) -> UIMenu?](uitextfielddelegate/textfield(_:editmenuforcharactersinranges:suggestedactions:).md)
- [func textField(UITextField, shouldChangeCharactersInRanges: [NSValue], replacementString: String) -> Bool](uitextfielddelegate/textfield(_:shouldchangecharactersinranges:replacementstring:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UISearchTextFieldDelegate](uisearchtextfielddelegate.md)

## See Also

- [var delegate: (any UITextFieldDelegate)?](uitextfield/delegate.md)
  The text field’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextfielddelegate)*