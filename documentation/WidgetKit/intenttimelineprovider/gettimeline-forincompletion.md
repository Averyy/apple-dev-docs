# getTimeline(for:in:completion:)

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
func getTimeline(for configuration: Self.Intent, in context: Self.Context, completion: @escaping (Timeline<Self.Entry>) -> Void)
```

#### Discussion

The `configuration` parameter provides user-customized values, as defined in your custom intent definition.

## Parameters

- `configuration`: The intent containing user-customized values.
- `context`: An object describing the context to show the widget in.
- `completion`: The completion handler to call after you create the   timeline.

## See Also

- [func getSnapshot(for: Self.Intent, in: Self.Context, completion: (Self.Entry) -> Void)](intenttimelineprovider/getsnapshot(for:in:completion:).md)
  Provides a timeline entry representing the current time and state of a widget.
- [func placeholder(in: Self.Context) -> Self.Entry](intenttimelineprovider/placeholder(in:).md)
  Provides a timeline entry representing a placeholder version of the widget.
- [associatedtype Entry : TimelineEntry](intenttimelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [associatedtype Intent : INIntent](intenttimelineprovider/intent.md)
  The intent that contains user-customized values.
- [func recommendations() -> [IntentRecommendation<Self.Intent>]](intenttimelineprovider/recommendations.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [IntentTimelineProvider.Context](intenttimelineprovider/context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intenttimelineprovider/gettimeline(for:in:completion:))*