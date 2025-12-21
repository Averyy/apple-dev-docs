# Preview(_:as:widget:timeline:)

**Framework**: WidgetKit  
**Kind**: macro

Preview a timeline-style widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview<Widget>(_ name: String? = nil, as family: WidgetFamily, widget: @escaping () -> Widget, @PreviewTimelineBuilder timeline: @escaping @MainActor () async -> [any TimelineEntry]) where Widget : Widget
```

## Mentions

- [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md)

#### Overview

Provide the preview with sample data and use it to step through the timeline while ignoring the dates of the entries, and test out the transitions between them.

> **Note**: The timeline entries must be of the type that the widget expects.

## Parameters

- `name`: An optional display name for the preview that appears in the Xcode preview canvas.
- `family`: The widget family to display.
- `widget`: A closure producing the widget to be previewed.
- `timeline`: A closure building the timeline of entries to be previewed.

## See Also

- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:widget:timelineprovider:).md)
  Preview a widget with a static configuration, using the specified timeline provider.
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:using:widget:timelineprovider:)-4ljg1.md)
  Preview a widget with an app intent configuration, using the specified timeline provider.
- [macro Preview<Widget, Provider>(String?, as: WidgetFamily, using: Provider.Intent, widget: () -> Widget, timelineProvider: () -> Provider)](preview(_:as:using:widget:timelineprovider:)-3df1l.md)
  Preview a widget with an intent configuration, using the specified timeline provider.
- [macro Preview<Widget, Entry>(String?, widget: () -> Widget, relevanceEntries: () async -> [Entry])](preview(_:widget:relevanceentries:).md)
  Preview a relevance configuration widget.
- [macro Preview<Widget, Provider>(String?, widget: () -> Widget, relevanceProvider: () -> Provider)](preview(_:widget:relevanceprovider:).md)
  Preview a widget with a relevance configuration, using the specified relevance provider.
- [macro Preview<Widget, Provider>(String?, widget: () -> Widget, relevanceProvider: () -> Provider, relevance: () async -> WidgetRelevance<Provider.Configuration>)](preview(_:widget:relevanceprovider:relevance:).md)
  Preview a widget with a relevance configuration, using the specified relevances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/preview(_:as:widget:timeline:))*