# StaticConfiguration

**Framework**: WidgetKit  
**Kind**: struct

An object describing the content of a widget that has no user-configurable options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct StaticConfiguration<Content> where Content : View
```

## Mentions

- [Creating a widget extension](creating-a-widget-extension.md)

#### Overview

The following example shows the configuration for the leaderboard widget of the [`Emoji Rangers: Supporting Live Activities, interactivity, and animations`](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project.

```swift
struct LeaderboardWidget: Widget {

    public var body: some WidgetConfiguration {
        StaticConfiguration(kind: EmojiRanger.LeaderboardWidgetKind, provider: LeaderboardProvider()) { entry in
            LeaderboardWidgetEntryView(entry: entry)
        }
        .configurationDisplayName("Ranger Leaderboard")
        .description("See all the rangers.")
        .supportedFamilies(LeaderboardWidget.supportedFamilies)
    }
}
```

Every widget has a unique `kind`, a string that you choose. You use this string to identify your widget when reloading its timeline with [`WidgetCenter`](widgetcenter.md).

The timeline provider is an object that determines the timeline for refreshing your widget. Providing future dates for updating your widget allows the system to optimize the refresh process.

The content closure contains the SwiftUI views that WidgetKit needs to render the widget. When WidgetKit invokes the content closure, it passes a timeline entry created by the widget provider’s [`getSnapshot(in:completion:)`](timelineprovider/getsnapshot(in:completion:).md) or [`getTimeline(in:completion:)`](timelineprovider/gettimeline(in:completion:).md) method.

Modifiers let you specify the families your widget supports, and the details shown when users add or edit their widgets.

## Topics

### Creating a widget configuration
- [init<Provider>(kind: String, provider: Provider, content: (Provider.Entry) -> Content)](staticconfiguration/init(kind:provider:content:).md)
  Creates a configuration for a widget, with no user-configurable options.
- [var body: Self.Body](../SwiftUI/WidgetConfiguration/body-swift.property.md)
  The content and behavior of this widget.
### Setting the display name
- [func configurationDisplayName<S>(S) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/configurationDisplayName(_:)-2c3zv.md)
  Sets the name shown for a widget when a user adds or edits it using the specified string.
- [func configurationDisplayName(Text) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/configurationDisplayName(_:)-3sbn4.md)
  Sets the name shown for a widget when a user adds or edits it using the contents of a text view.
- [func configurationDisplayName(LocalizedStringKey) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/configurationDisplayName(_:)-4v9q.md)
  Sets the localized name shown for a widget when a user adds or edits the widget.
### Setting the description
- [func description(Text) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/description(_:)-1bvuj.md)
  Sets the description shown for a widget when a user adds or edits it using the contents of a text view.
- [func description<S>(S) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/description(_:)-2bfr.md)
  Sets the description shown for a widget when a user adds or edits it using the specified string.
- [func description(LocalizedStringKey) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/description(_:)-4q9pa.md)
  Sets the localized description shown for a widget when a user adds or edits the widget.
### Setting the supported families
- [func supportedFamilies([WidgetFamily]) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/supportedFamilies(_:).md)
  Sets the sizes that a widget supports.
- [func supplementalActivityFamilies([ActivityFamily]) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/supplementalActivityFamilies(_:).md)
  Sets the sizes that a Live Activity supports.
### Handling background network requests
- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/backgroundTask(_:action:).md)
  Runs the given action when the system provides a background task.
- [func onBackgroundURLSessionEvents(matching: ((String) -> Bool)?, (String, () -> Void) -> Void) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/onBackgroundURLSessionEvents(matching:_:)-2e152.md)
  Adds an action to perform when events related to a URL session identified by a closure are waiting to be processed.
- [func onBackgroundURLSessionEvents(matching: String, (String, () -> Void) -> Void) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/onBackgroundURLSessionEvents(matching:_:)-fw6x.md)
  Adds an action to perform when events related to a URL session with a matching identifier are waiting to be processed.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [WidgetConfiguration](../SwiftUI/WidgetConfiguration.md)

## See Also

- [Creating a widget extension](creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Developing a WidgetKit strategy](developing-a-widgetkit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
  Create widgets that support additional platforms and adapt to their context.
- [protocol Widget](../SwiftUI/Widget.md)
  The configuration and content of a widget to display on the Home screen or in Notification Center.
- [enum WidgetFamily](widgetfamily.md)
  Values that define the widget’s size and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/staticconfiguration)*