# IntentTimelineProvider.Context

**Framework**: WidgetKit  
**Kind**: typealias  
**Role**: Type Alias

An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
typealias Context = TimelineProviderContext
```

## Discussion

For more information, see [`TimelineProviderContext`](../timelineprovidercontext.md).

## See Also

### Generating Timelines
- [func getSnapshot(for: Self.Intent, in: Self.Context, completion: (Self.Entry) -> Void)](./getsnapshot%28for,in,completion%29.md)
  Provides a timeline entry representing the current time and state of a widget.
- [func getTimeline(for: Self.Intent, in: Self.Context, completion: (Timeline<Self.Entry>) -> Void)](./gettimeline%28for,in,completion%29.md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [func placeholder(in: Self.Context) -> Self.Entry](./placeholder%28in%29.md)
  Provides a timeline entry representing a placeholder version of the widget.
- [associatedtype Entry : TimelineEntry](./entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [associatedtype Intent : INIntent](./intent.md)
  The intent that contains user-customized values.
- [func recommendations() -> [IntentRecommendation<Self.Intent>]](./recommendations%28%29.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intenttimelineprovider/context)*