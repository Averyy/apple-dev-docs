# cacheIntermediates

**Framework**: Core Image  
**Kind**: property

An option for whether the context caches the contents of any intermediate pixel buffers it uses during rendering.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
static let cacheIntermediates: CIContextOption
```

#### Discussion

The value for this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value. If this value is [`false`](https://developer.apple.com/documentation/swift/false), the context empties such buffers during and after renders. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [static let allowLowPower: CIContextOption](cicontextoption/allowlowpower.md)
- [static let highQualityDownsample: CIContextOption](cicontextoption/highqualitydownsample.md)
  An option controlling the quality of image downsampling operations performed by the context.
- [static let memoryTarget: CIContextOption](cicontextoption/memorytarget.md)
- [static let name: CIContextOption](cicontextoption/name.md)
- [static let outputColorSpace: CIContextOption](cicontextoption/outputcolorspace.md)
  A key for the color space to use for images before they are rendered to the context.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/cacheintermediates)*