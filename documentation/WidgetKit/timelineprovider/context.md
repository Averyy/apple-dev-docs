# TimelineProvider.Context

**Framework**: WidgetKit  
**Kind**: typealias

An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
typealias Context = TimelineProviderContext
```

#### Discussion

For more information, see [`TimelineProviderContext`](timelineprovidercontext.md).

## See Also

- [func getSnapshot(in: Self.Context, completion: (Self.Entry) -> Void)](timelineprovider/getsnapshot(in:completion:).md)
  Provides a timeline entry that represents the current time and state of a widget.
- [func getTimeline(in: Self.Context, completion: (Timeline<Self.Entry>) -> Void)](timelineprovider/gettimeline(in:completion:).md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [func placeholder(in: Self.Context) -> Self.Entry](timelineprovider/placeholder(in:).md)
  Provides a timeline entry representing a placeholder version of the widget.
- [associatedtype Entry : TimelineEntry](timelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineprovider/context)*