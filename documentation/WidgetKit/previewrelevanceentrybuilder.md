# PreviewRelevanceEntryBuilder

**Framework**: WidgetKit  
**Kind**: struct

A builder that allows you to construct a list of relevance entries to preview your widget.

**Availability**:
- watchOS 26.0+ (Beta)

## Declaration

```swift
@resultBuilder
struct PreviewRelevanceEntryBuilder<Entry> where Entry : RelevanceEntry
```

## Topics

### Previewing relevance widgets
- [static func buildArray([[Entry]]) -> [Entry]](previewrelevanceentrybuilder/buildarray(_:).md)
- [static func buildExpression(Entry) -> [Entry]](previewrelevanceentrybuilder/buildexpression(_:).md)
- [static func buildPartialBlock(first: [Entry]) -> [Entry]](previewrelevanceentrybuilder/buildpartialblock(first:).md)
- [static func buildPartialBlock(accumulated: [Entry], next: [Entry]) -> [Entry]](previewrelevanceentrybuilder/buildpartialblock(accumulated:next:).md)

## See Also

- [struct PreviewActivityBuilder](previewactivitybuilder.md)
- [struct PreviewTimelineBuilder](previewtimelinebuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/previewrelevanceentrybuilder)*