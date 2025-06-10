# priorityRequestLow

**Framework**: Core Image  
**Kind**: property

A key for enabling low-priority GPU use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
static let priorityRequestLow: CIContextOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. If this value is [`true`](https://developer.apple.com/documentation/swift/true), use of the Core Image context from a background thread takes lower priority than GPU usage from the main thread, allowing your app to perform Core Image rendering without disturbing the frame rate of UI animations.

## See Also

- [static let allowLowPower: CIContextOption](cicontextoption/allowlowpower.md)
- [static let cacheIntermediates: CIContextOption](cicontextoption/cacheintermediates.md)
  An option for whether the context caches the contents of any intermediate pixel buffers it uses during rendering.
- [static let highQualityDownsample: CIContextOption](cicontextoption/highqualitydownsample.md)
  An option controlling the quality of image downsampling operations performed by the context.
- [static let memoryTarget: CIContextOption](cicontextoption/memorytarget.md)
- [static let name: CIContextOption](cicontextoption/name.md)
- [static let outputColorSpace: CIContextOption](cicontextoption/outputcolorspace.md)
  A key for the color space to use for images before they are rendered to the context.
- [static let outputPremultiplied: CIContextOption](cicontextoption/outputpremultiplied.md)
  An option for whether output rendering by the context produces alpha-premultiplied pixels.
- [static let useSoftwareRenderer: CIContextOption](cicontextoption/usesoftwarerenderer.md)
  A key for enabling software renderer use.
- [static let workingColorSpace: CIContextOption](cicontextoption/workingcolorspace.md)
  A key for the color space to use for image operations.
- [static let workingFormat: CIContextOption](cicontextoption/workingformat.md)
  An option for the color format to use for intermediate results when rendering with the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/priorityrequestlow)*