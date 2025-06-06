# UITextInputContext

**Framework**: UIKit  
**Kind**: class

An object that reports the type of input your app receives.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
class UITextInputContext
```

#### Overview

Use the shared [`UITextInputContext`](uitextinputcontext.md) object to get information about the type of input your app receives. UIKit apps can receive text input from sources other than the software keyboard, including from dictation, Apple Pencil, and a connected keyboard. Use information about the likely input sources to adjust your UI to accommodate that input. For example, you might increase the size of text fields to accommodate handwriting input from Apple Pencil.

## Topics

### Getting the input context object
- [class func current() -> UITextInputContext!](uitextinputcontext/current.md)
  Returns the shared text-input context object.
### Getting the expected input type
- [var isDictationInputExpected: Bool](uitextinputcontext/isdictationinputexpected.md)
  Returns a Boolean value that indicates whether someone is likely to use dictation to input text to the app.
- [var isHardwareKeyboardInputExpected: Bool](uitextinputcontext/ishardwarekeyboardinputexpected.md)
  Returns a Boolean value that indicates whether someone is likely to enter text using a hardware keyboard.
- [var isPencilInputExpected: Bool](uitextinputcontext/ispencilinputexpected.md)
  Returns a Boolean value that indicates whether someone is likely to use Apple Pencil for input.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UITextInput](uitextinput.md)
  A set of methods for interacting with the text input system and enabling features in documents.
- [protocol UITextInputDelegate](uitextinputdelegate.md)
  An intermediary between a document and the text input system.
- [protocol UIKeyInput](uikeyinput.md)
  A set of methods a responder uses to implement simple text entry.
- [protocol UITextInputTraits](uitextinputtraits.md)
  A set of methods that defines features for keyboard input to a text object.
- [class UITextInputMode](uitextinputmode.md)
  The current text input mode.
- [class UITextInputAssistantItem](uitextinputassistantitem.md)
  An object that manages custom bar button items that you add to the shortcuts bar above the keyboard on iPad.
- [class UIDictationPhrase](uidictationphrase.md)
  An object that represents the textual interpretation of a spoken phrase that the user dictates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputcontext)*