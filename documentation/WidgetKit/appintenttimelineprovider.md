# AppIntentTimelineProvider

**Framework**: Widgetkit  
**Kind**: protocol

A type that advises WidgetKit when to update a user-configurable widget’s display.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- watchOS 10.0+

## Declaration

```swift
protocol AppIntentTimelineProvider
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)
- [Making a configurable widget](making-a-configurable-widget.md)

#### Overview

An App Intent timeline provider performs the same function as [`TimelineProvider`](timelineprovider.md), but it also incorporates user-configured details into timeline entries.

For example, in a widget that displays the health status of a game character the user has chosen, the provider receives a custom intent specifying the character to display. In your app code, you then define a custom App Intent. The intent can include the character’s details such as its name, avatar, strategic alliances, and so on.

```swift
struct CharacterConfiguration: WidgetConfigurationIntent {
    static var title: LocalizedStringResource = "Character"

    @Parameter(title: "Name")
    var name: String

    @Parameter(title: "Avatar", default: "Player 1")
    var avatar: String

    @Parameter(title: "Alliances", default: [])
    var alliances: [String]

    @Parameter(title: "Health", default: 100.0)
    var healthLevel: Double
}
```

Because users can add multiple instances of a particular widget, your provider needs a way to differentiate which instance WidgetKit is asking about. When WidgetKit calls [`snapshot(for:in:)`](appintenttimelineprovider/snapshot(for:in:).md) or [`timeline(for:in:)`](appintenttimelineprovider/timeline(for:in:).md), it passes an instance of your configuration intent, configured with the user-selected details. The game widget provider accesses the properties of the intent and includes them in the [`TimelineEntry`](timelineentry.md). WidgetKit then invokes the widget configuration’s content closure, passing the timeline entry to allow the views to access the user-configured properties. For example, the provider might implement a `TimelineEntry` with properties corresponding to those in the custom intent:

```swift
struct CharacterDetailEntry: TimelineEntry {
    var date: Date
    var name: String
    var avatar: String
    var alliances: [String]
    var healthLevel: Double
}
```

To generate a snapshot, the game widget provider initializes the character detail entry using the properties from the intent.

```swift
struct CharacterDetailProvider: AppIntentTimelineProvider {
    func snapshot(for configuration: CharacterConfiguration, in context: Context) async -> CharacterDetailEntry {
        return CharacterDetailEntry(
            date: Date(),
            name: configuration.characterName,
            avatar: configuration.avatar,
            alliances: configuration.alliances,
            healthLevel: configuration.healthLevel?.doubleValue
        )
    }
}
```

## Topics

### Generating timelines
- [func placeholder(in: Self.Context) -> Self.Entry](appintenttimelineprovider/placeholder(in:).md)
  Provides a timeline entry representing a placeholder version of the widget.
- [func recommendations() -> [AppIntentRecommendation<Self.Intent>]](appintenttimelineprovider/recommendations.md)
  Returns a set of intent recommendations you use to offer pre-configured widgets on platforms that don’t offer a dedicated user interface for customizing widget intents.
- [func snapshot(for: Self.Intent, in: Self.Context) async -> Self.Entry](appintenttimelineprovider/snapshot(for:in:).md)
  Provides a timeline entry representing the current time and state of a widget.
- [func timeline(for: Self.Intent, in: Self.Context) async -> Timeline<Self.Entry>](appintenttimelineprovider/timeline(for:in:).md)
  Provides an array of timeline entries for the current time and, optionally, any future times to update a widget.
- [AppIntentTimelineProvider.Context](appintenttimelineprovider/context.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [associatedtype Entry : TimelineEntry](appintenttimelineprovider/entry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [associatedtype Intent : WidgetConfigurationIntent](appintenttimelineprovider/intent.md)
  The intent that contains user-customized values.
### Instance Methods
- [func relevance() async -> WidgetRelevance<Self.Intent>](appintenttimelineprovider/relevance.md)
  Provides an object containing attributes that describe when a specific widget could be relevant.

## See Also

- [Keeping a widget up to date](keeping-a-widget-up-to-date.md)
  Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [protocol TimelineProvider](timelineprovider.md)
  A type that advises WidgetKit when to update a widget’s display.
- [protocol IntentTimelineProvider](intenttimelineprovider.md)
  A type that advises WidgetKit when to update a user-configurable widget’s display.
- [struct TimelineProviderContext](timelineprovidercontext.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [protocol TimelineEntry](timelineentry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [struct Timeline](timeline.md)
  An object that specifies a date for WidgetKit to update a widget’s view.
- [class WidgetCenter](widgetcenter.md)
  An object that contains a list of user-configured widgets and is used for reloading widget timelines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintenttimelineprovider)*