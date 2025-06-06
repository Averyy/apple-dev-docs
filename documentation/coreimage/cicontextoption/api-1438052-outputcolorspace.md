# outputColorSpace

**Framework**: Core Image  
**Kind**: structdata

A key for the color space to use for images before they are rendered to the context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let outputColorSpace: CIContextOption
```

#### Discussion

By default, Core Image uses the GenericRGB color space, which leaves color matching to the system. You can specify a different output color space by providing a Quartz 2D [`CGColorSpace`](https://developer.apple.com/documentation/coregraphics/cgcolorspace) object. (See [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) for information on creating and using [`CGColorSpace`](https://developer.apple.com/documentation/coregraphics/cgcolorspace) objects.)

To request that Core Image perform no color management, specify the [`NSNull`](https://developer.apple.com/documentation/foundation/nsnull) object as the value for this key. Use this option for images that don’t contain color data (such as elevation maps, normal vector maps, and sampled function tables).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/1438052-outputcolorspace)*