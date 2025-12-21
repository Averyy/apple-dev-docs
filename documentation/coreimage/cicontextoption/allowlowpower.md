# allowLowPower

**Framework**: Core Image  
**Kind**: property

A Boolean value to control the power level of Core Image context renders.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static let allowLowPower: CIContextOption
```

#### Discussion

This option only affects certain macOS devices with more than one available GPU device.

If this value is True, then rendering with the context will use a use allow power GPU device if available and the high power device is not already in use.

Otherwise, the context will use the highest power/performance GPU device.

## See Also

- [static let cacheIntermediates: CIContextOption](cicontextoption/cacheintermediates.md)
  A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [static let highQualityDownsample: CIContextOption](cicontextoption/highqualitydownsample.md)
  A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [static let memoryTarget: CIContextOption](cicontextoption/memorytarget.md)
  A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [static let name: CIContextOption](cicontextoption/name.md)
  A Boolean value to specify a client-provided name for a context.
- [static let outputColorSpace: CIContextOption](cicontextoption/outputcolorspace.md)
  A Core Image context option key to specify the default destination color space for rendering.
- [static let outputPremultiplied: CIContextOption](cicontextoption/outputpremultiplied.md)
  A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [static let priorityRequestLow: CIContextOption](cicontextoption/priorityrequestlow.md)
  A Boolean value to control the priority Core Image context renders.
- [static let useSoftwareRenderer: CIContextOption](cicontextoption/usesoftwarerenderer.md)
  A Boolean value to control if a Core Image context will use a software renderer.
- [static let workingColorSpace: CIContextOption](cicontextoption/workingcolorspace.md)
  A Core Image context option key to specify the working color space for rendering.
- [static let workingFormat: CIContextOption](cicontextoption/workingformat.md)
  A Core Image context option key to specify the pixel format to for intermediate results when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/allowlowpower)*