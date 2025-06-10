# init(_:image:content:)

**Framework**: WidgetKit  
**Kind**: init

Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and image resource.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleResource: LocalizedStringResource, image: ImageResource, @ViewBuilder content: () -> Content)
```

#### Discussion

This initializer creates a `Label` view on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `titleResource`: Resource for the  ’s localized   label.
- `image`: The image resource to lookup.
- `content`: A view builder for the content of the accessory group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:image:content:)-385rt)*