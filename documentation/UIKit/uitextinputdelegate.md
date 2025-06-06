# UITextInputDelegate

**Framework**: UIKit  
**Kind**: protocol

An intermediary between a document and the text input system.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITextInputDelegate : NSObjectProtocol
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)

#### Overview

A [`UITextInputDelegate`](uitextinputdelegate.md) conveys notifications of pending or transpired changes in text and selection in the document. UIKit provides a private text input delegate, which it assigns at runtime to the [`inputDelegate`](uitextinput/inputdelegate.md) property of the object whose class adopts the [`UITextInput`](uitextinput.md) protocol.

## Topics

### Notifying the delegate of textual changes
- [func textWillChange((any UITextInput)?)](uitextinputdelegate/textwillchange(_:).md)
  Tells the input delegate when text is about to change in the document.
- [func textDidChange((any UITextInput)?)](uitextinputdelegate/textdidchange(_:).md)
  Tells the input delegate when text has changed in the document.
### Notifying the delegate of selection changes
- [func selectionWillChange((any UITextInput)?)](uitextinputdelegate/selectionwillchange(_:).md)
  Tells the input delegate when the selection is about to change in the document.
- [func selectionDidChange((any UITextInput)?)](uitextinputdelegate/selectiondidchange(_:).md)
  Tells the input delegate when the selection has changed in the document.
### Notifying the delegate of conversation changes
- [func conversationContext(UIConversationContext?, didChange: (any UITextInput)?)](uitextinputdelegate/conversationcontext(_:didchange:).md)
  Tells the input delegate when text has changed in the input object for a conversation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIInputViewController](uiinputviewcontroller.md)

## See Also

- [protocol UITextInput](uitextinput.md)
  A set of methods for interacting with the text input system and enabling features in documents.
- [protocol UIKeyInput](uikeyinput.md)
  A set of methods a responder uses to implement simple text entry.
- [protocol UITextInputTraits](uitextinputtraits.md)
  A set of methods that defines features for keyboard input to a text object.
- [class UITextInputContext](uitextinputcontext.md)
  An object that reports the type of input your app receives.
- [class UITextInputMode](uitextinputmode.md)
  The current text input mode.
- [class UITextInputAssistantItem](uitextinputassistantitem.md)
  An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [class UIDictationPhrase](uidictationphrase.md)
  An object that represents the textual interpretation of a spoken phrase that the user dictates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate)*