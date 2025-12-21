# init(kind:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates a configuration for a control, with no user-configurable options.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(kind: String, @ControlWidgetTemplateBuilder content: @escaping () -> Content)
```

## Parameters

- `kind`: A string that uniquely identifies the type of control.
- `content`: A template that renders the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/staticcontrolconfiguration/init(kind:content:))*