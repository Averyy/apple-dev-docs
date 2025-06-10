# UITextInputMode

**Framework**: UIKit  
**Kind**: class

The current text input mode.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextInputMode
```

#### Overview

You can use this object to determine the primary language currently being used for text input.

## Topics

### Getting the current and active text-input modes
- [class var activeInputModes: [UITextInputMode]](uitextinputmode/activeinputmodes.md)
  The active text-input modes.
### Getting the primary language
- [var primaryLanguage: String?](uitextinputmode/primarylanguage.md)
  The primary language, if any, of the input mode.
### Notifications
- [class let currentInputModeDidChangeNotification: NSNotification.Name](uitextinputmode/currentinputmodedidchangenotification.md)
  A notification that posts when the current input mode changes.
### Structures
- [UITextInputMode.CurrentInputModeDidChangeMessage](uitextinputmode/currentinputmodedidchangemessage.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UITextInput](uitextinput.md)
  A set of methods for interacting with the text input system and enabling features in documents.
- [protocol UITextInputDelegate](uitextinputdelegate.md)
  An intermediary between a document and the text input system.
- [protocol UIKeyInput](uikeyinput.md)
  A set of methods a responder uses to implement simple text entry.
- [protocol UITextInputTraits](uitextinputtraits.md)
  A set of methods that defines features for keyboard input to a text object.
- [class UITextInputContext](uitextinputcontext.md)
  An object that reports the type of input your app receives.
- [class UITextInputAssistantItem](uitextinputassistantitem.md)
  An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [class UIDictationPhrase](uidictationphrase.md)
  An object that represents the textual interpretation of a spoken phrase that the user dictates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputmode)*