# Intent

**Framework**: WidgetKit  
**Kind**: associatedtype  
**Required**: Yes

The intent that contains user-customized values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
associatedtype Intent : INIntent
```

## See Also

- [func getSnapshot(for: Self.Intent, in: Self.Context, completion: (Self.Entry) -> Void)](intenttimelineprovider/getsnapshot(for:in:completion:).md)
  Provides a timeline entry representing the current time and state of a widget.
- [func getTimeline(for: Self.Intent, in: Self.Context, completion: (Timeline<Self.Entry>) -> Void)](intenttimelineprovider/gettimeline(for:in:completion:).md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [func placeholder(in: Self.Context) -> Self.Entry](intenttimelineprovider/placeholder(in:).md)
  Provides a timeline entry representing a placeholder version of the widget.
- [associatedtype Entry : TimelineEntry](intenttimelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [func recommendations() -> [IntentRecommendation<Self.Intent>]](intenttimelineprovider/recommendations.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [IntentTimelineProvider.Context](intenttimelineprovider/context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intenttimelineprovider/intent)*