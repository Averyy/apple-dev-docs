# WebPage.JavaScriptConfirmResult

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
enum JavaScriptConfirmResult
```

## Topics

### Enumeration Cases
- [WebPage.JavaScriptConfirmResult.cancel](./javascriptconfirmresult/cancel.md)
  Signals a negative action was produced by the invocation.
- [WebPage.JavaScriptConfirmResult.ok](./javascriptconfirmresult/ok.md)
  Signals an affirmative action was produced by the invocation.

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
- [WebPage.JavaScriptPromptResult](./javascriptpromptresult.md)
  The result of handling a JavaScript confirm invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/javascriptconfirmresult)*