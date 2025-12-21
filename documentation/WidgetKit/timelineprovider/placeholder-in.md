# placeholder(in:)

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Provides a timeline entry representing a placeholder version of the widget.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
func placeholder(in context: Self.Context) -> Self.Entry
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)

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

In addition, WidgetKit may render your widget as a placeholder if users choose to hide sensitive information on Apple Watch or the iPhone Lock Screen. To learn more about redacting sensitive data, see [`Creating a widget extension`](creating-a-widget-extension.md).

> ❗ **Important**: `placeholder(in:)` is synchronous and returns a `TimelineEntry` immediately. Return from `placeholder(in:)` as quickly as possible.

## Parameters

- `context`: An object that describes the context in which to   show the widget.

## See Also

- [func getSnapshot(in: Self.Context, completion: (Self.Entry) -> Void)](timelineprovider/getsnapshot(in:completion:).md)
  Provides a timeline entry that represents the current time and state of a widget.
- [func getTimeline(in: Self.Context, completion: (Timeline<Self.Entry>) -> Void)](timelineprovider/gettimeline(in:completion:).md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [associatedtype Entry : TimelineEntry](timelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [TimelineProvider.Context](timelineprovider/context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovider/placeholder(in:))*