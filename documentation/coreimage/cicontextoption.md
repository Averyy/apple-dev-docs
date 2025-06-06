# CIContextOption

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct CIContextOption
```

## Topics

### Initializers
- [init(rawValue: String)](cicontextoption/2998470-init.md)
### Type Properties
- [static let allowLowPower: CIContextOption](cicontextoption/3201363-allowlowpower.md)
- [static let cacheIntermediates: CIContextOption](cicontextoption/1642217-cacheintermediates.md)
  An option for whether the context caches the contents of any intermediate pixel buffers it uses during rendering.
- [static let highQualityDownsample: CIContextOption](cicontextoption/1437699-highqualitydownsample.md)
  An option controlling the quality of image downsampling operations performed by the context.
- [static let memoryTarget: CIContextOption](cicontextoption/4172811-memorytarget.md)
- [static let name: CIContextOption](cicontextoption/3577534-name.md)
- [static let outputColorSpace: CIContextOption](cicontextoption/1438052-outputcolorspace.md)
  A key for the color space to use for images before they are rendered to the context.
- [static let outputPremultiplied: CIContextOption](cicontextoption/1642216-outputpremultiplied.md)
  An option for whether output rendering by the context produces alpha-premultiplied pixels.
- [static let priorityRequestLow: CIContextOption](cicontextoption/1620424-priorityrequestlow.md)
  A key for enabling low-priority GPU use.
- [static let useSoftwareRenderer: CIContextOption](cicontextoption/1438047-usesoftwarerenderer.md)
  A key for enabling software renderer use.  If the associated [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) object  is [`true`](https://developer.apple.com/documentation/swift/true), the software renderer is required. 
- [static let workingColorSpace: CIContextOption](cicontextoption/1437728-workingcolorspace.md)
  A key for the color space to use for image operations.
- [static let workingFormat: CIContextOption](cicontextoption/1437788-workingformat.md)
  An option for the color format to use for intermediate results when rendering with the context.

## Relationships

### Conforms To
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption)*