# conversationContext

**Framework**: UIKit  
**Kind**: property

A reference to a conversation, such as a mail or messaging thread.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
@MainActor
optional var conversationContext: UIConversationContext? { get set }
```

## Mentions

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)

#### Discussion

Set this conversation context before the keyboard appears; the keyboard uses this context to initialize its conversation context value. When updates occur in the conversation, call [`conversationContext(_:didChange:)`](uitextinputdelegate/conversationcontext(_:didchange:).md) on the `inputDelegate` property for [`UITextInput`](uitextinput.md) objects, such as UITextView/inputDelegate`or`UITextField/inputDelegate``.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputtraits/conversationcontext)*