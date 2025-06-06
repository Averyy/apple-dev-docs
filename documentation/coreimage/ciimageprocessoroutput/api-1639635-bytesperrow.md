# bytesPerRow

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

The number of bytes per row of pixels for the output image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var bytesPerRow: Int { get }
```

## See Also

- [var region: CGRect](ciimageprocessoroutput/1639629-region.md)
  The rectangular region of the output image that your processor must provide.
- [var metalCommandBuffer: (any MTLCommandBuffer)?](ciimageprocessoroutput/1639641-metalcommandbuffer.md)
  A command buffer to use for image processing using Metal.
- [var format: CIFormat](ciimageprocessoroutput/1639628-format.md)
  The per-pixel data format expected of the output image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639635-bytesperrow)*