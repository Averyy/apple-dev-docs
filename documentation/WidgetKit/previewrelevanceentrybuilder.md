# PreviewRelevanceEntryBuilder

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

A builder that allows you to construct a list of relevance entries to preview your widget.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
@resultBuilder
struct PreviewRelevanceEntryBuilder<Entry> where Entry : RelevanceEntry
```

## Topics

### Previewing relevance widgets
- [static func buildArray([[Entry]]) -> [Entry]](./previewrelevanceentrybuilder/buildarray%28_%29.md)
- [static func buildExpression(Entry) -> [Entry]](./previewrelevanceentrybuilder/buildexpression%28_%29.md)
- [static func buildPartialBlock(first: [Entry]) -> [Entry]](./previewrelevanceentrybuilder/buildpartialblock%28first%29.md)
- [static func buildPartialBlock(accumulated: [Entry], next: [Entry]) -> [Entry]](./previewrelevanceentrybuilder/buildpartialblock%28accumulated,next%29.md)

## See Also

### Generated structures
- [struct PreviewActivityBuilder](./previewactivitybuilder.md)
- [struct PreviewTimelineBuilder](./previewtimelinebuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/previewrelevanceentrybuilder)*