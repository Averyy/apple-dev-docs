# workingColorSpace

**Framework**: Core Image  
**Kind**: instp

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

The working color space determines the color space used when executing filter kernels; Core Image automatically converts to and from the source and destination color spaces of input images and output contexts. You specify a working color space using the [`workingColorSpace`](cicontextoption/1437728-workingcolorspace.md) key in the `options` dictionary when creating a Core Image context.

## See Also

- [func clearCaches()](cicontext/1437790-clearcaches.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](cicontext/1437967-reclaimresources.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](cicontext/1437817-offlinegpucount.md)
  Returns the number of GPUs not currently driving a display.
- [var workingFormat: CIFormat](cicontext/1642215-workingformat.md)
  The working pixel format of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/1438061-workingcolorspace)*