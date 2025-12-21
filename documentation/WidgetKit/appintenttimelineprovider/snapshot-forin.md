# snapshot(for:in:)

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Provides a timeline entry representing the current time and state of a widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
func snapshot(for configuration: Self.Intent, in context: Self.Context) async -> Self.Entry
```

#### Return Value

A timeline entry representing the current time and state of a widget

#### Discussion

WidgetKit calls `snapshot(for:in:)` when the widget appears in transient situations. If context.isPreview is true, the widget appears in the widget gallery. In that case, return the `Entry` as quickly as possible, perhaps supplying sample data if it could take more than a few seconds to fetch or calculate the widget’s current state.

The `configuration` parameter provides user-customized values, as defined in your custom intent.

## Parameters

- `configuration`: The intent containing user-customized values.
- `context`: An object describing the context to show the widget in.

## See Also

- [func placeholder(in: Self.Context) -> Self.Entry](appintenttimelineprovider/placeholder(in:).md)
  Provides a timeline entry representing a placeholder version of the widget.
- [func recommendations() -> [AppIntentRecommendation<Self.Intent>]](appintenttimelineprovider/recommendations.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [func relevance() async -> WidgetRelevance<Self.Intent>](appintenttimelineprovider/relevance.md)
  Provides an object containing attributes that describe when a specific widget is relevant.
- [func timeline(for: Self.Intent, in: Self.Context) async -> Timeline<Self.Entry>](appintenttimelineprovider/timeline(for:in:).md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [AppIntentTimelineProvider.Context](appintenttimelineprovider/context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [associatedtype Entry : TimelineEntry](appintenttimelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [associatedtype Intent : WidgetConfigurationIntent](appintenttimelineprovider/intent.md)
  The intent that contains user-customized values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/snapshot(for:in:))*