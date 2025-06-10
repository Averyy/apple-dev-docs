# init(kind:provider:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates a configuration for a control, with no user-configurable options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init<Provider>(kind: String, provider: Provider, @ControlWidgetTemplateBuilder content: @escaping (Provider.Value) -> Content) where Provider : ControlValueProvider
```

## Parameters

- `kind`: A string that uniquely identifies the type of control.
- `provider`: An object that provides a value to the control template.
- `content`: A template that renders the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/staticcontrolconfiguration/init(kind:provider:content:))*