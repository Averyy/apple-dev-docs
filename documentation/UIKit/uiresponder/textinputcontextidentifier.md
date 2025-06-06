# textInputContextIdentifier

**Framework**: UIKit  
**Kind**: property

An identifier signifying that the responder should preserve its text input mode information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textInputContextIdentifier: String? { get }
```

#### Discussion

If you redefine this property and return a string value, UIKit tracks the current text input mode for the responder. While in tracking mode, any programmatic changes you make to the text input mode are remembered and restored whenever the responder becomes active.

## See Also

- [var textInputMode: UITextInputMode?](uiresponder/textinputmode.md)
  The text input mode for this responder object.
- [class func clearTextInputContextIdentifier(String)](uiresponder/cleartextinputcontextidentifier(_:).md)
  Clears text input mode information from the app’s user defaults.
- [var inputAssistantItem: UITextInputAssistantItem](uiresponder/inputassistantitem.md)
  The input assistant to use when configuring the keyboard’s shortcuts bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/textinputcontextidentifier)*