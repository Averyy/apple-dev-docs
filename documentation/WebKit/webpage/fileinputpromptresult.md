# WebPage.FileInputPromptResult

**Framework**: WebKit  
**Kind**: enum

The result of handling a JavaScript open invocation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum FileInputPromptResult
```

## Topics

### Enumeration Cases
- [WebPage.FileInputPromptResult.cancel](webpage/fileinputpromptresult/cancel.md)
  Signals a negative action was produced by the invocation.
- [WebPage.FileInputPromptResult.selected(_:)](webpage/fileinputpromptresult/selected(_:).md)
  Signals an affirmative action was produced by the invocation with the specified files.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol DialogPresenting](webpage/dialogpresenting.md)
  Allows providing custom behavior to handle JavaScript actions and provide a response.
- [WebPage.JavaScriptConfirmResult](webpage/javascriptconfirmresult.md)
  The result of handling a JavaScript confirm invocation.
- [WebPage.JavaScriptPromptResult](webpage/javascriptpromptresult.md)
  The result of handling a JavaScript confirm invocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/fileinputpromptresult)*