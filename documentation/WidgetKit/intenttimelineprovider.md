# IntentTimelineProvider

**Framework**: Widgetkit  
**Kind**: protocol

A type that advises WidgetKit when to update a user-configurable widget’s display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
protocol IntentTimelineProvider
```

#### Overview

An Intent timeline provider performs the same function as [`TimelineProvider`](timelineprovider.md), but it also incorporates user-configured details into timeline entries.

For example, in a widget that displays the health status of a game character the user has chosen, the provider receives a custom intent specifying the character to display. In your Xcode project, you then define a custom SiriKit Intent Definition file. The intent definition can include the character’s details such as its name, avatar, strategic alliances, and so on.

![A screenshot showing a custom intent definition file configured with an](https://docs-assets.developer.apple.com/published/cc1a99720381abca170a6ba17b6b24e6/IntentTimelineProvider-IntentDefinition%402x.png)

Xcode generates the following [`INIntent`](https://developer.apple.com/documentation/Intents/INIntent) custom intent:

```swift
public class SelectCharacterIntent: INIntent {
    @NSManaged public var characterName: String?
    @NSManaged public var avatar: String?
    @NSManaged public var alliances: [String]?
    @NSManaged public var healthLevel: NSNumber?
}
```

Because users can add multiple instances of a particular widget, your provider needs a way to differentiate which instance WidgetKit is asking about. When WidgetKit calls [`getSnapshot(for:in:completion:)`](intenttimelineprovider/getsnapshot(for:in:completion:).md) or [`getTimeline(for:in:completion:)`](intenttimelineprovider/gettimeline(for:in:completion:).md), it passes an instance of your custom `INIntent`, configured with the user-selected details. The game widget provider accesses the properties of the intent and includes them in the [`TimelineEntry`](timelineentry.md). WidgetKit then invokes the widget configuration’s content closure, passing the timeline entry to allow the views to access the user-configured properties. For example, the provider might implement a `TimelineEntry` with properties corresponding to those in the custom intent:

```swift
struct CharacterDetailEntry: TimelineEntry {
    var date: Date
    var name: String?
    var avatar: String?
    var alliances: [String]?
    var healthLevel: Double?
}
```

To generate a snapshot, the game widget provider initializes the character detail entry using the properties from the intent.

```swift
struct CharacterDetailProvider: IntentTimelineProvider {
    func getSnapshot(for configuration: SelectCharacterIntent, in context: Context, completion: @escaping (CharacterDetailEntry) -> Void) {
        let entry = CharacterDetailEntry(
            date: Date(),
            name: configuration.characterName,
            avatar: configuration.avatar,
            alliances: configuration.alliances,
            healthLevel: configuration.healthLevel?.doubleValue
        )
        completion(entry)
    }
}
```

## Topics

### Generating Timelines
- [func getSnapshot(for: Self.Intent, in: Self.Context, completion: (Self.Entry) -> Void)](intenttimelineprovider/getsnapshot(for:in:completion:).md)
  Provides a timeline entry representing the current time and state of a widget.
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
### Instance Methods
- [func relevance() async -> WidgetRelevance<Self.Intent>](intenttimelineprovider/relevance.md)
  Provides an object containing attributes that describe when a specific widget could be relevant.

## See Also

- [class INIntent](../Intents/INIntent.md)
  A request to fulfill in your app or Intents extension.
- [Keeping a widget up to date](keeping-a-widget-up-to-date.md)
  Plan your widget’s timeline to show timely, relevant information using dynamic views, and update the timeline when things change.
- [protocol TimelineProvider](timelineprovider.md)
  A type that advises WidgetKit when to update a widget’s display.
- [struct TimelineProviderContext](timelineprovidercontext.md)
  An object that contains details about how a widget is rendered, including its size and whether it appears in the widget gallery.
- [protocol TimelineEntry](timelineentry.md)
  A type that specifies the date to display a widget, and, optionally, indicates the current relevance of the widget’s content.
- [struct Timeline](timeline.md)
  An object that specifies a date for WidgetKit to update a widget’s view.
- [class WidgetCenter](widgetcenter.md)
  An object that contains a list of user-configured widgets and is used for reloading widget timelines.
- [protocol AppIntentTimelineProvider](appintenttimelineprovider.md)
  A type that advises WidgetKit when to update a user-configurable widget’s display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intenttimelineprovider)*