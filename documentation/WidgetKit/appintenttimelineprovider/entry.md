# Entry

**Framework**: WidgetKit  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
associatedtype Entry : TimelineEntry
```

## See Also

### Generating timelines
- [func placeholder(in: Self.Context) -> Self.Entry](./placeholder%28in%29.md)
  Provides a timeline entry representing a placeholder version of the widget.
- [func recommendations() -> [AppIntentRecommendation<Self.Intent>]](./recommendations%28%29.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [func relevance() async -> WidgetRelevance<Self.Intent>](./relevance%28%29.md)
  Provides an object containing attributes that describe when a specific widget is relevant.
- [func snapshot(for: Self.Intent, in: Self.Context) async -> Self.Entry](./snapshot%28for,in%29.md)
  Provides a timeline entry representing the current time and state of a widget.
- [func timeline(for: Self.Intent, in: Self.Context) async -> Timeline<Self.Entry>](./timeline%28for,in%29.md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [AppIntentTimelineProvider.Context](./context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [associatedtype Intent : WidgetConfigurationIntent](./intent.md)
  The intent that contains user-customized values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/entry)*