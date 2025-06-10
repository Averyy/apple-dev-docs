# relevance()

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Provides an object containing attributes that describe when a specific widget is relevant.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 26.0+ (Beta)
- watchOS 11.0+

## Declaration

```swift
func relevance() async -> WidgetRelevance<Self.Intent>
```

#### Return Value

The object that contains attributes that describe when a specific widget is relevant.

#### Discussion

The system can use the relevance to show this widget in the Smart Stack when the provided relevance matches a person’s context. For example, if you indicate relevance at a specific location, the system could show the widget when a person is at or close to the location.

By default, this method returns no relevances. Implement this requirement to tell the system that your widget is relevant.

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](widget-suggestions-in-smart-stacks.md).

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
- [associatedtype Intent : WidgetConfigurationIntent](appintenttimelineprovider/intent.md)
  The intent that contains user-customized values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/relevance())*