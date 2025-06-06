# init(_:image:content:)

**Framework**: Widgetkit  
**Kind**: init

Creates an `AccessoryWidgetGroup` that generates its label from a string and image resource.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ title: some StringProtocol, image: ImageResource, @ViewBuilder content: () -> Content)
```

#### Discussion

This initializer creates a `Label` view on your behalf, and treats the label similar to `Text/init(_:)-9d1g4`. See `Text` for more information about localizing strings.

## Parameters

- `title`: A string for the label of  .
- `image`: The image resource to lookup.
- `content`: A view builder for the content of the accessory group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:image:content:)-66iys)*