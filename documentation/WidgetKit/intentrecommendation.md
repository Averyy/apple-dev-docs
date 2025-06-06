# IntentRecommendation

**Framework**: Widgetkit  
**Kind**: struct

An object that describes a recommended intent configuration for a user-customizable widget.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
struct IntentRecommendation<T> where T : INIntent
```

#### Overview

By adding a custom SiriKit intent definition to your project and using an [`IntentTimelineProvider`](intenttimelineprovider.md), you allow users to configure widgets to show data that’s most relevant to them. Some platforms don’t have a dedicated user interface to configure all of your intent parameters. For example, watchOS doesn’t offer a dedicated user interface to configure data that appears on a complication. Use intent recommendations in watchOS to offer preconfigured complications that show data that’s most relevant to the user.

> **Note**: On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `IntentRecommendation` is inactive.

For example, say you develop a game app that allows users to view their in-game character. With intent recommendations, you can recommend an intent configuration for a watch complication that displays character information.

The following example shows a function to create a list of recommended configurations for a game widget that shows current energy levels for a game character.

```swift
public func recommendations() -> [IntentRecommendation<DynamicCharacterSelectionIntent>] {
    return CharacterDetail.availableCharacters.
        map { character in
            let hero = Hero(identifier: character.name, display: character.name)
            let intent = DynamicCharacterSelectionIntent()
            intent.hero = hero

            return IntentRecommendation(intent: intent, description: Text(character.name))
        }
    }
```

## Topics

### Creating a Recommended Widget Configuration
- [init(intent: T, description: LocalizedStringKey)](intentrecommendation/init(intent:description:)-1zh33.md)
  Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets with a localized description.
- [init(intent: T, description: Text)](intentrecommendation/init(intent:description:)-4epo2.md)
  Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.
- [init<S>(intent: T, description: S)](intentrecommendation/init(intent:description:)-6v7dj.md)
  Creates a recommended configuration for a widget on platforms that don’t offer a dedicated user interface to customize widgets.

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
- [struct IntentConfiguration](intentconfiguration.md)
  An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WidgetKit/intentrecommendation)*