# PreviewTimelineBuilder

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
@resultBuilder
struct PreviewTimelineBuilder
```

## Topics

### Previewing timelines
- [static func buildArray([[any TimelineEntry]]) -> [any TimelineEntry]](./previewtimelinebuilder/buildarray%28_%29.md)
- [static func buildExpression(some TimelineEntry) -> [any TimelineEntry]](./previewtimelinebuilder/buildexpression%28_%29.md)
- [static func buildPartialBlock(accumulated: [any TimelineEntry], next: [any TimelineEntry]) -> [any TimelineEntry]](./previewtimelinebuilder/buildpartialblock%28accumulated,next%29.md)
- [static func buildPartialBlock(first: [any TimelineEntry]) -> [any TimelineEntry]](./previewtimelinebuilder/buildpartialblock%28first%29.md)

## See Also

### Generated structures
- [struct PreviewActivityBuilder](./previewactivitybuilder.md)
- [struct PreviewRelevanceEntryBuilder](./previewrelevanceentrybuilder.md)
  A builder that allows you to construct a list of relevance entries to preview your widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/previewtimelinebuilder)*