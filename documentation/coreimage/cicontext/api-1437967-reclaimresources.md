# reclaimResources()

**Framework**: Core Image  
**Kind**: instm

Runs the garbage collector to reclaim any resources that the context no longer requires.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func reclaimResources()
```

#### Discussion

The system calls this method automatically after every rendering operation. You can use this method to remove textures from the texture cache that reference deleted images.  

## See Also

- [func clearCaches()](cicontext/1437790-clearcaches.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [class func offlineGPUCount() -> UInt32](cicontext/1437817-offlinegpucount.md)
  Returns the number of GPUs not currently driving a display.
- [var workingColorSpace: CGColorSpace?](cicontext/1438061-workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](cicontext/1642215-workingformat.md)
  The working pixel format of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/1437967-reclaimresources)*