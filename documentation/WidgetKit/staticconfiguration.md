# StaticConfiguration

**Framework**: WidgetKit  
**Kind**: struct

An object describing the content of a widget that has no user-configurable options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
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
- [@MainActor @preconcurrency var body: Self.Body { get }](../SwiftUI/WidgetConfiguration/body-swift.property.md)
  The content and behavior of this widget.
### Setting the display name
- [@MainActor @preconcurrency func configurationDisplayName<S>(_ displayName: S) -> some WidgetConfiguration where S : StringProtocol
](../SwiftUI/WidgetConfiguration/configurationDisplayName(_:)-2c3zv.md)
  Sets the name shown for a widget when a user adds or edits it using the specified string.
- [@MainActor @preconcurrency func configurationDisplayName(_ displayName: Text) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/configurationDisplayName(_:)-3sbn4.md)
  Sets the name shown for a widget when a user adds or edits it using the contents of a text view.
- [@MainActor @preconcurrency func configurationDisplayName(_ displayNameKey: LocalizedStringKey) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/configurationDisplayName(_:)-4v9q.md)
  Sets the localized name shown for a widget when a user adds or edits the widget.
### Setting the description
- [@MainActor @preconcurrency func description(_ description: Text) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/description(_:)-1bvuj.md)
  Sets the description shown for a widget when a user adds or edits it using the contents of a text view.
- [@MainActor @preconcurrency func description<S>(_ description: S) -> some WidgetConfiguration where S : StringProtocol
](../SwiftUI/WidgetConfiguration/description(_:)-2bfr.md)
  Sets the description shown for a widget when a user adds or edits it using the specified string.
- [@MainActor @preconcurrency func description(_ descriptionKey: LocalizedStringKey) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/description(_:)-4q9pa.md)
  Sets the localized description shown for a widget when a user adds or edits the widget.
### Setting the supported families
- [@MainActor @preconcurrency func supportedFamilies(_ families: [WidgetFamily]) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/supportedFamilies(_:).md)
  Sets the sizes that a widget supports.
- [@MainActor @preconcurrency func supplementalActivityFamilies(_ families: [ActivityFamily]) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/supplementalActivityFamilies(_:).md)
  Sets the sizes that a Live Activity supports.
### Handling background network requests
- [nonisolated func backgroundTask<D, R>(_ task: BackgroundTask<D, R>, action: @escaping (D) async -> R) -> some WidgetConfiguration where D : Sendable, R : Sendable
](../SwiftUI/WidgetConfiguration/backgroundTask(_:action:).md)
  Runs the given action when the system provides a background task.
- [@MainActor @preconcurrency func onBackgroundURLSessionEvents(matching matchingBlock: ((String) -> Bool)? = nil, _ urlSessionEvent: @escaping (String, @escaping () -> Void) -> Void) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/onBackgroundURLSessionEvents(matching:_:)-2e152.md)
  Adds an action to perform when events related to a URL session identified by a closure are waiting to be processed.
- [@MainActor @preconcurrency func onBackgroundURLSessionEvents(matching matchingString: String, _ urlSessionEvent: @escaping (String, @escaping () -> Void) -> Void) -> some WidgetConfiguration
](../SwiftUI/WidgetConfiguration/onBackgroundURLSessionEvents(matching:_:)-fw6x.md)
  Adds an action to perform when events related to a URL session with a matching identifier are waiting to be processed.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [WidgetConfiguration](../SwiftUI/WidgetConfiguration.md)

## See Also

- [Creating a widget extension](creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Supporting additional widget sizes](supporting-additional-widget-sizes.md)
  Offer widgets in additional contexts by adding support for various widget sizes.
- [Creating accessory widgets and watch complications](creating-accessory-widgets-and-watch-complications.md)
  Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [@MainActor @preconcurrency protocol Widget](../SwiftUI/Widget.md)
  The configuration and content of a widget to display on the Home screen or in Notification Center.
- [@MainActor @preconcurrency protocol WidgetBundle](../SwiftUI/WidgetBundle.md)
  A container used to expose multiple widgets from a single widget extension.
- [enum WidgetFamily](widgetfamily.md)
  Values that define the widget’s size and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/staticconfiguration)*