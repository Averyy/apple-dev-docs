# Entry

**Framework**: WidgetKit  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
associatedtype Entry : TimelineEntry
```

## See Also

### Generating Timelines
- [func getSnapshot(in: Self.Context, completion: (Self.Entry) -> Void)](./getsnapshot%28in,completion%29.md)
  Provides a timeline entry that represents the current time and state of a widget.
- [func getTimeline(in: Self.Context, completion: (Timeline<Self.Entry>) -> Void)](./gettimeline%28in,completion%29.md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [func placeholder(in: Self.Context) -> Self.Entry](./placeholder%28in%29.md)
  Provides a timeline entry representing a placeholder version of the widget.
- [TimelineProvider.Context](./context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovider/entry)*