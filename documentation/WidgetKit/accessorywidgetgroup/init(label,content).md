# init(label:content:)

**Framework**: WidgetKit  
**Kind**: init  
**Role**: Initializer

Creates an AccessoryWidgetGroup composed of a label and three circular or rounded square contents with equal spacing and vertical alignment.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder label: () -> Label, @ViewBuilder content: () -> Content)
```

Available when `Label` conforms to `View` and `Content` conforms to `View`.

## Parameters

- `label`: A label or a text to show up on the top corner of the widget view to describe the purpose of the group.
- `content`: A view builder for the content of the accessory group.

## See Also

### Creating an accessory widget group
- [init(some StringProtocol, content: () -> Content)](./init%28_,content%29-3ij0e.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a string.
- [init(LocalizedStringResource, content: () -> Content)](./init%28_,content%29-75rkg.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource.
- [init(LocalizedStringKey, content: () -> Content)](./init%28_,content%29-nb0.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string key.
- [init(LocalizedStringResource, image: ImageResource, content: () -> Content)](./init%28_,image,content%29-385rt.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and image resource.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup/init(label:content:))*