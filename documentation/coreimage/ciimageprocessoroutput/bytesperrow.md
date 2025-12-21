# bytesPerRow

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The bytes per row of the CPU memory that your Core Image Processor Kernel can write pixels to.

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

- [var region: CGRect](ciimageprocessoroutput/region.md)
  The rectangular region of the output image that your Core Image Processor Kernel must provide.
- [var metalCommandBuffer: (any MTLCommandBuffer)?](ciimageprocessoroutput/metalcommandbuffer.md)
  Returns a Metal command buffer object that can be used for encoding commands.
- [var format: CIFormat](ciimageprocessoroutput/format.md)
  The pixel format of the CPU memory that your Core Image Processor Kernel can write pixels to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/bytesperrow)*