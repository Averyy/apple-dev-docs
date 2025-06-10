# init(_:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleResource: LocalizedStringResource, @ViewBuilder content: () -> Content)
```

#### Discussion

This initializer creates a `Text` view on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `titleResource`: Resource for the  ’s localized   label.
- `content`: A view builder for the content of the accessory group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:content:)-75rkg)*