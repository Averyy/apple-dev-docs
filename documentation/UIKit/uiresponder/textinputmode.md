# textInputMode

**Framework**: UIKit  
**Kind**: property

The text input mode for this responder object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textInputMode: UITextInputMode? { get }
```

#### Discussion

The text input mode identifies the language and keyboard displayed when this responder is active.

For responders, the system normally displays a keyboard that’s based on the user’s language preferences. You can redefine this property and use it to return a different text input mode in cases where you want a responder to use a specific keyboard. The user can still change the keyboard while the responder is active, but switching away to another responder and then back restores the keyboard you specified.

## See Also

- [var textInputContextIdentifier: String?](uiresponder/textinputcontextidentifier.md)
  An identifier signifying that the responder should preserve its text input mode information.
- [class func clearTextInputContextIdentifier(String)](uiresponder/cleartextinputcontextidentifier(_:).md)
  Clears text input mode information from the app’s user defaults.
- [var inputAssistantItem: UITextInputAssistantItem](uiresponder/inputassistantitem.md)
  The input assistant to use when configuring the keyboard’s shortcuts bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/textinputmode)*