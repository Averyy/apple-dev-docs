# getSnapshot(for:in:completion:)

**Framework**: Widgetkit  
**Kind**: method  
**Required**: Yes

Provides a timeline entry representing the current time and state of a widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
func getSnapshot(for configuration: Self.Intent, in context: Self.Context, completion: @escaping (Self.Entry) -> Void)
```

#### Discussion

WidgetKit calls `getSnapshot(for:in:completion:)` when the widget appears in transient situations. If context.isPreview is true, the widget appears in the widget gallery. In that case, call the completion handler as quickly as possible, perhaps supplying sample data if it could take more than a few seconds to fetch or calculate the widget’s current state.

The `configuration` parameter provides user-customized values, as defined in your custom intent definition.

## Parameters

- `configuration`: The intent containing user-customized values.
- `context`: An object describing the context to show the widget in.
- `completion`: The completion handler to call after you create the   snapshot entry.

## See Also

- [func getTimeline(for: Self.Intent, in: Self.Context, completion: (Timeline<Self.Entry>) -> Void)](intenttimelineprovider/gettimeline(for:in:completion:).md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
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

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intenttimelineprovider/getsnapshot(for:in:completion:))*