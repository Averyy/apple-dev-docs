# init(kind:provider:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates a configuration for a widget, with no user-configurable options.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency init<Provider>(kind: String, provider: Provider, @ViewBuilder content: @escaping (Provider.Entry) -> Content) where Provider : TimelineProvider
```

## Parameters

- `kind`: A unique string that you choose.
- `provider`: An object that determines the timing of updates   to the widget’s views.
- `content`: A view that renders the widget.

## See Also

- [@MainActor @preconcurrency var body: Self.Body { get }](../SwiftUI/WidgetConfiguration/body-swift.property.md)
  The content and behavior of this widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/staticconfiguration/init(kind:provider:content:))*