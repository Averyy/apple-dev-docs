# Intent

**Framework**: Widgetkit  
**Kind**: associatedtype  
**Required**: Yes

The intent that contains user-customized values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- watchOS 10.0+

## Declaration

```swift
associatedtype Intent : WidgetConfigurationIntent
```

## See Also

- [func placeholder(in: Self.Context) -> Self.Entry](appintenttimelineprovider/placeholder(in:).md)
  Provides a timeline entry representing a placeholder version of the widget.
- [func recommendations() -> [AppIntentRecommendation<Self.Intent>]](appintenttimelineprovider/recommendations.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [func snapshot(for: Self.Intent, in: Self.Context) async -> Self.Entry](appintenttimelineprovider/snapshot(for:in:).md)
  Provides a timeline entry representing the current time and state of a widget.
- [func timeline(for: Self.Intent, in: Self.Context) async -> Timeline<Self.Entry>](appintenttimelineprovider/timeline(for:in:).md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [AppIntentTimelineProvider.Context](appintenttimelineprovider/context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [associatedtype Entry : TimelineEntry](appintenttimelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/intent)*