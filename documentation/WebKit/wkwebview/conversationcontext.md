# conversationContext

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var conversationContext: UIConversationContext { get set }
```

```objc
@property (nonatomic, strong) UIConversationContext * conversationContext;
```

## Discussion

A reference to a conversation, such as a mail or messaging thread.

Set this conversation context before the keyboard appears; the keyboard uses this context to initialize its conversation context value. When your conversation updates, update the smart reply by setting this property.

## See Also

### Supporting Writing Tools
- [var isWritingToolsActive: Bool](./iswritingtoolsactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/conversationcontext)*