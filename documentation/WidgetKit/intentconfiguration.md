# IntentConfiguration

**Framework**: WidgetKit  
**Kind**: struct

An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.

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

- [Making a configurable widget](making-a-configurable-widget.md)
  Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](migrating-from-sirikit-intents-to-app-intents.md)
  Configure your widgets for backward compatibility.
- [struct AppIntentConfiguration](appintentconfiguration.md)
  An object describing the content of a widget that uses a custom intent to provide user-configurable options.
- [struct WidgetInfo](widgetinfo.md)
  A structure that contains information about user-configured widgets.
- [struct AppIntentRecommendation](appintentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.
- [struct IntentRecommendation](intentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intentconfiguration)*