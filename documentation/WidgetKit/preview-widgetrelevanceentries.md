# Preview(_:widget:relevanceEntries:)

**Framework**: WidgetKit  
**Kind**: macro

Preview a relevance configuration widget.

**Availability**:
- watchOS 26.0+ (Beta)

## Declaration

```swift
@freestanding
(declaration) macro Preview<Widget, Entry>(_ name: String? = nil, widget: @escaping @MainActor () -> Widget, @PreviewRelevanceEntryBuilder<Entry> relevanceEntries: @escaping @MainActor () async -> [Entry]) where Widget : Widget, Entry : RelevanceEntry
```

#### Overview

The preview will allow you to step through your entries.

> **Note**: The entries must be of the type expected by the widget. (This will be enforced at run-time.)

## Parameters

- `name`: An optional display name for the preview, which will appear in the canvas.
- `widget`: A closure producing the widget to be previewed.
- `relevanceEntries`: A closure building the entries to be previewed.

## See Also

- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:widget:timelineprovider:).md)
  Preview a widget with a static configuration, using the specified timeline provider.
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:using:widget:timelineprovider:)-4ljg1.md)
  Preview a widget with an app intent configuration, using the specified timeline provider.
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:using:widget:timelineprovider:)-3df1l.md)
  Preview a widget with an intent configuration, using the specified timeline provider.
- [macro Preview<Widget>(String?, as: WidgetFamily, widget: () -> Widget, timeline: () async -> [any TimelineEntry])](preview(_:as:widget:timeline:).md)
  Preview a timeline-style widget.
- [macro Preview<Widget, Provider>(String?, widget: () -> Widget, relevanceProvider: () -> Provider)](preview(_:widget:relevanceprovider:).md)
  Preview a widget with a relevance configuration, using the specified relevance provider.
- [macro Preview<Widget, Provider>(String?, widget: () -> Widget, relevanceProvider: () -> Provider, relevance: () async -> WidgetRelevance<Provider.Configuration>)](preview(_:widget:relevanceprovider:relevance:).md)
  Preview a widget with a relevance configuration, using the specified relevances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/preview(_:widget:relevanceentries:))*