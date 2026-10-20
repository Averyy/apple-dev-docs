# conversationContext(_:didChange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the input delegate when text has changed in the input object for a conversation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
func conversationContext(_ context: UIConversationContext?, didChange textInput: (any UITextInput)?)
```

```objc
- (void) conversationContext:(UIConversationContext *) context didChange:(id<UITextInput>) textInput;
```

## Mentions

- [Adopting Smart Reply in your messaging or email app](../adopting-smart-reply-in-your-messaging-or-email-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate/conversationcontext(_:didchange:))*