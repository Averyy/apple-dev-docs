# VTDecompressionOutputCallbackRecord

**Framework**: Video Toolbox  
**Kind**: struct

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
struct VTDecompressionOutputCallbackRecord
```

## Topics

### Initializers
- [init()](vtdecompressionoutputcallbackrecord/init.md)
- [init(decompressionOutputCallback: VTDecompressionOutputCallback?, decompressionOutputRefCon: UnsafeMutableRawPointer?)](vtdecompressionoutputcallbackrecord/init(decompressionoutputcallback:decompressionoutputrefcon:).md)
### Instance Properties
- [var decompressionOutputCallback: VTDecompressionOutputCallback?](vtdecompressionoutputcallbackrecord/decompressionoutputcallback.md)
- [var decompressionOutputRefCon: UnsafeMutableRawPointer?](vtdecompressionoutputcallbackrecord/decompressionoutputrefcon.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class VTDecompressionSession](vtdecompressionsession.md)
  A reference to a decompression session.
- [struct VTDecodeFrameFlags](vtdecodeframeflags.md)
  Flags to pass to a decompression session and the video decoder.
- [struct VTDecodeInfoFlags](vtdecodeinfoflags.md)
  Flags that provide information about the status of a decode operation.
- [typealias VTDecompressionOutputCallback](vtdecompressionoutputcallback.md)
  The prototype for the callback invoked when frame decompression is complete.
- [typealias VTDecompressionOutputHandler](vtdecompressionoutputhandler.md)
  The prototype for the block invoked when frame decompression is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputcallbackrecord)*