# placeholder(in:)

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Provides a timeline entry representing a placeholder version of the widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 26.0+ (Beta)
- watchOS 10.0+

## Declaration

```swift
func placeholder(in context: Self.Context) -> Self.Entry
```

#### Return Value

A timeline entry that represents a placeholder version of the widget.

#### Discussion

When WidgetKit displays your widget for the first time, it renders the widget’s view as a placeholder. A placeholder view displays a generic representation of your widget, giving the user a general idea of what the widget shows. WidgetKit calls `placeholder(in:)` to request an entry representing the widget’s placeholder configuration. For example, the game status widget would implement this method as follows:

```swift
struct GameStatusProvider: TimelineProvider {
    func placeholder(in context: Context) -> SimpleEntry {
       GameStatusEntry(date: Date(), gameStatus: "—")
    }
}
```

In addition, WidgetKit may render your widget as a placeholder if user’s choose to hide sensitive information on Apple Watch or the iPhone Lock Screen. To learn more about redacting sensitive data, see [`Creating a widget extension`](creating-a-widget-extension.md).

> ❗ **Important**: `placeholder(in:)` is synchronous and returns a `TimelineEntry` immediately. Return from `placeholder(in:)` as quickly as possible.

## Parameters

- `context`: An object that describes the context in which to   show the widget.

## See Also

- [func recommendations() -> [AppIntentRecommendation<Self.Intent>]](appintenttimelineprovider/recommendations.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [func relevance() async -> WidgetRelevance<Self.Intent>](appintenttimelineprovider/relevance.md)
  Provides an object containing attributes that describe when a specific widget is relevant.
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

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider/placeholder(in:))*