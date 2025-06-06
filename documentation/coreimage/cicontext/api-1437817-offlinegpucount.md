# offlineGPUCount()

**Framework**: Core Image  
**Kind**: clm

Returns the number of GPUs not currently driving a display.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func offlineGPUCount() -> UInt32
```

#### Return_value

The number of offline GPU devices.

#### Discussion

If this count is greater than zero, the system has attached GPU devices that are not currently driving a display. You can use these devices for Core Image rendering by creating a context with the [`init(forOfflineGPUAt:)`](cicontext/1437772-init.md) or[`init(forOfflineGPUAt:colorSpace:options:sharedContext:)`](cicontext/1437758-init.md) method.

## See Also

- [func clearCaches()](cicontext/1437790-clearcaches.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](cicontext/1437967-reclaimresources.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [var workingColorSpace: CGColorSpace?](cicontext/1438061-workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](cicontext/1642215-workingformat.md)
  The working pixel format of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/1437817-offlinegpucount)*