# clearTextInputContextIdentifier(_:)

**Framework**: UIKit  
**Kind**: method

Clears text input mode information from the app’s user defaults.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func clearTextInputContextIdentifier(_ identifier: String)
```

#### Discussion

Calling this method removes any text input mode information associated with the specified identifier from the app’s user defaults. Removing this information causes the responder to use the default text input mode again.

## Parameters

- `identifier`: An identifier assigned to the   property of one of your responders.

## See Also

- [var textInputMode: UITextInputMode?](uiresponder/textinputmode.md)
  The text input mode for this responder object.
- [var textInputContextIdentifier: String?](uiresponder/textinputcontextidentifier.md)
  An identifier signifying that the responder should preserve its text input mode information.
- [var inputAssistantItem: UITextInputAssistantItem](uiresponder/inputassistantitem.md)
  The input assistant to use when configuring the keyboard’s shortcuts bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiresponder/cleartextinputcontextidentifier(_:))*