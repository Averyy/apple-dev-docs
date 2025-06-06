# workingFormat

**Framework**: Core Image  
**Kind**: instp

The working pixel format of the Core Image context.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var workingFormat: CIFormat { get }
```

#### Discussion

The working format determines the pixel format that Core Image uses to create intermediate buffers for executing filter kernels. Core Image automatically converts to and from the source and destination pixel formats of input images and output  contexts. You specify a working pixel format using the [`workingFormat`](cicontextoption/1437788-workingformat.md) key in the `options` dictionary when creating a Core Image context.

## See Also

- [func clearCaches()](cicontext/1437790-clearcaches.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](cicontext/1437967-reclaimresources.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](cicontext/1437817-offlinegpucount.md)
  Returns the number of GPUs not currently driving a display.
- [var workingColorSpace: CGColorSpace?](cicontext/1438061-workingcolorspace.md)
  The working color space of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/1642215-workingformat)*