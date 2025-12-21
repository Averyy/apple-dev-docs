# workingColorSpace

**Framework**: Core Image  
**Kind**: property

A Core Image context option key to specify the working color space for rendering.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static let workingColorSpace: CIContextOption
```

#### Discussion

Contexts support automatic color management by performing all processing operations in a working color space. This means that unless told otherwise:

- All input images are color matched from the input’s color space to the working space.
- All renders are color matched from the working space to the destination’s color space.

The default working space is the extended sRGB color space with linear gamma. On macOS before 10.10, the default is extended Generic RGB with linear gamma.

The value of this option can be either:

- A `CGColorSpace` instance with an RGB color model that supports output.
- An `NSNull` instance to request that Core Image perform no color management.

If this option is not specified, then the default working space is used.

## See Also

- [static let allowLowPower: CIContextOption](cicontextoption/allowlowpower.md)
  A Boolean value to control the power level of Core Image context renders.
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
- [static let workingFormat: CIContextOption](cicontextoption/workingformat.md)
  A Core Image context option key to specify the pixel format to for intermediate results when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/workingcolorspace)*