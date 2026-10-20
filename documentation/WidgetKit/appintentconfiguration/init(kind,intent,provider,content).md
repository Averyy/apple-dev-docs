# init(kind:intent:provider:content:)

**Framework**: WidgetKit  
**Kind**: init  
**Role**: Initializer

Creates a configuration for a widget by using a custom intent to provide user-configurable options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 26.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency init<Provider>(kind: String, intent: Intent.Type = Intent.self, provider: Provider, @ViewBuilder content: @escaping (Provider.Entry) -> Content) where Intent == Provider.Intent, Provider : AppIntentTimelineProvider
```

Available when `Intent` conforms to `WidgetConfigurationIntent` and `Content` conforms to `View`.

## Parameters

- `kind`: A unique string that you choose.
- `intent`: A custom intent containing user-editable parameters.
- `provider`: An object that determines the timing of updates to the widget’s views.
- `content`: A view that renders the widget.

## See Also

### Creating a widget configuration
- [var body: Self.Body](../../SwiftUI/widgetconfiguration/body-swift.property.md)
  The content and behavior of this widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/appintentconfiguration/init(kind:intent:provider:content:))*