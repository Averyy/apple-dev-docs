# init(_:content:)

**Framework**: Widgetkit  
**Kind**: init

Creates an `AccessoryWidgetGroup` that generates its label from a localized string key.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleKey: LocalizedStringKey, @ViewBuilder content: () -> Content)
```

#### Discussion

This initializer creates a `Text` view on your behalf, and treats the localized key similar to `Text/init(_:tableName:bundle:comment:)`. See `Text` for more information about localizing strings.

## Parameters

- `titleKey`: The key for the  ’s localized label.
- `content`: A view builder for the content of the accessory group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:content:)-nb0)*