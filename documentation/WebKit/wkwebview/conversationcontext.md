# conversationContext

**Framework**: WebKit  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var conversationContext: UIConversationContext { get set }
```

#### Discussion

A reference to a conversation, such as a mail or messaging thread.

Set this conversation context before the keyboard appears; the keyboard uses this context to initialize its conversation context value. When your conversation updates, update the smart reply by setting this property.

## See Also

- [var isWritingToolsActive: Bool](wkwebview/iswritingtoolsactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/conversationcontext)*