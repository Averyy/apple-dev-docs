# WebPage.JavaScriptPromptResult

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

The result of handling a JavaScript confirm invocation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum JavaScriptPromptResult
```

## Topics

### Enumeration Cases
- [WebPage.JavaScriptPromptResult.cancel](./javascriptpromptresult/cancel.md)
  Signals a negative action was produced by the invocation.
- [WebPage.JavaScriptPromptResult.ok(_:)](./javascriptpromptresult/ok%28_%29.md)
  Signals an affirmative action was produced by the invocation with the specified text.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing JavaScript dialogs
- [protocol DialogPresenting](./dialogpresenting.md)
  Allows providing custom behavior to handle JavaScript actions and provide a response.
- [WebPage.FileInputPromptResult](./fileinputpromptresult.md)
  The result of handling a JavaScript open invocation.
- [WebPage.JavaScriptConfirmResult](./javascriptconfirmresult.md)
  The result of handling a JavaScript confirm invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/javascriptpromptresult)*