# init(_:content:)

**Framework**: Widgetkit  
**Kind**: init

Creates an `AccessoryWidgetGroup` that generates its label from a string.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ title: some StringProtocol, @ViewBuilder content: () -> Content)
```

#### Discussion

This initializer creates a `Text` view on your behalf, and treats the label similar to `Text/init(_:)-9d1g4`. See `Text` for more information about localizing strings.

## Parameters

- `title`: A string for the label of  .
- `content`: A view builder for the content of the accessory group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:content:)-3ij0e)*