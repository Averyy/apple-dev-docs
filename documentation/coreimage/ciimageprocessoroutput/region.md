# region

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The rectangular region of the output image that your processor must provide.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var region: CGRect { get }
```

#### Discussion

Your image processor block may be invoked multiple times to provide output for multiple regions, and the region for which output is needed may not match the bounds of the output buffer, texture, or surface.

## See Also

- [var metalCommandBuffer: (any MTLCommandBuffer)?](ciimageprocessoroutput/metalcommandbuffer.md)
  A command buffer to use for image processing using Metal.
- [var bytesPerRow: Int](ciimageprocessoroutput/bytesperrow.md)
  The number of bytes per row of pixels for the output image.
- [var format: CIFormat](ciimageprocessoroutput/format.md)
  The per-pixel data format expected of the output image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/region)*