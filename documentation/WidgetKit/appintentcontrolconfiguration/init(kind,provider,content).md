# init(kind:provider:content:)

**Framework**: WidgetKit  
**Kind**: init  
**Role**: Initializer

Creates a configuration for a control that uses a custom app intent to provide user-configurable options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init<Provider>(kind: String, provider: Provider, @ControlWidgetTemplateBuilder content: @escaping (Provider.Value) -> Content) where Configuration == Provider.Configuration, Provider : AppIntentControlValueProvider
```

Available when `Configuration` conforms to `ControlConfigurationIntent` and `Content` conforms to `ControlWidgetTemplate`.

## Parameters

- `kind`: A string that uniquely identifies the type of control.
- `provider`: An object that provides a value to the control template. The provider uses your custom intent to prepare this value.
- `content`: A template that renders the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentcontrolconfiguration/init(kind:provider:content:))*