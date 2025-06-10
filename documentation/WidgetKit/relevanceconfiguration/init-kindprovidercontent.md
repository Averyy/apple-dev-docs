# init(kind:provider:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates a configuration for a widget that provides relevance clues to the system.

**Availability**:
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init<Provider>(kind: String, provider: Provider, @ViewBuilder content: @escaping @MainActor (Provider.Entry) -> Content) where Provider : RelevanceEntriesProvider
```

## Parameters

- `kind`: A unique string that you choose.
- `provider`: An object that determines the relevance and data of the widget.
- `content`: A view that renders the widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/relevanceconfiguration/init(kind:provider:content:))*