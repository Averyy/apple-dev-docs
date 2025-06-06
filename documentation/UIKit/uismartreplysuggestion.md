# UISmartReplySuggestion

**Framework**: UIKit  
**Kind**: class

A class you use to handle a Smart Reply suggestion.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class UISmartReplySuggestion
```

#### Overview

Use the [`smartReply`](uismartreplysuggestion/smartreply.md) string as a signal of the user’s intention when you generate long form text based on the option the user selected.

## Topics

### Getting the Smart Reply
- [var smartReply: String](uismartreplysuggestion/smartreply.md)
  A string from the Smart Reply option the user selected.

## Relationships

### Inherits From
- [UIInputSuggestion](uiinputsuggestion.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)
  Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [class UIConversationContext](uiconversationcontext.md)
  A base class that represents a conversation between participants, such as in an email or messaging app.
- [UIConversationContext.Entry](uiconversationcontext/entry.md)
  A base class that represents a message in a conversation.
- [class UIMailConversationContext](uimailconversationcontext.md)
  A class that represents an email conversation.
- [UIMailConversationContext.MailEntry](uimailconversationcontext/mailentry.md)
  A class that represents a specific email in an email thread.
- [class UIMessageConversationContext](uimessageconversationcontext.md)
  A class that represents a message conversation.
- [UIMessageConversationContext.MessageEntry](uimessageconversationcontext/messageentry.md)
  A class that represents a message in a message conversation.
- [class UIInputSuggestion](uiinputsuggestion.md)
  A base class you use to handle suggestions from the keyboard or system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uismartreplysuggestion)*