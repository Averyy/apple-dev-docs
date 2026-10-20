# init(_:image:content:)

**Framework**: WidgetKit  
**Kind**: init  
**Role**: Initializer

Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and image resource.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleResource: LocalizedStringResource, image: ImageResource, @ViewBuilder content: () -> Content)
```

Available when `Label` is `Label<Text, Image>` and `Content` conforms to `View`.

#### Discussion

This initializer creates a `Label` view on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `titleResource`: Resource for the `AccessoryWidgetGroup`’s localized label.
- `image`: The image resource to lookup.
- `content`: A view builder for the content of the accessory group.

## See Also

### Creating an accessory widget group
- [init(some StringProtocol, content: () -> Content)](./init%28_,content%29-3ij0e.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a string.
- [init(LocalizedStringResource, content: () -> Content)](./init%28_,content%29-75rkg.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource.
- [init(LocalizedStringKey, content: () -> Content)](./init%28_,content%29-nb0.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string key.
- [init(LocalizedStringKey, image: ImageResource, content: () -> Content)](./init%28_,image,content%29-50iyk.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string key and image resource.
- [init(some StringProtocol, image: ImageResource, content: () -> Content)](./init%28_,image,content%29-66iys.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a string and image resource.
- [init(LocalizedStringResource, systemImage: String, content: () -> Content)](./init%28_,systemimage,content%29-3mynu.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and a system image name.
- [init(LocalizedStringKey, systemImage: String, content: () -> Content)](./init%28_,systemimage,content%29-54h9w.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string key and a system image name.
- [init(some StringProtocol, systemImage: String, content: () -> Content)](./init%28_,systemimage,content%29-7rnqc.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a string and system image name.
- [init(label: () -> Label, content: () -> Content)](./init%28label,content%29.md)
  Creates an AccessoryWidgetGroup composed of a label and three circular or rounded square contents with equal spacing and vertical alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(_:image:content:)-385rt)*