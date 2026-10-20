# PreviewActivityBuilder

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@resultBuilder
struct PreviewActivityBuilder<A> where A : ActivityAttributes
```

## Topics

### Previewing Live Activities
- [static func buildArray([[A.ContentState]]) -> [A.ContentState]](./previewactivitybuilder/buildarray%28_%29.md)
- [static func buildExpression(A.ContentState) -> [A.ContentState]](./previewactivitybuilder/buildexpression%28_%29.md)
- [static func buildPartialBlock(accumulated: [A.ContentState], next: [A.ContentState]) -> [A.ContentState]](./previewactivitybuilder/buildpartialblock%28accumulated,next%29.md)
- [static func buildPartialBlock(first: [A.ContentState]) -> [A.ContentState]](./previewactivitybuilder/buildpartialblock%28first%29.md)

## See Also

### Generated structures
- [struct PreviewRelevanceEntryBuilder](./previewrelevanceentrybuilder.md)
  A builder that allows you to construct a list of relevance entries to preview your widget.
- [struct PreviewTimelineBuilder](./previewtimelinebuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/previewactivitybuilder)*