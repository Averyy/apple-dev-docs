# init(kind:intent:provider:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates a configuration for a widget by using a custom intent to provide user-configurable options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init<Provider>(kind: String, intent: Intent.Type = Intent.self, provider: Provider, @ViewBuilder content: @escaping (Provider.Entry) -> Content) where Intent == Provider.Intent, Provider : AppIntentTimelineProvider
```

## Parameters

- `kind`: A unique string that you choose.
- `intent`: A custom intent containing user-editable   parameters.
- `provider`: An object that determines the timing of updates   to the widget’s views.
- `content`: A view that renders the widget.

## See Also

- [var body: Self.Body](../SwiftUI/WidgetConfiguration/body-swift.property.md)
  The content and behavior of this widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentconfiguration/init(kind:intent:provider:content:))*