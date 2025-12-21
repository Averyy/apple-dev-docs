# TimelineEntry

**Framework**: WidgetKit  
**Kind**: protocol

A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
protocol TimelineEntry
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)

#### Overview

A [`TimelineProvider`](timelineprovider.md) creates one or more timeline entries with dates that tell WidgetKit when to display a widget. To render a widget, WidgetKit executes the `content` block of the widget’s configuration, passing the corresponding timeline entry.

When you declare a structure conforming to `TimelineEntry`, include any additional information that the configuration’s content block requires to render the widget. The following code shows a timeline entry structure for a widget that displays a game character’s health level.

```swift
struct CharacterDetailEntry: TimelineEntry {
    var date: Date
    var healthLevel: Double
}
```

The content block of the widget’s configuration receives the entry as a parameter and then passes the relevant information to the view that renders your widget.

```swift
struct CharacterDetailWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: "com.mygame.character-detail",
            provider: CharacterDetailProvider()) { entry in
            CharacterDetailView(entry: entry)
        }
        .configurationDisplayName("Character Details")
        .description("Displays a character's health and other details")
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}
```

## Topics

### Configuring Timeline Entry Properties
- [var date: Date](timelineentry/date.md)
  The date for WidgetKit to render a widget.
- [var relevance: TimelineEntryRelevance?](timelineentry/relevance.md)
  The relevance of a widget’s content to the user.

## See Also

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md)
  Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [protocol TimelineProvider](timelineprovider.md)
  A type that advises WidgetKit when to update a widget’s display.
- [protocol AppIntentTimelineProvider](appintenttimelineprovider.md)
  A type that advises WidgetKit when to update a user-configurable widget’s display.
- [protocol IntentTimelineProvider](intenttimelineprovider.md)
  A type that advises WidgetKit when to update a user-configurable widget’s display.
- [struct TimelineProviderContext](timelineprovidercontext.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [struct Timeline](timeline.md)
  An object that specifies a date for WidgetKit to update a widget’s view.
- [class WidgetCenter](widgetcenter.md)
  An object that contains a list of user-configured widgets and is used for reloading widget timelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/timelineentry)*