# getSnapshot(in:completion:)

**Framework**: Widgetkit  
**Kind**: method  
**Required**: Yes

Provides a timeline entry that represents the current time and state of a widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
func getSnapshot(in context: Self.Context, completion: @escaping (Self.Entry) -> Void)
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)

#### Discussion

WidgetKit calls `getSnapshot(in:completion:)` when the widget appears in transient situations. If `context.isPreview` is `true`, the widget appears in the widget gallery. In that case, call the `completion` handler as quickly as possible, perhaps supplying sample data if it could take more than a few seconds to fetch or calculate the widget’s current state.

## Parameters

- `context`: An object describing the context to show the widget in.
- `completion`: The completion handler to call after you create the   snapshot entry.

## See Also

- [func getTimeline(in: Self.Context, completion: (Timeline<Self.Entry>) -> Void)](timelineprovider/gettimeline(in:completion:).md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [func placeholder(in: Self.Context) -> Self.Entry](timelineprovider/placeholder(in:).md)
  Provides a timeline entry representing a placeholder version of the widget.
- [associatedtype Entry : TimelineEntry](timelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [TimelineProvider.Context](timelineprovider/context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovider/getsnapshot(in:completion:))*