# IntentConfiguration

**Framework**: WidgetKit  
**Kind**: struct

An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.

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
@preconcurrency struct IntentConfiguration<Intent, Content> where Intent : INIntent, Content : View
```

#### Overview

The following example shows the configuration for a game widget that displays details about a chosen character.

```swift
struct CharacterDetailWidget: Widget {
    var body: some WidgetConfiguration {
        IntentConfiguration(
            kind: "com.mygame.character-detail",
            intent: SelectCharacterIntent.self,
            provider: CharacterDetailProvider(),
        ) { entry in
            CharacterDetailView(entry: entry)
        }
        .configurationDisplayName("Character Details")
        .description("Displays a character's health and other details")
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}
```

Every widget has a unique `kind`, a string that you choose. You use this string to identify your widget when reloading its timeline with [`WidgetCenter`](widgetcenter.md).

The `intent` is a custom SiriKit intent definition containing user-editable parameters.

The timeline provider is an object that determines the timeline for refreshing your widget. Providing future dates for updating your widget allows the system to optimize the refresh process.

The content closure contains the SwiftUI views that WidgetKit needs to render the widget. When WidgetKit invokes the content closure, it passes a timeline entry created by the widget provider’s [`getSnapshot(for:in:completion:)`](intenttimelineprovider/getsnapshot(for:in:completion:).md) or [`getTimeline(for:in:completion:)`](intenttimelineprovider/gettimeline(for:in:completion:).md) method.

Modifiers let you specify the families your widget supports, and the details shown when users add or edit their widgets.

## Topics

### Creating a widget configuration
- [init<Provider>(kind: String, intent: Intent.Type, provider: Provider, content: (Provider.Entry) -> Content)](intentconfiguration/init(kind:intent:provider:content:).md)
  Creates a configuration for a widget by using a custom intent definition to provide user-configurable options.
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

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)
  Provide contextual information and donate intents to the system to make sure your widget appears prominently in Smart Stacks.
- [struct TimelineEntryRelevance](timelineentryrelevance.md)
  An object that describes the relative importance of a timeline entry compared to other entries in the current and past timelines.
- [struct RelevanceConfiguration](relevanceconfiguration.md)
  A type that describes the content of a widget that uses relevance clues.
- [protocol RelevanceEntriesProvider](relevanceentriesprovider.md)
  A type that provides the content for a widget that uses relevance clues to display information in the Smart Stack.
- [protocol RelevanceEntry](relevanceentry.md)
  A type that specifies the information to render a widget at a specific relevance configuration.
- [struct WidgetRelevance](widgetrelevance.md)
  A type collecting the relevances for a widget kind.
- [struct WidgetRelevanceAttribute](widgetrelevanceattribute.md)
  A type that describes when a specific widget could be relevant.
- [struct WidgetRelevanceGroup](widgetrelevancegroup.md)
  A type for configuring widget behavior in the watchOS Smart Stack.
- [struct AppIntentRecommendation](appintentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.
- [struct IntentRecommendation](intentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intentconfiguration)*