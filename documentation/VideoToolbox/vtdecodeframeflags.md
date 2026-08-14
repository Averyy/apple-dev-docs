# VTDecodeFrameFlags

**Framework**: Video Toolbox  
**Kind**: struct

Flags to pass to a decompression session and the video decoder.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
struct VTDecodeFrameFlags
```

## Topics

### Flags
- [init(rawValue: UInt32)](vtdecodeframeflags/init(rawvalue:).md)
  Creates a flags structure with a raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [class VTDecompressionSession](vtdecompressionsession.md)
  A reference to a decompression session.
- [struct VTDecodeInfoFlags](vtdecodeinfoflags.md)
  Flags that provide information about the status of a decode operation.
- [typealias VTDecompressionOutputCallback](vtdecompressionoutputcallback.md)
  The prototype for the callback invoked when frame decompression is complete.
- [struct VTDecompressionOutputCallbackRecord](vtdecompressionoutputcallbackrecord.md)
- [typealias VTDecompressionOutputHandler](vtdecompressionoutputhandler.md)
  The prototype for the block invoked when frame decompression is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecodeframeflags)*