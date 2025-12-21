# init(kind:intent:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates a configuration for a control that uses a custom app intent to provide user-configurable options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(kind: String, intent: Configuration.Type = Configuration.self, @ControlWidgetTemplateBuilder content: @escaping (Configuration) -> Content)
```

## Parameters

- `kind`: A string that uniquely identifies the type of control.
- `intent`: A custom intent containing user-editable parameters.
- `content`: A template that renders the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentcontrolconfiguration/init(kind:intent:content:))*