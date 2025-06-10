# PreviewTimelineBuilder

**Framework**: WidgetKit  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 26.0+ (Beta)
- watchOS 10.0+

## Declaration

```swift
@resultBuilder
struct PreviewTimelineBuilder
```

## Topics

### Previewing timelines
- [static func buildArray([[any TimelineEntry]]) -> [any TimelineEntry]](previewtimelinebuilder/buildarray(_:).md)
- [static func buildExpression(some TimelineEntry) -> [any TimelineEntry]](previewtimelinebuilder/buildexpression(_:).md)
- [static func buildPartialBlock(accumulated: [any TimelineEntry], next: [any TimelineEntry]) -> [any TimelineEntry]](previewtimelinebuilder/buildpartialblock(accumulated:next:).md)
- [static func buildPartialBlock(first: [any TimelineEntry]) -> [any TimelineEntry]](previewtimelinebuilder/buildpartialblock(first:).md)

## See Also

- [struct PreviewActivityBuilder](previewactivitybuilder.md)
- [struct PreviewRelevanceEntryBuilder](previewrelevanceentrybuilder.md)
  A builder that allows you to construct a list of relevance entries to preview your widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/previewtimelinebuilder)*