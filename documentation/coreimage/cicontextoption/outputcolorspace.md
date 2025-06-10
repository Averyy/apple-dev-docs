# outputColorSpace

**Framework**: Core Image  
**Kind**: property

A key for the color space to use for images before they are rendered to the context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static let outputColorSpace: CIContextOption
```

#### Discussion

By default, Core Image uses the GenericRGB color space, which leaves color matching to the system. You can specify a different output color space by providing a Quartz 2D [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) object. (See [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) for information on creating and using [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace) objects.)

To request that Core Image perform no color management, specify the [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) object as the value for this key. Use this option for images that don’t contain color data (such as elevation maps, normal vector maps, and sampled function tables).

## See Also

- [static let allowLowPower: CIContextOption](cicontextoption/allowlowpower.md)
- [static let cacheIntermediates: CIContextOption](cicontextoption/cacheintermediates.md)
  An option for whether the context caches the contents of any intermediate pixel buffers it uses during rendering.
- [static let highQualityDownsample: CIContextOption](cicontextoption/highqualitydownsample.md)
  An option controlling the quality of image downsampling operations performed by the context.
- [static let memoryTarget: CIContextOption](cicontextoption/memorytarget.md)
- [static let name: CIContextOption](cicontextoption/name.md)
- [static let outputPremultiplied: CIContextOption](cicontextoption/outputpremultiplied.md)
  An option for whether output rendering by the context produces alpha-premultiplied pixels.
- [static let priorityRequestLow: CIContextOption](cicontextoption/priorityrequestlow.md)
  A key for enabling low-priority GPU use.
- [static let useSoftwareRenderer: CIContextOption](cicontextoption/usesoftwarerenderer.md)
  A key for enabling software renderer use.
- [static let workingColorSpace: CIContextOption](cicontextoption/workingcolorspace.md)
  A key for the color space to use for image operations.
- [static let workingFormat: CIContextOption](cicontextoption/workingformat.md)
  An option for the color format to use for intermediate results when rendering with the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/outputcolorspace)*