# VTDecompressionSession

**Framework**: Video Toolbox  
**Kind**: class

A reference to a decompression session.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
class VTDecompressionSession
```

#### Overview

A decompression session supports the decompression of a sequence of video frames. The session is a reference-counted Core Foundation (CF) object.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct VTDecodeFrameFlags](vtdecodeframeflags.md)
  Flags to pass to a decompression session and the video decoder.
- [struct VTDecodeInfoFlags](vtdecodeinfoflags.md)
  Flags that provide information about the status of a decode operation.
- [typealias VTDecompressionOutputCallback](vtdecompressionoutputcallback.md)
  The prototype for the callback invoked when frame decompression is complete.
- [struct VTDecompressionOutputCallbackRecord](vtdecompressionoutputcallbackrecord.md)
- [typealias VTDecompressionOutputHandler](vtdecompressionoutputhandler.md)
  The prototype for the block invoked when frame decompression is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsession)*