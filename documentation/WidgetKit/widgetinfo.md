# WidgetInfo

**Framework**: WidgetKit  
**Kind**: struct

A structure that contains information about user-configured widgets.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
struct WidgetInfo
```

## Mentions

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md)
- [Making a configurable widget](making-a-configurable-widget.md)

## Topics

### Getting Configured Widget Information
- [let kind: String](widgetinfo/kind.md)
  The string specified during creation of the widget’s configuration.
- [let family: WidgetFamily](widgetinfo/family.md)
  The size of the widget: small, medium, or large.
- [let configuration: INIntent?](widgetinfo/configuration.md)
  A SiriKit intent that contains user-edited values.
### Identifying Widget Information
- [var id: WidgetInfo](widgetinfo/id.md)
  The stable identity of the widget.
### Instance Methods
- [func widgetConfigurationIntent<Intent>(of: Intent.Type) -> Intent?](widgetinfo/widgetconfigurationintent(of:).md)
  Gets the associated App Intent.
### Default Implementations
- [Identifiable Implementations](widgetinfo/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Making a configurable widget](making-a-configurable-widget.md)
  Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](migrating-from-sirikit-intents-to-app-intents.md)
  Configure your widgets for backward compatibility.
- [struct AppIntentConfiguration](appintentconfiguration.md)
  An object describing the content of a widget that uses a custom intent to provide user-configurable options.
- [struct AppIntentRecommendation](appintentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.
- [struct IntentConfiguration](intentconfiguration.md)
  An object describing the content of a widget that uses a custom intent definition to provide user-configurable options.
- [struct IntentRecommendation](intentrecommendation.md)
  An object that describes a recommended intent configuration for a user-customizable widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetinfo)*