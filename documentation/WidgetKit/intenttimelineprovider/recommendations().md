# recommendations()

**Framework**: WidgetKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
func recommendations() -> [IntentRecommendation<Self.Intent>]
```

## Default Implementations

### IntentTimelineProvider Implementations
- [func recommendations() -> [IntentRecommendation<Self.Intent>]](./recommendations%28%29-5qmcg.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.

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
- [IntentTimelineProvider.Context](./context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intenttimelineprovider/recommendations())*