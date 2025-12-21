# init(kind:intent:provider:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates a configuration for a widget by using a custom intent definition to provide user-configurable options.

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
@preconcurrency init<Provider>(kind: String, intent: Intent.Type, provider: Provider, @ViewBuilder content: @escaping (Provider.Entry) -> Content) where Intent == Provider.Intent, Provider : IntentTimelineProvider
```

## Parameters

- `kind`: A unique string that you choose.
- `intent`: A custom intent definition containing user-editable   parameters.
- `provider`: An object that determines the timing of updates   to the widget’s views.
- `content`: A view that renders the widget.

## See Also

- [var body: Self.Body](../SwiftUI/WidgetConfiguration/body-swift.property.md)
  The content and behavior of this widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/intentconfiguration/init(kind:intent:provider:content:))*