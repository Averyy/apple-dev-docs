# getTimeline(in:completion:)

**Framework**: Widgetkit  
**Kind**: method  
**Required**: Yes

Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
func getTimeline(in context: Self.Context, completion: @escaping (Timeline<Self.Entry>) -> Void)
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)
- [Making network requests in a widget extension](making-network-requests-in-a-widget-extension.md)

## Parameters

- `context`: An object describing the context to show the widget in.
- `completion`: The completion handler to call after you create the   timeline.

## See Also

- [func getSnapshot(in: Self.Context, completion: (Self.Entry) -> Void)](timelineprovider/getsnapshot(in:completion:).md)
  Provides a timeline entry that represents the current time and state of a widget.
- [func placeholder(in: Self.Context) -> Self.Entry](timelineprovider/placeholder(in:).md)
  Provides a timeline entry representing a placeholder version of the widget.
- [associatedtype Entry : TimelineEntry](timelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [TimelineProvider.Context](timelineprovider/context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovider/gettimeline(in:completion:))*