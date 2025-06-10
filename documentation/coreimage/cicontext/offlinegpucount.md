# offlineGPUCount()

**Framework**: Core Image  
**Kind**: method

Returns the number of GPUs not currently driving a display.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func offlineGPUCount() -> UInt32
```

#### Return Value

The number of offline GPU devices.

#### Discussion

If this count is greater than zero, the system has attached GPU devices that are not currently driving a display. You can use these devices for Core Image rendering by creating a context with the [`init(forOfflineGPUAtIndex:)`](cicontext/init(forofflinegpuatindex:).md) or[`init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)`](cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:).md) method.

## See Also

- [func clearCaches()](cicontext/clearcaches.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](cicontext/reclaimresources.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [var workingColorSpace: CGColorSpace?](cicontext/workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](cicontext/workingformat.md)
  The working pixel format of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/offlinegpucount())*