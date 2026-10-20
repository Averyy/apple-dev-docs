# WidgetInfo

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

A structure that contains information about user-configured widgets.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
struct WidgetInfo
```

## Mentions

- [Making a configurable widget](./making-a-configurable-widget.md)
- [Updating widgets with WidgetKit push notifications](./updating-widgets-with-widgetkit-push-notifications.md)

## Topics

### Getting Configured Widget Information
- [let kind: String](./widgetinfo/kind.md)
  The string specified during creation of the widget’s configuration.
- [let family: WidgetFamily](./widgetinfo/family.md)
  The size of the widget: small, medium, or large.
- [let configuration: INIntent?](./widgetinfo/configuration.md)
  A SiriKit intent that contains user-edited values.
### Identifying Widget Information
- [var id: WidgetInfo](./widgetinfo/id.md)
  The stable identity of the widget.
### Instance Methods
- [func widgetConfigurationIntent<Intent>(of: Intent.Type) -> Intent?](./widgetinfo/widgetconfigurationintent%28of%29.md)
  Gets the associated App Intent.
### Default Implementations
- [Identifiable Implementations](./widgetinfo/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configurable widgets
- [Making a configurable widget](./making-a-configurable-widget.md)
  Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](./migrating-from-sirikit-intents-to-app-intents.md)
  Configure your widgets for backward compatibility.
- [struct AppIntentConfiguration](./appintentconfiguration.md)
  An object describing the content of a widget that uses a custom intent to provide user-configurable options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetinfo)*