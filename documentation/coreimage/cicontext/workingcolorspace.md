# workingColorSpace

**Framework**: Core Image  
**Kind**: property

The working color space of the Core Image context.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var workingColorSpace: CGColorSpace? { get }
```

#### Discussion

The working color space determines the color space used when executing filter kernels; Core Image automatically converts to and from the source and destination color spaces of input images and output contexts. You specify a working color space using the [`workingColorSpace`](cicontextoption/workingcolorspace.md) key in the `options` dictionary when creating a Core Image context.

## See Also

- [func clearCaches()](cicontext/clearcaches.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](cicontext/reclaimresources.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](cicontext/offlinegpucount.md)
  Returns the number of GPUs not currently driving a display.
- [var workingFormat: CIFormat](cicontext/workingformat.md)
  The working pixel format of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/workingcolorspace)*