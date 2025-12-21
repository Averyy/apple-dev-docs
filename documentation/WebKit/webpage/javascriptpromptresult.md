# WebPage.JavaScriptPromptResult

**Framework**: WebKit  
**Kind**: enum

The result of handling a JavaScript confirm invocation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum JavaScriptPromptResult
```

## Topics

### Enumeration Cases
- [WebPage.JavaScriptPromptResult.cancel](webpage/javascriptpromptresult/cancel.md)
  Signals a negative action was produced by the invocation.
- [WebPage.JavaScriptPromptResult.ok(_:)](webpage/javascriptpromptresult/ok(_:).md)
  Signals an affirmative action was produced by the invocation with the specified text.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol DialogPresenting](webpage/dialogpresenting.md)
  Allows providing custom behavior to handle JavaScript actions and provide a response.
- [WebPage.FileInputPromptResult](webpage/fileinputpromptresult.md)
  The result of handling a JavaScript open invocation.
- [WebPage.JavaScriptConfirmResult](webpage/javascriptconfirmresult.md)
  The result of handling a JavaScript confirm invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/javascriptpromptresult)*