# clearCaches()

**Framework**: Core Image  
**Kind**: instm

Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func clearCaches()
```

#### Discussion

You can use this method to remove textures from the texture cache that reference deleted images.

## See Also

- [func reclaimResources()](cicontext/1437967-reclaimresources.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](cicontext/1437817-offlinegpucount.md)
  Returns the number of GPUs not currently driving a display.
- [var workingColorSpace: CGColorSpace?](cicontext/1438061-workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](cicontext/1642215-workingformat.md)
  The working pixel format of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/1437790-clearcaches)*