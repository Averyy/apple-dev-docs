# metalCommandBuffer

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

A command buffer to use for image processing using Metal.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var metalCommandBuffer: (any MTLCommandBuffer)? { get }
```

#### Discussion

If you perform image processing with a Metal shader (and write output to the [`metalTexture`](ciimageprocessoroutput/1639631-metaltexture.md) property), encode your render or compute commands to this buffer. Core Image uses the same command buffer to render other effects that precede or follow your processor in a filter chain.

## See Also

- [var region: CGRect](ciimageprocessoroutput/1639629-region.md)
  The rectangular region of the output image that your processor must provide.
- [var bytesPerRow: Int](ciimageprocessoroutput/1639635-bytesperrow.md)
  The number of bytes per row of pixels for the output image.
- [var format: CIFormat](ciimageprocessoroutput/1639628-format.md)
  The per-pixel data format expected of the output image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639641-metalcommandbuffer)*