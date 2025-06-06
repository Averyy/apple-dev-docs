# init(label:content:)

**Framework**: Widgetkit  
**Kind**: init

Creates an AccessoryWidgetGroup composed of a label and three circular or rounded square contents with equal spacing and vertical alignment.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder label: () -> Label, @ViewBuilder content: () -> Content)
```

## Parameters

- `label`: A label or a text to show up on the top corner of the widget view to describe the purpose of the group.
- `content`: A view builder for the content of the accessory group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(label:content:))*