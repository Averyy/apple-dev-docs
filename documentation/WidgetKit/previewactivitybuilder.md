# PreviewActivityBuilder

**Framework**: WidgetKit  
**Kind**: struct

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
- [static func buildArray([[A.ContentState]]) -> [A.ContentState]](previewactivitybuilder/buildarray(_:).md)
- [static func buildExpression(A.ContentState) -> [A.ContentState]](previewactivitybuilder/buildexpression(_:).md)
- [static func buildPartialBlock(accumulated: [A.ContentState], next: [A.ContentState]) -> [A.ContentState]](previewactivitybuilder/buildpartialblock(accumulated:next:).md)
- [static func buildPartialBlock(first: [A.ContentState]) -> [A.ContentState]](previewactivitybuilder/buildpartialblock(first:).md)

## See Also

- [struct PreviewRelevanceEntryBuilder](previewrelevanceentrybuilder.md)
  A builder that allows you to construct a list of relevance entries to preview your widget.
- [struct PreviewTimelineBuilder](previewtimelinebuilder.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/previewactivitybuilder)*